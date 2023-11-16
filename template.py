import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name = 'textsummarizer'

list_of_files = [

        ".github/workflows/.gitkeep",
        "src/{}/__init__.py".format(project_name),
        'src/{}/components/__init__.py'.format(project_name),
        'src/{}/utils/__init__.py'.format(project_name),
        'src/{}/utils/common.py'.format(project_name),
        'src/{}/logging/__init__.py'.format(project_name),
        'src/{}/config/__init__.py'.format(project_name),
        'src/{}/config/configuration.py'.format(project_name),
        'src/{}/pipeline/__init__.py'.format(project_name),
        'src/{}/entity/__init__.py'.format(project_name),
        'src/{}/constants/__init__.py'.format(project_name),

        'config/config.yaml',
        'params.yaml',
        "Dockerfile",
        'app.py',
        'main.py',
        'requirements.txt',
        'setup.py',
        'research/trails.ipynb'

]

for file in list_of_files:
    file = os.path.abspath(file)
    filedir,filename = os.path.split(file)

    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info('Creating directory :{} for the file {}'.format(filedir, filename))

    if (not os.path.exists(file)) or (os.path.getsize(file) == 0):
        with open(file,'w') as f:
            pass
            logging.info('Creating empty file :{}'.format(file))

    else:
        logging.info('File already exists :{}'.format(file))
