# 변경사항

* * *

## 0.0.1

Thu Jul 15 2021

### 모듈 추가·변경사항

-   `BOJProblem` 객체 구현
    -   문제 번호를 이용하여 백준 온라인 저지에서 문제 데이터를 불러옵니다.

### 기타 추가·변경사항

-   `unittest` 모듈을 이용한 유닛테스트 관리
-   Docker를 사용한 개발환경 구축 과정 간소화

* * *

## 0.0.2a

Wed Aug 11 2021

### 모듈 추가·변경사항

-   설치시 오류 수정 [#56](https://github.com/Hepheir/BOJ-Offline-Judge/issues/56)

### 기타 추가·변경사항

-   유닛테스트 관련 변경사항:

    `pyttest` 모듈을 이용한 유닛테스트 관리

    -   `unittest` 모듈에 의존하지 않음
    -   `boj`<sup>(본 프로젝트)</sup> 모듈의 소스코드 사이 `*_test.py` 패턴으로 존재하던 유닛테스트들을 모두 옮겨 "/tests" 디렉토리에서 관리

-   패키지 관리 관련 변경사항:

    `poetry` 모듈을 이용한 패키지 관리

    -   "pyproject.toml"에서 다음 파일들의 내용을 함께 관리:

        -   "requirements.txt": 모듈 의존성 (개발)
        -   "setup.cfg": 패키지 정보
        -   "pyproject.toml": 빌드 및 모듈 의존성

-   버전명에 Alpha Release 임을 명시
    <sup>[\[참고1\]](https://packaging.python.org/guides/distributing-packages-using-setuptools/#choosing-a-versioning-scheme)</sup>
    <sup>[\[참고2\]](https://www.python.org/dev/peps/pep-0440/#public-version-identifiers)</sup>
    <sup>[\[참고3\]](https://doc.sitecore.com/en/SdnArchive/FAQ/Administration/ALPHA%20BETA.html)</sup>
