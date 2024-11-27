# Proposed Hybrid Scoring Framework

> [!CAUTION]
> ***Scoring Framework Beta Version***
> This evaluation system is **actively being developed and refined.** We welcome **community feedback and contributions through GitHub issues** to improve its accuracy and reliability.

<br>

# Scoring Framework Beta Version (100 points total)

## External Benchmarks (60 points)

### Entity Benchmarks (25 points)

- Artificial Analysis (when available)
- LiveCodeBench (when available)
- Big Code Models Leaderboard (when available)
- OpenVLM Leaderboard (when available)
- Open LLM Leaderboard (when available)
- MMBench Leaderboard (when available)

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

Here's the weighted distribution for LLM benchmarks:

> **Weight distribution principles**
>
> Non-contaminated benchmarks (BFCL): 10%
> Unknown contamination status (MMLU Pro, AlignBench): 5.5% each
> Contaminated benchmarks: 3.5% each

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

| Benchmark Name | Contamination Sensitive | Percentage Weight | Description |
|----------------|------------------------|-------------------|-------------|
| MMMU | Yes | 4.0% | Multimodal understanding benchmark testing various visual and language tasks |
| MathVista | Yes | 4.0% | Tests mathematical reasoning abilities with visual inputs |
| MMStar | Yes | 4.0% | Evaluates multimodal understanding across diverse visual scenarios |
| DocVQA | Yes | 4.0% | Question answering tasks on document images |
| TextVQA | Yes | 4.0% | Visual questions requiring text reading and comprehension in images |
| InfoVQA | Yes | 4.0% | Information extraction and question answering from visual data |
| ChartQA | Yes | 4.0% | Question answering tasks specifically for charts and graphs |
| OCRBench | Yes | 4.0% | Tests optical character recognition capabilities in various contexts |
| MTVQA | No | 12.0% | Multilingual and multimodal question answering on TV show content |
| VCR | Yes | 4.0% | Visual Commonsense Reasoning with complex scene understanding |
| MMBench | Yes | 4.0% | Comprehensive multimodal benchmark testing various capabilities |
| MMT-Bench | Yes | 4.0% | Multi-turn conversations about visual content |
| HallBench | Yes | 4.0% | Tests hallucination detection in multimodal responses |
| AI2 Diagram | Yes | 4.0% | Understanding and reasoning about scientific diagrams |
| MVBench | Yes | 4.0% | Motion and video understanding benchmark |
| PerceptionTest | Yes | 4.0% | Tests visual perception and understanding capabilities |
| EgoSchema | No | 12.0% | Evaluates understanding of egocentric video content |
| Video-MME | Yes | 4.0% | Multimodal evaluation focusing on video understanding |

<br>

### Score Adjustment Formula

When benchmarks are missing, the total score should be normalized using:

$$ \text{Final Score} = \frac{\sum_{i=1}^{n} w_i s_i}{\sum_{i=1}^{n} w_i} \times 100 $$

Where:
- $$w_i$$ is the weight of benchmark i
- $$s_i$$ is the score of benchmark i
- n is the number of available benchmarks

#### Weight Redistribution

For missing benchmarks, their weights are redistributed proportionally:

$$ w'_i = w_i \times \frac{100}{\sum_{j=1}^{m} w_j} $$

Where:
- $$ w'_i $$ is the adjusted weight
- m is the number of available benchmarks
- $$ w_j $$ represents the original weights of available benchmarks

## Example

If we have 3 benchmarks with original weights:
- A: 40%
- B: 35% 
- C: 25%

If benchmark C is missing:

$$ w'_A = 40 \times \frac{100}{75} = 53.33\% $$
$$ w'_B = 35 \times \frac{100}{75} = 46.67\% $$

#### Example Calculation

If a benchmark with 10% weight is missing from a set of benchmarks:
1. Remove the missing benchmark's weight
2. Multiply remaining weights by $$\frac{100}{90}$$ to maintain 100% total
3. Calculate final score using the normalized weights

This approach ensures:
- Fair comparison between models
- Maintenance of relative importance between remaining benchmarks
- Statistical validity of the final score


<br>
<br>

## Community Assessment (20 points)

- Lmsys Arena Elo score (when available)
- OpenLM arena Elo score (when available)
- Imgsys Elo score (when available)

<br>

## Technical Performance (20 points)

- Price per USD per 1M Tokens
- Output Tokens per Second
- Context window
- Model size vs. performance ratio
- Fine-tuning cost and efficiency

<br>
<br>

## Final Score Calculation

FirstFinal Score = (External × 0.6) + (Community × 0.2) + (Technical × 0.2)

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
