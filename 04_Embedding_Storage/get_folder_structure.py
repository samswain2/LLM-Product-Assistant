import os

def generate_markdown_folder_structure(root_dir):
    """
    Generates the folder structure in a markdown format starting from the given root directory.
    """
    markdown_structure = ""
    for root, dirs, files in os.walk(root_dir):
        level = root.replace(root_dir, '').count(os.sep)
        indent = ' ' * 4 * level
        if root != root_dir:
            markdown_structure += f'{indent}├── {os.path.basename(root)}/\n'
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            markdown_structure += f'{subindent}├── {f}\n'

    return markdown_structure.strip()

# Example usage
markdown_folder_structure = generate_markdown_folder_structure('.')
print(markdown_folder_structure)