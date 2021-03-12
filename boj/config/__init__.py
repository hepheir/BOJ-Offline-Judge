import codecs
import configparser
import os

from boj.config.settings_directory import SETTINGS_DIRECTORY
from boj.config.default_settings import DEFAULT_SETTINGS
from boj.config.user_settings import USER_SETTINGS
from boj.__version__ import __version__

CONFIG_FILE = os.path.join(SETTINGS_DIRECTORY, 'config.ini')


###############################################################

def _save_as(filename, *args, **kwargs):
    with open(filename, 'w', encoding='utf8') as config_file:
        config.write(config_file)


config = configparser.ConfigParser()
config.save_as = _save_as

print('[INFO]', f'설정 파일 "{CONFIG_FILE}"')
print('----------------------------------------------------------------')

if os.path.isfile(CONFIG_FILE):
    print('[INFO]', '설정 파일을 발견하였습니다.')
    config.read_file(codecs.open(CONFIG_FILE, "r", "utf8"))

    if config.get('user', 'version', fallback='<no_version>') != __version__:
        print('[INFO]', '설정 파일을 현재의 버전에 맞도록 업데이트 합니다.')
        config['DEFAULT'] = DEFAULT_SETTINGS
        # 기존 사용자 설정은 유지하며 새로운 항목 업데이트
        for option, default_value in USER_SETTINGS.items():
            config['user'][option] = config.get('user', option, fallback=default_value)
        config.save_as(CONFIG_FILE)
        print('[INFO]', '설정 파일 업데이트를 완료했습니다.')
    else:
        print('[INFO]', '설정 파일을 불러왔습니다.')

elif os.path.isdir(CONFIG_FILE):
    raise IsADirectoryError('설정 파일을 생성 할 수 없습니다.\n같은 명의 디렉토리가 존재합니다.')

else:
    print('[INFO]', '설정 파일을 생성하고 있습니다...')
    config['DEFAULT'] = DEFAULT_SETTINGS
    config['user'] = USER_SETTINGS
    config.save_as(CONFIG_FILE)
    print('[INFO]', '설정 파일 생성을 완료했습니다.')

print('================================================================')
