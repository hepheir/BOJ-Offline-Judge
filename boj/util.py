import os
import sys

PACKAGE_ROOT = os.path.dirname(sys.modules['boj'].__file__)
TMP_DIRECTORY = os.path.join(PACKAGE_ROOT, 'tmp')


class units:
    class ms(int):
        pass

    class KB(int):
        pass


def shorten_path(path:str):
    abspath = os.path.abspath(path)
    common_path = os.path.commonpath([abspath, os.getcwd()])
    return abspath.replace(common_path, "")


###############################################################
# 임시 디렉토리 생성
###############################################################

if os.path.exists(TMP_DIRECTORY):
    if os.path.isfile(TMP_DIRECTORY):
        raise FileExistsError('이미 존재하는 파일입니다.')
else:
    os.makedirs(TMP_DIRECTORY)
