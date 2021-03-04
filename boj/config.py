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


if not os.path.exists(__CONFIG_FILE):
    # DEFAULT CONFIGURATION
    __CONFIG = {
        "data.in.path.pattern": "{srcDirname}\\data\\**\\*.in",
        "data.out.path.pattern": "{srcDirname}\\data\\**\\*.out",

        "timelimit.ms": 10000,

        "result.include.time": True,
        "result.include.datapath": True,

        "cpp.compiler.path": "c:\\MinGW\\bin\\g++.exe",
        "c.compiler.path": "c:\\MinGW\\bin\\gcc.exe"
    }
    with open(__CONFIG_FILE, 'w') as f:
        f.write(json.dumps(__CONFIG))
else:
    with open(__CONFIG_FILE, 'r') as f:
        __CONFIG = json.loads(f.read())

