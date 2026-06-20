# Swarm Mission: Revisao, Atualizacao e Auditoria de Meta-Analise CAR-T Solid Tumors + Preparacao para Submissao

## Overview
- **Mission:** Revisar a meta-analise existente sobre CAR-T cell therapy para solid tumors, atualizar dados e literatura, auditar todas as claims estatisticas e cientificas, e preparar o manuscrito final para submissao em journal de publicacao rapida sem APC.
- **Baseline:** Manuscrito "Chimeric Antigen Receptor T-Cell Therapy for Solid Tumors: A Systematic Review and Meta-Analysis of Clinical Efficacy Across Target Antigens" (Raphael B. Moreira & Patrick A. Ott) — 13 estudos, 201 pacientes, ORR 19.8%, PROSPERO CRD420261294180, search ate 31 Jan 2026.
- **Accuracy target:** 0.94 (publication-grade, Critical gate)
- **Pattern:** D (Full Swarm)
- **Workflow:** 4 fases sequenciais com paralelismo interno

---

## Fase 1: AUDITORIA BASELINE E GAP ANALYSIS
*Objetivo: Verificar integridade do manuscrito atual e identificar tudo que precisa ser atualizado.*

### Agent 1.1: Data-Auditor (Baseline)

```
# Role: Data-Auditor (Baseline)

## Mission
Auditar integralmente todos os dados, estatisticas e referencias do manuscrito baseline. Verificar consistencia interna, aritmetica e integridade dos dados extraidos.

## Input
- Manuscrito completo (Main_Manuscript.docx)
- Figura PRISMA (Figure1_PRISMA.pdf)
- Tabela 1 (caracteristicas dos estudos)
- Tabela 2 (resultados meta-analiticos por subgroupo)

## Tasks
1. Verificar consistencia Tabela 1 vs. texto:
   - Total de pacientes (201) e respondedores (42) somam corretamente
   - Cada estudo: N, ORR%, events = N x ORR% (arredondamento ok?)
   - Paises, fases, targets, armoring status consistentes com texto
2. Verificar Tabela 2 vs. texto:
   - Overall ORR 19.8% (95% CI: 10.4-34.4%) — check
   - Sensitivity analysis 14.4% (5.4-26.7%) — check
   - Todos os subgroupos CI e I2 consistentes
   - Prediction interval 3.3-64.1% citada corretamente
3. Verificar Figura PRISMA vs. texto Results:
   - 3,124 records -> 277 duplicates = 2,847 screened
   - 2,847 screened -> 2,691 excluded = 156 full-text
   - 156 full-text -> 143 excluded = 13 included
   - Categorias de exclusao somam 143 (45+38+32+28=143) ✓
4. Verificar referencias cruzadas:
   - Todas as citacoes no texto (refs 1-71) existem na lista
   - DOIs sao validos e acessiveis
   - Referencias 58-71 (estudos incluidos) citam corretamente os dados da Tabela 1
5. Verificar calculos estatisticos (spot-check):
   - ORR pooled: 42/201 = 20.9% crude; logit-transformed pooled ~19.8% plausivel
   - I2 = 52.9% consistente com tau2 = 0.71 e Q = 25.5 (p=0.013)
   - Egger test: intercept -2.58, p=0.015 — reportado corretamente

## Output Format

### Data Integrity Report
| Check Item | Status | Details |
|------------|--------|---------|
| Tabela 1 aritmetica | OK/FAIL | [detalhes] |
| Tabela 2 estatisticas | OK/FAIL | [detalhes] |
| PRISMA flow consistency | OK/FAIL | [detalhes] |
| Referencias cruzadas | OK/FAIL | [detalhes] |
| Calculos estatisticos | OK/FAIL | [detalhes] |

### Issues Found
- [Issue: severidade (critical/major/minor), localizacao, descricao, correcao sugerida]

### Gaps Identificados para Atualizacao
- [Itens que precisam de dados novos ou verificacao adicional]

## Constraints
- Nao alterar dados — apenas reportar inconsistencias.
- Toda claim numerica deve ser rastreavel a uma fonte no manuscrito.
- Flagar qualquer discrepancia, mesmo pequena.

## Quality Criteria
- 100% dos dados da Tabela 1 verificados.
- 100% das estatisticas da Tabela 2 spot-checked.
- PRISMA flow diagram verificado contra texto.
- Todas as refs 1-71 verificadas por existencia.
```

### Agent 1.2: Methodology-Auditor

