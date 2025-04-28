# ------------------------------------------------------------------------------------------------
# License
# ------------------------------------------------------------------------------------------------

# Copyright (c) 2024 LSeu-Open
# 
# This code is licensed under the MIT License.
# See LICENSE-CODE file in the root directory

# ------------------------------------------------------------------------------------------------
# Description
# ------------------------------------------------------------------------------------------------

# This script is used to score large language models based on the following criteria:
# - Entity benchmarks
# - Dev benchmarks
# - Community score
# - Technical specifications

# This file is the ModelScorer class, to run the scoring system, please use the Run_Scoring.py file

# This is the Alpha v0.3 of the scoring system

# ------------------------------------------------------------------------------------------------
# ModelScorer class
# ------------------------------------------------------------------------------------------------

class ModelScorer:
    """
    A class for scoring and evaluating large language models based on multiple criteria.
    
    This class implements a comprehensive scoring system that evaluates models on:
    - Entity benchmarks (25 points max)
    - Dev benchmarks (35 points max) 
    - Community engagement (20 points max)
    - Technical specifications (20 points max)
    
    The final score is calculated out of 100 points total.
    
    Attributes:
        model_name (str): Name of the model being scored. Defaults to "Unnamed Model".
        external_score (float): Combined score from entity and dev benchmarks (set externally)
        community_score (float): Score based on community engagement (set externally)
        technical_score (float): Score based on technical specs (set externally)
    """

    def __init__(self, model_name="Unnamed Model"):
        """
        Initialize a ModelScorer instance.
        
        Args:
            model_name (str, optional): Name of the model to score. Defaults to "Unnamed Model".
        """
        self.model_name = model_name
        
    def calculate_entity_benchmarks(self, benchmark_scores):
        """
        Calculate entity benchmarks score out of 25 points maximum.
        
        Evaluates performance on core entity benchmarks like artificial analysis,
        live code bench, big code models and open LLM evaluations.
        
        Args:
            benchmark_scores (dict): Dictionary mapping benchmark names to scores (0-1 range)
            
        Returns:
            float: Weighted score out of 25 points
        """
        if not benchmark_scores:
            return 0
            
        # Define relative weights for each benchmark
        weights = {
            'artificial_analysis': 25,
            'live_code_bench': 25, 
            'big_code_models': 25,
            'open_llm': 25,
        }
        
        score = 0
        available_weights = 0
        
        # Calculate weighted average of available scores
        for bench, result in benchmark_scores.items():
            if result is not None:
                score += (result * weights[bench])
                available_weights += weights[bench]
                
        # Scale to 25 points maximum if we have scores
        if available_weights > 0:
            return (score / available_weights) * 25
        return 0

    def calculate_dev_benchmarks(self, benchmark_scores):
        """
        Calculate dev benchmarks score out of 35 points maximum.
        
        Evaluates performance across a wide range of development benchmarks including:
        - Language understanding (MMLU, BigBench)
        - Reasoning (DROP, HellaSwag)
        - Math & coding (MATH, HumanEval)
        - And many others
        
        Args:
            benchmark_scores (dict): Dictionary mapping benchmark names to scores (0-1 range)
            
        Returns:
            float: Weighted score out of 35 points
        """
        if not benchmark_scores:
            return 0
            
        # Define relative weights for each benchmark based on importance
        weights = {
            'MMLU': 3.0,
            'MMLU Pro': 8.0,
            'BigBench': 3.0,
            'DROP': 7.0,
            'HellaSwag': 7.0,
            'GPQA': 2.0,
            'ARC-C': 2.0,
            'LiveBench': 1.5,
            'LatestEval': 1.5,
            'AlignBench': 4.0,
            'Wild Bench': 4.0,
            'MT-bench': 4.0,
            'IFEval': 4.0,
            'Arena-Hard': 4.5,
            'TruthfulQA': 4.5,
            'MATH': 4.0,
            'GSM-8K': 4.0,
            'MGSM': 7.0,
            'HumanEval': 3.0,
            'HumanEval Plus': 3.0,
            'MBPP': 3.0,
            'MBPP Plus': 3.0,
            'SWE-bench': 2.0,
            'API-Bank': 2.0,
            'BFCL': 5.0,
            'Gorilla Benchmark': 2.0,
            'Nexus': 2.0
        }
        
        score = 0
        available_weights = 0
        
        # Calculate weighted average of available scores
        for bench, result in benchmark_scores.items():
            if result is not None and bench in weights:
                score += (result * weights[bench])
                available_weights += weights[bench]
                
        # Scale to 35 points maximum if we have scores
        if available_weights > 0:
            return (score / available_weights) * 35
        return 0

    def calculate_external_benchmarks(self, entity_benchmarks, dev_benchmarks=None):
        """
        Calculate total external benchmarks score out of 60 points maximum.
        
        Combines entity benchmarks (25 points) and dev benchmarks (35 points).
        
        Args:
            entity_benchmarks (dict): Entity benchmark scores
            dev_benchmarks (dict, optional): Dev benchmark scores. If None, uses entity_benchmarks
            
        Returns:
            float: Combined external benchmark score out of 60 points
        """
        if dev_benchmarks is None:
            dev_benchmarks = entity_benchmarks  # For backward compatibility
        
        entity_score = self.calculate_entity_benchmarks(entity_benchmarks)
        dev_score = self.calculate_dev_benchmarks(dev_benchmarks)
        return entity_score + dev_score

    def calculate_community_score(self, elo_rating):
        """
        Calculate community engagement score out of 20 points maximum.
        
        Converts ELO rating to a normalized score between 0-20 points.
        
        Args:
            elo_rating (float): Model's ELO rating from community evaluations
            
        Returns:
            float: Community score out of 20 points, or None if no rating provided
        """
        if elo_rating is None:
            return None
            
        base_elo = 1000  # Minimum expected ELO
        max_elo = 1402   # Maximum expected ELO
        
        # Normalize to percentage then scale to 20 points
        normalized_score = ((elo_rating - base_elo) / (max_elo - base_elo)) * 100
        return (normalized_score * 0.2)  # 20 points max

    def _calculate_price_score(self, price):
        """
        Calculate score based on model's price point (8 points max).
        
        Args:
            price (float): Price per million tokens in USD
            
        Returns:
            int: Score from 1-8 based on price brackets
        """
        if price is None:
            return 0
        if price < 1: return 8
        elif price < 3: return 7
        elif price < 5: return 6
        elif price < 10: return 5
        elif price < 20: return 4
        elif price < 40: return 3
        elif price < 80: return 2
        else: return 1

    def _calculate_context_score(self, context_size):
        """
        Calculate score based on context window size (6 points max).
        
        Args:
            context_size (int): Maximum context window size in tokens
            
        Returns:
            int: Score from 1-6 based on context size brackets
        """
        if context_size is None:
            return 0
        if context_size > 200000: return 6
        elif context_size > 100000: return 5
        elif context_size > 32000: return 4
        elif context_size > 16000: return 3
        elif context_size > 8000: return 2
        else: return 1

    def calculate_size_perf_ratio(self, benchmark_score, param_count):
        """
        Calculate performance-to-size efficiency ratio score (6 points max).
        
        Evaluates how well the model performs relative to its parameter count.
        Higher scores indicate better efficiency.
        
        Args:
            benchmark_score (float): Average benchmark performance (0-100)
            param_count (float): Number of parameters in billions
            
        Returns:
            float: Efficiency score from 2-6 points
        """
        # Base score from performance - adjusted thresholds
        if benchmark_score > 85:     
            base_score = 6.0            # Excellent (>85%)
        elif benchmark_score > 75:      # Changed >= to >
            base_score = 5.0            # Good (76-85%)
        elif benchmark_score > 65:      # Changed >= to >
            base_score = 4.0            # Decent (66-75%)
        elif benchmark_score > 55:      # Keep as >
            base_score = 3.0            # Moderate (56-65%)
        else:                           
            base_score = 2.0            # Poor (≤55%)
        
        # Apply size efficiency multiplier
        if param_count >= 70:           
            return min(base_score, 3.0) 
        elif param_count >= 40:         
            return min(base_score, 4.0) 
        elif param_count >= 30:         
            return min(base_score, 5.0) 
        elif param_count >= 15:         
            return min(base_score, 5.5) 
        else:                          
            return min(base_score, 6.0)

    def _calculate_ratio_score(self, ratio):
        """
        Calculate score based on size-performance ratio (6 points max).
        
        Args:
            ratio (float): Size-performance ratio score
            
        Returns:
            int: Score from 2-6 based on ratio brackets
        """
        if ratio is None:
            return 0
        if ratio > 90: return 6
        elif ratio > 80: return 5
        elif ratio > 70: return 4
        elif ratio > 60: return 3
        else: return 2

    def calculate_technical_score(self, price, context_window, size_perf_ratio):
        """
        Calculate technical specifications score out of 20 points maximum.
        
        Combines scores for:
        - Price efficiency (8 points)
        - Context window size (6 points)
        - Size-performance ratio (6 points)
        
        Args:
            price (float): Price per million tokens in USD
            context_window (int): Maximum context window size in tokens
            size_perf_ratio (float): Performance to parameter count ratio
            
        Returns:
            float: Combined technical score out of 20 points
        """
        price_score = self._calculate_price_score(price)
        context_score = self._calculate_context_score(context_window)
        ratio_score = self._calculate_ratio_score(size_perf_ratio)
        
        return price_score + context_score + ratio_score

    def calculate_final_score(self):
        """
        Calculate final comprehensive score out of 100 points.
        
        Combines:
        - External benchmarks (60 points)
        - Community score (20 points)
        - Technical score (20 points)
        
        All component scores must be set before calling this method.
        
        Returns:
            float: Final rounded score out of 100 points
            
        Raises:
            ValueError: If any component scores are not set
        """
        # Verify all required scores are set
        if not hasattr(self, 'external_score') or \
           not hasattr(self, 'community_score') or \
           not hasattr(self, 'technical_score'):
            raise ValueError("All component scores must be set before calculating final score")
        
        # Calculate total score
        final_score = self.external_score + self.community_score + self.technical_score
        
        # Print detailed breakdown
        print(f"\n=== Score Breakdown for {self.model_name} ===")
        print(f"External Score:   {self.external_score:>6.2f}/60")
        print(f"Community Score:  {self.community_score:>6.2f}/20")
        print(f"Technical Score:  {self.technical_score:>6.2f}/20")
        print(f"Final Score:      {final_score:>6.2f}/100")
        print("=" * 40)
        
        return round(final_score, 2)
