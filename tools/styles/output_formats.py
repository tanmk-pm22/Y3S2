"""
Output formatting utilities for Jupyter notebooks.
Provides consistent styling and formatting for notebook outputs.
"""

from IPython.display import HTML, Markdown, display
import json


def format_section_header(title, level=1, emoji=""):
    """
    Create a formatted section header.

    Args:
        title (str): Section title
        level (int): Header level (1-6)
        emoji (str): Optional emoji prefix
    """
    prefix = emoji + " " if emoji else ""
    header = f"{'#' * level} {prefix}{title}"
    display(Markdown(header))


def format_alert(message, alert_type="info"):
    """
    Display a styled alert box.

    Args:
        message (str): Alert message
        alert_type (str): Type of alert (info, warning, success, danger)
    """
    html = f'''
    <div class="alert alert-{alert_type}" role="alert">
        {message}
    </div>
    '''
    display(HTML(html))


def format_code_output(code, language="python"):
    """
    Display code with syntax highlighting.

    Args:
        code (str): Code to display
        language (str): Programming language
    """
    markdown = f"```{language}\n{code}\n```"
    display(Markdown(markdown))


def format_table(data, headers=None):
    """
    Create a formatted markdown table.

    Args:
        data (list): List of rows (each row is a list)
        headers (list): Optional column headers
    """
    if headers:
        table = "| " + " | ".join(headers) + " |\n"
        table += "| " + " | ".join(["---"] * len(headers)) + " |\n"
    else:
        table = ""

    for row in data:
        table += "| " + " | ".join(str(cell) for cell in row) + " |\n"

    display(Markdown(table))


def format_key_points(points, title="Key Points"):
    """
    Display a formatted list of key points.

    Args:
        points (list): List of key points
        title (str): Section title
    """
    markdown = f"### {title}\n\n"
    for point in points:
        markdown += f"- {point}\n"
    display(Markdown(markdown))


def format_exercise(number, description, hints=None):
    """
    Format an exercise block.

    Args:
        number (int): Exercise number
        description (str): Exercise description
        hints (list): Optional hints
    """
    markdown = f"### Exercise {number}\n\n"
    markdown += f"**Task:** {description}\n\n"

    if hints:
        markdown += "**Hints:**\n"
        for hint in hints:
            markdown += f"- {hint}\n"

    display(Markdown(markdown))


def format_solution(code, explanation=""):
    """
    Format a solution with collapsible details.

    Args:
        code (str): Solution code
        explanation (str): Optional explanation
    """
    html = f'''
    <details>
    <summary><b>Click to see solution</b></summary>

    ```python
{code}
    ```

    {f"<p><b>Explanation:</b> {explanation}</p>" if explanation else ""}

    </details>
    '''
    display(HTML(html))


def format_progress_bar(current, total, label="Progress"):
    """
    Display a progress bar.

    Args:
        current (int): Current progress
        total (int): Total items
        label (str): Progress bar label
    """
    percentage = (current / total) * 100
    html = f'''
    <div style="margin: 10px 0;">
        <p><strong>{label}:</strong> {current}/{total} ({percentage:.1f}%)</p>
        <div style="width: 100%; background-color: #f0f0f0; border-radius: 5px; overflow: hidden;">
            <div style="width: {percentage}%; background-color: #3498db; height: 20px; transition: width 0.3s;"></div>
        </div>
    </div>
    '''
    display(HTML(html))


def format_comparison_table(labels, values1, values2, label1="Method 1", label2="Method 2"):
    """
    Create a comparison table for two datasets.

    Args:
        labels (list): Row labels
        values1 (list): Values for first column
        values2 (list): Values for second column
        label1 (str): Header for first column
        label2 (str): Header for second column
    """
    headers = ["Metric", label1, label2]
    data = [[labels[i], values1[i], values2[i]] for i in range(len(labels))]
    format_table(data, headers)


def format_objectives(objectives, title="Learning Objectives"):
    """
    Display learning objectives as a checklist.

    Args:
        objectives (list): List of learning objectives
        title (str): Section title
    """
    markdown = f"### {title}\n\n"
    markdown += "By the end of this section, you should be able to:\n\n"
    for obj in objectives:
        markdown += f"- [ ] {obj}\n"
    display(Markdown(markdown))


def format_summary(points, title="Summary"):
    """
    Create a formatted summary section.

    Args:
        points (dict): Dictionary of summary points (key: category, value: list of points)
        title (str): Summary title
    """
    markdown = f"## {title}\n\n"
    for category, items in points.items():
        markdown += f"### {category}\n\n"
        for item in items:
            markdown += f"- {item}\n"
        markdown += "\n"
    display(Markdown(markdown))


# Color schemes for different output types
COLORS = {
    'primary': '#3498db',
    'success': '#27ae60',
    'warning': '#f39c12',
    'danger': '#e74c3c',
    'info': '#16a085',
    'dark': '#2c3e50',
    'light': '#ecf0f1'
}


def get_color(color_name):
    """Get color code from predefined color scheme."""
    return COLORS.get(color_name, COLORS['primary'])
