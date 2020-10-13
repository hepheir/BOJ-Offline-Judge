import io
import os
import shutil
import subprocess
import resource

from .Unit import Unit
from ..lang import Language

STDIN = io.TextIOWrapper(io.BytesIO())
STDOUT = io.TextIOWrapper(io.BytesIO())
STDERR = io.TextIOWrapper(io.BytesIO())

def task_generator(code_file:os.PathLike, language:Language, allow_handicap:bool=True):
    shutil.copyfile(code_file, language.CODE)
    print('[INFO] Start Compile')
    subprocess.run(language.COMPILE,
                   shell=True,
                   check=True)
    def task_wrappper(stdin_data:str, stdout_data:str, timelimit:Unit.Seconds, memlimit:Unit.Bytes):
        return __task(language, stdin_data, stdout_data, timelimit, memlimit, allow_handicap)
    return task_wrappper

def __task(language:Language, stdin_data:str, stdout_data:str, timelimit:Unit.Seconds, memlimit:Unit.Bytes, allow_handicap:bool=True):
    # 입출력 준비
    STDIN.seek(0)
    STDIN.write(stdin_data)
    for stream in [STDIN, STDOUT, STDERR]:
        stream.seek(0)
    # 핸디캡 적용
    timelimit = language.timelimit(timelimit) if allow_handicap else timelimit
    memlimit = language.memlimit(memlimit) if allow_handicap else memlimit
    # 메모리 제한
    softlimit = memlimit
    hardlimit = resource.RLIM_INFINITY
    preexec = lambda: resource.setrlimit(resource.RLIMIT_AS, (softlimit, hardlimit))
    # 프로세스 열기
    proc = subprocess.Popen(language.COMPILE,
                            shell=True,
                            stdin=STDIN,
                            stdout=STDOUT,
                            stderr=STDERR,
                            preexec_fn=preexec)
    # 시간 초과 감지
    try:
        proc.communicate(timeout=timelimit)
    except subprocess.TimeoutExpired:
        proc.kill()
        raise TimeoutError()
    finally:
        proc.kill()
    # 런타임 에러 감지
    if STDERR.tell() > 0:
        raise RuntimeError()
    # 정답 여부 판별
    STDOUT.seek(0)
    outs = STDOUT.read()
    if stdout_data.rstrip() != outs.rstrip():
        raise ValueError()
    # 맞았습니다!!
    return True