import os
import re
import shutil

def create_public_folder(base_dir):
    public_dir = os.path.join(base_dir, 'public')
    if not os.path.exists(public_dir):
        os.makedirs(public_dir)
    return public_dir

def move_images_to_public(public_dir, base_dir):
    image_paths = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                old_path = os.path.join(root, file)
                new_path = os.path.join(public_dir, file)
                
                # If a file with the same name already exists in the public folder, rename the new file
                if os.path.exists(new_path):
                    base, ext = os.path.splitext(file)
                    counter = 1
                    while os.path.exists(new_path):
                        new_path = os.path.join(public_dir, f"{base}_{counter}{ext}")
                        counter += 1
                
                shutil.move(old_path, new_path)
                image_paths.append((old_path, new_path))
    return image_paths

def update_image_references(file_path, image_paths):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    for old_path, new_path in image_paths:
        old_image = os.path.basename(old_path)
        new_image = os.path.basename(new_path)
        # Update all instances of the old image path in the markdown file content
        content = re.sub(rf'(\!\[.*?\]\()\.\/{old_image}(\))', rf'\1../public/{new_image}\2', content, flags=re.IGNORECASE)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def process_markdown_files(base_dir, image_paths):
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                update_image_references(file_path, image_paths)

if __name__ == "__main__":
    # Base directory containing markdown files and images
    base_dir = r'C:/Users/czh99/Documents/work_for_free/vitepress-blog/docs'
    
    # Create a public folder to move images to
    public_dir = create_public_folder(base_dir)
    
    # Move images to the public folder and get the list of moved images
    image_paths = move_images_to_public(public_dir, base_dir)
    
    # Update markdown files with the new image references
    process_markdown_files(base_dir, image_paths)
