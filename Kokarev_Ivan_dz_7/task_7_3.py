import os
import shutil

for root, dirs, files in os.walk('my_project'):
    if root.find('templates') > 0 and len(files) == 0:
        shutil.copytree(root, 'my_project/templates', dirs_exist_ok=True)

# для html:

folder = 'my_project'
dst = 'my_project/templates'

for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith('.html'):
            path = os.path.split(root)[0]
            shutil.copytree(path, dst, dirs_exist_ok=True)
