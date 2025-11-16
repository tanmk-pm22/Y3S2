# Y3S2 Jupyter Notebooks - Usage Guide

This guide will help you get started with your learning notebooks.

## Quick Start

### 1. Environment Setup

First, set up your environment by installing all dependencies:

```bash
python3 tools/scripts/setup_environment.py
```

This will:
- Install all required Python packages
- Configure Jupyter extensions
- Set up custom styling
- Install the IPython kernel

### 2. Launch Jupyter

```bash
jupyter notebook
```

Navigate to the `notebooks/` directory and select your course.

---

## Directory Overview

### 📚 notebooks/
Your learning notebooks organized by course:
- **DPP/** - Distributed Parallel Processing (12 chapters + practicals)
- **ECP/** - English for Career Preparation (4 modules)

### 📖 resources/
Original course materials (PDFs, slides) - read-only reference

### 📊 outputs/
Generated content from your notebooks:
- **code/** - Extracted Python code
- **images/** - Visualizations and diagrams
- **reports/** - Exported HTML/PDF reports
- **drafts/** - Proposal drafts (ECP)

### 🛠️ tools/
Utilities to enhance your workflow:
- **templates/** - Notebook templates
- **styles/** - Custom CSS and formatting
- **scripts/** - Automation scripts

---

## Working with Notebooks

### Creating a New Notebook

#### Using Python Script:

```bash
# Create a chapter notebook
python3 tools/scripts/create_notebook.py chapter 1 --course DPP --title "Introduction"

# Create a practical notebook
python3 tools/scripts/create_notebook.py practical 1 --title "Concurrency Basics"

# Create a notes notebook
python3 tools/scripts/create_notebook.py notes notebooks/DPP/Notes/my-notes.ipynb
```

#### Using Claude Code Slash Commands:

```
/new-chapter 1 DPP "Introduction"
/new-practical 1 "Concurrency Basics"
```

### Available Templates

1. **chapter_template.ipynb**
   - Structured learning notebook
   - Sections: Introduction, Key Concepts, Examples, Exercises, Summary
   - Includes learning objectives and TOC

2. **practical_template.ipynb**
   - Hands-on exercise notebook
   - Setup, tasks, testing, analysis, visualization
   - Performance comparison sections

3. **notes_template.ipynb**
   - Quick reference and personal notes
   - Flexible structure for capturing ideas

---

## Exporting Notebooks

### Export to HTML

```bash
python3 tools/scripts/export_utils.py notebooks/DPP/00-Introduction/chapter-00.ipynb --format html
```

### Export Entire Course

```bash
# Export all DPP notebooks to HTML
python3 tools/scripts/export_utils.py notebooks/DPP --format html --recursive
```

### Supported Formats
- **html** - Web page (recommended for sharing)
- **pdf** - PDF document (requires LaTeX)
- **markdown** - Markdown file
- **slides** - HTML slides presentation
- **script** - Python script (code only)

### Using Slash Commands:

```
/export-notebook notebooks/DPP/00-Introduction/chapter-00.ipynb html
```

---

## Styling and Formatting

### Custom CSS

Custom styling is automatically applied via `tools/styles/custom.css`. Features include:
- Professional color scheme
- Enhanced code highlighting
- Styled tables and alerts
- Collapsible sections

### Output Formatting

Use the output formatting utilities in your notebooks:

```python
# Import formatting utilities
import sys
sys.path.append('../../tools/styles')
from output_formats import *

# Create formatted section headers
format_section_header("Key Concepts", level=2, emoji="🔑")

# Display alerts
format_alert("This is an important concept!", "info")
format_alert("Warning: Complex topic ahead", "warning")

# Create formatted tables
headers = ["Method", "Time Complexity", "Space Complexity"]
data = [
    ["Bubble Sort", "O(n²)", "O(1)"],
    ["Quick Sort", "O(n log n)", "O(log n)"],
]
format_table(data, headers)

# Format exercises
format_exercise(1, "Implement parallel merge sort",
                hints=["Consider divide and conquer", "Use threading"])

# Progress tracking
format_progress_bar(7, 12, "Chapter Progress")
```

---

## Best Practices

### 1. Notebook Organization

- Keep one major topic per notebook
- Use clear, descriptive names
- Number notebooks if order matters
- Add table of contents for long notebooks

### 2. Version Control

- Clean outputs before committing:
  ```bash
  python3 tools/scripts/export_utils.py notebook.ipynb --clean
  ```
- Commit regularly with clear messages
- Don't commit large data files

### 3. Learning Workflow

**Recommended approach:**

1. **Read** course materials in `resources/`
2. **Create** notebook from template
3. **Take notes** while learning concepts
4. **Code along** with examples
5. **Practice** with exercises
6. **Export** completed work to `outputs/`
7. **Review** and revise regularly

### 4. Code Quality

- Use meaningful variable names
- Add comments explaining complex logic
- Test your code in cells
- Use the formatting utilities for clean output

### 5. Staying Organized

- **DPP Course:**
  - Follow chapter order (00-11)
  - Complete practicals after related chapters
  - Use Exercises/ folder for extra practice
  - Keep notes in Notes/ folder

- **ECP Course:**
  - Work through modules sequentially
  - Save proposal drafts in outputs/ECP/drafts/
  - Analyze sample proposals in 03-Sample-Analysis/

---

## Troubleshooting

### Jupyter Won't Start

```bash
# Reinstall Jupyter
pip install --upgrade jupyter notebook

# Check if port is in use
jupyter notebook --port=8889
```

### Extensions Not Working

```bash
# Reinstall extensions
jupyter contrib nbextension install --user
jupyter nbextensions_configurator enable --user
```

### Import Errors

```bash
# Reinstall requirements
pip install -r requirements.txt --upgrade
```

### Custom CSS Not Applied

```bash
# Manually copy CSS
cp tools/styles/custom.css $(jupyter --config-dir)/custom/custom.css
```

---

## Useful Keyboard Shortcuts

### Command Mode (press Esc):
- **A** - Insert cell above
- **B** - Insert cell below
- **DD** - Delete cell
- **M** - Convert to markdown
- **Y** - Convert to code
- **Shift+Enter** - Run cell and select below

### Edit Mode (press Enter):
- **Ctrl+Shift+-** - Split cell
- **Tab** - Code completion
- **Shift+Tab** - Documentation

---

## Tips for Success

1. **Study Consistently** - Set aside dedicated time daily
2. **Practice Actively** - Write code, don't just read
3. **Take Good Notes** - Summarize concepts in your own words
4. **Complete Exercises** - Don't skip the practice problems
5. **Review Regularly** - Revisit previous chapters
6. **Ask Questions** - Use markdown cells to note questions
7. **Export Your Work** - Keep HTML copies as backups

---

## Additional Resources

### Jupyter Documentation
- [Official Jupyter Docs](https://jupyter-notebook.readthedocs.io/)
- [Markdown Guide](https://www.markdownguide.org/)

### Python for Scientific Computing
- NumPy, Pandas, Matplotlib tutorials
- [Python.org Documentation](https://docs.python.org/)

### Getting Help
- Review README files in each directory
- Check tool documentation in `tools/`
- Consult course materials in `resources/`

---

## Quick Reference Commands

```bash
# Setup environment
python3 tools/scripts/setup_environment.py

# Create new notebook
python3 tools/scripts/create_notebook.py chapter 1 --course DPP

# Export to HTML
python3 tools/scripts/export_utils.py path/to/notebook.ipynb --format html

# Clean outputs
python3 tools/scripts/export_utils.py path/to/notebook.ipynb --clean

# Launch Jupyter
jupyter notebook

# Launch JupyterLab (alternative interface)
jupyter lab
```

---

Happy Learning! 🎓
