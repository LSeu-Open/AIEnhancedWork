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

# Scoring is done by the ModelScorer class, which is imported from Models_Scoring_System.py

# This script is the main script to run the scoring system

# This is the Alpha v0.3 of the scoring system

# ------------------------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------------------------

from typing import Dict, Optional, Union, Any
import json
import os
import logging
from Models_Scoring_System import ModelScorer


# ------------------------------------------------------------------------------------------------*
# Constants and validation schema
# ------------------------------------------------------------------------------------------------

# Constants for scoring and validation
SCORE_SCALE = 100

SCORE_BOUNDS = {
    "MIN": 0,
    "MAX": 100
}

# Community score bounds (based on the community score of the best models 20 feb 2025)
COMMUNITY_SCORE_BOUNDS = {
    "MIN": 1000,
    "MAX": 1500
}

# Directory and file constants
MODELS_DIR = "Models"
RESULTS_DIR = "Results"
LOG_FILE = "model_scoring.log"

# Required sections and fields that must be present in model JSON files for validation
REQUIRED_SECTIONS = {
    'entity_benchmarks': [
        'artificial_analysis',
        'live_code_bench',
        'big_code_models',
        'open_llm'
    ],
    'dev_benchmarks': [
        'MMLU', 'MMLU Pro', 'BigBench', 'DROP', 'HellaSwag', 'GPQA', 
        'ARC-C', 'LiveBench', 'LatestEval', 'AlignBench', 'Wild Bench',
        'MT-bench', 'IFEval', 'Arena-Hard', 'TruthfulQA', 'MATH',
        'GSM-8K', 'MGSM', 'HumanEval', 'HumanEval Plus', 'MBPP',
        'MBPP Plus', 'SWE-bench', 'API-Bank', 'BFCL',
        'Gorilla Benchmark', 'Nexus'
    ],
    'model_specs': ['price', 'context_window', 'param_count'],
    'community_score': None
}

# ------------------------------------------------------------------------------------------------
# Logging and type aliases
# ------------------------------------------------------------------------------------------------

# Configure logging with both file and console output
# The file handler writes logs to model_scoring.log while the stream handler prints to console
# Format includes timestamp, log level, and message for comprehensive logging
logging.basicConfig(
    level=logging.INFO,  # Set base logging level to INFO to capture important events
    format='%(asctime)s - %(levelname)s - %(message)s',  # Standard format with timestamp
    handlers=[
        logging.FileHandler('model_scoring.log'),  # Persistent log file
        logging.StreamHandler()  # Console output for immediate feedback
    ]
)
logger = logging.getLogger(__name__)  # Get logger instance for this module

# Type aliases to improve code readability and maintainability
# These aliases document the expected structure of key data types used throughout the codebase
ModelData = Dict[str, Any]  # Raw model data containing all attributes and scores
BenchmarkScores = Dict[str, Optional[float]]  # Benchmark results, allowing for missing scores
ModelSpecs = Dict[str, float]  # Technical specifications of the model (price, context window, etc)
ScoringResults = Dict[str, Union[str, Dict[str, float], ModelData]]  # Final scoring output format

# ------------------------------------------------------------------------------------------------
# Custom exceptions for better error handling
# ------------------------------------------------------------------------------------------------

class ModelScoringError(Exception):
    """Base exception for all model scoring errors"""
    pass

class ModelDataValidationError(ModelScoringError):
    """Raised when model data validation fails"""
    pass

class BenchmarkScoreError(ModelDataValidationError):
    """Raised when benchmark scores are invalid"""
    pass

class ModelSpecificationError(ModelDataValidationError):
    """Raised when model specifications are invalid"""
    pass

class CommunityScoreError(ModelDataValidationError):
    """Raised when community score validation fails"""
    pass

# ------------------------------------------------------------------------------------------------
# Model data validation
# ------------------------------------------------------------------------------------------------

