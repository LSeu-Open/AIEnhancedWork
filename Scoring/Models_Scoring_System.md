# Proposed Hybrid Scoring Framework

> [!IMPORTANT]
> ***Scoring Framework Alpha Version***
> 
> This evaluation system provides an objective way to assess LLM models through standardized metrics.  We welcome **community feedback and contributions through GitHub issues** to improve its accuracy and reliability.
>
> To use the [framework](https://github.com/LSeu-Open/AIEnhancedWork/tree/main/Scoring) :
> 
> Download both script files.
>
> Input your benchmark results and metrics in ```run_scoring.py```.
>
> Then Run ```run_scoring.py``` to generate a comprehensive model assessment.
>
> ***Note: This is an alpha release. Metrics and scoring criteria may be refined in future versions.***

> [!NOTE]
> **Current Support:**
> 
> General-purpose Large Language Models (LLMs)
>
> **Upcoming tailored Scripts:**
>
> Vision Language Models (VLMs)
>
> Code-specialized Language Models

<div align="center" > <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Triangular%20Flag.png" alt="Triangular Flag" width="25" height="25" /> Current Version of the Scoring System : Alpha v0.2 <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Triangular%20Flag.png" alt="Triangular Flag" width="25" height="25" /> </div>

<br>

## Scoring Framework Alpha Version (100 points total)

![Scoring_Framework](https://github.com/user-attachments/assets/f705f0d5-2859-4872-8b43-3c772c7ff8b6)

<br>

## Limitations of the current Framework 

### Potential Exclusion Scenarios

**External Benchmarks (60 points)**
- Models without public benchmark scores cannot be evaluated (Will become a exclusion rule in the final framework)
- Small or specialized models may not have resources to participate in all required benchmarks (Score Adjustment and Weight Redistribution can resolve this)
- Non-English models might be excluded from primarily English-based benchmarks (this is an issue LT)

**Community Assessment (20 points)**
- New models without sufficient arena participation would be disadvantaged (Score Adjustment and Weight Redistribution can partially resolve this until participation is sufficient) 
- Models not publicly available for testing would be excluded (Will become a exclusion rule in the final framework)
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

### Entity Benchmarks (25 points)

#### Considered Entity Benchmarks for LLMS

- [Artificial Analysis](https://artificialanalysis.ai/models)
- [LiveCodeBench](https://livecodebench.github.io/leaderboard.html)
- [Big Code Models Leaderboard](https://huggingface.co/spaces/bigcode/bigcode-models-leaderboard)
- [Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)

#### Considered Entity Weighting

**Scaling Formula**

Entity Score = Final Score × (25/100)

When all benchmarks are available:
Each leaderboard gets equal weight: 25% (100% ÷ 4)
 
**Example Calculation**

If a model scores:

Artificial Analysis: 82%
LiveCodeBench: Not Available
Big Code Models: 75%
Open LLM: 85%


Adjust weights for 3 available benchmarks:
33% each

Calculate weighted average:
Final Score = (82×20)+(75×20)+(85×20)/100= 80.66%  
​
Scale to framework points:
Entity Score = 80.66 × (25/100) = 20.165 points

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

### Dev Benchmarks (35 points)

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

##### General Reasoning and Comprehension

| Benchmark | Handles Contamination | Description |
|-----------|---------------------|-------------|
| MMLU | Yes | 3.5% |
| MMLU Pro | Unknown | 5.5% |
| BigBench | No | Large-scale tasks testing model capabilities |
| DROP | No | Tests numerical reasoning and reading comprehension |
| HellaSwag | No | Evaluates commonsense completion prediction |
| GPQA | Yes | Graduate-level science questions with contamination resistance |
| ARC-C | No | Tests commonsense and implicit knowledge |
| LiveBench | Yes | Continuously updated questions from recent sources |
| LatestEval | Yes | Uses recent data to prevent memorization |

##### Instruction Following

| Benchmark | Handles Contamination | Description |
|-----------|---------------------|-------------|
| AlignBench | Yes | Tests Chinese language model alignment |
| Wild Bench | No | Real-world user query evaluation |
| MT-bench | No | Multi-turn conversation assessment |
| IFEval | No | Instruction following evaluation |
| Arena-Hard | No | Challenging user queries from Chatbot Arena |
| TruthfulQA | No | Tests factual accuracy and truthfulness |

##### Mathematical Reasoning

| Benchmark | Handles Contamination | Description |
|-----------|---------------------|-------------|
| MATH | No | Mathematical problem-solving evaluation |
| GSM-8K | No | Grade school math word problems |
| MGSM | No | Multilingual grade school math problems |

##### Code Generation

| Benchmark | Handles Contamination | Description |
|-----------|---------------------|-------------|
| HumanEval | No | Programming challenges for code generation |
| HumanEval Plus | No | Extended version with additional tests |
| MBPP | No | Python programming problems |
| MBPP Plus | No | Enhanced MBPP with more test cases |

##### Tool Use

| Benchmark | Handles Contamination | Description |
|-----------|---------------------|-------------|
| SWE-bench | No | Software engineering problem solving |
| API-Bank | No | API usage scenario testing |
| BFCL | Yes | Berkeley Function-Calling evaluation |
| Gorilla | No | API interaction capability testing |
| Nexus | No | Tool and API usage assessment |


<br>
<br>

New weighted distribution that accounts for both contamination sensitivity and the different benchmark categories

##### General Reasoning and Comprehension (35%)

| Benchmark Name | Contamination Sensitive | Weight |
|----------------|------------------------|---------|
| MMLU | No | 3.0% |
| MMLU Pro | Yes | 8.0% |
| BigBench | Yes | 3.0% |
| DROP | No | 7.0% |
| HellaSwag | No | 7.0% |
| GPQA | Yes | 2.0% |
| ARC-C | Yes | 2.0% |
| LiveBench | Yes | 1.5% |
| LatestEval | Yes | 1.5% |

##### Instruction Following (25%)

| Benchmark Name | Contamination Sensitive | Weight |
|----------------|------------------------|---------|
| AlignBench | Unknown | 4.0% |
| Wild Bench | Yes | 4.0% |
| MT-bench | Yes | 4.0% |
| IFEval | Yes | 4.0% |
| Arena-Hard | Yes | 4.5% |
| TruthfulQA | Yes | 4.5% |

##### Mathematical Reasoning (15%)

| Benchmark Name | Contamination Sensitive | Weight |
|----------------|------------------------|---------|
| MATH | Yes | 4.0% |
| GSM-8K | Yes | 4.0% |
| MGSM | No | 7.0% |

##### Code Generation (12%)

| Benchmark Name | Contamination Sensitive | Weight |
|----------------|------------------------|---------|
| HumanEval | Yes | 3.0% |
| HumanEval Plus | Yes | 3.0% |
| MBPP | Yes | 3.0% |
| MBPP Plus | Yes | 3.0% |

##### Tool Use (13%)

| Benchmark Name | Contamination Sensitive | Weight |
|----------------|------------------------|---------|
| SWE-bench | Yes | 2.0% |
| API-Bank | Yes | 2.0% |
| BFCL | No | 5.0% |
| Gorilla Benchmark | Yes | 2.0% |
| Nexus | Yes | 2.0% |

This distribution:
- Prioritizes non-contaminated benchmarks with higher weights
- Maintains category importance (General > Instruction > Math > Code/Tool)
- Allocates more weight to fundamental capabilities
- Ensures all weights sum to 100%

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

## Community Assessment (20 points)

- Lmsys Arena Elo score (when available)
- OpenLM arena Elo score (when available)

**Scoring Formula**

Community Score = Normalized Elo × (20/100)
 
**Elo Score Normalization**

Based on current arena standings:

- Top performers: ~1300-1365 Elo
- Strong performers: ~1200-1300 Elo
- Average performers: ~1100-1200 Elo
- Base rating: 1000 Elo

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

- Price per USD per 1M Tokens
- Context window
- Model size vs. performance ratio

**Price per USD per 1M Tokens (8 points)**

| Cost Range (USD/1M tokens) | Points |
|-----------|--------|
|< $1 |	8.0 |
| $1 - $3 |	7.0 |
| $3 - $5 |	6.0 |
| $5 - $10 | 5.0 |
| $10 - $20 |	4.0 |
| > $20 |	3.0 |
| > $40 |	2.0 |
| > $80 |	1.0 |

**Context Window (6 points)**

| Window Size | Points |
|-----------|--------|
| > 200K |	6.0 |
| > 100K |	5.0 |
| 32K - 100K |	4.0 |
| 16K - 32K |	3.0 |
| 8K - 16K |	2.0 |
| < 8K	| 1.0 |

**Model Size vs Performance Ratio (6 points)**

|Performance & Size Category |	Points |
|-----------|--------|
| Excellent (≥85% benchmark) with Size Efficiency* | 	6.0 |
| Good (75-84% benchmark) with Size Efficiency* |	5.0 |
| Decent (65-74% benchmark) with Size Efficiency* |	4.0 |
| Moderate (55-64% benchmark) |	3.0 |
| Poor (<55% benchmark) |	2.0 |

Size Efficiency Thresholds:
- Ultra Efficient (<15B params): No reduction in base score
- Very Efficient (15-29B params): Max 5.5 points
- Efficient (30-39B params): Max 5.0 points
- Moderate (40-69B params): Max 4.0 points
- Large (≥70B params): Max 3.0 points

*Final score is the minimum between the performance-based score and the size efficiency maximum threshold.

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
