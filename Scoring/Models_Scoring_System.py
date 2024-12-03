class ModelScorer:
    def __init__(self, model_name="Unnamed Model"):
        self.model_name = model_name
        pass
        
    def calculate_entity_benchmarks(self, benchmark_scores):
        """Calculate entity benchmarks score (25 points max)"""
        if not benchmark_scores:
            return 0
            
        weights = {
            'artificial_analysis': 25,
            'live_code_bench': 25,
            'big_code_models': 25,
            'open_llm': 25,
        }
        
        score = 0
        available_weights = 0
        
        for bench, result in benchmark_scores.items():
            if result is not None:
                score += (result * weights[bench])
                available_weights += weights[bench]
                
        if available_weights > 0:
            return (score / available_weights) * 25
        return 0

    def calculate_dev_benchmarks(self, benchmark_scores):
        """Calculate dev benchmarks score (35 points max)"""
        if not benchmark_scores:
            return 0
            
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
        
        for bench, result in benchmark_scores.items():
            if result is not None and bench in weights:
                score += (result * weights[bench])
                available_weights += weights[bench]
                
        if available_weights > 0:
            return (score / available_weights) * 35
        return 0

    def calculate_external_benchmarks(self, entity_benchmarks, dev_benchmarks=None):
        """Calculate external benchmarks score (60 points max)"""
        if dev_benchmarks is None:
            dev_benchmarks = entity_benchmarks  # For backward compatibility
        
        entity_score = self.calculate_entity_benchmarks(entity_benchmarks)
        dev_score = self.calculate_dev_benchmarks(dev_benchmarks)
        return entity_score + dev_score

    def calculate_community_score(self, elo_rating):
        """Calculate community score (20 points max)"""
        if elo_rating is None:
            return None
            
        base_elo = 1000
        max_elo = 1365
        
        normalized_score = ((elo_rating - base_elo) / (max_elo - base_elo)) * 100
        return (normalized_score * 0.2)  # 20 points max

    def _calculate_price_score(self, price):
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
        if context_size is None:
            return 0
        if context_size > 200000: return 6
        elif context_size > 100000: return 5
        elif context_size > 32000: return 4
        elif context_size > 16000: return 3
        elif context_size > 8000: return 2
        else: return 1

    def calculate_size_perf_ratio(self, benchmark_score, param_count):
        """Calculate performance-to-size ratio score (6 points max)"""
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
        
        # Size efficiency multiplier
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
        if ratio is None:
            return 0
        if ratio > 90: return 6
        elif ratio > 80: return 5
        elif ratio > 70: return 4
        elif ratio > 60: return 3
        else: return 2

    def calculate_technical_score(self, price, context_window, size_perf_ratio):
        """Calculate technical score (20 points max)"""
        price_score = self._calculate_price_score(price)
        context_score = self._calculate_context_score(context_window)
        ratio_score = self._calculate_ratio_score(size_perf_ratio)
        
        return price_score + context_score + ratio_score

    def calculate_final_score(self):
        """
        Calculate the final score by combining all component scores.
        Returns a score out of 100.
        """
        # Check if scores have been explicitly set
        if not hasattr(self, 'external_score') or \
           not hasattr(self, 'community_score') or \
           not hasattr(self, 'technical_score'):
            raise ValueError("All component scores must be set before calculating final score")
        
        # Sum all scores to get final score out of 100
        final_score = self.external_score + self.community_score + self.technical_score
        
        # Print detailed score breakdown with model name
        print(f"\n=== Score Breakdown for {self.model_name} ===")
        print(f"External Score:   {self.external_score:>6.2f}/60")
        print(f"Community Score:  {self.community_score:>6.2f}/20")
        print(f"Technical Score:  {self.technical_score:>6.2f}/20")
        print(f"Final Score:      {final_score:>6.2f}/100")
        print("=" * 40)
        
        return round(final_score, 2)
