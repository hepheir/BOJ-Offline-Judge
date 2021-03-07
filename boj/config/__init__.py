import configparser
import os
import sys

VERSION = '1.0.2'
SETTINGS_DIRECTORY =  os.path.join(os.getcwd(), '.boj')
CONFIG_FILE = os.path.join(SETTINGS_DIRECTORY, 'config.ini')

config = configparser.ConfigParser()

# DEFAULT SETTINGS
config['DEFAULT'] = {
    'version': VERSION,
    'path.settings.dirname': SETTINGS_DIRECTORY,

    'path.temp.dirname': os.path.join('%(path.settings.dirname)s', 'temp'),
    'path.temp.stdout.filename': os.path.join('%(path.temp.dirname)s', 'stdout.txt'),
    'path.problem.dirname': os.path.join('problem', '%(problem.number)s %(problem.title)s'),
    'path.inputfile.ext': '.in',
    'path.outputfile.ext': '.out',
    'path.data.boj.sample.dirname': os.path.join('%(path.problem.dirname)s', 'data', 'boj', 'sample'),
    
    'judge.run.timelimit': 4000,
    'judge.brief.time': True,
    'judge.brief.inputfile': True,
    
    'language.cpp.compiler.path': 'g++',
    'language.c.compiler.path': 'gcc',
    'language.python3.python.path': sys.executable,
}


###############################################################
# .boj 디렉토리 생성
###############################################################
if not os.path.exists(SETTINGS_DIRECTORY):
    os.makedirs(SETTINGS_DIRECTORY)
    # .gitignore 생성
    with open(os.path.join(SETTINGS_DIRECTORY, '.gitignore'), 'w') as gitignore_file:
        gitignore_file.write('*\n')
    print('[INFO]',f'임시 디렉토리를 생성하였습니다: "{SETTINGS_DIRECTORY}"')


###############################################################
# 설정 파일 생성/불러오기
###############################################################
if not os.path.exists(CONFIG_FILE):
    print('[INFO]', '설정 파일을 생성하고 있습니다...'                      )
    config['user'] = {}
else:
    print('[INFO]', '설정 파일을 불러오고 있습니다...'                      )
    config.read(CONFIG_FILE, encoding='utf-8')


###############################################################
# 설정 파일 업데이트
###############################################################
with open(CONFIG_FILE, 'w') as config_file:
    config.write(config_file)
    print('[INFO]',f'설정 파일을 업데이트 했습니다: "{CONFIG_FILE}"'        )


###############################################################
# 버전 정보 확인
###############################################################
if config.get('DEFAULT', 'version', fallback='0.0.0') != VERSION:
    print('[INFO]', '구 버전의 설정파일이 감지되었습니다.'                  )


if True:
    print('----------------------------------------------------------------')
