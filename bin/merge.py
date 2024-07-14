#-*- coding: utf-8 -*-

#merge md and it folder



# work folder C:\Users\czh99\Documents\work_for_free\vitepress-blog\docs\old-blog
# for any markdown files in C:\Users\czh99\Documents\work_for_free\vitepress-blog\docs\old-blog
# copy the files to their same name folder
# And generate the list with following format
#     - theme: brand
#      text: <markdown file>
#      link: /old-blog/<markdown file>/<markdown file>
import os
import shutil

# Define the base directory
base_dir = r'C:\Users\czh99\Documents\work_for_free\vitepress-blog\docs\old-blog'

# List to hold the output in the required format
output_list = []

# Iterate over all files in the base directory
for filename in os.listdir(base_dir):
    if filename.endswith('.md'):
        # Define full file paths
        file_path = os.path.join(base_dir, filename)
        folder_name = filename[:-3]  # Remove the '.md' extension
        new_folder_path = os.path.join(base_dir, folder_name)
        
        # Create new folder
        os.makedirs(new_folder_path, exist_ok=True)
        
        # Define new file path
        new_file_path = os.path.join(new_folder_path, filename)
        
        # Copy the file to the new folder
        shutil.copy(file_path, new_file_path)
        
        # Add entry to the output list
        output_list.append({
            'theme': 'brand',
            'text': filename,
            'link': f'/old-blog/{folder_name}/{folder_name}'
        })

# Print the output list in the required format
for item in output_list:
    print(f"- theme: {item['theme']}")
    print(f"  text: {item['text']}")
    print(f"  link: {item['link']}")

# for every ![<name of picture>](/<name of picture>) in md file
#replace it with ![<name of picture>](./<name of picture>) 
#