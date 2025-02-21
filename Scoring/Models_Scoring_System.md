# Proposed Hybrid Scoring Framework

<div align="center" > <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Triangular%20Flag.png" alt="Triangular Flag" width="25" height="25" /> Current Version of the Scoring System : Alpha v0.3 <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Triangular%20Flag.png" alt="Triangular Flag" width="25" height="25" /> </div>

<br>

## System Overview

The scoring system evaluates models based on four main criteria:
1. Entity benchmarks (25 points)
2. Dev benchmarks (35 points)
3. Community engagement (20 points)
4. Technical specifications (20 points)

> [!IMPORTANT]
> ***Scoring Framework Alpha Version***
> 
> This evaluation system provides an objective way to assess LLM models through standardized metrics.  We welcome **community feedback and contributions through GitHub issues** to improve its accuracy and reliability.
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

## Setup Requirements

1. Required files:
```
project/
│
├── Run_Scoring.py
├── Models_Scoring_System.py
├── Models/                  # Directory for model JSON files
│   └── model_name.json
└── Results/                # Directory for output files
```

2. Required Python packages:
```python
import json
import os
import logging
from typing import Dict, Optional, Union, Any
```

## Model Data Format

Create a JSON file for each model in the `Models` directory using this structure:

This framework supports benchmarks with missing values, as it is not always feasible to have complete data for all models. Benchmark values should be either numeric (ranging from 0 to 100) or `null` to indicate missing data.

```json
{
    "entity_benchmarks": {
        "artificial_analysis": 85.5,
        "live_code_bench": 78.2,
        "big_code_models": 82.1,
        "open_llm": 80.0
    },
    "dev_benchmarks": {
        "MMLU": 82.5,
        "MMLU Pro": 79.8,
        "BigBench": 77.4,
        "DROP": 85.2,
        "HellaSwag": 83.1,
        // ... other dev benchmarks ...
    },
    "model_specs": {
        "price": 15.0,         // USD per million tokens
        "context_window": 32000,// Maximum context length
        "param_count": 70      // Billions of parameters
    },
    "community_score": 1250    // ELO rating (1000-1500 range)
}
```

## Using the System

### 1. Single Model Evaluation

### 2. Batch Processing

## Score Components Explanation

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

3. Size-Performance Ratio (6 points):
Based on benchmark performance relative to parameter count

## Output and Results

1. The system creates detailed JSON results:
```json
{
    "model_name": "ModelName",
    "scores": {
        "entity_score": 20.5,
        "dev_score": 30.2,
        "external_score": 50.7,
        "community_score": 15.8,
        "technical_score": 16.5,
        "final_score": 83.0,
        "avg_performance": 82.5,
        "size_perf_ratio": 4.2
    },
    "input_data": {
        // Original input data
    }
}
```

2. Results are saved in:
- JSON file: `Results/ModelName_results.json`
- Log file: `model_scoring.log`

## Common Issues and Solutions

1. Missing Data:
   - Ensure all required benchmarks are present
   - Use `null` for unavailable scores

2. Validation Errors:
   - Check score ranges (0-100)
   - Verify community score range (1000-1500)
   - Ensure positive values for technical specs

3. File Structure:
   - Maintain correct JSON format
   - Use correct file naming
   - Place files in proper directories

This scoring system provides a comprehensive evaluation of language models, considering both performance metrics and practical aspects like cost and efficiency.
