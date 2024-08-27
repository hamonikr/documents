---
description: 디스크 사용량 분석기 및 추적기
---

# ncdu (disk usage analysis)

## ncdu란?

nudu는 du(disk usage- 파일, 디렉토리 용량을 확인할 때 사용하는 명령) 명령의 명령줄 버전입니다. &#x20;

ncurses를 기반으로 하며 디스크 공간을 사용하는 파일과 디렉토리를 가장 빠르게 분석하고 추적 할 수 있는 방법을 제공하는 명령어 입니다.&#x20;



### ncdu 설치

`sudo apt-get install ncdu`



## ncdu  기본 사용법&#x20;

터미널에 `ncdu`를 입력하면 파일 및 디렉토리 수와 현재 작업 디렉토리의 디스크 사용량 스캔이 실행됩니다.

스캔이 완료되면 그래픽 막대 표시와 함께 디스크 사용량과 함께 파일 및 폴더의 트리 구조가 표시됩니다.&#x20;

<figure><img src="../../.gitbook/assets/스크린샷, 2022-10-06 15-48-45.png" alt=""><figcaption></figcaption></figure>

더 자세히 보고싶은 디렉토리를 선택해서 i 를 누르면 상세 정보 화면이 보여집니다.&#x20;

i를 한번 더 눌러 상세 정보 화면을 숨길 수 있습니다.&#x20;

<figure><img src="../../.gitbook/assets/스크린샷, 2022-10-06 15-53-20.png" alt=""><figcaption></figcaption></figure>

선택한 파일 또는 디렉토리를 삭제하기 위해 d를 누르면 확인 메세지가 보여집니다.

yes 를 선택하면 삭제가 진행됩니다.&#x20;

<figure><img src="../../.gitbook/assets/스크린샷, 2022-10-06 16-19-02.png" alt=""><figcaption></figcaption></figure>

shift + ? 를 누르면 ncdu가 진행되는 동안 사용 가능한 옵션 목록 확인이 가능합니다.

키보드 방향키를 이용해 더 많은 옵션 목록을 확인할 수 있습니다.&#x20;

옵션 목록을 종료하고 싶으면 q를 눌러줍니다.&#x20;

<figure><img src="../../.gitbook/assets/스크린샷, 2022-10-06 16-25-05.png" alt=""><figcaption></figcaption></figure>

