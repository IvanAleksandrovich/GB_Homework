import os

listdir = ['settings', 'mainapp', 'adminapp', 'authapp']

for _dir in listdir:
    if not os.path.exists(_dir):
        os.makedirs(f'my_project/{_dir}')
