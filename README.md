<!-- Badges -->

[![PyPI/version]][pypi/package]
[![PyPI/license]][pypi/package]
[![PyPI/downloads]][pypi/package]
[![PyPI/status]][pypi/package]
[![GitHub/issues]][github/repo]

# BOJ 오프라인 저지

당신의 채점 결과를 예측해드립니다.

## 요구 사항

-   **Python 3.7^** (외부 라이브러리는 사용되지 않았음)

-   **사용하고자 하는 언어의 컴파일러** (설치된 경로를 `.boj/config.ini`안에 적절하게 입력해주세요)

## 지원 언어

-   Python3

-   C++

* * *

## 사용 방법

### 1. 데이터 셋 준비

작성한 소스코드와 같은 디렉토리 내에 `data` 폴더를 생성하고, `~~.in`, `~~.out`으로 끝나는 채점 데이터 파일을 준비해주세요.

**예시:**

    problem # 문제 별 폴더
    ├── data
    │ ├── boj
    │ │ ├── sample
    │ │ │ ├── 1.in  # 데이터 셋 1
    │ │ │ └── 1.out # 데이터 셋 1
    │ │ │
    │ │ └── hepheir
    │ │   ├── 1.in  # 데이터 셋 2
    │ │   └── 1.out # 데이터 셋 2
    │ │
    │ ├── a.in  # 데이터 셋 3
    │ └── a.out # 데이터 셋 3
    │
    └── source.py # 채점할 소스

### 2. 가채점기 실행

```bash
python -m boj.judge "채점 소스코드"
```

-   만약 잘 실행이 되지 않는다면, 파이썬 혹은 컴파일러 경로가 올바르지 않아서 오류가 발생하는 것일 가능성이 높습니다. `.boj/config.ini` 에서 잘못된 정보가 있는지 확인해주세요.

### 3. Visual Studio Code

<kbd>Ctrl</kbd>+<kbd>P</kbd>를 누른 뒤, `> Tasks: Configure Tasks`, `Others` 를 선택하면 나오는 `.vscode/tasks.json` 파일에서 다음과 같은 작업을 등록하여 가채점 과정을 더욱 편리하게 할 수 있습니다.

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "[BOJ Offline Judge] 현재 열린 파일 가채점",
      "type": "shell",
      "command": "python",
      "args": ["-m", "boj.judge", "${file}"],
      "group": "build"
    }
  ]
}
```

등록된 작업은 [ <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>B</kbd> ] 에서 빠르게 호출 할 수 있습니다.

## 업데이트 로그

-   [별도 문서](https://github.com/Hepheir/BOJ-Offline-Judge/Update.md)로 분리

<!-- References -->

[pypi/package]: https://pypi.org/project/boj/

[pypi/python]: https://img.shields.io/pypi/pyversions/boj

[pypi/version]: https://img.shields.io/pypi/v/boj

[pypi/downloads]: https://img.shields.io/pypi/dm/boj

[pypi/license]: https://img.shields.io/pypi/l/boj

[pypi/status]: https://img.shields.io/pypi/status/boj

[github/repo]: https://github.com/Hepheir/BOJ-Offline-Judge

[github/stars]: https://img.shields.io/github/stars/Hepheir/BOJ-Offline-Judge.svg

[github/issues]: https://img.shields.io/github/issues/Hepheir/BOJ-Offline-Judge.svg
