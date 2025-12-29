import os
import importlib
from pathlib import Path

# Shared prompts structures
prompts = {}

# Dynamically import all Python files in this directory
current_dir = Path(__file__).parent

for file in current_dir.glob("*.py"):
    # Skip __init__.py
    if file.name == "__init__.py":
        continue
    
    # Import the module
    module_name = file.stem  # filename without .py
    importlib.import_module(f".{module_name}", package=__package__)

__all__ = ["prompts"]