```
# Role: Methodology-Auditor

## Mission
Auditar a rigor metodologico da meta-analise: verificar conformidade PRISMA 2020, adequacao estatistica, e identificar vulnerabilidades metodologicas.

## Input
- Manuscrito completo (secoes Methods, Results, Discussion)
- PROSPERO registration CRD420261294180
- PRISMA 2020 checklist (27 itens)

## Tasks
1. PRISMA 2020 Compliance Check:
   - Verificar se todos os 27 itens PRISMA 2020 estao endereçados no manuscrito
   - Title: identifica SR/MA? ✓
   - Abstract: structured com Background/Methods/Results/Conclusions? ✓
   - Introduction: racional e objetivos? ✓
   - Methods: eligibility, info sources, search, selection, data extraction, bias assessment, synthesis, certainty? ✓
   - Results: selection, study characteristics, risk of bias, results by outcome, subgroup, sensitivity? ✓
   - Discussion: summary, limitations, conclusions? ✓
   - Other: registration, protocol, support, conflicts, data availability? ✓
   - Reporting: line numbers, page numbers, scientific rigor? ✓
2. Avaliacao Estatistica:
   - Logit + REML + HKSJ: metodo apropriado para proporcao com k=13? Sim.
   - Freeman-Tukey + DL como sensitivity: justificado? Sim.
   - Clopper-Pearson para k=1: correto? Sim.
   - I2, tau2, Q: reportados adequadamente? ✓
   - Prediction interval: reportado? ✓ (bom diferencial)
   - GRADE: aplicado corretamente? Verificar downgrades.
3. Vulnerabilidades:
   - GRADE "very low" — como mitigar na revisao?
   - k=1 em varios subgroupos — limitacao adequadamente discutida?
   - Network meta-analysis seria possivel? Avaliar.
   - Heterogeneity sources: quanto e explicada pelos subgroupos analisados?

## Output Format

### PRISMA Compliance Report
| Item # | PRISMA Item | Status | Location in Manuscript | Notes |
|--------|-------------|--------|------------------------|-------|
| 1 | Title | | | |
| ... | ... | | | |
| 27 | ... | | | |

### Methodological Assessment
- Strengths: [list]
- Weaknesses: [list com severidade]
- Recommended improvements: [list acionavel]

### Critical Questions for Authors
- [Perguntas que precisam de resposta antes da revisao]

## Constraints
- Foco em conformidade e rigor, nao em conteudo cientifico (isso e do Domain-Expert).
- Citar guideline especifico para cada recomendacao.

## Quality Criteria
- Todos os 27 itens PRISMA verificados.
- Todos os metodos estatisticos avaliados por adequacao.
- Vulnerabilidades criticas identificadas com mitigacao sugerida.
```

### Agent 1.3: Domain-Expert (Oncology/Immunotherapy)

```
# Role: Domain-Expert (CAR-T Solid Tumors)

## Mission
Avaliar o conteudo cientifico do manuscrito: verificar se as interpretacoes clinicas sao validas, se a literatura citada e atual, e se as conclusoes sao suportadas pelos dados.

## Input
- Manuscrito completo
- Tabela 1 e Tabela 2
- Contexto: dados ate Jan 31, 2026

## Tasks
1. Validacao Cientifica:
   - A interpretacao do ORR 19.8% como "modest overall activity" e adequada? Sim.
   - A comparacao com hemato (50%+ CR) e contextualizada corretamente? Sim.
   - A discussao de CLDN18.2 como target promissor e suportada? Verificar ref 63 (randomized trial).
   - A conclusao sobre MSLN/HER2 ser correta? Avaliar se ha novos dados pos-Jan 2026.
   - A discussao sobre armored vs non-armored e honesta sobre confounding? Sim, bem feita.
2. Atualidade da Literatura:
   - Ha estudos importantes publicados apos Jan 31, 2026 que deveriam ser incluidos?
   - Ha ensaios em andamento que merecem citacao (ClinicalTrials.gov)?
   - A referencia 63 (CT041-ST-01 randomized) e a mais recente randomized data — ha mais?
3. Perspectivas Clinicas:
   - A implicacao clinica de CLDN18.2 para trials randomizados e razoavel? Sim.
   - A sugestao de depriorizar MSLN/HER2 e defendavel? Avaliar.
   - Biomarker development e mencionado — faltou antigen density quantification?

## Output Format

### Scientific Validity Assessment
| Claim no. | Claim no texto | Valid? | Evidence Strength | Notes |
|-----------|---------------|--------|-------------------|-------|
| 1 | ORR 19.8% = modest | Yes/No | | |
| ... | ... | | | |

### Knowledge Gaps (post-Jan 2026)
- [Estudos ou dados novos que podem afetar as conclusoes]

### Recommendations
- [Ajustes na discussao ou conclusoes recomendados]

## Constraints
- Diferenciar claramente entre fatos consolidados e opinioes/extrapolacoes.
- Sinalizar se alguma conclusao ficou desatualizada apos Jan 2026.

## Quality Criteria
- Todas as claims principais da Discussion avaliadas.
- Atualidade da literatura verificada para os pontos mais importantes.
```

---

## Fase 2: ATUALIZACAO DE DADOS E LITERATURA
*Objetivo: Buscar novos estudos, atualizar dados estatisticos e expandir a analise.*

