"""
Backend package initialization.
"""

from backend.project_manager import ProjectManager
from backend.document_processor import DocumentProcessor
from backend.knowledge_extractor import KnowledgeExtractor
from backend.llm_interface import LLMInterface

__all__ = [
    'ProjectManager',
    'DocumentProcessor',
    'KnowledgeExtractor',
    'LLMInterface',
]
