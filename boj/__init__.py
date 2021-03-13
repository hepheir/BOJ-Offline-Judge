"""BOJ. Offline Judge

백준 온라인 저지의 문제풀이를 보다 알차게 해줄 모듈.

사용법:
    python -m boj judge {src}
        주어진 소스코드를 채점합니다.
        
        채점시 사용되는 데이터는 소스코드와 같은 폴더 내에 있는 모든 .in, .out 파일을 사용합니다.
        같은 폴더 내에 있다는 것은, 그 하위 경로도 포함하기에, 재귀적으로 폴더를 순회하며 데이터 파일을 찾아 사용하게 됩니다.
        
        현재 다음과 같은 채점 결과를 지원합니다.
        -   맞았습니다!!
        -   틀렸습니다
        -   시간 초과
        -   런타임 에러
        -   출력 없음
    
    python -m boj setup
        문제 폴더를 구축합니다.

        실행 시, 문제 번호를 묻는 prompt가 출력되며, 문제 번호를 입력하면
        .boj/config.ini 에 명시된 폴더 명 규칙에 따라, 문제 폴더를 생성하고
        https://acmicpc.net/ 으로 부터 예제 입출력을 내려받아 저장하게 됩니다.
"""

from boj.__version__ import __version__

print('================================================================')
print('                 :: BOJ. Offline Judge ::                       ')
print('                                                                ')
print('            당신의 채점 결과를 예측해 드립니다.                 ')
print(f'                                                      v{__version__}')
print('================================================================')

import boj.util as util
import boj.judge as judge
import boj.config as config