class ModelDataValidator:
    """Class to handle model data validation"""
    
    @staticmethod
    def validate_benchmarks(data: Dict, section: str, model_name: str) -> None:
        """
        Validates benchmark scores for a specific section of model data.

        Args:
            data (Dict): The model data dictionary containing benchmark scores
            section (str): The section name to validate (e.g. 'entity_benchmarks', 'dev_benchmarks')
            model_name (str): Name of the model being validated

        Raises:
            BenchmarkScoreError: If any validation check fails:
                - Section is not a dictionary
                - Required benchmark is missing
                - Score is not a number
                - Score is outside valid bounds

        Notes:
            - All scores are normalized by dividing by SCORE_SCALE
            - Valid scores must be between SCORE_BOUNDS["MIN"] and SCORE_BOUNDS["MAX"]
            - Scores can be None, which indicates benchmark was not run
        """
        # Verify section exists and is a dictionary
        if not isinstance(data[section], dict):
            raise BenchmarkScoreError(
                f"Section '{section}' must be a dictionary in model '{model_name}'"
            )
        
        # Validate all required benchmarks are present and have valid scores
        for field in REQUIRED_SECTIONS[section]:
            # Check benchmark exists
            if field not in data[section]:
                raise BenchmarkScoreError(
                    f"Missing benchmark '{field}' in {section} for model '{model_name}'"
                )
            
            score = data[section][field]
            # Only validate non-null scores
            if score is not None:
                # Verify score is numeric
                if not isinstance(score, (int, float)):
                    raise BenchmarkScoreError(
                        f"Invalid score type for '{field}' in {section}: expected number, got {type(score).__name__}"
                    )
                
                # Verify score is within valid bounds
                if score < SCORE_BOUNDS["MIN"] or score > SCORE_BOUNDS["MAX"]:
                    raise BenchmarkScoreError(
                        f"Score for '{field}' in {section} must be between {SCORE_BOUNDS['MIN']} and {SCORE_BOUNDS['MAX']}, got {score}"
                    )
                
                # Normalize score
                data[section][field] = score/SCORE_SCALE

    @staticmethod
    def validate_model_specs(specs: Dict, model_name: str) -> None:
        """Validate technical specifications for a language model.
        
        This method performs validation checks on the model's technical specifications
        to ensure all required fields are present and valid.

        Args:
            specs (Dict): Dictionary containing the model's technical specifications
                Expected fields are defined in REQUIRED_SECTIONS['model_specs']
            model_name (str): Name of the model being validated

        Raises:
            ModelSpecificationError: If any of these validation checks fail:
                - Required specification field is missing
                - Specification value is not a number (int/float)
                - Specification value is not positive (>0)

        Notes:
            - All specification values must be positive numbers
            - Common specs include parameters like model size, context length, etc.
            - The specific required fields are defined in REQUIRED_SECTIONS['model_specs']
        """
        # Validate each required specification field
        for field in REQUIRED_SECTIONS['model_specs']:
            # Check if required field exists
            if field not in specs:
                raise ModelSpecificationError(
                    f"Missing specification '{field}' in model_specs for '{model_name}'"
                )
            
            # Verify specification value is numeric
            if not isinstance(specs[field], (int, float)):
                raise ModelSpecificationError(
                    f"Invalid type for '{field}' in model_specs: expected number, got {type(specs[field]).__name__}"
                )
            
            # Ensure specification value is positive
            if specs[field] <= 0:
                raise ModelSpecificationError(
                    f"Specification '{field}' must be positive, got {specs[field]}"
                )

    @staticmethod
    def validate_community_score(score: Any, model_name: str) -> None:
        """Validate the community score for a language model.
        
        This method performs validation checks on a model's community score to ensure
        it meets the required criteria for validity.

        Args:
            score (Any): The community score value to validate. Must be a number.
            model_name (str): Name of the model being validated, used in error messages.

        Raises:
            CommunityScoreError: If any of these validation checks fail:
                - Score is not a numeric type (int/float)
                - Score is negative
                - Score is below minimum threshold (COMMUNITY_SCORE_BOUNDS["MIN"])
                - Score exceeds maximum threshold (COMMUNITY_SCORE_BOUNDS["MAX"])

        Notes:
            - Community scores represent the model's rating/reputation in the community
            - Valid scores must be positive numbers within defined bounds
            - Bounds are defined in COMMUNITY_SCORE_BOUNDS constants
        """
        # Validate score is numeric type
        if not isinstance(score, (int, float)):
            raise CommunityScoreError(
                f"Invalid community score type for '{model_name}': expected number, got {type(score).__name__}"
            )

        # Ensure score is not negative
        if score < 0:
            raise CommunityScoreError(
                f"Community score must be positive, got {score}"
            )

        # Validate score meets minimum threshold
        if score < COMMUNITY_SCORE_BOUNDS["MIN"]:
            raise CommunityScoreError(
                f"Community score must be at least {COMMUNITY_SCORE_BOUNDS['MIN']}, got {score}"
            )

        # Validate score does not exceed maximum threshold  
        if score > COMMUNITY_SCORE_BOUNDS["MAX"]:
            raise CommunityScoreError(
                f"Community score must be less than {COMMUNITY_SCORE_BOUNDS['MAX']}, got {score}"
            )

