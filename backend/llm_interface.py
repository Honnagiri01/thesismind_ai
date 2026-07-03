"""
LLM Interface for ThesisMind AI.
Connects to language models for content generation.
"""

from typing import Optional, Dict
from utils.config import APP_CONFIG


class LLMInterface:
    """Interface to language models."""
    
    def __init__(self):
        """Initialize LLM interface."""
        self.model_name = APP_CONFIG["llm_model"]
        self.temperature = APP_CONFIG["temperature"]
        self.llm = None
        self._initialize_model()
    
    def _initialize_model(self):
        """
        Initialize the language model.
        """
        try:
            # Try to import langchain
            try:
                from langchain.llms import Ollama
                
                print(f"Initializing Ollama model: {self.model_name}")
                
                self.llm = Ollama(
                    model=self.model_name,
                    base_url=APP_CONFIG["llm_host"],
                    temperature=self.temperature,
                )
                
                print("Model initialized successfully")
            except ImportError:
                print("langchain not installed. Using basic LLM interface.")
                self.llm = None
        
        except Exception as e:
            print(f"Error initializing LLM: {e}")
            self.llm = None
    
    def generate(self, prompt: str) -> str:
        """
        Generate text using the LLM.
        
        Args:
            prompt: Input prompt
        
        Returns:
            str: Generated text
        """
        try:
            if self.llm is None:
                return "[LLM not initialized - Install langchain: pip install langchain ollama]"
            
            response = self.llm(prompt)
            return response
        
        except Exception as e:
            return f"[Error: {str(e)}]"
    
    def generate_chapter(self, chapter_title: str, context: str = "", previous_content: str = "") -> str:
        """
        Generate a thesis chapter.
        
        Args:
            chapter_title: Title of chapter
            context: Context for generation
            previous_content: Previous chapter content for consistency
        
        Returns:
            str: Generated chapter
        """
        prompt = f"""
        Write an academic chapter titled: {chapter_title}
        
        Context: {context}
        
        Previous content summary: {previous_content[:500] if previous_content else "None"}
        
        Requirements:
        - Professional academic writing style
        - 500-1000 words
        - Include key points and analysis
        - Maintain consistency with previous content
        """
        
        return self.generate(prompt)
    
    def generate_abstract(self, context: str) -> str:
        """
        Generate an abstract.
        
        Args:
            context: Context for generation
        
        Returns:
            str: Generated abstract
        """
        prompt = f"""
        Generate a professional research abstract based on:
        {context}
        
        Requirements:
        - 150-250 words
        - Summarize main contributions
        - Highlight methodology and results
        """
        
        return self.generate(prompt)
    
    def review_and_edit(self, content: str) -> str:
        """
        Review and edit content for quality.
        
        Args:
            content: Content to review
        
        Returns:
            str: Edited content
        """
        prompt = f"""
        Review and improve the following academic content:
        
        {content}
        
        Requirements:
        - Fix grammar and spelling
        - Improve clarity
        - Ensure academic tone
        - Keep original meaning
        """
        
        return self.generate(prompt)
