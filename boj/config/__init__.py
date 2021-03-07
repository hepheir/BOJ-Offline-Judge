import configparser
import os
import sys

VERSION = '1.0.2'
SETTINGS_DIRECTORY = os.path.join(os.getcwd(), '.boj')
CONFIG_FILE = os.path.join(SETTINGS_DIRECTORY, 'config.ini')

config = configparser.ConfigParser()

# DEFAULT SETTINGS
config['DEFAULT'] = {
    'version': VERSION,
    
    'path.temp.dirname': os.path.join(SETTINGS_DIRECTORY, 'temp'),
    'path.temp.stdout.filename': os.path.join('%(path.temp.dirname)s', 'stdout.txt'),

    'data.dirname': '%(srcDirname)s',
    'data.extension.inputfile': '.in',
    'data.extension.outputfile': '.out',
    
    'judge.run.timelimit': 4000,
    'judge.brief.time': True,
    'judge.brief.inputfile': True,
    
    'language.cpp.compiler.path': 'g++',
    'language.c.compiler.path': 'gcc',
    'language.python3.python.path': sys.executable,
}


if not os.path.exists(SETTINGS_DIRECTORY):
    os.makedirs(SETTINGS_DIRECTORY)
    with open(os.path.join(SETTINGS_DIRECTORY, '.gitignore'), 'w') as gitignore_file:
        gitignore_file.write('*\n')
    print('[INFO]',f'임시 디렉토리를 생성하였습니다: "{SETTINGS_DIRECTORY}"')

if not os.path.exists(CONFIG_FILE):
    print('[INFO]', '설정 파일을 생성하고 있습니다...'                      )
    config['user'] = {}
    with open(CONFIG_FILE, 'w') as config_file:
        config.write(config_file)
    print('[INFO]',f'설정 파일을 생성했습니다: "{CONFIG_FILE}"'             )
else:
    print('[INFO]', '설정 파일을 불러오고 있습니다...'                      )
    config.read(CONFIG_FILE, encoding='utf-8')

if config.get('DEFAULT', 'version', fallback='0.0.0') != VERSION:
    print('[INFO]', '구 버전의 설정파일이 감지되었습니다.'                  )
    
if True:
    print('----------------------------------------------------------------')
