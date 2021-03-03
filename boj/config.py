import json
import os


from boj.util import PACKAGE_ROOT


__CONFIG_FILE = os.path.join(PACKAGE_ROOT, 'config.json')
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