# ------------------------------------------------------------------------------------------------
# Model data loading and validation
# ------------------------------------------------------------------------------------------------

def load_model_data(model_name: str, models_directory: str = MODELS_DIR) -> Optional[ModelData]:
    """Find, load and validate model data from a JSON file.

    This function handles the complete process of loading model data:
    1. Locates the model's JSON file
    2. Loads and parses the JSON data
    3. Validates the data structure and contents
    
    Args:
        model_name (str): Name of the model to load data for
        models_directory (str, optional): Directory containing model JSON files. 
            Defaults to MODELS_DIR constant.

    Returns:
        Optional[ModelData]: The loaded and validated model data dictionary if successful,
            None if any step fails (file not found, invalid JSON, validation error)

    Raises:
        No exceptions are raised - all errors are caught, logged and return None

    Notes:
        - JSON files should be named "{model_name}.json"
        - File search is case-insensitive
        - All validation errors are logged before returning None
    """
    try:
        # First try to locate the model's JSON file
        json_file = find_model_file(model_name, models_directory)
        if not json_file:
            return None

        # Load and parse the JSON data
        data = load_json_file(json_file)
        if not data:
            return None

        # Validate the loaded data structure and contents
        validate_model_data(data, model_name)
        
        logger.info(f"Successfully validated data for model '{model_name}'")
        return data

    except Exception as e:
        # Catch and log any unexpected errors
        logger.error(f"Error processing model '{model_name}': {str(e)}")
        return None

def find_model_file(model_name: str, models_directory: str) -> Optional[str]:
    """Locate the JSON file for a given model in the models directory.
    
    This function searches for a model's JSON file using the following strategy:
    1. First checks for an exact match with the model name
    2. If not found, tries a case-insensitive search
    
    Args:
        model_name (str): Name of the model to find the JSON file for
        models_directory (str): Directory path where model JSON files are stored
        
    Returns:
        Optional[str]: Full path to the model's JSON file if found, None otherwise
        
    Notes:
        - Expected JSON filename format is "{model_name}.json"
        - Search is case-insensitive as a fallback
        - All errors are logged before returning None
    """
    # First verify the models directory exists
    if not os.path.exists(models_directory):
        logger.error(f"Models directory '{models_directory}' not found")
        return None

    # Try exact match first (case-sensitive)
    json_file = os.path.join(models_directory, f"{model_name}.json")
    if os.path.exists(json_file):
        return json_file

    # Fall back to case-insensitive search if exact match fails
    for filename in os.listdir(models_directory):
        if filename.lower() == f"{model_name.lower()}.json":
            return os.path.join(models_directory, filename)

    # No matching file found after both attempts
    logger.error(f"No JSON file found for model '{model_name}'")
    return None

def load_json_file(file_path: str) -> Optional[Dict]:
    """Load and parse JSON file"""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON format in '{file_path}': {str(e)}")
        return None

def validate_model_data(data: Dict, model_name: str) -> None:
    """Validate all model data"""
    validator = ModelDataValidator()
    
    # Verify all required sections exist
    for section in REQUIRED_SECTIONS:
        if section not in data:
            raise ModelDataValidationError(
                f"Missing required section '{section}' in model data for '{model_name}'"
            )

    # Validate benchmarks
    validator.validate_benchmarks(data, 'entity_benchmarks', model_name)
    validator.validate_benchmarks(data, 'dev_benchmarks', model_name)
    
    # Validate model specs
    validator.validate_model_specs(data['model_specs'], model_name)
    
    # Validate community score
    validator.validate_community_score(data['community_score'], model_name)

# ------------------------------------------------------------------------------------------------
# Scoring process
# ------------------------------------------------------------------------------------------------

