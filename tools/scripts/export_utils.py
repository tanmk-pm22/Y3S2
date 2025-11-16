#!/usr/bin/env python3
"""
Utilities for exporting Jupyter notebooks to various formats.
"""

import os
import subprocess
import argparse
from pathlib import Path


def export_notebook(notebook_path, output_format, output_dir=None):
    """
    Export a Jupyter notebook to specified format.

    Args:
        notebook_path (str): Path to the notebook
        output_format (str): Output format (html, pdf, markdown, slides)
        output_dir (str): Optional output directory
    """
    if not os.path.exists(notebook_path):
        print(f"[!] Error: Notebook not found: {notebook_path}")
        return False

    # Determine output directory
    if output_dir is None:
        notebook_dir = os.path.dirname(notebook_path)
        if "DPP" in notebook_path:
            output_dir = "outputs/DPP/reports"
        elif "ECP" in notebook_path:
            output_dir = "outputs/ECP/exports"
        else:
            output_dir = "outputs"

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Get notebook name without extension
    notebook_name = Path(notebook_path).stem

    # Build export command
    if output_format == "html":
        output_file = os.path.join(output_dir, f"{notebook_name}.html")
        command = f"jupyter nbconvert --to html '{notebook_path}' --output '{output_file}'"

    elif output_format == "pdf":
        output_file = os.path.join(output_dir, f"{notebook_name}.pdf")
        command = f"jupyter nbconvert --to pdf '{notebook_path}' --output '{output_file}'"

    elif output_format == "markdown":
        output_file = os.path.join(output_dir, f"{notebook_name}.md")
        command = f"jupyter nbconvert --to markdown '{notebook_path}' --output '{output_file}'"

    elif output_format == "slides":
        output_file = os.path.join(output_dir, f"{notebook_name}_slides.html")
        command = f"jupyter nbconvert --to slides '{notebook_path}' --output '{output_file}'"

    elif output_format == "script":
        output_file = os.path.join(output_dir, f"{notebook_name}.py")
        command = f"jupyter nbconvert --to script '{notebook_path}' --output '{output_file}'"

    else:
        print(f"[!] Error: Unknown format '{output_format}'")
        return False

    # Execute export
    print(f"[*] Exporting {notebook_path} to {output_format}...")
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"[✓] Successfully exported to: {output_file}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[!] Error during export: {e}")
        return False


def export_directory(directory, output_format, recursive=False):
    """
    Export all notebooks in a directory.

    Args:
        directory (str): Directory containing notebooks
        output_format (str): Output format
        recursive (bool): Recursively export subdirectories
    """
    if recursive:
        pattern = "**/*.ipynb"
    else:
        pattern = "*.ipynb"

    notebooks = list(Path(directory).glob(pattern))

    if not notebooks:
        print(f"[!] No notebooks found in {directory}")
        return

    print(f"[*] Found {len(notebooks)} notebook(s)")

    success_count = 0
    for notebook in notebooks:
        if export_notebook(str(notebook), output_format):
            success_count += 1

    print(f"\n[✓] Successfully exported {success_count}/{len(notebooks)} notebooks")


def clean_notebook_outputs(notebook_path):
    """
    Clean all outputs from a notebook (useful before committing to git).

    Args:
        notebook_path (str): Path to the notebook
    """
    command = f"jupyter nbconvert --clear-output --inplace '{notebook_path}'"
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"[✓] Cleaned outputs from: {notebook_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[!] Error cleaning notebook: {e}")
        return False


def extract_code(notebook_path, output_dir=None):
    """
    Extract all code cells from a notebook to a Python file.

    Args:
        notebook_path (str): Path to the notebook
        output_dir (str): Optional output directory
    """
    if output_dir is None:
        if "DPP" in notebook_path:
            output_dir = "outputs/DPP/code"
        elif "ECP" in notebook_path:
            output_dir = "outputs/ECP/code"
        else:
            output_dir = "outputs"

    return export_notebook(notebook_path, "script", output_dir)


def batch_export(course, output_format):
    """
    Export all notebooks for a specific course.

    Args:
        course (str): Course name (DPP or ECP)
        output_format (str): Output format
    """
    course_dir = f"notebooks/{course}"
    if not os.path.exists(course_dir):
        print(f"[!] Error: Course directory not found: {course_dir}")
        return

    export_directory(course_dir, output_format, recursive=True)


def main():
    """Main function for command-line usage."""
    parser = argparse.ArgumentParser(description="Export Jupyter notebooks")
    parser.add_argument("path", help="Path to notebook or directory")
    parser.add_argument("--format", "-f", default="html",
                        choices=["html", "pdf", "markdown", "slides", "script"],
                        help="Export format")
    parser.add_argument("--output", "-o", help="Output directory")
    parser.add_argument("--recursive", "-r", action="store_true",
                        help="Recursively process directories")
    parser.add_argument("--clean", action="store_true",
                        help="Clean outputs instead of exporting")

    args = parser.parse_args()

    if args.clean:
        if os.path.isfile(args.path):
            clean_notebook_outputs(args.path)
        else:
            notebooks = Path(args.path).glob("**/*.ipynb" if args.recursive else "*.ipynb")
            for notebook in notebooks:
                clean_notebook_outputs(str(notebook))
    else:
        if os.path.isfile(args.path):
            export_notebook(args.path, args.format, args.output)
        else:
            export_directory(args.path, args.format, args.recursive)


if __name__ == "__main__":
    main()
