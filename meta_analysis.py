#!/usr/bin/env python3
"""
CAR-T Solid Tumors Meta-Analysis
Evidence mapping with integrated meta-analysis of proportions
Methods: Logit transformation + REML estimation + HKSJ adjustment

Corresponds to: Moreira RB et al., npj Precision Oncology (submitted)
PROSPERO: CRD420261294180

Usage: python meta_analysis.py
Output: Prints all results + saves to analysis_results.json

Dependencies: numpy, scipy, pandas
"""

import numpy as np
import pandas as pd
from scipy import stats, optimize
import json

# ============================================================================
# EXTRACTED DATA — 13 single-arm CAR-T trials in solid tumors
# Source: Peer-reviewed publications 2014–2025
# ============================================================================
STUDIES = [
    {"author": "Beatty GL",    "target": "MSLN",      "tumor": "Pancreatic",     "year": 2014, "n": 6,  "events": 0,  "armored": False},
    {"author": "Ahmed N",      "target": "HER2",      "tumor": "Sarcoma",        "year": 2015, "n": 10, "events": 0,  "armored": False},
    {"author": "Junghans",     "target": "PSMA",      "tumor": "Prostate",       "year": 2016, "n": 7,  "events": 2,  "armored": False},
    {"author": "Katz SC",      "target": "CEA",       "tumor": "Colorectal",     "year": 2015, "n": 10, "events": 0,  "armored": False},
    {"author": "Hege",         "target": "TAG-72",    "tumor": "Colorectal",     "year": 2017, "n": 16, "events": 0,  "armored": False},
    {"author": "Adusumilli",   "target": "MSLN",      "tumor": "Mesothelioma",   "year": 2021, "n": 21, "events": 0,  "armored": False},
    {"author": "Haas",         "target": "MSLN",      "tumor": "Solid tumors",   "year": 2019, "n": 15, "events": 0,  "armored": False},
    {"author": "Shi",          "target": "GPC3",      "tumor": "HCC",            "year": 2020, "n": 13, "events": 1,  "armored": False},
    {"author": "Heczey",       "target": "GPC3",      "tumor": "HCC",            "year": 2024, "n": 30, "events": 12, "armored": True},
    {"author": "Chen N",       "target": "GCC+CD19",  "tumor": "Colorectal",     "year": 2024, "n": 15, "events": 6,  "armored": True},
    {"author": "Narayan",      "target": "PSMA",      "tumor": "Prostate",       "year": 2022, "n": 11, "events": 3,  "armored": True},
    {"author": "Wang",         "target": "MSLN",      "tumor": "Solid tumors",   "year": 2021, "n": 10, "events": 0,  "armored": True},
    {"author": "Qi",           "target": "CLDN18.2",  "tumor": "Gastric/GEJ",    "year": 2022, "n": 37, "events": 18, "armored": False},
]


def logit_transform(events, n, cc=0.5):
    """Logit transformation with continuity correction for zero/n cells."""
    e_adj = np.where(events == 0, cc,
            np.where(events == n, n - cc, events))
    p = e_adj / n
    y = np.log(p / (1 - p))
    v = 1.0 / e_adj + 1.0 / (n - e_adj)
    return y, v


def inv_logit(x):
    """Inverse logit transformation."""
    return np.exp(x) / (1.0 + np.exp(x))


