
<div align="center"> 

<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/LLMScoreEngine.png">

<br>
<br>

***A comprehensive system for evaluating and scoring large language models based on multiple criteria.***

<br>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat)](https://github.com/LSeu-Open/LLMScoreEngine/blob/main/LICENSE)
![LastCommit](https://img.shields.io/github/last-commit/LSeu-Open/LLMScoreEngine?style=flat)
![LastRelease](https://img.shields.io/github/v/release/LSeu-Open/LLMScoreEngine?style=flat)

</div>

<br>

This framework aims to provide a comprehensive system for evaluating and scoring large language models based on multiple criteria.

Since benchmarks cannot always be trusted and existing leaderboards typically focus only on one aspect of modern LLMs' capabilities, we chose to develop our own approach.

Our approach aims to cover a wide range of benchmarks, leaderboards, community assessments, and technical specifications, trying to provide an unbiased estimation of the overall capacities of any public LLM.


> [!NOTE]
> ***Formerly developed within this repository, the scoring framework is now under development in a dedicated repository [LLMScoreEngine](https://github.com/LSeu-Open/LLMScoreEngine).***

<br>

 ## V0.4.0 Score Components Explanation  (100 points total)
 
 ## Entity Benchs (30 points)

### Generalist

Artificial Analysis Intelligence Score (10 %)
OpenCompass LLM Average Score (10 %)
LLM Explorer Score (10 %)
Livebench Average Score (10 %)
Open LLM Leaderboard AverageScore (10 %)
UGI Leaderboard UGI Score (10 %)

### Coding

BigCodeBench Leaderboard Score (10 %)
EvalPlus Leaderboard Pass@1 score (10 %)
Webdev Arena score (10 %)

### Vision

Open VLM Leaderboard Average Score (10 %)


## Dev Benchs (30 points)

We try to cover every area of the capacity of the modern SOTA models.

We give higher value (weight) to benchmarks that are aware of data contamination.

the benchmarks cover area of multimodal models.

### General knowledge and reasoning

| Benchmark            | Contamination Free | Weight |
|----------------------|--------------------|--------|
| MMLU                 | No                 | 3    |
| MMLU Pro             | No                 | 5    |
| BigBenchHard         | No                 | 3    |
| GPQA diamond         | Yes                | 7    |
| DROP                 | No                 | 3    |
| Humanity's Last Exam | No                 | 4    |
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
| HumanEval      | No                 | 1    |
| Mbp            | No                 | 1    |
| LiveCodeBench  | Yes                | 4    |
| Aider Polyglot | No                 | 2    |
| SWE-Bench      | No                 | 2    |
| SciCode        | Yes                | 3    |

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


**Formula**

Framework Score for dev Benchmarks section = Final Score × (3à/100)

​
**Complete Example**

Final Dev Benchmarks = 83.84
Scale to framework points:
Framework Score = 83.84 × (30/100) = 25.152 points

This means:
Maximum possible: 30 points
Achieved score: 25.152 points
Performance percentage: 83.84%

**Interpretation**
Score >= 25: Excellent
Score 20-25: Good
Score 15-20: Average
Score < 15: Below average

### Framework Score Calculation

The final score for the Dev Benchmarks section (out of 100) is scaled to fit the framework's total point allocation for this category (30 points).

**Formula:**

\[ \text{Framework Score} = \text{Final Score} \times \frac{30}{100} \]

*   `Final Score`: The calculated weighted score (0-100) based on available benchmarks.
*   `Framework Score`: The score for this section contributing to the total framework score (0-30).

**Example:**

If a model achieves a `Final Score` of `83.84` across the available benchmarks (calculated as shown below):

\[ \text{Framework Score} = 83.84 \times \frac{30}{100} \approx 25.15 \]

This model would receive approximately **25.15** points (out of a possible 30) for the Dev Benchmarks category.

**Interpretation (Based on 0-30 Framework Score):**

*   Score >= 25: Excellent performance
*   Score 20-25: Good performance
*   Score 15-20: Average performance
*   Score < 15: Below average performance

### Benchmark Score Normalization and Weighting

**Score Normalization (`s_i`):**
The raw results from different benchmarks (e.g., MMLU accuracy, HumanEval pass@k) need to be normalized onto a consistent scale, typically 0-100, to be used as the score (`s_i`) in the final calculation. **The specific normalization method for each benchmark (e.g., linear scaling, percentile ranking) needs to be defined.**

**Weight Calculation (`w_i`):**
The weights assigned in the benchmark tables (e.g., MMLU: 3, GPQA: 7) represent relative importance. These need to be converted into percentage weights (`w_i`) used in the final scoring formula. **The specific method for converting table weights into formula weights (`w_i`) needs to be defined (e.g., normalizing the sum of all weights across all categories to 100%).**

### Final Score Calculation (Handling Missing Benchmarks)

When benchmark scores are available, the `Final Score` (0-100 scale) is calculated as the weighted average of the normalized scores for the *available* benchmarks. This formula inherently handles missing benchmarks by only considering the weights and scores of those that are present, automatically preserving the relative importance of the remaining benchmarks.

**Formula:**

\[ \text{Final Score} = \frac{\sum_{i=1}^{n} w_i s_i}{\sum_{i=1}^{n} w_i} \]

Where:
*   `n`: The number of *available* benchmarks for the model.
*   `w_i`: The defined percentage weight of available benchmark `i`.
*   `s_i`: The normalized score (0-100) for available benchmark `i`.

**Example (Illustrative - Assumes weights `w_i` and scores `s_i` are defined):**

Suppose a model has the following *available* normalized scores and *defined* percentage weights:

| Benchmark         | Normalized Score (`s_i`) | Defined Weight (`w_i`) | `w_i * s_i` |
|-------------------|--------------------------|------------------------|-------------|
| MMLU              | 85                       | 6.0                    | 510         |
| MMLU Pro          | 90                       | 5.5                    | 495         |
| Multilingual MMLU | 80                       | 5.0                    | 400         |
| *GSM-8K (Missing)*| *-*                      | *(5.0)*               | *-*         |
| API-Bank          | 92                       | 4.5                    | 414         |
| BFCL              | 78                       | 10.0                   | 780         |
| **Totals**        |                          | **31.0** (`sum(w_i)`)  | **2599** (`sum(w_i*s_i)`) |

**Calculation:**

\[ \text{Final Score} = \frac{2599}{31.0} \approx 83.84 \]

The final score of 83.84 reflects the weighted performance across the benchmarks for which scores were provided, correctly adjusting for the absence of GSM-8K. This score is then used to calculate the `Framework Score` (approximately 25.15 in this case).

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


## Community Benchs (20 points)

:NOTE: No sentiment analysis for now

### LMsys Arena Elo Score (10 points)

setup multiple time points via a early score (model just got released), and a late score (model has been released for a long time)

Provisional score (first month after release) : predictive scoring based on model architecture , tech specs, and model performance on the dev benchs.

Stable score (after 1 month) : based on the actual LMsys Arena score if it is available and with sufficient battles count or use the provisional score.

:TODO: the test implementation OK, need a robust dataset to train the model for a better prediction, feature correlation and hyperparameter tuning.

:TODO: Need more definition on how to handle models not on LMsys arena (Use the provisional score as potentiel usable score ??)


### Hugging Face Community Metrics (10 points)

In order to avoid over reliance on the LMsys Arena score, we will try to use a custom Hugging Face Community Score as a complement.

The Hugging Face Community Score (0-10 points) evaluates a model's community adoption and maturity using three weighted components:

**Downloads (4 points)**

Points are awarded based on the model's download count (`D`). The scoring uses a logarithmic scale (base 2) to reflect the diminishing returns of higher download counts, ensuring significant gains for initial adoption and smaller gains for massive adoption levels.

*   **Formula:** `Points ≈ 0.2007 * log2(D) - 0.6667`
    *   Where `D` is the download count.
    *   `log2` is the logarithm base 2.
*   **Minimum Points:** If `D < 10`, `Points = 0.0`.
*   **Maximum Points:** The calculated score is capped at `4.0`.
*   **Calculation:** `Points = max(0.0, min(4.0, 0.2007 * log2(D) - 0.6667))` (for D >= 10)

*Example Scores (Approximate):*
*   10 downloads (`D=10`): `max(0.0, min(4.0, 0.2007*3.32 - 0.6667)) ≈ max(0.0, min(4.0, 0.00)) = 0.0` points
*   1K downloads (`D=1000`): `max(0.0, min(4.0, 0.2007*9.97 - 0.6667)) ≈ max(0.0, min(4.0, 1.33)) = 1.3` points
*   100K downloads (`D=100000`): `max(0.0, min(4.0, 0.2007*16.61 - 0.6667)) ≈ max(0.0, min(4.0, 2.67)) = 2.7` points
*   10M downloads (`D=10000000`): `max(0.0, min(4.0, 0.2007*23.25 - 0.6667)) ≈ max(0.0, min(4.0, 4.00)) = 4.0` points

This formula provides a continuous score reflecting download popularity, replacing the previous discrete table.

**Likes (4 points)**

Points are awarded based on the model's likes count (`L`) on platforms like Hugging Face. The scoring uses a logarithmic scale (base 2) to reflect community appreciation, where initial likes contribute more significantly to the score than later ones.

*   **Formula:** `Points ≈ 0.477 * log2(L) - 0.756`
    *   Where `L` is the likes count.
    *   `log2` is the logarithm base 2.
*   **Minimum Points:** If `L < 3`, `Points = 0.0`.
*   **Maximum Points:** The calculated score is capped at `4.0`.
*   **Calculation:** `Points = max(0.0, min(4.0, 0.477 * log2(L) - 0.756))` (for L >= 3)

*Example Scores (Approximate):*
*   3 likes (`L=3`): `max(0.0, min(4.0, 0.477*1.58 - 0.756)) ≈ max(0.0, min(4.0, 0.00)) = 0.0` points
*   10 likes (`L=10`): `max(0.0, min(4.0, 0.477*3.32 - 0.756)) ≈ max(0.0, min(4.0, 0.83)) = 0.8` points
*   100 likes (`L=100`): `max(0.0, min(4.0, 0.477*6.64 - 0.756)) ≈ max(0.0, min(4.0, 2.41)) = 2.4` points
*   1,000 likes (`L=1000`): `max(0.0, min(4.0, 0.477*9.97 - 0.756)) ≈ max(0.0, min(4.0, 4.00)) = 4.0` points

This formula provides a continuous score reflecting community validation, replacing the previous discrete table.

**Age/Maturity (2 points)**

Points are awarded based on the model's age (`M` in months since release or significant update). The scoring aims to balance maturity (indicating stability and community testing) with recency (reducing the risk of outdatedness). The score increases linearly to a peak at 12 months and then drops to a stable value.

*   **Formula (Piecewise Linear):**
    *   If `0 <= M < 1`: `Points = 0.5 * M`
    *   If `1 <= M < 3`: `Points = 0.5 + 0.5 * (M - 1)`
    *   If `3 <= M <= 12`: `Points = 1.5 + (0.5 / 9) * (M - 3)`
    *   If `M > 12`: `Points = 1.5`
*   **Maximum Points:** The score peaks at `2.0` when `M = 12`.
*   **Minimum Points:** The score approaches `0.0` as `M` approaches 0.

*Example Scores (Approximate):*
*   0.5 months (`M=0.5`): `0.5 * 0.5 = 0.25` points
*   2 months (`M=2`): `0.5 + 0.5 * (2 - 1) = 1.0` points
*   6 months (`M=6`): `1.5 + (0.5 / 9) * (6 - 3) ≈ 1.5 + 0.167 = 1.67` points
*   12 months (`M=12`): `1.5 + (0.5 / 9) * (12 - 3) = 1.5 + 0.5 = 2.0` points
*   18 months (`M=18`): `1.5` points

This formula provides a continuous score reflecting the trade-off between model maturity and recency, replacing the previous discrete table.

This balanced approach produces a score that effectively differentiates between:

| Score Range | Model Category |
|-------------|----------------|
| <3 points | Niche models |
| 3-6 points | Moderately adopted models |
| 6-8 points | Community favorites |
| 8-10 points | Industry-leading models |

## Technical Performance (20 points) => Fully implemented

- Price (USD) per 1M Tokens
- Context window
- Efficiency and Performance Balance 

**Price (USD) per 1M Tokens (8 points)**

Points are awarded based on the cost per 1 million tokens (e.g., using the average of input and output costs if they differ). The scoring follows a linear scale designed to heavily reward lower prices:

*   **Formula:** `Points = 8.0 - (0.35 * Price)`
    *   Where `Price` is the cost in USD per 1M tokens.
*   **Maximum Points:** If `Price <= $0.00`, `Points = 8.0`.
*   **Minimum Points:** If `Price >= $20.00`, `Points = 1.0`.

This formula ensures that points decrease linearly from a maximum of 8.0 for free models down to a minimum of 1.0 for models costing $20.00 or more per 1M tokens. This approach provides a continuous score reflecting cost-effectiveness without discrete steps.

**Context Window (6 points)**

Points are awarded based on the model's maximum context window size in tokens (`W`). The scoring uses a logarithmic scale (base 2) to reflect the diminishing marginal value of extremely large context windows, ensuring significant gains for initial increases (e.g., 8K to 32K) and smaller gains for very large increases (e.g., 1M to 2M).

*   **Formula:** `Points ≈ 0.571 * log2(W) - 5.929`
    *   Where `W` is the context window size in tokens.
    *   `log2` is the logarithm base 2.
*   **Minimum Points:** If `W < 8192`, `Points = 1.0`.
*   **Maximum Points:** The calculated score is capped at `6.0`.
*   **Calculation:** `Points = max(1.0, min(6.0, 0.571 * log2(W) - 5.929))`

*Example Scores:*
*   8K tokens (`W=8192`): `max(1.0, min(6.0, 0.571*13 - 5.929)) ≈ max(1.0, min(6.0, 1.49)) = 1.5` points
*   32K tokens (`W=32768`): `max(1.0, min(6.0, 0.571*15 - 5.929)) ≈ max(1.0, min(6.0, 2.64)) = 2.6` points
*   128K tokens (`W=131072`): `max(1.0, min(6.0, 0.571*17 - 5.929)) ≈ max(1.0, min(6.0, 3.78)) = 3.8` points
*   1M tokens (`W=1048576`): `max(1.0, min(6.0, 0.571*20 - 5.929)) ≈ max(1.0, min(6.0, 5.49)) = 5.5` points
*   2M tokens (`W=2097152`): `max(1.0, min(6.0, 0.571*21 - 5.929)) ≈ max(1.0, min(6.0, 6.062)) = 6.0` points

**Model Size vs Performance Ratio (6 points)**

This component assesses a model's performance relative to its size and architectural efficiency. Points are awarded based on a `Combined Score` using a linear scale.

*   **Points Calculation:**
    The final points awarded (between 1.0 and 6.0) are calculated as follows:
    `Points = max(1.0, min(6.0, 1.0 + 5.0 * Combined Score))`

*   **Combined Score Calculation:**
    The `Combined Score` balances the model's benchmark performance against its overall efficiency:
    `Combined Score = (Benchmark Score / 100) × Total Efficiency Factor`
    *   *(Note: Dividing Benchmark Score by 100 assumes it's normalized to a 0-100 scale, bringing the Combined Score into a range suitable for the point calculation).*

*   **Total Efficiency Factor Calculation:**
    This factor adjusts the benchmark score based on model size and architecture:
    `Total Efficiency Factor = Base Size Factor × Architecture Factor`

*   **Average Benchmark Score Definition:**
    `Average Benchmark Score` is calculated as the weighted average of all Dev Benchmarks scores, normalized to a 0-100 scale based on each benchmark's distribution.

*   **Component Factor Definitions:**

    *   **Base Size Factor:** (Factor decreases for larger models, penalizing size for efficiency)
        - < 3B parameters: 1.00
        - 3B - 10B parameters: 0.95
        - 10B - 30B parameters: 0.90
        - 30B - 80B parameters: 0.80
        - 80B - 200B parameters: 0.70
        - > 200B parameters: 0.60

    *   **Architecture Factor:** (Adjusts for inherent computational efficiency of different architectures)
        - Mixture of Experts (MoE) models: 1.2
        - State Space Models (SSM): 1.1
        - Dense Transformer models: 1.0
        - Other specialized efficient architectures: 1.1
        *:Note: The "Other specialized efficient architectures" category might need refinement over time.*


## Final Score Calculation

Final Score = (External × 0.6) + (Community × 0.2) + (Technical × 0.2)

<br>
<br>