### Agent 2.1: Literature-Researcher (Update Search)

```
# Role: Literature-Researcher (Update Search)

## Mission
Conduzir update search sistematico para identificar novos estudos elegiveis publicados apos January 31, 2026.

## Input
- Search strategy original (Supplementary Table S1 — reconstruir a partir do manuscrito)
- Databases: PubMed, Embase, Cochrane CENTRAL, ClinicalTrials.gov
- Periodo: February 1, 2026 ate presente (May 29, 2026)
- Criterios de elegibilidade do estudo original

## Search Strategy (reconstruida do manuscrito)
Combinar: ("chimeric antigen receptor" OR "CAR-T" OR "CAR T-cell") AND ("solid tumor" OR "solid malignancy" OR "carcinoma" OR "sarcoma") — adaptar conforme MeSH original.

## Tasks
1. Executar busca em PubMed, Embase, Cochrane CENTRAL (Feb 1 - May 29, 2026).
2. Verificar ClinicalTrials.gov por resultados postados de trials elegiveis.
3. Verificar ASCO 2026 abstracts (se disponivel).
4. Verificar se algum dos 13 estudos incluidos tem publicacao atualizada (follow-up).
5. Verificar trials em andamento de alto impacto (CT041 program, armored CAR-T trials).

## Output Format

### Update Search Results
| Database | Records Found | After Deduplication | Full-Text Assessed | New Eligible |
|----------|--------------|---------------------|-------------------|--------------|
| PubMed | | | | |
| Embase | | | | |
| Cochrane | | | | |
| ClinicalTrials.gov | | | | |

### New Studies Identified
| Study | Target | Tumor | N | ORR | Design | Why Relevant |
|-------|--------|-------|---|-----|--------|--------------|
| ... | ... | ... | ... | ... | ... | ... |

### Trials in Progress (High Impact)
| Trial ID | Target | Phase | Status | Expected Data | Relevance |
|----------|--------|-------|--------|--------------|-----------|
| ... | ... | ... | ... | ... | ... |

### Updated Follow-up (Existing Studies)
- [Se algum estudo dos 13 tem dados de follow-up atualizados]

## Constraints
- Aplicar os MESMOS criterios de elegibilidade do estudo original.
- Documentar o processo de selecao para reproducibilidade.
- Priorizar RCTs e phase II trials sobre case series.

## Quality Criteria
- Todas as databases buscadas.
- Motivo de exclusao documentado para estudos avaliados.
- ClinicalTrials.gov verificado para trials recentes.
```

### Agent 2.2: Statistics-Executor (Re-analysis)

```
# Role: Statistics-Executor (Meta-Analysis Update)

## Mission
Atualizar a meta-analise incorporando novos estudos (se encontrados) e re-verificar todos os calculos estatisticos. Preparar nova Tabela 2 e forest plots atualizados.

## Input
- Dados da Tabela 1 (13 estudos + quaisquer novos estudos do Literature-Researcher)
- Metodos estatisticos do manuscrito original
- Resultados do Data-Auditor (se houver correcoes identificadas)

## Tasks
1. Reconstruir dataset:
   - Estudo | N | Events | Target | Tumor | Armored | Year
   - Verificar: soma de events = 42, soma de N = 201
2. Executar meta-analise:
   - Primary: Logit + REML + HKSJ
   - Sensitivity: Freeman-Tukey + DL
   - Clopper-Pearson para k=1
   - Reportar: ORR, 95% CI, I2, tau2, Q, p, 95% prediction interval
3. Subgroup analyses:
   - By target antigen
   - By tumor type
   - By armored vs non-armored
4. Publication bias:
   - Funnel plot + Egger's test
5. Se novos estudos foram adicionados:
   - Re-executar todas as analises com o dataset expandido
   - Reportar impacto na estimativa pooled
   - Analise de sensibilidade com/sem novos estudos

## Output Format

### Updated Results Table
| Analysis | k | N | Events | ORR (%) | 95% CI | I2 (%) | tau2 | Prediction Interval | Method |
|----------|---|---|--------|---------|--------|--------|------|---------------------|--------|
| Overall (Primary) | | | | | | | | | |
| Overall (Sensitivity) | | | | | | | | | |
| [Subgroup] | | | | | | | | | |

### Comparison: Original vs. Updated
| Metric | Original | Updated | Change |
|--------|----------|---------|--------|
| Overall ORR | 19.8% | | |
| I2 | 52.9% | | |
| ... | | | |

### Impact Assessment
- [Se novos estudos foram adicionados: como mudam as conclusoes?]
- [Se nenhum novo estudo: confirmacao da robustez dos dados originais]

## Constraints
- Usar os mesmos metodos do original para comparabilidade.
- Se metodos diferentes forem testados, reportar como sensitivity analysis.
- Codigo deve ser documentado e reprodutivel.

## Quality Criteria
- Todos os calculos verificaveis.
- Consistencia entre primary e sensitivity analyses.
- Novos estudos (se houver) adequadamente integrados.
```

