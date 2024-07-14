import os
import re
from pypinyin import pinyin, Style

def chinese_to_pinyin(chinese_string):
    """Convert Chinese characters to Pinyin."""
    pinyin_list = pinyin(chinese_string, style=Style.NORMAL)
    return ''.join(word[0] for word in pinyin_list)

def rename_files_and_update_references(root_dir):
    # Traverse all subfolders
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.png'):
                # Check if the filename contains Chinese characters
                if any('\u4e00' <= char <= '\u9fff' for char in file):
                    # Convert the filename to Pinyin
                    pinyin_name = chinese_to_pinyin(os.path.splitext(file)[0]) + '.png'
                    old_path = os.path.join(subdir, file)
                    new_path = os.path.join(subdir, pinyin_name)
                    
                    # Rename the file
                    os.rename(old_path, new_path)
                    print(f"Renamed: {old_path} -> {new_path}")
                    
                    # Update references in Markdown files
                    for subdir_md, _, files_md in os.walk(root_dir):
                        for file_md in files_md:
                            if file_md.endswith('.md'):
                                md_path = os.path.join(subdir_md, file_md)
                                with open(md_path, 'r', encoding='utf-8') as md_file:
                                    content = md_file.read()
                                
                                # Update the reference
                                updated_content = re.sub(re.escape(file), pinyin_name, content)
                                
                                if content != updated_content:
                                    with open(md_path, 'w', encoding='utf-8') as md_file:
                                        md_file.write(updated_content)
                                    print(f"Updated reference in: {md_path}")

# Set the root directory
root_directory = 'C:\\Users\\czh99\\Documents\\work_for_free\\vitepress-blog\\docs\\old-blog'

# Run the function
rename_files_and_update_references(root_directory)