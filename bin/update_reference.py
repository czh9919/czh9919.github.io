# Write a script for every markdown file in sub folder in a folder
# Update the picture reference from ./<pict>.PNG to ./<path_to_folder>/<pict>.PNG>
# 新的图片路径应当为C:\Users\czh99\Documents\work_for_free\vitepress-blog\docs的相对路径
# For example, the picture reference is C:/Users/czh99/Documents/work_for_free/vitepress-blog/docs/old-blog/Affine-softmax层的实现/Affine1.png
# The picture should update from ![1.png](./Affine1.png) to <!--  -->
import os
import re

# Function to update image paths in a markdown file
def update_image_paths(file_path, base_dir):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Define the pattern to find image references
    pattern = r'!\[(.*?)\]\(\./(.*?\.(?:jpg|png|PNG))\)'
    matches = re.findall(pattern, content, re.IGNORECASE)
    
    # Update the image references
    for match in matches:
        alt_text, image_name = match
        # Compute the relative path from base directory
        relative_image_path = os.path.relpath(file_path, base_dir).replace('\\', '/')
        # Compute the new image path
        new_image_path = os.path.join('/', os.path.dirname(relative_image_path), image_name).replace('\\', '/')
        # Replace the old path with the new path in the content
        content = content.replace(f'./{image_name}', new_image_path)
    
    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Function to process all markdown files in subfolders
def process_markdown_files(base_dir):
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                update_image_paths(file_path, base_dir)

if __name__ == "__main__":
    # Base directory containing markdown files
    base_dir = r'C:/Users/czh99/Documents/work_for_free/vitepress-blog/docs'
    
    # Process all markdown files
    process_markdown_files(base_dir)
