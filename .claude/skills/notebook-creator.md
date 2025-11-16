# Notebook Creator Skill

This skill helps create structured Jupyter notebooks from course materials.

## Capabilities

1. Analyze PDF lecture notes or materials
2. Extract key concepts, headings, and structure
3. Create well-organized notebook with:
   - Clear section headings
   - Learning objectives
   - Code examples (where applicable)
   - Exercise placeholders
   - Summary sections

## Usage

When asked to create a notebook from course materials:

1. Read the source material (PDF or other)
2. Identify main topics and subtopics
3. Create notebook structure following the chapter template
4. Populate sections with:
   - Explanatory markdown cells
   - Code cells for examples
   - Exercise cells with hints
   - Summary and references

## Template Location

Base template: tools/templates/chapter_template.ipynb

## Output Location

- DPP notebooks: notebooks/DPP/{chapter-folder}/
- ECP notebooks: notebooks/ECP/{topic-folder}/
