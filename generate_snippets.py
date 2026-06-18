import ast
import json
import sys
from pathlib import Path

def extract_methods_to_snippets(source_file):
    path = Path(source_file)
    if not path.exists():
        print(f"Error: {source_file} not found.")
        return

    with open(path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=source_file)

    snippets = {}

    for node in ast.walk(tree):
        # Target both standalone functions and class methods
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            func_name = node.name
            
            # Skip private/magic methods if you don't want them cluttering snippets
            if func_name.startswith("__") and func_name.endswith("__"):
                continue

            # Extract the raw source lines for this specific method
            # ast.get_source_segment is available in Python 3.8+
            with open(path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                # ast lines are 1-indexed
                start_line = node.lineno - 1
                end_line = node.end_lineno
                body_lines = [line.rstrip() for line in lines[start_line:end_line]]

            # Create the VS Code snippet structure
            snippets[f"Method: {func_name}"] = {
                "prefix": f"snip-{func_name}",
                "body": body_lines,
                "description": f"Custom snippet for {func_name} from {path.name}"
            }

    # Output to a JSON file
    output_path = path.parent / f"{path.stem}_snippets.code-snippets"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(snippets, f, indent=4)
    
    print(f"Success! Snippets saved to {output_path}")
    print("Copy the contents of this file into your Codium user snippets.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_snippets.py <path_to_your_file.py>")
    else:
        extract_methods_to_snippets(sys.argv[1])