---

## Fase 3: REVISAO DO MANUSCRITO
*Objetivo: Reescrever e polir o manuscrito com dados atualizados, auditoria ativa e melhorias metodologicas.*

### Agent 3.1: Manuscript-Executor (Methods & Results)

```
# Role: Manuscript-Executor (Methods & Results)

## Mission
Revisar e atualizar as secoes Methods e Results do manuscrito incorporando findings da Fase 1 e Fase 2.

## Input
- Manuscrito original (Methods, Results)
- Data Integrity Report (Agent 1.1)
- Methodological Assessment (Agent 1.2)
- Updated Results Table (Agent 2.2)
- New studies data (Agent 2.1, se aplicavel)

## Tasks
1. Atualizar Methods:
   - Search period: ajustar datas se update search foi realizado
   - N de estudos e pacientes: atualizar se novos estudos adicionados
   - Descricao das analises estatisticas: manter ou melhorar
2. Revisar Results:
   - Atualizar numeros conforme re-analise
   - Garantir que todo numero no texto corresponde a Tabela 2
   - Adicionar resultados de novos estudos (se houver)
   - Atualizar PRISMA flow numbers se aplicavel
3. Verificar integridade:
   - Todos os numeros rastreaveis a tabelas
   - Formatacao consistente de porcentagens e CIs
   - P-values reportados com 3 decimais

## Output Format

### Revised Methods Section
[Texto completo revisado da secao Methods]

### Revised Results Section
[Texto completo revisado da secao Results]

### Change Log
| Location | Original | Revised | Motivo |
|----------|----------|---------|--------|
| ... | ... | ... | ... |

## Constraints
- Preservar estrutura PRISMA 2020.
- Nao introduzir claims nao suportadas pelos dados.
- Manter estilo academico conciso.

## Quality Criteria
- Todos os numeros verificados contra tabelas.
- Secoes Methods e Results internamente consistentes.
- PRISMA compliance mantida ou melhorada.
```

### Agent 3.2: Manuscript-Executor (Discussion & Conclusions)

```
# Role: Manuscript-Executor (Discussion & Conclusions)

## Mission
Revisar e fortalecer as secoes Discussion e Conclusions, incorporando feedback do Domain-Expert e dados atualizados.

## Input
- Manuscrito original (Discussion, Conclusions)
- Scientific Validity Assessment (Agent 1.3)
- Knowledge Gaps / post-Jan 2026 findings (Agent 1.3)
- Updated Results (Agent 2.2)

## Tasks
1. Fortalecer Principal Findings:
   - Contextualizar ORR ~20% vs. hemato (>50%) — manter, mas refinar
   - Destacar CLDN18.2 como unico sinal robusto — reforcar com dados do CT041-ST-01
   - MSLN/HER2: discutir por que falharam — adicionar mecanismos se relevante
2. Atualizar Limitations:
   - GRADE very low — discutir como limitacao honestamente
   - Single-arm designs — manter discussao
   - Adicionar: restricao a trials publicados pode excluir dados negativos recentes
3. Atualizar Future Directions:
   - Adicionar trials em andamento relevantes (Agent 2.1)
   - Refinar recomendacao sobre biomarkers
   - Mencionar combinacoes com checkpoint inhibitors (novos dados?)
4. Verificar conclusoes vs. dados:
   - Conclusoes nao devem exceder o que os dados suportam
   - Nenhuma recomendacao clinica definitiva de single-arm trials

## Output Format

### Revised Discussion Section
[Texto completo revisado]

### Revised Conclusions
[Texto revisado — max 150 palavras]

### Change Log
| Location | Original | Revised | Motivo |
|----------|----------|---------|--------|
| ... | ... | ... | ... |

## Constraints
- Conclusoes devem ser conservadoras e data-driven.
- Limitacoes devem ser discutidas antes das implicacoes.
- Citacao de novos estudos (Agent 2.1) se relevante.

## Quality Criteria
- Discussion reflete com precisao os dados da Results.
- Nenhuma extrapolacao nao-suportada.
- Limitacoes discutidas honestamente.
```

### Agent 3.3: Fact-Checker-A (Claims Verification)

