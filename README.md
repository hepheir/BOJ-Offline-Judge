# BOJ 오프라인 저지

당신의 채점 결과를 예측해드립니다.


## 요구 사항

* **Python 3.7^** (외부 라이브러리는 사용되지 않았음)

* **사용하고자 하는 언어의 컴파일러** (설치된 경로를 `config.json`안에 적절하게 입력해주세요)

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
python -m boj "채점 소스코드"
```


## 버젼 형식 안내

버젼은 다음 형식에 따라 붙여집니다.

[![](https://digitalcommunications.wp.st-andrews.ac.uk/files/2017/01/semver03.png)](https://digitalcommunications.wp.st-andrews.ac.uk/2017/03/17/what-our-version-numbers-mean/)
