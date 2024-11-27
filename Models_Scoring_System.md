# Proposed Hybrid Scoring Framework

> [!CAUTION]
> ***Scoring Framework Beta Version***
> This evaluation system is **actively being developed and refined.** We welcome **community feedback and contributions through GitHub issues** to improve its accuracy and reliability.

## Core Components (100 points total)

### External Benchmarks (60 points)

#### Entity Benchmarks

- Artificial Analysis (when available)
- LiveCodeBench (when available)
- Big Code Models Leaderboard (when available)
- OpenVLM Leaderboard (when available)
- Open LLM Leaderboard (when available)
- MMBench Leaderboard (when available)

#### Dev Benchmarks

***Considered Benchmarks***

**General**
- MMLU
- MMLU Pro
- Multilingual MMLU 
- IFEval

**Reasoning**
- GPQA
- ARC-C

**Math**
- MATH
- GSM-8K

**Code**
- HumanEval
- HumanEval Plus

**Tool Use**
- API-Bank
- BFCL
- Gorilla Benchmark
- Nexus 

- MBPP
- MBPP Plus
- MultiPL-E
- Arena-Hard
- AlignBench
- Wild Bench
- MT-bench

### Community Assessment (40 points)

#### User Experience 

- Lmsys Arena Elo score (when available)
- OpenLM arena Elo score (when available)
- Imgsys Elo score (when available)

#### Technical Performance

- Price per USD per 1M Tokens
- Output Tokens per Second

### Score Calculation

Final Score = (External × 0.6) + (Community × 0.4)