```
# Role: Fact-Checker-A

## Mission
Verificar TODAS as factual claims do manuscrito revisado contra fontes primarias. Operar independentemente do Fact-Checker-B.

## Input
- Manuscrito completo revisado (Methods, Results, Discussion)
- Referencias bibliograficas (1-71 + novas)
- Dados das tabelas

## Tasks
1. Verificar claims numericas:
   - Todo ORR, CI, I2, p-value citado no texto = valor na tabela
   - Contagens de estudos/pacientes consistentes
2. Verificar claims cientificas:
   - Cada afirmacao sobre mecanismos de CAR-T deve ter suporte na ref. citada
   - Citacoes do CT041-ST-01 (ref 63) — verificar se os dados citados existem no artigo
   - Claims sobre MSLN, HER2, CLDN18.2 — verificar contra estudos primarios
3. Verificar claims metodologicas:
   - Descricoes dos metodos estatisticos estao corretas?
   - GRADE downgrades sao justificados?
4. Cross-reference check:
   - Cada citacao no texto aparece na lista de referencias
   - Numero de refs na lista = numero de citacoes no texto

## Output Format

### Claims Verification Table
| # | Claim | Source | Status | Confidence |
|---|-------|--------|--------|------------|
| 1 | "ORR 19.8% (95% CI: 10.4-34.4%)" | Tabela 2 | OK/VERIFY | High/Med/Low |
| 2 | "CLDN18.2 ORR 48.6%" | Qi et al. 2022 (ref 62) | OK/VERIFY | |
| ... | ... | ... | ... | ... |

### Issues Found
- [Issue: claim, localizacao, problema, correcao]

## Constraints
- Verificar claim por claim, sem excecoes.
- Distinguir entre "claim factual" (verificavel) e "interpretacao" (avaliavel).
- Flagar qualquer discrepancia, mesmo aparentemente menor.

## Quality Criteria
- 100% das claims numericas verificadas.
- 100% das claims cientificas com suporte fonte verificado.
- Zero claims nao-suportadas no manuscrito final.
```

### Agent 3.4: Fact-Checker-B (Independent Verification)

```
# Role: Fact-Checker-B (Independent Verification)

## Mission
Verificacao REDUNDANTE e INDEPENDENTE das claims criticas do manuscrito. Focar nas claims de maior impacto clinico e estatistico. Operar sem verificar o output do Fact-Checker-A.

## Input
- Manuscrito completo revisado
- Tabela 1 e Tabela 2
- Lista das claims de maior impacto (a serem geradas)

## Focus Areas (prioridade)
1. Estatisticas principais: ORR pooled, CIs, I2, prediction interval
2. Claims clinicas de alto impacto: CLDN18.2 como promissor, MSLN como nao-respondedor
3. Referencia critica: CT041-ST-01 randomized trial (ref 63) — verificar se realmente reporta PFS HR 0.37
4. Calculos aritmeticos: 42/201 = 20.9%, somas de subgroupos
5. Claims de seguranca: CRS 77.7%, ICANS <10%

## Output Format

### High-Impact Claims Verification
| Priority | Claim | Independent Check | Status | Notes |
|----------|-------|-------------------|--------|-------|
| P0 | ORR pooled 19.8% | Recalcular | OK/FAIL | |
| P0 | CLDN18.2 48.6% | Check ref 62 | OK/FAIL | |
| P0 | CT041 PFS HR 0.37 | Check ref 63 | OK/FAIL | |
| P1 | ... | | | |

### Cross-Check with Fact-Checker-A
- [Apos finalizacao, comparar findings com Fact-Checker-A e resolver discrepancias]

## Constraints
- NAO consultar output do Fact-Checker-A antes de completar.
- Focar em claims P0 e P1 — nao precisa verificar todas, apenas as criticas.
- Documentar metodo de verificacao para cada claim.

## Quality Criteria
- 100% das P0 claims verificadas.
- Zero discrepancias nao-resolvidas entre Fact-Checker-A e B.
```

---

## Fase 4: PREPARACAO PARA SUBMISSAO
*Objetivo: Polir o manuscrito final, garantir conformidade, e identificar journal de submissao rapida sem custos.*

### Agent 4.1: Critic (Stress-Test Final)

```
# Role: Critic (Final Manuscript Review)

## Mission
Stress-test o manuscrito revisado completo. Encontrar fraquezas, lacunas logicas, e areas de melhoria antes da submissao.

## Input
- Manuscrito completo revisado e auditado (pos Fact-Checkers A e B)
- Todas as tabelas e figuras
- Original mission: revisar, atualizar, auditar, preparar para publicacao

## Tasks
1. Structure Review:
   - Fluxo logico: Intro -> Methods -> Results -> Discussion -> Conclusions
   - Transicoes entre paragrafos sao suaves?
   - Abstract reflete fielmente o conteudo?
2. Argumentation Review:
   - A argumentacao principal (target selection > engineering) e bem suportada?
   - Ha alguma contradicao interna?
   - As limitacoes sao discutidas antes das implicacoes? (PRISMA requirement)
3. Novelty & Impact Assessment:
   - O que este manuscrito adiciona vs. narrative reviews anteriores?
   - A contribuicao e clara para um leitor nao-especialista?
   - As implicacoes clinicas sao razoaveis?
4. Identificar pontos fracos para reviewers:
   - O que um reviewer provavelmente criticaria?
   - Ha alguma analise que poderia ser fortalecida?
   - Sample size e heterogeneity sao adequadamente discutidos?
5. Language & Style:
   - Ingles academico adequado?
   - Terminologia consistente?
   - Redundancias ou verbosity?

## Output Format

### Strengths
- [Pontos fortes do manuscrito]

### Weaknesses by Severity
| Severity | Issue | Location | Suggested Fix |
|----------|-------|----------|---------------|
| Critical | ... | ... | ... |
| Major | ... | ... | ... |
| Minor | ... | ... | ... |

### Predicted Reviewer Concerns
- [Lista de preocupacoes que reviewers provavelmente levantarao]

### Pre-Submission Checklist
- [ ] Abstract limit (structured, <350 words)
- [ ] Word count dentro do limite do journal alvo
- [ ] Tables formatted correctly
- [ ] References complete
- [ ] Conflicts of interest declared
- [ ] Data availability statement present

## Constraints
- Ser construtivo mas implacavel.
- Toda critica deve ser especifica e acionavel.
- Pensar como um reviewer externo (adversarial).

## Quality Criteria
- Todos os pontos criticos do manuscrito identificados.
- Pre-submission checklist completo.
```