def run_scoring(model_name: str, models_directory: str = MODELS_DIR) -> Optional[ScoringResults]:
    """
    Run the scoring process for a given model by loading its JSON from the Models directory.
    
    Args:
        model_name: Name of the model to score
        models_directory: Path to the directory containing model JSONs
    
    Returns:
        Scoring results if successful, None otherwise
    """
    logger.info(f"Starting scoring process for model '{model_name}'")
    
    # Load and validate the model data
    data = load_model_data(model_name, models_directory)
    if not data:
        logger.error(f"Failed to load data for model '{model_name}'")
        return None

    try:
        # Initialize scorer with model name
        scorer = ModelScorer(model_name)
        
        # Extract data from JSON
        entity_benchmarks: BenchmarkScores = data.get('entity_benchmarks', {})
        dev_benchmarks: BenchmarkScores = data.get('dev_benchmarks', {})
        community_score: float = data.get('community_score', 0)
        model_specs: ModelSpecs = data.get('model_specs', {})

        # Calculate average benchmark performance
        available_scores: list[float] = (
            [score for score in entity_benchmarks.values() if score is not None] +
            [score for score in dev_benchmarks.values() if score is not None]
        )
        avg_performance: float = sum(available_scores) / len(available_scores) * 100  # Convert to percentage

        # Calculate size/performance ratio
        size_perf_ratio: float = scorer.calculate_size_perf_ratio(avg_performance, model_specs['param_count'])

        # Calculate scores
        entity_score: float = scorer.calculate_entity_benchmarks(entity_benchmarks)
        dev_score: float = scorer.calculate_dev_benchmarks(dev_benchmarks)
        external_score: float = scorer.calculate_external_benchmarks(entity_benchmarks, dev_benchmarks)
        community_score: float = scorer.calculate_community_score(community_score)
        technical_score: float = scorer.calculate_technical_score(
            price=model_specs['price'],
            context_window=model_specs['context_window'],
            size_perf_ratio=size_perf_ratio
        )

        # Set scores
        scorer.external_score = external_score
        scorer.community_score = community_score 
        scorer.technical_score = technical_score

        # Calculate final score
        final_score: float = scorer.calculate_final_score()

        # Prepare results dictionary
        results: ScoringResults = {
            'model_name': model_name,
            'scores': {
                'entity_score': entity_score,
                'dev_score': dev_score,
                'external_score': external_score,
                'community_score': community_score,
                'technical_score': technical_score,
                'final_score': final_score,
                'avg_performance': avg_performance,
                'size_perf_ratio': size_perf_ratio
            },
            'input_data': data  # Include input data for reference
        }
        
        logger.info(f"Successfully completed scoring for model '{model_name}'")
        return results

    except Exception as e:
        logger.error(f"Error during scoring process: {str(e)}")
        return None

# ------------------------------------------------------------------------------------------------
# Main and batch processing
# ------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        # List of model names to process - can be expanded as needed
        model_names: list[str] = ["DeepSeek-V3", "MiniMax-Text-01"]
        
        # Create Results directory if it doesn't exist
        os.makedirs("Results", exist_ok=True)
        
        # Track total number of models for progress reporting
        total_models = len(model_names)
        
        # Process each model sequentially
        for index, model_name in enumerate(model_names, 1):
            # Visual separator and progress indicator in logs
            logger.info("\n" + "="*80)
            logger.info(f"Processing model {index}/{total_models}: {model_name}")
            logger.info("="*80 + "\n")
            
            # Run scoring pipeline for current model
            results: Optional[ScoringResults] = run_scoring(model_name)
            
            if results:
                # Save results to JSON file in Results directory
                output_file: str = os.path.join("Results", f"{model_name}_results.json")
                with open(output_file, 'w') as f:
                    json.dump(results, f, indent=4)
                logger.info(f"Results saved to {output_file}")
                
                # Visual separator after successful processing
                logger.info("\n" + "-"*80 + "\n")
            else:
                # Log error if scoring failed
                logger.error(f"Failed to generate results for {model_name}")
                # Visual separator after error
                logger.info("\n" + "-"*80 + "\n")
        
        # Log final summary of batch processing
        logger.info("="*80)
        logger.info(f"Batch processing completed for {total_models} models")
        logger.info("="*80)
            
    except Exception as e:
        # Log any unexpected errors during batch processing
        logger.error(f"Batch processing failed: {str(e)}")
