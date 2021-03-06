<!-- Badges -->

[![PyPI/version]][pypi/package]
[![PyPI/license]][pypi/package]
[![PyPI/downloads]][pypi/package]
[![PyPI/status]][pypi/package]
[![GitHub/issues]][github/repo]

[pypi/package]: https://pypi.org/project/boj/
[pypi/python]: https://img.shields.io/pypi/pyversions/boj
[pypi/version]: https://img.shields.io/pypi/v/boj
[pypi/downloads]: https://img.shields.io/pypi/dm/boj
[pypi/license]: https://img.shields.io/pypi/l/boj
[pypi/status]: https://img.shields.io/pypi/status/boj
[github/repo]: https://github.com/Hepheir/BOJ-Offline-Judge
[github/stars]: https://img.shields.io/github/stars/Hepheir/BOJ-Offline-Judge.svg
[github/issues]: https://img.shields.io/github/issues/Hepheir/BOJ-Offline-Judge.svg

# BOJ 오프라인 저지

당신의 채점 결과를 예측해드립니다.

## 요구 사항

- **Python 3.7^** (외부 라이브러리는 사용되지 않았음)

- **사용하고자 하는 언어의 컴파일러** (설치된 경로를 `패키지설치경로/config/__init__.py`안에 적절하게 입력해주세요)

## 지원 언어

- Python3
- C++

---

## 사용 방법

### 1. 데이터 셋 준비

작성한 소스코드와 같거나 하위 폴더내에 `.in`, `.out`으로 끝나는 채점 데이터 파일을 준비해주세요.

예시:

```
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
```

### 2. 간채점기 실행

```bash
python -m boj judge "채점 소스코드"
```

---

## 계획

- 더 많은 언어 지원
- 메모리 사용량 측정
- 문제별 시간/메모리 상한선 설정

## 버젼 형식 안내

버젼은 다음 형식에 따라 붙여집니다.

[![](https://digitalcommunications.wp.st-andrews.ac.uk/files/2017/01/semver03.png)](https://digitalcommunications.wp.st-andrews.ac.uk/2017/03/17/what-our-version-numbers-mean/)

---

## 업데이트 로그

### 1.0.0

- 간채점기 배포 시작

### 1.0.1

- **버그 수정**
- **실행 방법 변경** (향후 기능 확장 고려)
  | 변경 후 | `python -m boj judge source_file` |
  | ------- | --------------------------------- |
  | 변경 전 | `python -m boj source_file`       |
