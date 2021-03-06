import time
import typing

from boj.util.units import ms


def now() -> ms:
    return time.time() * 1000


class EmptyStackException(BaseException):
    pass


class TimeRecorder:
    STACK: typing.List[ms] = [now()]

    @classmethod
    def push(cls, time: ms):
        cls.STACK.append(time)

    @classmethod
    def pop(cls) -> ms:
        if len(cls.STACK) == 1:
            raise EmptyStackException
        else:
            return round(cls.STACK.pop() - cls.STACK[-1])

    @classmethod
    def check(cls):
        cls.push(now())
