---
description: 터미널에서 인터넷 속도 확인하기
---

# speedtest-cli (network speed benchmark)

## speedtest-cli란?

speedtest는 웹에서 가까운 speedtest.net 서버에서 파일을 다운로드하여 광대역 연결을 테스트하기 위한 웹서비스입니다. 이 명령어를 사용해서 인터넷 속도를 터미널에서 테스트할 수 있습니다. -->> ??&#x20;

&#x20;

## 명령어 사용법

speedtest -h 또는 speedtest --help를 이용해서 명령어 사용법 확인이 가능합니다.&#x20;

<figure><img src="../../.gitbook/assets/스크린샷, 2022-10-21 16-26-36.png" alt=""><figcaption></figcaption></figure>



주요 명령어를 확인하고 사용하기 쉽게 예시를 -->? 생각해보기.. 포함하여 한국어로 번역했습니다.&#x20;

```
# 도움말 명령어
--help

# 버전 확인
--version

# 다운로드 테스트를 수행하지 않습니다.
-no-downalod

# 업로드 테스트를 수행하지 않습니다.
-no-upload

# 다중 연결 대신 단일 연결만 사용합니다. 
-single

# 비트 대신 바이트로 값 표시 
-bytes 

# 공유 결과 이미지에 대한 url을 생성하고 제공 
--share speedtest.net

# 기본 정보만 표시
-simple

# 기본 정보를 csv 형식으로 표시
--csv

# 
--csv-delimiter 

# csv 헤더 인쇄 
--csv-header

# 기본 정보만 json 형식으로 표시 (속도는 비트/초로 나열)
--json

# 거리별로 정렬된 speedtest.net 서버 목록 표시
--list

# 테스트할 서버 ID 지정
--server SERVER

# EXCLUDE 선택에서 서버 제외
--exclude EXCLUDE

# Speedtest Mini 서버의 URL
--mini MINI

# 바인딩할 소스 IP 주소 
--source SOURCE

# 
--timeout TIMEOUT HTTP

# speedtest.net운영 서버와 통신할 때 HTTP 대신 HTTPS 사용 
--secure

# 업로드 데이터를 미리 할당하지 않습니다. 사전 할당은 기본적으로 활성화되어 있습니다.
--no-pre-allocate

#

```
