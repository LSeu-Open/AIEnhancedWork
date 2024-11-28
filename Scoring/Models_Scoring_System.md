# Proposed Hybrid Scoring Framework

> [!CAUTION]
> ***Scoring Framework Alpha Version***
> This evaluation system is **actively being developed and refined.** We welcome **community feedback and contributions through GitHub issues** to improve its accuracy and reliability.

<br>

## Scoring Framework Alpha Version (100 points total)

![Scoring_Framework](https://github.com/user-attachments/assets/f705f0d5-2859-4872-8b43-3c772c7ff8b6)

## Alpha ruleset

### Mandatory Requirements
- Models must have publicly available benchmark scores
- Models must be publicly available for testing
- Models must have at least one verifiable benchmark score in each major category

### Rules with Adjustments

**Benchmark Flexibility**
- Minimum 50% of required benchmarks must be completed
- Missing benchmarks trigger weight redistribution
- Specialized models can substitute domain-specific benchmarks

**Community Assessment**
- New models get 2-month grace period with weight redistribution
- Alternative feedback methods accepted during grace period
- Regional models can use local community metrics

**Technical Performance**
- Open-source models can use estimated pricing based on deployment costs
- Research models evaluated on available metrics with adjusted weights
- Specialized models compared within their category only

### Documentation Requirements
- Clear marking of missing metrics
- Justification for weight redistributions
- Temporary score validity period

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

## External Benchmarks (60 points)

### Entity Benchmarks (25 points)

- Artificial Analysis (when available)
- LiveCodeBench (when available)
- Big Code Models Leaderboard (when available)
- OpenVLM Leaderboard (when available)
- Open LLM Leaderboard (when available)
- MMBench Leaderboard (when available)

**Scaling Formula**

Entity Score = Final Score × (25/100)

When all benchmarks are available:
Each leaderboard gets equal weight: 16.67% (100% ÷ 6)
 
**Example Calculation**

If a model scores:
Artificial Analysis: 82%
LiveCodeBench: Not Available
Big Code Models: 75%
OpenVLM: 90%
Open LLM: 85%
MMBench: 88%

Adjust weights for 5 available benchmarks:
20% each

Calculate weighted average:
Final Score = (82×20)+(75×20)+(90×20)+(85×20)+(88×20)/100= 84% 
​
Scale to framework points:
Entity Score = 84 × (25/100) = 21 points

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

**Why Non-Contaminated Benchmarks Should Have Higher Weights**

**Statistical Reliability**

- Non-contaminated benchmarks provide more reliable and unbiased evaluation of true model capabilities
- Results from these benchmarks have higher statistical validity for comparing models
  
**Future Proofing**

- Clean benchmarks remain relevant even as training datasets evolve
- They provide consistent evaluation metrics across model generations
  
**True Performance Indication**

- Non-contaminated benchmarks better reflect real-world performance
- They test genuine learning rather than potential memorization

Here's the weighted distribution for benchmarks:

> **Weight distribution principles**
>
> Non-contaminated benchmarks (BFCL): 10%
> Unknown contamination status (MMLU Pro, AlignBench): 5.5% each
> Contaminated benchmarks: 3.5% each


***Considered Benchmarks for LLMS***

| Benchmark Name | Contamination Sensitive | Description |
|:--------------:|:-----------------------:|-------------|
| MMLU | Yes | Multiple-choice questions covering 57 subjects across STEM, humanities, and social sciences. [1][2] |
| MMLU Pro | No | Enhanced version of MMLU with expanded task diversity and increased complexity. [3] |
| Multilingual MMLU | Yes | Multilingual version of MMLU testing language understanding across different languages. |
| IFEval | Yes | Evaluates instruction-following capabilities through verifiable instructions. [4] |
| Arena-Hard | Yes | 500 challenging user queries from Chatbot Arena, designed to robustly separate model capabilities. [5] |
| GPQA | Yes | Graduate-level questions in biology, physics, and chemistry requiring expert knowledge. [6] |
| ARC-C | Yes | Multiple-choice questions testing commonsense reasoning and implicit knowledge. [7] |
| BigBench | Yes | Comprehensive benchmark focusing on tasks beyond current model capabilities. [8] |
| TruthfulQA | Yes | Evaluates truthfulness and factual accuracy in model responses. [9] |
| AlignBench | No | Evaluates alignment performance of Chinese language models. [10] |
| Wild Bench | Yes | 1,024 tasks from real-world user queries testing model capabilities. [11] |
| MT-bench | Yes | Multi-turn benchmark testing conversation flow and instruction following. [12] |
| MATH | Yes | Comprehensive evaluation of mathematical problem-solving abilities. [13] |
| GSM-8K | Yes | 1,319 grade school math word problems requiring multi-step reasoning. [14] |
| HumanEval | Yes | 164 hand-crafted programming challenges testing code generation. [15] |
| HumanEval Plus | Yes | Enhanced version of HumanEval with additional test cases |
| MBPP | Yes | Collection of verified Python programming problems. [16] |
| MBPP Plus | Yes | Enhanced version of MBPP with additional test cases. [16] |
| SWE-bench | Yes | Evaluates capability in resolving real-world software issues. [17] |
| API-Bank | Yes | Tests tool-augmented LLMs through API usage scenarios. [18] |
| BFCL | No | Berkeley Function-Calling Leaderboard testing function-calling capabilities. [19] |
| Gorilla Benchmark | Yes | Evaluates API interaction capabilities across multiple frameworks. [20] |
| Nexus | Yes | Tests model's ability to use tools and APIs |

<br>

| Benchmark Name | Contamination Sensitive | Percentage Weight |
|----------------|------------------------|-------------------|
| MMLU | Yes | 3.5% |
| MMLU Pro | Unknown | 5.5% |
| Multilingual MMLU | Yes | 3.5% |
| IFEval | Yes | 3.5% |
| Arena-Hard | Yes | 3.5% |
| GPQA | Yes | 3.5% |
| ARC-C | Yes | 3.5% |
| BigBench | Yes | 3.5% |
| TruthfulQA | Yes | 3.5% |
| AlignBench | Unknown | 5.5% |
| Wild Bench | Yes | 3.5% | 
| MT-bench | Yes | 3.5% |
| MATH | Yes | 3.5% |
| GSM-8K | Yes | 3.5% |
| HumanEval | Yes | 3.5% |
| HumanEval Plus | Yes | 3.5% |
| MBPP | Yes | 3.5% |
| MBPP Plus | Yes | 3.5% |
| SWE-bench | Yes | 3.5% |
| API-Bank | Yes | 3.5% |
| BFCL | No | 10.0% |
| Gorilla Benchmark | Yes | 3.5% |
| Nexus | Yes | 3.5% |

<br>
<br>

***Considered Benchmarks for VLMS***

| Benchmark Name | Contamination Sensitive | Description |
|:--------------:|:-----------------------:|-------------|
| MMMU | Yes | Multimodal understanding benchmark testing various visual and language tasks |
| MathVista | Yes | Tests mathematical reasoning abilities with visual inputs |
| MMStar | Yes | Evaluates multimodal understanding across diverse visual scenarios |
| DocVQA | Yes | Question answering tasks on document images |
| TextVQA | Yes | Visual questions requiring text reading and comprehension in images |
| InfoVQA | Yes | Information extraction and question answering from visual data |
| ChartQA | Yes | Question answering tasks specifically for charts and graphs |
| OCRBench | Yes | Tests optical character recognition capabilities in various contexts |
| MTVQA | No | Multilingual and multimodal question answering on TV show content |
| VCR | Yes | Visual Commonsense Reasoning with complex scene understanding |
| MMBench | Yes | Comprehensive multimodal benchmark testing various capabilities |
| MMT-Bench | Yes | Multi-turn conversations about visual content |
| HallBench | Yes | Tests hallucination detection in multimodal responses |
| AI2 Diagram | Yes | Understanding and reasoning about scientific diagrams |
| MVBench | Yes | Motion and video understanding benchmark |
| PerceptionTest | Yes | Tests visual perception and understanding capabilities |
| EgoSchema | No | Evaluates understanding of egocentric video content |
| Video-MME | Yes | Multimodal evaluation focusing on video understanding |

<br>

> Weight distribution principles
> 
> Non-contaminated benchmarks (MTVQA, EgoSchema): 12% each
> 
> Contaminated benchmarks: 4% each

Here's the revised VLMs benchmark table with weights prioritizing non-contaminated benchmarks:

| Benchmark Name | Contamination Sensitive | Percentage Weight |
|----------------|------------------------|-------------------|
| MMMU | Yes | 4.0% |
| MathVista | Yes | 4.0% |
| MMStar | Yes | 4.0% |
| DocVQA | Yes | 4.0% |
| TextVQA | Yes | 4.0% |
| InfoVQA | Yes | 4.0% |
| ChartQA | Yes | 4.0% |
| OCRBench | Yes | 4.0% |
| MTVQA | No | 12.0% |
| VCR | Yes | 4.0% |
| MMBench | Yes | 4.0% |
| MMT-Bench | Yes | 4.0% |
| HallBench | Yes | 4.0% |
| AI2 Diagram | Yes | 4.0% |
| MVBench | Yes | 4.0% |
| PerceptionTest | Yes | 4.0% |
| EgoSchema | No | 12.0% |
| Video-MME | Yes | 4.0% |


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

|Ratio Category | Points |
|-----------|--------|
| Exceptional (>90% benchmark score at <70B params) |	6.0 |
| Strong (>80% benchmark score at <70B params) |	5.0 |
| Good (>70% benchmark score at <70B params) |	4.0 |
| Average (>60% benchmark score at any size) |	3.0 |
| Below Average (<60% benchmark score) |	2.0 |


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
