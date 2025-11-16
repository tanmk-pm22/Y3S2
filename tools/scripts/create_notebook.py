#!/usr/bin/env python3
"""
Script to create new notebooks from templates.
"""

import os
import shutil
import argparse
from pathlib import Path


TEMPLATES = {
    "chapter": "tools/templates/chapter_template.ipynb",
    "practical": "tools/templates/practical_template.ipynb",
    "notes": "tools/templates/notes_template.ipynb",
}


def create_notebook(template_type, output_path, title=None):
    """
    Create a new notebook from a template.

    Args:
        template_type (str): Type of template (chapter, practical, notes)
        output_path (str): Where to save the new notebook
        title (str): Optional title for the notebook
    """
    if template_type not in TEMPLATES:
        print(f"[!] Error: Unknown template type '{template_type}'")
        print(f"[*] Available templates: {', '.join(TEMPLATES.keys())}")
        return False

    template_path = TEMPLATES[template_type]

    if not os.path.exists(template_path):
        print(f"[!] Error: Template not found: {template_path}")
        return False

    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    # Copy template to output location
    try:
        shutil.copy(template_path, output_path)
        print(f"[✓] Created notebook: {output_path}")

        # TODO: If title is provided, could modify the notebook to include it
        # This would require reading the JSON, modifying it, and writing back

        return True
    except Exception as e:
        print(f"[!] Error creating notebook: {e}")
        return False


def create_chapter_notebook(chapter_number, course="DPP", title=None):
    """
    Create a chapter notebook with proper naming and location.

    Args:
        chapter_number (int): Chapter number
        course (str): Course name (DPP or ECP)
        title (str): Chapter title
    """
    chapter_dir = f"notebooks/{course}/{chapter_number:02d}-Chapter-{chapter_number:02d}"

    if not os.path.exists(chapter_dir):
        print(f"[!] Warning: Directory {chapter_dir} doesn't exist")
        print(f"[*] Creating directory...")
        os.makedirs(chapter_dir, exist_ok=True)

    if title:
        filename = f"chapter-{chapter_number:02d}-{title.lower().replace(' ', '-')}.ipynb"
    else:
        filename = f"chapter-{chapter_number:02d}.ipynb"

    output_path = os.path.join(chapter_dir, filename)

    return create_notebook("chapter", output_path, title)


def create_practical_notebook(practical_number, title=None):
    """
    Create a practical notebook.

    Args:
        practical_number (int): Practical number
        title (str): Practical title
    """
    practical_dir = "notebooks/DPP/Practicals"

    if title:
        filename = f"P{practical_number:02d}-{title.lower().replace(' ', '-')}.ipynb"
    else:
        filename = f"P{practical_number:02d}-practical-{practical_number}.ipynb"

    output_path = os.path.join(practical_dir, filename)

    return create_notebook("practical", output_path, title)


def main():
    """Main function for command-line usage."""
    parser = argparse.ArgumentParser(description="Create new Jupyter notebooks from templates")
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Chapter notebook
    chapter_parser = subparsers.add_parser("chapter", help="Create a chapter notebook")
    chapter_parser.add_argument("number", type=int, help="Chapter number")
    chapter_parser.add_argument("--course", "-c", default="DPP", help="Course name (DPP or ECP)")
    chapter_parser.add_argument("--title", "-t", help="Chapter title")

    # Practical notebook
    practical_parser = subparsers.add_parser("practical", help="Create a practical notebook")
    practical_parser.add_argument("number", type=int, help="Practical number")
    practical_parser.add_argument("--title", "-t", help="Practical title")

    # Notes notebook
    notes_parser = subparsers.add_parser("notes", help="Create a notes notebook")
    notes_parser.add_argument("path", help="Output path for the notebook")
    notes_parser.add_argument("--title", "-t", help="Notes title")

    # Generic notebook
    generic_parser = subparsers.add_parser("create", help="Create a notebook from template")
    generic_parser.add_argument("template", choices=TEMPLATES.keys(), help="Template type")
    generic_parser.add_argument("output", help="Output path")
    generic_parser.add_argument("--title", "-t", help="Notebook title")

    args = parser.parse_args()

    if args.command == "chapter":
        create_chapter_notebook(args.number, args.course, args.title)
    elif args.command == "practical":
        create_practical_notebook(args.number, args.title)
    elif args.command == "notes":
        create_notebook("notes", args.path, args.title)
    elif args.command == "create":
        create_notebook(args.template, args.output, args.title)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