def meta_reml_hksj(y, v, conf_level=0.95):
    """
    Random-effects meta-analysis with REML tau2 and HKSJ confidence intervals.
    
    Parameters
    ----------
    y : array — effect sizes (transformed)
    v : array — within-study variances
    conf_level : float — confidence level (default 0.95)
    
    Returns
    -------
    dict — pooled estimate, CIs, prediction interval, heterogeneity stats
    """
    k = len(y)
    
    # Fixed-effect
    w_fe = 1.0 / v
    y_fe = np.sum(w_fe * y) / np.sum(w_fe)
    Q = np.sum(w_fe * (y - y_fe)**2)
    
    # REML tau2 estimation via profile likelihood
    def neg_reml_ll(tau2):
        if tau2 < 0:
            return 1e10
        w = 1.0 / (v + tau2)
        S = np.sum(w)
        y_bar = np.sum(w * y) / S
        return 0.5 * (np.sum(np.log(v + tau2)) + 
                      np.sum((y - y_bar)**2 / (v + tau2)) + 
                      np.log(S))
    
    opt = optimize.minimize_scalar(
        neg_reml_ll, bounds=(0.0, 50.0), method='bounded', 
        options={'xatol': 1e-12, 'maxiter': 10000}
    )
    tau2 = opt.x
    
    # Random-effects weights
    w = 1.0 / (v + tau2)
    sum_w = np.sum(w)
    beta = np.sum(w * y) / sum_w
    
    # HKSJ variance
    var_hksj = np.sum(w**2 * (y - beta)**2 / sum_w**2) * (k / (k - 1))
    se_hksj = np.sqrt(var_hksj)
    
    # Critical value (t-distribution)
    t_crit = stats.t.ppf(1.0 - (1.0 - conf_level) / 2.0, k - 1)
    
    # Confidence and prediction intervals
    ci_l = beta - t_crit * se_hksj
    ci_u = beta + t_crit * se_hksj
    pi_l = beta - t_crit * np.sqrt(var_hksj + tau2)
    pi_u = beta + t_crit * np.sqrt(var_hksj + tau2)
    
    # I-squared
    I2 = max(0.0, (Q - (k - 1)) / Q * 100.0) if Q > 0 else 0.0
    
    return {
        'beta': beta, 'tau2': tau2, 'se': se_hksj,
        'ci_lower': ci_l, 'ci_upper': ci_u,
        'pi_lower': pi_l, 'pi_upper': pi_u,
        'I2': I2, 'Q': Q, 't_crit': t_crit
    }


def run_subgroup(df, mask):
    """Run meta-analysis on a subgroup."""
    sub = df[mask]
    y, v = logit_transform(sub['events'].values, sub['n'].values)
    return meta_reml_hksj(y, v)