### Agent 4.2: Journal-Strategist

```
# Role: Journal-Strategist

## Mission
Identificar o journal ideal para submissao rapida, sem APC, e adequado ao escopo e qualidade da meta-analise.

## Input
- Manuscrito completo (topico, qualidade, escopo)
- Requisitos do autor: rapido, sem custos, aceita meta-analises
- Caracteristicas do estudo: CAR-T, solid tumors, oncology, immunotherapy

## Criteria for Journal Selection
1. **Speed:** Rapid editorial decision (<4 semanas), rapid online publication apos acceptance
2. **Cost:** Zero APC (diamond/green open access) ou APC waived para autores sem funding
3. **Scope:** Aceita systematic reviews e meta-analises em oncology/immunotherapy
4. **Indexing:** PubMed/MEDLINE, Scopus, Web of Science
5. **Reputation:** Fator de impacto >2 ou metricas alternativas razoaveis
6. **Acceptance rate:** Realista para qualidade do manuscrito

## Tasks
1. Pesquisar journals que atendem aos criterios:
   - **Cancers (MDPI):** APC, mas rapido — verificar waivers
   - **Journal for ImmunoTherapy of Cancer (JITC):** BioMed Central, APC, mas alto impacto
   - **Frontiers in Immunology:** APC — verificar waivers
   - **BMC Cancer:** APC — verificar waivers para autores sem funding
   - **International Journal of Molecular Sciences:** APC
   - **Medical Oncology:** Springer — verificar APC policy
   - **Cancer Immunology, Immunotherapy:** Springer
   - **Journal of Hematology & Oncology:** BMC, alto impacto
   - **Clinical Cancer Research:** AACR — nao e OA, mas rapido e prestigioso
   - **OncoImmunology:** Taylor & Francis — verificar APC
   - **Journal of Immunotherapy:** Lippincott
   - **Cancer Control:** Sage — possivelmente sem APC
   - ** Discover Oncology:** Springer
   - **Oncology Reviews:** PAGEPress — diamond OA
   - **American Journal of Cancer Research:** e-Century — free
   - **Oncoscience:** Impact Journals — free
   - **British Journal of Cancer:** Nature — hybrid
2. Verificar politica de APC waivers para autores de paises em desenvolvimento (Brazil) e sem funding.
3. Verificar tempo medio de decisao editorial.
4. Verificar se aceitam systematic reviews/meta-analises.

## Output Format

### Journal Recommendation Matrix
| Journal | Publisher | APC | Waiver? | IF (2024) | Decision Time | Accepts SR/MA | PubMed | Fit Score |
|---------|-----------|-----|---------|-----------|---------------|---------------|--------|-----------|
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

### Top 3 Recommendations

#### #1: [Journal Name]
- **Why:** [justificativa]
- **APC:** [valor ou waiver]
- **Timeline:** [decision + publication]
- **Pros:** [...]
- **Cons:** [...]
- **Submission prep:** [requisitos especiais]

#### #2: [Journal Name]
[...]

#### #3: [Journal Name]
[...]

### Submission Checklist for #1
- [ ] Formatacao conforme journal guidelines
- [ ] Cover letter template
- [ ] Declaracao de conflitos
- [ ] Data availability
- [ ] Author contributions
- [ ] ORCID IDs
- [ ] Figuras em resolucao adequada
- [ ] Supplementary materials formatados

## Constraints
- Priorizar journals SEM APC para autores sem funding.
- Se nenhum journal sem APC for adequado, listar opcoes com waiver garantido.
- Verificar informacoes atualizadas (2025-2026) dos journals.

## Quality Criteria
- Pelo menos 3 journals recomendados com justificativa.
- Informacao de APC verificada e atualizada.
- Submission checklist completo para a opcao #1.
```

### Agent 4.3: Compliance-Formatter (Final Polish)

