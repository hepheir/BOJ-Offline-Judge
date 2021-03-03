import json
import os

__CONFIG_FILE:os.PathLike = os.path.join(*__file__.split(os.sep)[:-2], 'config.json')
__CONFIG:dict = {}


class NotConfigurableError(BaseException):
    pass


def from_json(key):
    if key not in __CONFIG:
        raise NotConfigurableError(f'{__CONFIG_FILE}에 "{key}"가 없습니다.')
    return __CONFIG[key]


###############################################################
# 설정 불러오기
###############################################################


with open(__CONFIG_FILE, 'r') as f:
    __CONFIG = json.loads(f.read())



###############################################################
# 임시 디렉토리 생성
###############################################################

__TEMP_DIR = from_json('tmp.directory')

if os.path.exists(__TEMP_DIR):
    if os.path.isfile(__TEMP_DIR):
        raise FileExistsError('이미 존재하는 파일입니다.')
else:
    os.makedirs(__TEMP_DIR)

