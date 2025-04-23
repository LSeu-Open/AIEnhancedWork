

## Scoring Framework Alpha Version (100 points total)

![Scoring_Framework](https://github.com/user-attachments/assets/f705f0d5-2859-4872-8b43-3c772c7ff8b6)

<br>

## Limitations of the current Framework 

### Potential Exclusion Scenarios

**External Benchmarks (60 points)**
- Models without public benchmark scores cannot be evaluated (Will become a exclusion rule in the final framework)
- Non-English models might be excluded from primarily English-based benchmarks (this is an issue LT)

**Community Assessment (20 points)**
- New models without sufficient arena participation would be disadvantaged (Score Adjustment and Weight Redistribution can partially resolve this until participation is sufficient) 
- Models not publicly available for testing would be excluded
- Regional models might lack sufficient community exposure (this is an issue LT)

**Technical Performance (20 points)**
- Open-source models might lack standardized pricing metrics (Score Adjustment and Weight Redistribution can resolve this)
- Research models might not have production-ready context windows (Score Adjustment and Weight Redistribution can resolve this)
- Specialized models might be unfairly judged on general performance ratios (this is an issue LT)

### Ideas to avoid Exclusion
- Create tiered evaluation categories (Research, Production, Specialized)
- Allow partial scoring with clear documentation of missing metrics
- Implement weighted adjustments for specialized models
- Temporary score until more metrics are available

<br>


## External Benchmarks (60 points)

### Entity Benchmarks (30 points)

#### Considered Entity Benchmarks for LLMS

**Generalist**
- [Artificial Analysis](https://artificialanalysis.ai/models)
- [Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
- [OpenCompass LLM Leaderboard](https://rank.opencompass.org.cn/leaderboard-llm/?m=25-01)
- [LiveBench Leaderboard](https://livebench.ai/#/)
- [LLM Explorer Leaderboard](https://llm.extractum.io/list/)
- [UGI Leaderboard](https://huggingface.co/spaces/DontPlanToEnd/UGI-Leaderboard)

**Coding**

- [Big Code Models Leaderboard](https://huggingface.co/spaces/bigcode/bigcode-models-leaderboard)
- [EvalPlus Leaderboard](https://evalplus.github.io/leaderboard.html)
- [Webdev Arena](https://web.lmarena.ai/leaderboard)

**Vision**

- [Open VLM Leaderboard](https://huggingface.co/spaces/opencompass/open_vlm_leaderboard)


#### Considered Entity Weighting

**Scaling Formula**

Entity Score = Final Score × (25/100)

When all benchmarks are available:
Each leaderboard gets equal weight: 10% (100% ÷ 10)

**Interpretation**

Score > 20 points (>80%) = Excellent Performance
- Indicates strong performance across multiple leaderboards
- Demonstrates consistent high ranking across different evaluation contexts

Score 15-20 points (60-80%) = Good Performance
- Shows competitive performance on most benchmarks
- May have some variation across different evaluation types

Score 10-15 points (40-60%) = Average Performance
- Indicates moderate ranking on leaderboards
- Performance may be inconsistent across different benchmarks

Score < 10 points (<40%) = Below Average Performance
- Shows weak comparative performance
- Significant room for improvement across multiple metrics
  
<br>

### Dev Benchmarks (30 points)

#### Why Non-Contaminated Benchmarks Should Have Higher Weights

**Statistical Reliability**

- Non-contaminated benchmarks provide more reliable and unbiased evaluation of true model capabilities
- Results from these benchmarks have higher statistical validity for comparing models
  
**Future Proofing**

- Clean benchmarks remain relevant even as training datasets evolve
- They provide consistent evaluation metrics across model generations
  
**True Performance Indication**

- Non-contaminated benchmarks better reflect real-world performance
- They test genuine learning rather than potential memorization

#### Considered Benchmarks for LLMS

### General knowledge and reasoning

| Benchmark            | Contamination Free | Weight |
|----------------------|--------------------|--------|
| MMLU                 | No                 | 3    |
| MMLU Pro             | No                 | 5    |
| BigBenchHard         | No                 | 3    |
| GPQA diamond         | Yes                | 7    |
| DROP                 | No                 | 3    |
| Humanity's Last Exam | No                 | 5    |
| HellaSwag            | No                 | 3    |
| ARC-C                | No                 | 3    |

### Instruction following

| Benchmark   | Contamination Free | Weight |
|-------------|--------------------|--------|
| Wild bench  | No                 | 3    |
| MT bench    | No                 | 3   |
| IFEval      | No                 | 3    |
| Arena Hard  | No                 | 3   |

### Math

| Benchmark | Contamination Free | Weight |
|-----------|--------------------|--------|
| Math      | No                 | 3    |
| GSM8K     | No                 | 3    |
| AIME      | No                 | 4   |

### Coding

| Benchmark      | Contamination Free | Weight |
|----------------|--------------------|--------|
| LiveCodeBench  | Yes                | 4    |
| Aider Polyglot | No                 | 2    |
| SWE-Bench      | No                 | 2    |
| SciCode        | Yes                | 4    |

### Multilingual

| Benchmark | Contamination Free | Weight |
|-----------|--------------------|--------|
| MGSM      | No                 | 2      |
| MMMLU     | No                 | 2      |
| C-Eval or CMMLU    | No        | 2      |
| AraMMLu   | No                 | 2      |

### Context

| Benchmark  | Contamination Free | Weight |
|------------|--------------------|--------|
| LongBench  | No                 | 2   |
| RULER 128K | No                 | 2    |
| RULER 32K  | No                 | 2    |
| MTOB       | No                 | 2    |

### Function calling (tool use and agent)

| Benchmark | Contamination Free | Weight |
|-----------|--------------------|--------|
| BFCL      | Yes                | 3    |
| AgentBench | No                | 2    |
| Gorilla   | No                 | 1    |
| ToolBench | No                 | 2    |
| MINT      | No                 | 2    |

### Vision

| Benchmark | Contamination Free | Weight |
|-----------|--------------------|--------|
| MMMU      | No                 | 2    |
| Mathvista | yes                | 3    |
| ChartQA   | No                 | 1    |
| DocVQA    | No                 | 1    |
| AI2D      | No                 | 1    |


<br>
<br>


**Scaling Formula**

Framework Score for dev Benchmarks section = Final Score × (35/100)

​
**Complete Example**

Final Dev Benchmarks = 83.84
Scale to framework points:
Framework Score = 83.84 × (35/100) = 29.34 points

This means:
Maximum possible: 35 points
Achieved score: 29.34 points
Performance percentage: 83.84%

**Interpretation**
Score > 30 points: Excellent performance
Score 25-30 points: Good performance
Score 20-25 points: Average performance
Score < 20 points: Below average performance

### Score Adjustment Formula

When benchmarks are missing, the total score should be normalized using:

$$ \text{Final Score} = \frac{\sum_{i=1}^{n} w_i s_i}{\sum_{i=1}^{n} w_i} \times 100 $$

Where:
- $$w_i$$ is the weight of benchmark i
- $$s_i$$ is the score of benchmark i
- n is the number of available benchmarks

#### Score Adjustment Formula Example  

Let's demonstrate the Score Adjustment Formula with a clear example:

| Benchmark | Score | Weight |
|-----------|--------|---------|
| MMLU | 85 | 6.0% |
| MMLU Pro | 90 | 5.5% |
| Multilingual MMLU | 80 | 5.0% |
| GSM-8K | 88 | 5.0% |
| API-Bank | 92 | 4.5% |
| BFCL | 78 | 10.0% |

When GSM-8K is Missing

Calculation:
1. Numerator = (85 × 6.0) + (90 × 5.5) + (80 × 5.0) + (92 × 4.5) + (78 × 10.0)
2. Denominator = 6.0 + 5.5 + 5.0 + 4.5 + 10.0
3. Final Score = (2601/31) × 100 = 83.84

The final score represents the weighted average of the available benchmarks, automatically adjusting for the missing GSM-8K benchmark.


### Weight Redistribution

For missing benchmarks, their weights are redistributed proportionally:

![image](https://github.com/user-attachments/assets/3269d940-333c-4819-b65c-20f31b6ac0d9)

![image](https://github.com/user-attachments/assets/8deb02f8-a8cf-4ec2-a7ad-0b7e6bc38095)

#### Weight Redistribution Example

If we have 3 benchmarks with original weights:
- A: 40%
- B: 35% 
- C: 25%

If benchmark C is missing:

$$ w'_A = 40 \times \frac{100}{75} = 53.33\% $$
$$ w'_B = 35 \times \frac{100}{75} = 46.67\% $$

This approach ensures:
- Fair comparison between models
- Maintenance of relative importance between remaining benchmarks
- Statistical validity of the final score
- 
<br>
<br>

## Community Benchs (20 points)

No sentiment analysis for now

### LMsys Arena Elo Score (10 points)

setup multiple time points via a early score (model just got released), and a late score (model has been released for a long time)

Provisional score (first month after release) : predictive scoring based on model architecture , tech specs, and model performance on the dev benchs.

Stable score (after 1 month) : based on the actual LMsys Arena score if it is available and with sufficient battles count or use the provisional score.

:TODO: the test implementation OK, need a robust dataset to train the model for a better prediction, feature correlation and hyperparameter tuning.


### Hugging Face Community Metrics (10 points)

hf community likes or monthly downloads

:TODO: Explore the hf community metrics and how it can be used to evaluate the community support of a model

**Scoring Formula**

Community Score = Normalized Elo × (20/100)

Normalized Elo = ((Model Elo − 1000) / 365) × 100

**Example**

For a model with 1250 Elo:

first Normalize: $\frac{1250 - 1000}{365} \times 100 = 68.49%$

Final Community Score: 68.49% x 20 = 13.70 points

**Interpretation**

Score > 16 points (Elo > 1300) = Elite Performance
- Consistently outperforms most models
- Top-tier user preference in blind comparisons

Score 12-16 points (Elo 1200-1300) = Strong Performance
- Competitive with leading models
- High user preference

Score 8-12 points (Elo 1100-1200) = Good Performance
- Above baseline performance
- Positive user reception

Score < 8 points (Elo ≤ 1000) = Average/Below Average
- Baseline or lower performance
- Mixed to negative user preference

<br>


## Technical Performance (20 points)

- Price (USD) per 1M Tokens
- Context window
- Model size vs. performance ratio

**Price (USD) per 1M Tokens (8 points)**

| Cost Range (USD/1M tokens) | Points |
|----------------------------|--------|
| < $0.10 | 8.0 |
| $0.10 - $0.50 | 7.0 |
| $0.50 - $1.00 | 6.0 |
| $1.00 - $3.00 | 5.0 |
| $3.00 - $5.00 | 4.0 |
| $5.00 - $10.00 | 3.0 |
| $10.00 - $20.00 | 2.0 |
| > $20.00 | 1.0 |

**Context Window (6 points)**

| Window Size | Points |
|-----------|--------|
| > 1M      |	6.0 |
| 200K - 1M |	5.0 |
| 100K - 200K |	4.0 |
| 32K - 100K |	3.0 |
| 8K - 32K   |	2.0 |
| < 8K      |	1.0 |

**Model Size vs Performance Ratio (6 points)**

| Combined Score | Points |
|----------------|--------|
| ≥ 1.0          | 6.0 |
| 0.8 - 0.99     | 5.0 |
| 0.6 - 0.79     | 4.0 |
| 0.4 - 0.59     | 3.0 |
| 0.2 - 0.39     | 2.0 |
| < 0.2         | 1.0 |

Where Combined Score = (Average Benchmark Score × Efficiency Factor)

Efficiency Factor:

<15B params: 1.0
15-40B params: 0.9
40-70B params: 0.8
70-100B params: 0.7
>100B params: 0.6

<br>
<br>

### Exploring Problematic scenarios

#### No Community score (no Elo grading from leaderboard)

**Potential Model Categories for This Scenario**

- Research Models: Models developed by academic institutions or research organizations, often focusing on specific aspects of a larger problem.
- Niche Models: Models created by specialized entities or small teams, tailored to address unique or particular challenges within the broader context.

**Redistribution Method**

New Point Distribution (100 points total)
- External Benchmarks: 75 points
  - Entity Benchmarks: 31.25 points (previously 25)
  - Dev Benchmarks: 43.75 points (previously 35)
- Technical Performance: 25 points (previously 20)

**Calculation Formula**

Adjustment Factor = 100/80 = 1.25

For each remaining category

New Score = Original Score × 1.25

**Implementation Example**

If a model scores:
Entity Benchmarks: 20/25 points
Dev Benchmarks: 28/35 points
Technical Performance: 15/20 points

New adjusted scores:
Entity Benchmarks: 20 × 1.25 = 25/31.25 points
Dev Benchmarks: 28 × 1.25 = 35/43.75 points
Technical Performance: 15 × 1.25 = 18.75/25 points
Total Final Score: 78.75/100 points

This approach maintains the relative importance of each category while ensuring the final score remains on a 100-point scale.

<br>
<br>
<br>

## Calculation

Final Score = (External × 0.6) + (Community × 0.2) + (Technical × 0.2)

<br>
<br>

## Citations

- [1] https://docs.confident-ai.com/docs/benchmarks-mmlu
- [2] https://paperswithcode.com/dataset/mmlu
- [3] https://klu.ai/glossary/mmlu-pro-eval
- [4] http://arxiv.org/abs/2311.07911
- [5] https://paperswithcode.com/dataset/arena-hard
- [6] https://datatunnel.io/glossary/gpqa/
- [7] https://datatunnel.io/glossary/arc-c/
- [8] https://www.charlesrathkopf.net/publication/bigbench/bigbench.pdf
- [9] https://www.theainavigator.com/blog/what-is-truthfulqa
- [10] https://paperswithcode.com/dataset/alignbench
- [11] https://arxiv.org/html/2406.04770v1
- [12] https://klu.ai/glossary/mt-bench-eval
- [13] https://klu.ai/glossary/math-eval
- [14] https://docs.confident-ai.com/docs/benchmarks-gsm8k
- [15] https://klu.ai/glossary/humaneval-benchmark
- [16] https://evalplus.github.io/leaderboard.html
- [17] https://arxiv.org/html/2410.06992v1
- [18] https://aclanthology.org/2023.emnlp-main.187.pdf
- [19] https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html
- [20] https://arxiv.org/pdf/2305.15334.pdf
