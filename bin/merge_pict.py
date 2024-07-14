import re
import os

def update_image_paths_in_file(file_path):
    # Define the regex pattern to match the image references
    pattern = re.compile(r'!\[([^\]]+)\]\(/([^\)]+)\)')
    
    try:
        # Read the contents of the markdown file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Replace the matches with the desired format
        updated_content = pattern.sub(r'![\1](./\2)', content)

        # Write the updated content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)

        print(f"Updated {file_path}")
    
    except Exception as e:
        print(f"Failed to update {file_path}: {e}")

base_dir = r'C:\Users\czh99\Documents\work_for_free\vitepress-blog\docs\old-blog'

# Iterate over all files in the base directory
for filename in os.listdir(base_dir):
    file_path = os.path.join(base_dir, filename)
    if os.path.isfile(file_path) and file_path.endswith('.md'):
        update_image_paths_in_file(file_path)