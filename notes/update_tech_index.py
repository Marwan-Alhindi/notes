import os
import re
from collections import defaultdict

# Your Dendron vault path (adjust to your actual folder)
VAULT_PATH = "./notes"  # <-- change this to your actual notes folder path

# Markers for generated section
START_MARK = "<!-- AUTO-GENERATED CHILDREN START -->"
END_MARK = "<!-- AUTO-GENERATED CHILDREN END -->"

def collect_children():
    """
    Build a mapping of parent -> list of children based on note file names.
    For example, a note "tech.python.test1" will contribute "tech.python" as a parent.
    """
    files = [f[:-3] for f in os.listdir(VAULT_PATH) if f.endswith(".md")]
    hierarchy = defaultdict(list)
    for note in files:
        parts = note.split(".")
        for i in range(1, len(parts)):
            parent = ".".join(parts[:i])
            hierarchy[parent].append(note)
    return hierarchy

def update_note_file(note_name, children):
    """
    Update the note file identified by note_name (if it exists) by inserting or
    replacing the auto-generated children section with the links to its children.
    """
    filepath = os.path.join(VAULT_PATH, f"{note_name}.md")
    if not os.path.exists(filepath):
        return
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Generate children links (sorted alphabetically)
    children_links = "\n".join(f"- [[{child}]]" for child in sorted(children))
    replacement = f"{START_MARK}\n{children_links}\n{END_MARK}"
    pattern = re.compile(f"{re.escape(START_MARK)}.*?{re.escape(END_MARK)}", re.DOTALL)

    if pattern.search(content):
        # Replace existing auto-generated section
        content = pattern.sub(replacement, content)
    else:
        # Append the auto-generated section
        content += f"\n\n{replacement}"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Updated {note_name}.md")

def main():
    """
    Collects the current children mapping and then updates every note file that:
      - Appears as a parent in the hierarchy, or
      - Already contains the auto-generated children marker.
    This way, if a child note is deleted, its parent's file will be updated (even if no children remain).
    """
    hierarchy = collect_children()
    files = [f[:-3] for f in os.listdir(VAULT_PATH) if f.endswith(".md")]
    for note in files:
        filepath = os.path.join(VAULT_PATH, f"{note}.md")
        # Read the current file content
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        # Get the children for this note, if any
        children = hierarchy.get(note, [])
        # If this note already has an auto-generated section OR there are children to list, update it.
        if children or START_MARK in content:
            update_note_file(note, children)

if __name__ == "__main__":
    main()