# Code Extractor Skill

This skill extracts and organizes code examples from notebooks.

## Capabilities

1. Extract all code cells from a notebook
2. Remove Jupyter-specific magic commands
3. Add proper comments and documentation
4. Organize code into logical functions/classes
5. Save to outputs/*/code/ directory

## Usage

When asked to extract code from notebooks:

1. Read the specified notebook(s)
2. Extract code cells
3. Clean and organize the code
4. Add appropriate headers and documentation
5. Save to the outputs directory with proper naming

## Output Format

- Python files (.py) with proper structure
- Include imports at the top
- Organize into functions/classes
- Add docstrings where appropriate
- Save to outputs/DPP/code/ or outputs/ECP/code/
