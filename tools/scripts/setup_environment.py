#!/usr/bin/env python3
"""
Setup script for Jupyter notebook learning environment.
Installs dependencies and configures Jupyter extensions.
"""

import subprocess
import sys
import os


def run_command(command, description):
    """Run a shell command and handle errors."""
    print(f"\n{'=' * 60}")
    print(f"[*] {description}")
    print(f"{'=' * 60}")
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"[!] Error: {e}")
        print(e.stderr)
        return False


def install_requirements():
    """Install Python requirements."""
    print("\n[1/5] Installing Python requirements...")
    return run_command(
        f"{sys.executable} -m pip install -r requirements.txt",
        "Installing dependencies from requirements.txt"
    )


def setup_jupyter_extensions():
    """Set up Jupyter notebook extensions."""
    print("\n[2/5] Setting up Jupyter extensions...")

    commands = [
        ("jupyter contrib nbextension install --user", "Installing Jupyter contrib extensions"),
        ("jupyter nbextensions_configurator enable --user", "Enabling extensions configurator"),
    ]

    for cmd, desc in commands:
        if not run_command(cmd, desc):
            print(f"[!] Warning: {desc} failed (may already be installed)")

    # Enable useful extensions
    extensions = [
        "toc2/main",  # Table of Contents
        "execute_time/ExecuteTime",  # Show execution time
        "code_prettify/code_prettify",  # Code formatting
        "collapsible_headings/main",  # Collapsible sections
        "codefolding/main",  # Code folding
    ]

    for ext in extensions:
        run_command(
            f"jupyter nbextension enable {ext}",
            f"Enabling {ext} extension"
        )


def install_jupyter_kernel():
    """Install IPython kernel."""
    print("\n[3/5] Installing IPython kernel...")
    return run_command(
        f"{sys.executable} -m ipykernel install --user --name=python3 --display-name='Python 3 (Y3S2)'",
        "Installing IPython kernel for Y3S2"
    )


def setup_custom_css():
    """Copy custom CSS to Jupyter config."""
    print("\n[4/5] Setting up custom CSS...")

    # Get Jupyter config directory
    try:
        result = subprocess.run(
            "jupyter --config-dir",
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        config_dir = result.stdout.strip()
        custom_dir = os.path.join(config_dir, "custom")
        os.makedirs(custom_dir, exist_ok=True)

        # Copy custom CSS
        custom_css_source = os.path.join("tools", "styles", "custom.css")
        custom_css_dest = os.path.join(custom_dir, "custom.css")

        if os.path.exists(custom_css_source):
            import shutil
            shutil.copy(custom_css_source, custom_css_dest)
            print(f"[✓] Custom CSS copied to {custom_css_dest}")
            return True
        else:
            print(f"[!] Warning: {custom_css_source} not found")
            return False
    except Exception as e:
        print(f"[!] Error setting up custom CSS: {e}")
        return False


def verify_installation():
    """Verify that key packages are installed."""
    print("\n[5/5] Verifying installation...")

    required_packages = [
        "jupyter",
        "notebook",
        "jupyterlab",
        "numpy",
        "pandas",
        "matplotlib",
    ]

    all_installed = True
    for package in required_packages:
        try:
            __import__(package)
            print(f"[✓] {package} is installed")
        except ImportError:
            print(f"[✗] {package} is NOT installed")
            all_installed = False

    return all_installed


def main():
    """Main setup function."""
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║       Y3S2 Jupyter Notebook Environment Setup                ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """)

    # Check if running in correct directory
    if not os.path.exists("requirements.txt"):
        print("[!] Error: requirements.txt not found!")
        print("[!] Please run this script from the Y3S2 directory.")
        sys.exit(1)

    steps = [
        install_requirements,
        setup_jupyter_extensions,
        install_jupyter_kernel,
        setup_custom_css,
        verify_installation,
    ]

    for step in steps:
        try:
            step()
        except Exception as e:
            print(f"[!] Error during {step.__name__}: {e}")
            print("[!] Continuing with next step...")

    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                    Setup Complete!                           ║
║                                                              ║
║  Next steps:                                                 ║
║  1. Launch Jupyter: jupyter notebook                         ║
║  2. Navigate to notebooks/ directory                         ║
║  3. Start learning!                                          ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """)


if __name__ == "__main__":
    main()