def main():
    df = pd.DataFrame(STUDIES)
    
    print("=" * 68)
    print("CAR-T SOLID TUMORS: META-ANALYSIS OF PROPORTIONS")
    print("Logit transformation + REML estimation + HKSJ adjustment")
    print("=" * 68)
    
    # Primary analysis
    y, v = logit_transform(df['events'].values, df['n'].values)
    r = meta_reml_hksj(y, v)
    
    print("\n--- PRIMARY ANALYSIS ---")
    print("Studies:       k = %d" % len(df))
    print("Patients:      N = %d" % df['n'].sum())
    print("Events:        %d" % df['events'].sum())
    print("ORR:           %.1f%% (95%% CI: %.1f-%.1f%%)" % (
        inv_logit(r['beta']) * 100,
        inv_logit(r['ci_lower']) * 100,
        inv_logit(r['ci_upper']) * 100))
    print("Prediction:    %.1f-%.1f%%" % (
        inv_logit(r['pi_lower']) * 100,
        inv_logit(r['pi_upper']) * 100))
    print("tau-squared:   %.2f" % r['tau2'])
    print("I-squared:     %.1f%%" % r['I2'])
    print("Q-statistic:   %.2f" % r['Q'])
    
    # Sensitivity: Freeman-Tukey + DL
    from scipy.stats import norm
    p = df['events'] / df['n']
    n = df['n']
    # Freeman-Tukey transform
    ft = 0.5 * (np.arcsin(np.sqrt(p * n / (n + 1))) + 
                np.arcsin(np.sqrt((p * n + 1) / (n + 1))))
    v_ft = 1.0 / (4.0 * (n + 1.0))
    
    # DL for FT
    w_ft = 1.0 / v_ft
    y_ft_fe = np.sum(w_ft * ft) / np.sum(w_ft)
    Q_ft = np.sum(w_ft * (ft - y_ft_fe)**2)
    tau2_ft = max(0.0, (Q_ft - (len(df) - 1)) / 
                  (np.sum(w_ft) - np.sum(w_ft**2)/np.sum(w_ft)))
    w_ft_re = 1.0 / (v_ft + tau2_ft)
    y_ft_re = np.sum(w_ft_re * ft) / np.sum(w_ft_re)
    
    # Back-transform (approximate)
    # sin(y)^2 * (n+1)/n - 0.5/n, averaged
    p_ft = np.mean(np.sin(y_ft_re)**2)
    
    print("\n--- SENSITIVITY (Freeman-Tukey + DL) ---")
    print("ORR approx:    %.1f%%" % (p_ft * 100))
    print("tau-squared:   %.2f" % tau2_ft)
    
    # Subgroups
    print("\n--- ARMORED vs NON-ARMORED ---")
    r_arm = run_subgroup(df, df['armored'])
    r_noarm = run_subgroup(df, ~df['armored'])
    print("Armored:       %.1f%% (%.1f-%.1f%%)  k=%d  N=%d" % (
        inv_logit(r_arm['beta'])*100, inv_logit(r_arm['ci_lower'])*100,
        inv_logit(r_arm['ci_upper'])*100, df['armored'].sum(),
        df[df['armored']]['n'].sum()))
    print("Non-armored:   %.1f%% (%.1f-%.1f%%)  k=%d  N=%d" % (
        inv_logit(r_noarm['beta'])*100, inv_logit(r_noarm['ci_lower'])*100,
        inv_logit(r_noarm['ci_upper'])*100, (~df['armored']).sum(),
        df[~df['armored']]['n'].sum()))
    
    # Target-specific
    print("\n--- TARGET-SPECIFIC (exact binomial, k=1) ---")
    for target, group in df.groupby('target'):
        tn = int(group['n'].sum())
        te = int(group['events'].sum())
        ci = stats.binomtest(te, tn).proportion_ci()
        print("%-12s:  %.1f%% (%.1f-%.1f%%)  k=%d  n=%d  events=%d" % (
            target, te/tn*100, ci.low*100, ci.high*100, len(group), tn, te))
    
    # Safety
    print("\n--- SAFETY ---")
    # Approximate: pooled CRS rate from reported studies
    crs_rates = np.array([0.95, 0.78, 0.82, 0.65, 0.70])  # reported rates
    crs_n = np.array([37, 15, 30, 27, 11])
    crs_events = (crs_rates * crs_n).astype(int)
    y_crs, v_crs = logit_transform(crs_events, crs_n)
    r_crs = meta_reml_hksj(y_crs, v_crs)
    print("CRS (pooled):  %.1f%% (%.1f-%.1f%%)" % (
        inv_logit(r_crs['beta'])*100,
        inv_logit(r_crs['ci_lower'])*100,
        inv_logit(r_crs['ci_upper'])*100))
    
    # Save results
    results = {
        'primary': {
            'method': 'Logit + REML + HKSJ',
            'k': len(df), 'N': int(df['n'].sum()), 'events': int(df['events'].sum()),
            'ORR_pct': round(inv_logit(r['beta'])*100, 1),
            'CI_95': [round(inv_logit(r['ci_lower'])*100, 1), round(inv_logit(r['ci_upper'])*100, 1)],
            'PI_95': [round(inv_logit(r['pi_lower'])*100, 1), round(inv_logit(r['pi_upper'])*100, 1)],
            'tau2': round(r['tau2'], 2), 'I2': round(r['I2'], 1), 'Q': round(r['Q'], 2)
        },
        'paper_reported': {
            'ORR_pct': 19.8, 'CI_95': [10.4, 34.4],
            'PI_95': [3.3, 64.1], 'tau2': 0.71, 'I2': 52.9
        }
    }
    
    with open('analysis_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    df.to_csv('extracted_data.csv', index=False)
    print("\n" + "=" * 68)
    print("Files saved: extracted_data.csv, analysis_results.json")
    print("=" * 68)


if __name__ == '__main__':
    main()
