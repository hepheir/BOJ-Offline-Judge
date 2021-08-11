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

## `BOJProblem`

`boj.BOJProblem()` 객체를 이용하여 문제 데이터에 접근할 수 있습니다.

### 인스턴스 생성

객체의 인스턴스는 다음과 같이 생성합니다.

```python
>>> from boj import BOJProblem
>>> problem = BOJProblem(1000)
```

Args:

-   `number`: (int) 필수; 문제의 번호입니다.

### 프로퍼티

현재 사용할 수 있는 프로퍼티에는 다음의 값들이 있습니다.

-   `problem_id`: (int) 문제의 번호
-   `problem_lang`: (int) 문제의 언어 (0: 한국어, 1: 영어)
-   `title`: (str) 문제의 제목
-   `description`: (str) 문제의 내용 (HTML 문서)
-   `input`: (str) 문제의 입력 설명 (HTML 문서)
-   `output`: (str) 문제의 출력 설명 (HTML 문서)
-   `hint`: (str) 문제의 힌트 (HTML 문서)

### 예시 코드

다음은 `boj` 모듈을 사용하여 1000번 A+B 문제 데이터를 불러오는 예시 코드 입니다.

```python
>>> from boj import BOJProblem

>>> problem = BOJProblem(1000)

>>> print(problem.problem_id)
1000

>>> print(problem.title)
'A+B'

>>> print(problem.data)
[{'problem_id': '1000', 'problem_lang': '0', 'title': 'A+B', 'description': '<p>두 정수 A와 B를 입력받은 다음, ...', ... }, ... ]

>>> print(problem.json)
b'[{"problem_id": "1000", "problem_lang": "0", "title": "A+B", "description": "<p>\\ub450 \\uc815\\uc218 ...'
```
