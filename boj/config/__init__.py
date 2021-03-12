import configparser
import os

from boj.config.settings_directory import SETTINGS_DIRECTORY
from boj.config.default_settings import DEFAULT_SETTINGS
from boj.config.user_settings import USER_SETTINGS
from boj.__version__ import __version__


###############################################################

CONFIG_FILE = os.path.join(SETTINGS_DIRECTORY, 'config.ini')

print('[INFO]', f'설정 파일 "{CONFIG_FILE}"')
print('----------------------------------------------------------------')

config = configparser.ConfigParser()

if os.path.isfile(CONFIG_FILE):
    print('[INFO]', '설정 파일을 발견하였습니다.')
    config.read(CONFIG_FILE, encoding='utf-8')

    if config.get('user', 'version', fallback='<no_version>') != __version__:
        print('[INFO]', '설정 파일을 현재의 버전에 맞도록 업데이트 합니다.')
        config['DEFAULT'] = DEFAULT_SETTINGS
        # 기존 사용자 설정은 유지하며 새로운 항목 업데이트
        for option, default_value in USER_SETTINGS.items():
            config['user'][option] = config.get(
                'user', option, fallback=default_value)
        # 설정 파일 생성
        with open(CONFIG_FILE, 'w') as config_file:
            config.write(config_file)
        print('[INFO]', '설정 파일 업데이트를 완료했습니다.')
    else:
        print('[INFO]', '설정 파일을 불러왔습니다.')

elif os.path.isdir(CONFIG_FILE):
    raise IsADirectoryError('설정 파일을 생성 할 수 없습니다.\n같은 명의 디렉토리가 존재합니다.')

else:
    print('[INFO]', '설정 파일을 생성하고 있습니다...')
    config['DEFAULT'] = DEFAULT_SETTINGS
    config['user'] = USER_SETTINGS
    # 설정 파일 생성
    with open(CONFIG_FILE, 'w') as config_file:
        config.write(config_file)
    print('[INFO]', '설정 파일 생성을 완료했습니다.')

print('================================================================')
