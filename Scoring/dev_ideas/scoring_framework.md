
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

 ## V0.3.1 Score Components Explanation  (100 points total)
 
 ### 1. Entity Benchmarks (25 points)
 - artificial_analysis
 - live_code_bench
 - big_code_models
 - open_llm
 
 Each benchmark is weighted equally (25% each)
 
 ### 2. Dev Benchmarks (35 points)
 Key benchmarks with their weights:
 - MMLU Pro (8.0)
 - DROP, HellaSwag, MGSM (7.0 each)
 - Arena-Hard, TruthfulQA (4.5 each)
 - Other benchmarks (1.5-4.0 each)
 
 ### 3. Community Score (20 points)
 Based on ELO rating from Lmsys chatbot-arena-leaderboard :
 - Minimum: 1000
 - Maximum: 1500
 - Converted to 0-20 points scale
 
 ### 4. Technical Score (20 points)
 Combines three factors:
 1. Price Efficiency (8 points):
 ```
 < $1/M tokens    : 8 points
 $1-3/M tokens    : 7 points
 $3-5/M tokens    : 6 points
 ...and so on
 ```
 
 2. Context Window (6 points):
 ```
 > 200K tokens    : 6 points
 100K-200K tokens : 5 points
 32K-100K tokens  : 4 points
 ...and so on
 ```
<br>

## Final Score Calculation

Final Score = (External × 0.6) + (Community × 0.2) + (Technical × 0.2)

<br>
<br>
