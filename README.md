<!-- Badges -->

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c0158b110a54cce953d319d5f5b438d)](https://www.codacy.com/gh/Hepheir/BOJ-Offline-Judge/dashboard?utm_source=github.com&utm_medium=referral&utm_content=Hepheir/BOJ-Offline-Judge&utm_campaign=Badge_Grade)
[![Shields Badge - PyPI/version](https://img.shields.io/pypi/v/boj)](https://pypi.org/project/boj/)
[![Shields Badge - PyPI/license](https://img.shields.io/pypi/l/boj)](https://pypi.org/project/boj/)
[![Shields Badge - PyPI/downloads](https://img.shields.io/pypi/dm/boj)](https://pypi.org/project/boj/)
[![Shields Badge - PyPI/status](https://img.shields.io/pypi/status/boj)](https://pypi.org/project/boj/)
[![GitHub/issues](https://img.shields.io/github/issues/Hepheir/BOJ-Offline-Judge.svg)](https://github.com/Hepheir/BOJ-Offline-Judge/issues)

# BOJ Offline Judge

## 개요

BOJ-Offline-Judge는 백준 온라인 저지를 CLI, 혹은 Python 스크립트에서 이용 하기 위한 패키지입니다.

BOJ는 간단한 JSON혹은 Python의 딕셔너리 형태의 문제 데이터를 제공합니다.

## 사용방법

다음은 `boj` 모듈을 사용하여 1000번 A+B 문제 데이터를 불러오는 예시 코드 입니다.

```python
>>> from boj import BOJProblem

>>> problem = BOJProblem(1000)

>>> print(problem.problem_id)
1000

>>> print(problem.title)
'A+B'

>>> print(problem.data)
[{'problem_id': '1000', 'problem_lang': '0', ... }, {...}]
```