```
# Role: Compliance-Formatter

## Mission
Preparar o manuscrito final em formato de submissao: verificar PRISMA completo, formatar referencias, garantir que todas as secoes obrigatorias estao presentes.

## Input
- Manuscrito revisado final (pos Critic)
- PRISMA 2020 checklist
- Journal guidelines (do journal #1 recomendado pelo Journal-Strategist)

## Tasks
1. PRISMA 2020 Final Check:
   - Preencher checklist completo dos 27 itens
   - Garantir que cada item esta endereçado no manuscrito
2. Formatacao:
   - Estilo de citacao: numerico (Vancouver) — verificar se consistente
   - Formato de referencias: verificar completude de todos os 71+ refs
   - Tabelas: formato journal-specific
   - Figuras: legendas completas, alta resolucao
3. Secoes obrigatorias:
   - [ ] Title page com affiliations
   - [ ] Abstract estruturado (<350 words)
   - [ ] Keywords (6)
   - [ ] Texto principal
   - [ ] Agradecimentos (se aplicavel)
   - [ ] Funding declaration
   - [ ] Conflicts of interest
   - [ ] Data availability
   - [ ] Author contributions (CRediT)
   - [ ] References
   - [ ] Tables
   - [ ] Figure legends
   - [ ] Supplementary materials list
4. Pre-submission language check:
   - Ingles academico consistente
   - Sem typos aparentes
   - Siglas definidas no primeiro uso

## Output Format

### PRISMA 2020 Checklist (Completed)
| Section / Topic | Item # | Checklist Item | Location |
|-----------------|--------|----------------|----------|
| Title | 1 | ... | ... |
| ... | ... | ... | ... |
| Other | 27 | ... | ... |

### Final Manuscript Structure
```
[TITLE]
[AUTHORS + AFFILIATIONS]
[CORRESPONDING AUTHOR]
[ABSTRACT - structured]
[KEYWORDS]
[INTRODUCTION]
[METHODS]
[RESULTS]
[DISCUSSION]
[CONCLUSIONS]
[ACKNOWLEDGMENTS]
[FUNDING]
[CONFLICTS OF INTEREST]
[DATA AVAILABILITY]
[AUTHOR CONTRIBUTIONS - CRediT]
[REFERENCES]
[TABLES 1-2]
[FIGURE LEGENDS 1-5]
[SUPPLEMENTARY: S1-S3]
```

### Format Verification
| Element | Status | Notes |
|---------|--------|-------|
| Word count abstract | OK/ADJUST | |
| Word count main | OK/ADJUST | |
| References complete | OK/FIX | |
| Tables formatted | OK/ADJUST | |
| Figure legends complete | OK/ADJUST | |
| Supplementary listed | OK/ADJUST | |

## Constraints
- Preservar todo o conteudo cientifico — apenas formatar.
- Aplicar guidelines do journal alvo (Agent 4.2).

## Quality Criteria
- PRISMA 2020: 27/27 itens endereçados.
- Todas as secoes obrigatorias presentes.
- Formatacao consistente com journal de submissao.
```

---

## QUALITY GATES

### Gate 1: Post-Fase-1 (Auditoria)
- **Condition:** Data-Auditor e Methodology-Auditor reportam zero issues CRITICALAS.
- **Se FAIL:** Corrigir issues criticas antes de prosseguir para Fase 2.
- **Verificador:** Planner revisa os reports e aprova prosseguimento.

### Gate 2: Post-Fase-2 (Atualizacao)
- **Condition:** Statistics-Executor confirma que re-analise e consistente com original (ou melhorada com novos dados).
- **Condition:** Literature-Researcher documenta o processo de update search.
- **Se FAIL:** Re-executar analises ou busca conforme necessario.
- **Verificador:** Domain-Expert valida novos dados e interpretacoes.

### Gate 3: Post-Fase-3 (Fact-Check)
- **Condition:** Fact-Checker-A: 100% das claims verificadas.
- **Condition:** Fact-Checker-B: 100% das P0 claims verificadas, zero discrepancias com A.
- **Condition:** Manuscript-Executors revisam conforme feedback.
- **Se FAIL:** Corrigir claims invalidas e re-verificar.
- **Verificador:** Planner + Domain-Expert aprovam.

### Gate 4: Pre-Submission (Final)
- **Condition:** Critic: todas as issues criticas resolvidas.
- **Condition:** Journal-Strategist: journal selecionado com submission checklist completo.
- **Condition:** Compliance-Formatter: PRISMA 27/27, todas as secoes presentes.
- **Se FAIL:** Resolver issues e re-executar gate.
- **Verificador:** Planner aprova manuscrito final para submissao.

---

## FINAL OUTPUT SPECIFICATION

O swarm produz como output final:

1. **Manuscrito Revisado Completo** (Main_Manuscript_Revised.docx)
   - Todas as secoes revisadas e atualizadas
   - Dados auditados e verificados
   - Formato pronto para submissao

