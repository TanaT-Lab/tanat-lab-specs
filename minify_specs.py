#!/usr/bin/env python3
"""Minify Markdown files for context generation."""

import os
import re
import sys


def compress_md(text):
    """Compress Markdown text by removing comments and simplifying whitespace."""
    # 1. Remove Markdown comments
    text = re.sub(r"", "", text, flags=re.DOTALL)
    # 2. Simplify whitespace: replace multiple newlines with a single one
    text = re.sub(r"\n\s*\n", "\n", text)
    # 3. Remove trailing spaces
    text = re.sub(r"[ \t]+$", "", text, flags=re.MULTILINE)
    # 4. Remove bold/italic for LLM (optional, but saves tokens)
    text = text.replace("**", "").replace("__", "")
    return text.strip()


def generate_context(feature_name):
    """
    Generate a minified context file for a given feature by aggregating and compressing relevant Markdown files.
    """
    base_dir = "."
    constitution_path = os.path.join(base_dir, "constitution.md")
    feature_dir = os.path.join(base_dir, "features", feature_name)
    spec_path = os.path.join(feature_dir, "spec.md")
    tasks_path = os.path.join(feature_dir, "tasks.md")
    output_path = os.path.join(feature_dir, "context.min.md")

    if not os.path.exists(feature_dir):
        print(f"Error: Feature directory '{feature_dir}' not found.")
        return

    combined_content = []

    # Aggregation
    for label, path in [
        ("CONSTITUTION", constitution_path),
        ("SPEC", spec_path),
        ("TASKS", tasks_path),
    ]:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                content = compress_md(f.read())
                combined_content.append(f"### {label}\n{content}")
        else:
            print(f"Warning: {label} not found at {path}")

    # Final writing
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(combined_content))

    print(f"Context minified for '{feature_name}' at {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/minify_spec.py <feature_name>")
    else:
        generate_context(sys.argv[1])
