"""
Project Manager for ThesisMind AI.
Handles project creation, loading, and management.
"""

import json
from pathlib import Path
from datetime import datetime
import uuid
from typing import List, Dict, Optional

from utils.config import PROJECTS_DIR, get_project_path


class ProjectManager:
    """Manage research projects."""
    
    def __init__(self):
        """Initialize project manager."""
        self.projects_dir = PROJECTS_DIR
        self.projects_dir.mkdir(parents=True, exist_ok=True)
    
    def create_project(self, name: str, description: str = "") -> str:
        """
        Create a new project.
        
        Args:
            name: Project name
            description: Project description
        
        Returns:
            str: Project ID
        """
        project_id = str(uuid.uuid4())[:8]
        
        project_data = {
            "id": project_id,
            "name": name,
            "description": description,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "status": "active",
            "progress": 0,
            "documents": [],
            "generated_thesis": None,
        }
        
        # Save project
        project_path = get_project_path(project_id)
        project_file = project_path / "metadata.json"
        
        with open(project_file, "w") as f:
            json.dump(project_data, f, indent=2)
        
        return project_id
    
    def list_projects(self) -> List[str]:
        """
        List all projects.
        
        Returns:
            List[str]: List of project names
        """
        project_names = []
        
        for project_dir in self.projects_dir.iterdir():
            if project_dir.is_dir():
                metadata_file = project_dir / "metadata.json"
                if metadata_file.exists():
                    with open(metadata_file, "r") as f:
                        data = json.load(f)
                        project_names.append(data["name"])
        
        return sorted(project_names)
    
    def get_project_by_name(self, name: str) -> Optional[Dict]:
        """
        Get project data by name.
        
        Args:
            name: Project name
        
        Returns:
            Dict: Project data or None
        """
        for project_dir in self.projects_dir.iterdir():
            if project_dir.is_dir():
                metadata_file = project_dir / "metadata.json"
                if metadata_file.exists():
                    with open(metadata_file, "r") as f:
                        data = json.load(f)
                        if data["name"] == name:
                            return data
        return None
    
    def save_project(self, project_id: str, project_data: Dict) -> bool:
        """
        Save project data.
        
        Args:
            project_id: Project ID
            project_data: Project data
        
        Returns:
            bool: Success status
        """
        try:
            project_path = get_project_path(project_id)
            project_file = project_path / "metadata.json"
            
            project_data["updated_at"] = datetime.now().isoformat()
            
            with open(project_file, "w") as f:
                json.dump(project_data, f, indent=2)
            
            return True
        except Exception as e:
            print(f"Error saving project: {e}")
            return False
    
    def delete_project(self, project_id: str) -> bool:
        """
        Delete a project.
        
        Args:
            project_id: Project ID
        
        Returns:
            bool: Success status
        """
        try:
            import shutil
            project_path = get_project_path(project_id)
            if project_path.exists():
                shutil.rmtree(project_path)
            return True
        except Exception as e:
            print(f"Error deleting project: {e}")
            return False
    
    def add_document(self, project_id: str, doc_info: Dict) -> bool:
        """
        Add a document to a project.
        
        Args:
            project_id: Project ID
            doc_info: Document information
        
        Returns:
            bool: Success status
        """
        try:
            project = None
            for project_dir in self.projects_dir.iterdir():
                if project_dir.name == project_id:
                    metadata_file = project_dir / "metadata.json"
                    if metadata_file.exists():
                        with open(metadata_file, "r") as f:
                            project = json.load(f)
                        break
            
            if project:
                project["documents"].append(doc_info)
                self.save_project(project_id, project)
                return True
            return False
        except Exception as e:
            print(f"Error adding document: {e}")
            return False