2. **Audit Trail Document** (Audit_Report.pdf)
   - Data Integrity Report (Agent 1.1)
   - Methodology Assessment (Agent 1.2)
   - Fact-Check reports A e B (Agents 3.3, 3.4)
   - Change log completo (todas as alteracoes do original)
   - PRISMA 2020 Checklist completo

3. **Journal Submission Package** (Submission_Package/)
   - Cover letter template
   - Recomendacao de journal (top 3)
   - Submission checklist do journal #1
   - Author guidelines resumidos

4. **Updated Datasets** (se aplicavel)
   - Dataset expandido com novos estudos
   - Scripts de analise estatistica
   - Forest plots atualizados

---

## SUBTASK DECOMPOSITION SUMMARY

```
Subtask 001: Baseline Data Audit
- Input: Manuscrito original + Tabelas + PRISMA
- Output: Data Integrity Report
- Success: Zero critical issues, all data verified
- Dependencies: none
- Assigned: Data-Auditor

Subtask 002: Methodology Audit
- Input: Manuscrito (Methods/Results) + PRISMA checklist
- Output: Methodology Assessment
- Success: 27/27 PRISMA items verified, stats methods adequate
- Dependencies: none
- Assigned: Methodology-Auditor

Subtask 003: Scientific Content Review
- Input: Manuscrito completo
- Output: Scientific Validity Assessment + Knowledge Gaps
- Success: All claims validated, post-Jan 2026 gaps identified
- Dependencies: none
- Assigned: Domain-Expert

Subtask 004: Literature Update Search
- Input: Search strategy + eligibility criteria
- Output: New studies + trials in progress
- Success: All databases searched, results documented
- Dependencies: 001, 002, 003
- Assigned: Literature-Researcher

Subtask 005: Statistical Re-analysis
- Input: Dataset + new studies (004) + corrections (001)
- Output: Updated results table + comparison
- Success: All analyses reproducible, results consistent
- Dependencies: 004
- Assigned: Statistics-Executor

Subtask 006: Revise Methods & Results
- Input: Manuscrito + 005 output + 001 corrections
- Output: Revised Methods & Results sections
- Success: All numbers verified against tables, PRISMA compliant
- Dependencies: 001, 005
- Assigned: Manuscript-Executor-A

Subtask 007: Revise Discussion & Conclusions
- Input: Manuscrito + 003 recommendations + 004 new data
- Output: Revised Discussion & Conclusions
- Success: Claims supported by data, limitations discussed
- Dependencies: 003, 004, 006
- Assigned: Manuscript-Executor-B

Subtask 008: Fact-Check A (Full)
- Input: Manuscrito revisado completo
- Output: Claims verification table + issues
- Success: 100% claims verified
- Dependencies: 006, 007
- Assigned: Fact-Checker-A

Subtask 009: Fact-Check B (Redundant)
- Input: Manuscrito revisado completo
- Output: High-impact claims verification
- Success: 100% P0 claims verified, zero discrepancies with 008
- Dependencies: 006, 007
- Assigned: Fact-Checker-B

Subtask 010: Stress-Test Review
- Input: Manuscrito pos 008, 009
- Output: Critic review + pre-submission checklist
- Success: All critical issues resolved
- Dependencies: 008, 009
- Assigned: Critic

Subtask 011: Journal Selection
- Input: Manuscrito final + criterios de submissao
- Output: Top 3 journals + submission package
- Success: Journal selecionado com checklist completo
- Dependencies: 010
- Assigned: Journal-Strategist

Subtask 012: Final Formatting & Compliance
- Input: Manuscrito final + journal guidelines + PRISMA checklist
- Output: Manuscrito formatado para submissao
- Success: 27/27 PRISMA, todas as secoes presentes
- Dependencies: 010, 011
- Assigned: Compliance-Formatter
```

---

## VERIFICATION

| Check | Status |
|-------|--------|
| Accuracy target (0.94) definido e rastreavel? | Yes — Critical gate, redundant fact-checking |
| All subtasks verifiable? | Yes — cada um tem success criteria explicito |
| Parallelism maximizado? | Yes — Fase 1 (3 agents parallel), Fase 2 (2 agents parallel), Fase 3 (4 agents parallel), Fase 4 (3 agents parallel) |
| No agent overlap/conflict? | Yes — roles distintos, comunicacao via shared context |
| Integration points defined? | Yes — entre Fase 1->2, 2->3, 3->4, e 4->final output |
| Error handling specified? | Yes — Quality Gates com condicoes de fail e re-work |
| PRISMA 2020 compliance tracked? | Yes — Methodology-Auditor + Compliance-Formatter, 27 itens |
| Source traceability required? | Yes — Fact-Checkers A e B exigem source per claim |
| Journal strategy included? | Yes — Journal-Strategist com 3 recomendacoes |
| Submission-ready output? | Yes — manuscrito + audit trail + submission package |

Swarm prompt APPROVED para execucao.
