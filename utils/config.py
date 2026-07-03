"""
Configuration and constants for ThesisMind AI.
"""

from pathlib import Path
from datetime import datetime
import json
import logging

# ============================================================================
# PATHS
# ============================================================================

PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
UPLOADS_DIR = DATA_DIR / "uploads"
PROJECTS_DIR = DATA_DIR / "projects"
OUTPUTS_DIR = DATA_DIR / "outputs"
LOGS_DIR = PROJECT_ROOT / "logs"

# Create directories if they don't exist
for directory in [DATA_DIR, UPLOADS_DIR, PROJECTS_DIR, OUTPUTS_DIR, LOGS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# ============================================================================
# APPLICATION CONFIGURATION
# ============================================================================

APP_CONFIG = {
    "version": "0.1.0",
    "name": "ThesisMind AI",
    "description": "AI-powered Research Synthesis Platform",
    "author": "Honnagiri Gowda L",
    
    # Document settings
    "max_documents": 20,
    "max_file_size_mb": 100,
    "supported_formats": ["pdf", "docx", "txt", "doc"],
    
    # Processing settings
    "chunk_size": 1000,
    "overlap": 200,
    
    # LLM settings
    "temperature": 0.7,
    "top_p": 0.9,
    "max_length": 2048,
    "llm_model": "llama2",
    "llm_host": "http://localhost:11434",
    
    # Export formats
    "export_formats": {
        "docx": "Word Document",
        "pdf": "PDF",
        "markdown": "Markdown",
        "latex": "LaTeX",
    },
}

# ============================================================================
# THESIS STRUCTURE
# ============================================================================

THESIS_STRUCTURE = {
    1: "Abstract",
    2: "Introduction",
    3: "Literature Survey",
    4: "Problem Statement",
    5: "Research Gap",
    6: "Objectives",
    7: "Proposed Methodology",
    8: "System Architecture",
    9: "Algorithms",
    10: "Implementation",
    11: "Results",
    12: "Performance Evaluation",
    13: "Future Work",
    14: "Conclusion",
    15: "References",
}

OUTPUT_FORMATS = {
    "docx": "📄 Word Document",
    "pdf": "📕 PDF",
    "markdown": "📝 Markdown",
    "latex": "🔬 LaTeX",
}

# ============================================================================
# LOGGING SETUP
# ============================================================================

def setup_logging():
    """
    Setup logging for the application.
    
    Returns:
        logging.Logger: Configured logger instance
    """
    logger = logging.getLogger("thesismind")
    
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        
        # File handler
        log_file = LOGS_DIR / f"thesismind_{datetime.now().strftime('%Y%m%d')}.log"
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.WARNING)
        
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    return logger

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def get_project_path(project_id: str) -> Path:
    """
    Get the path for a project directory.
    
    Args:
        project_id: Project identifier
    
    Returns:
        Path: Project directory path
    """
    project_path = PROJECTS_DIR / project_id
    project_path.mkdir(parents=True, exist_ok=True)
    return project_path

def get_upload_path(project_id: str) -> Path:
    """
    Get the path for uploads directory of a project.
    
    Args:
        project_id: Project identifier
    
    Returns:
        Path: Upload directory path
    """
    upload_path = UPLOADS_DIR / project_id
    upload_path.mkdir(parents=True, exist_ok=True)
    return upload_path

def get_output_path(project_id: str) -> Path:
    """
    Get the path for outputs directory of a project.
    
    Args:
        project_id: Project identifier
    
    Returns:
        Path: Output directory path
    """
    output_path = OUTPUTS_DIR / project_id
    output_path.mkdir(parents=True, exist_ok=True)
    return output_path
