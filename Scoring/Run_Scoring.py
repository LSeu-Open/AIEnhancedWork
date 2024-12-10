# Copyright (c) 2024 LSeu-Open
# 
# This code is licensed under the MIT License.
# See LICENSE-CODE file in the root directory

from Models_Scoring_System import ModelScorer

# Initialize scorer with model name
scorer = ModelScorer("Gemini 1.5 Pro")

# Example benchmark scores
entity_benchmarks = {
    'artificial_analysis': 79.7/100,
    'live_code_bench': 36.4/100,
    'big_code_models': None,
    'open_llm': None,
}

dev_benchmarks = {
    'MMLU': 78.76/100,
    'MMLU Pro': 55.63/100,
    'BigBench': None,
    'DROP': None,
    'HellaSwag': None,
    'GPQA': None,
    'ARC-C': 67.24/100,
    'LiveBench': None,
    'LatestEval': None,
    'AlignBench': None,
    'Wild Bench': None,
    'MT-bench': None,
    'IFEval': None,
    'Arena-Hard': None,
    'TruthfulQA': None,
    'MATH': None,
    'GSM-8K': 76.04/100,
    'MGSM': None,
    'HumanEval': None,
    'HumanEval Plus': None,
    'MBPP': None,
    'MBPP Plus': None,
    'SWE-bench': None,
    'API-Bank': None,
    'BFCL': None,
    'Gorilla Benchmark': None,
    'Nexus': None
}

community_score = 1301

# Model specifications
model_specs = {
    'price': 2.188,                # dollars per million tokens
    'context_window': 2000000,    # tokens
    'param_count': 200           # billions of parameters
}

# Calculate average benchmark performance
available_scores = (
    [score for score in entity_benchmarks.values() if score is not None] +
    [score for score in dev_benchmarks.values() if score is not None]
)
avg_performance = sum(available_scores) / len(available_scores) * 100  # Convert to percentage

# Calculate size/performance ratio using the ModelScorer method
size_perf_ratio = scorer.calculate_size_perf_ratio(avg_performance, model_specs['param_count'])

# Calculate scores
entity_score = scorer.calculate_entity_benchmarks(entity_benchmarks)
dev_score = scorer.calculate_dev_benchmarks(dev_benchmarks)
external_score = scorer.calculate_external_benchmarks(entity_benchmarks, dev_benchmarks)
community_score = scorer.calculate_community_score(community_score)
technical_score = scorer.calculate_technical_score(
    price=model_specs['price'],
    context_window=model_specs['context_window'],
    size_perf_ratio=size_perf_ratio
)

# Set scores
scorer.external_score = external_score
scorer.community_score = community_score 
scorer.technical_score = technical_score

# Calculate final score
final_score = scorer.calculate_final_score()
