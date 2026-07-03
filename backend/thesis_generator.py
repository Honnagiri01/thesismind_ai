"""
Thesis generation engine for ThesisMind AI.
Orchestrates the complete thesis generation workflow.
"""

from typing import Dict, List, Optional
from loguru import logger
from backend.llm_interface import LLMInterface
from backend.knowledge_extractor import KnowledgeExtractor
from utils.config import THESIS_STRUCTURE


class ThesisGenerator:
    """Generate complete thesis from document knowledge."""
    
    def __init__(self):
        """Initialize thesis generator."""
        self.llm = LLMInterface()
        self.extractor = KnowledgeExtractor()
    
    def generate_thesis(self, documents: List[Dict], thesis_config: Dict) -> Dict:
        """
        Generate a complete thesis from documents.
        
        Args:
            documents: List of processed document information
            thesis_config: Configuration for thesis generation
        
        Returns:
            Dict: Generated thesis content
        """
        thesis = {
            "title": thesis_config.get("title", "Research Thesis"),
            "type": thesis_config.get("type", "PhD Thesis"),
            "chapters": {},
            "metadata": {
                "total_documents": len(documents),
                "total_pages": sum(doc.get("pages", 0) for doc in documents),
                "status": "in_progress"
            }
        }
        
        # Extract knowledge from all documents
        all_knowledge = []
        for doc in documents:
            knowledge = self.extractor.extract_from_document(doc)
            all_knowledge.append(knowledge)
        
        # Identify research gaps
        gaps = self.extractor.identify_research_gaps(all_knowledge)
        
        # Generate each chapter
        chapters_to_generate = thesis_config.get("chapters", list(THESIS_STRUCTURE.values()))
        
        previous_content = ""
        
        for chapter_title in chapters_to_generate:
            logger.info(f"Generating chapter: {chapter_title}")
            
            context = self._prepare_chapter_context(
                chapter_title,
                all_knowledge,
                gaps,
                thesis_config
            )
            
            chapter_content = self.llm.generate_chapter(
                chapter_title,
                context,
                previous_content
            )
            
            thesis["chapters"][chapter_title] = chapter_content
            previous_content = chapter_content[:1000]
        
        thesis["metadata"]["status"] = "completed"
        logger.info("Thesis generation completed")
        
        return thesis
    
    def _prepare_chapter_context(self, chapter_title: str, all_knowledge: List[Dict],
                                 gaps: List[str], config: Dict) -> str:
        """
        Prepare context for chapter generation.
        
        Args:
            chapter_title: Title of chapter to generate
            all_knowledge: Extracted knowledge from all documents
            gaps: Identified research gaps
            config: Thesis configuration
        
        Returns:
            str: Context for LLM
        """
        context = f"""
        Thesis Title: {config.get('title', '')}
        Thesis Type: {config.get('type', '')}
        Keywords: {', '.join(config.get('keywords', []))}
        
        Relevant Research Areas:
        """
        
        # Add knowledge from documents
        for i, knowledge in enumerate(all_knowledge[:3], 1):
            context += f"\n{i}. {knowledge.get('methodology', 'Research methodology')}\n"
        
        if gaps:
            context += "\nIdentified Research Gaps:\n"
            for gap in gaps[:3]:
                context += f"- {gap}\n"
        
        return context
