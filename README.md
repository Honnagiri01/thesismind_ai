# ThesisMind AI - AI-powered Research Synthesis Platform

**AI-powered Research Synthesis Platform**

ThesisMind AI is a professional Streamlit web application that understands multiple research papers, theses, technical books, and reports, then generates an original, well-structured research thesis based on the knowledge extracted from them.

## Key Features

- **Multi-Document Analysis**: Upload and analyze 4-20 research documents
- **Knowledge Synthesis**: Extract and synthesize knowledge from multiple sources
- **Thesis Generation**: Generate complete, original research theses
- **Research Gap Analysis**: Identify research gaps and opportunities
- **Multiple Export Formats**: Export as DOCX, PDF, Markdown, or LaTeX
- **Project Management**: Create, save, and manage multiple research projects
- **Professional UI**: Dark mode, interactive visualizations, responsive design

## Quick Start

### Prerequisites
- Python 3.9 or higher
- 4GB RAM minimum (8GB recommended)

### Installation

```bash
# Clone the repository
git clone https://github.com/Honnagiri01/thesismind_ai.git
cd thesismind_ai

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt

# Setup Ollama (optional, for local LLM)
ollama pull llama2
ollama serve

# Run application
streamlit run app.py
```

The application will open at `http://localhost:8501`

## Usage Guide

### Step 1: Create a Project
- Navigate to **Projects** page
- Click **Create Project**
- Enter project name and description

### Step 2: Upload Documents
- Go to **Upload Documents**
- Upload PDF, DOCX, or TXT files (max 100MB each)
- System automatically processes documents

### Step 3: Analyze Documents
- Visit **Analysis** page
- View document overview, statistics, and trends
- Compare documents and find common themes

### Step 4: Identify Research Gaps
- Go to **Research Gap** page
- Review identified gaps and opportunities
- Use insights to guide thesis direction

### Step 5: Generate Thesis
- Navigate to **Generate Thesis**
- Configure thesis parameters and chapters
- Click **Start Generation**
- Review and edit chapters as needed

### Step 6: Export Thesis
- Go to **Downloads**
- Select format (DOCX, PDF, Markdown, LaTeX)
- Configure format-specific options
- Click **Export Thesis**

## Project Structure

```
thesismind_ai/
├── app.py                          # Main Streamlit application
├── pages/                          # Page modules
│   ├── dashboard.py               # Dashboard
│   ├── projects.py                # Project management
│   ├── upload_documents.py        # Document upload
│   ├── analysis.py                # Document analysis
│   ├── research_gap.py            # Research gap identification
│   ├── generate_thesis.py         # Thesis generation
│   ├── downloads.py               # Export options
│   └── settings.py                # Settings
├── backend/                        # Backend modules
│   ├── project_manager.py         # Project management
│   ├── document_processor.py      # Document parsing
│   ├── knowledge_extractor.py     # Knowledge extraction
│   ├── llm_interface.py           # LLM integration
│   ├── thesis_generator.py        # Thesis generation
│   └── export_manager.py          # Export functionality
├── utils/                          # Utility modules
│   ├── config.py                  # Configuration
│   └── ui.py                      # UI components
├── data/                           # Data directories
├── requirements.txt                # Dependencies
└── README.md                       # Documentation
```

## Technology Stack

- **Framework**: Streamlit 1.28+
- **Language**: Python 3.9+
- **LLM Models**: Llama 2, Mistral, or other open-weight models
- **NLP**: Transformers, LangChain
- **Document Processing**: PyPDF2, python-docx, pdfplumber
- **Data Processing**: Pandas, NumPy, Scikit-learn
- **Visualization**: Plotly, Matplotlib

## Supported Formats

| Input Formats | Output Formats |
|---|---|
| PDF | Word (.docx) |
| DOCX | PDF |
| TXT | Markdown (.md) |
| DOC | LaTeX (.tex) |

## Configuration

### Environment Variables

Create `.env` file:
```env
LLM_MODEL=llama2
LLM_HOST=http://localhost:11434
TEMPERATURE=0.7
MAX_DOCUMENTS=20
MAX_FILE_SIZE_MB=100
```

## Troubleshooting

### LLM Connection Issues
```bash
# Check Ollama is running
curl http://localhost:11434/api/tags

# Restart Ollama
ollama serve
```

### Document Processing Errors
- Ensure documents are valid PDF/DOCX/TXT files
- Check file size (max 100 MB)
- Verify file isn't corrupted

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to branch
5. Open a Pull Request

## License

MIT License - See LICENSE file for details

## Support

- **Issues**: [GitHub Issues](https://github.com/Honnagiri01/thesismind_ai/issues)
- **Email**: lhonnagirigowda@gmail.com

## Acknowledgments

- Streamlit for the amazing web framework
- Hugging Face for transformer models
- Open-source community for various libraries

---

**Made with ❤️ for researchers and academics**
