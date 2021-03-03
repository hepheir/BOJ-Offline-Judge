# 짭준 오프라인 저지

당신의 채점 결과를 예측해드립니다.

## 실행

```shell
python -m python.index <source_file>
```

## 요구 사항

* **Python 3.9** (외부 라이브러리는 사용되지 않았음)

* **사용하고자 하는 언어의 컴파일러** (설치된 경로를 `config.json`안에 적절하게 입력해주세요)

## Git 레포지토리에 설치

```bash
git submodule add https://github.com/Hepheir/BOJ-Offline-Judge
```

## Visual Studio Code 편의성

`.vscode/tasks.json`에 다음 항목을 추가하여 더욱 편리하게 사용할 수 있습니다.

```json
        {
            "type": "shell",
            "label": "[BOJ-Offline-Judge] 짭준 오프라인 저지 :: 현재 소스코드 간채점",
            "options": {
                "cwd": "${workspaceFolder}/BOJ-Offline-Judge"
            },
            "command": "python",
            "windows": {
                "command": "C:\\Program Files\\Python\\Python39\\python.exe",
            },
            "args": [
                "-m",
                "python.index",
                "${file}"
            ],
            "group": {
                "kind": "test",
                "isDefault": true
            }
        }
```

채점할 소스코드를 열고 VS Code 내장 기능인 `run task`로 짭준을 호출합니다.
