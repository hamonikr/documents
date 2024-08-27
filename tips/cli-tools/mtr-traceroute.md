---
description: 네트워크 진단 도구
---

# mtr (traceroute)

## mtr이란?

mtr은 traceroute와 ping의 기능을 하나의 프로그램으로 결합한 네트워크 진단 도구입니다.

mtr을 이용해 트워크 응답 및 연결을 실시간으로 확인할 수 있습니다.&#x20;



### mtr 설치하기&#x20;

`sudo apt install mtr`&#x20;



## mtr 실행하기

### 네트워크 경로 확인

네트워크 경로 확인을 위해 원격시스템의 도메인 이름이나 IP 주소를 넣어서 명령어를 입력해줍니다.&#x20;

<figure><img src="../../.gitbook/assets/스크린샷, 2022-10-06 13-28-46.png" alt=""><figcaption></figcaption></figure>

명령어를 입력하면 네트워크 경로의 실시간 업데이트 확인이 가능하고, q 또는 ctrl + c를 입력해서 프로그램 종료가 가능합니다. &#x20;

<figure><img src="../../.gitbook/assets/스크린샷, 2022-10-06 13-29-57.png" alt=""><figcaption></figcaption></figure>



### 명령

`mtr --help` 명령어를 통하여 사용 방법을 확인할 수 있습니다.&#x20;

<figure><img src="../../.gitbook/assets/스크린샷, 2022-10-06 13-48-10.png" alt=""><figcaption></figcaption></figure>

주요 명령어를 확인하고 사용하기 쉽게 예시를 포함하여 한국어로 번역했습니다.

<pre><code># 도움말 명령어
--help

# 버전 확인
--version

# 파일에서 호스트 이름을 읽습니다.
--file FILE

# IPv4/ IPv6만 사용합니다.
-4 / -6

# ICMP 에코 대신 UDP / TCP를 사용합니다.
--udp / --tcp

# 명명된 네트워크 인터페이스를 사용합니다.
--interface NAME

# 나가는 소켓을 ADDRESS에 바인딩합니다.
--address ADDRESS

# 시작할 TTL을 설정합니다.
--first-ttl NUMBER

# 최대 hops?? 
--max-ttl NUMBER

# 알 수 없는 최대 호스트
--max-unknown NUMBER

# TCP, SCTP 또는 UDP에 대한 대상 포트 번호
-P, --port PORT

# UDP의 소스 포트 번호
 -L, --localport LOCALPORT
 
# 프로빙에 사용되는 패킷 크기 설정
 -s, --psize PACKETSIZE 
 
# 페이로드에 사용할 비트 패턴 설정
-B, --bitpattern NUMBER   

# ICMP 에코 요청 간격
-i, --interval SECONDS 
 
# 응답을 기다리는 시간(초)
-G, --gracetime SECONDS 

# IP 헤더의 서비스 필드 유형
-Q, --tos NUMBER   

# ICMP 확장의 정보 표시
-e, --mpls        

# 프로브 소켓을 열린 상태로 유지하기 위한 시간(초)
-Z, --timeout SECONDS

# 각 보낸 패킷을 표시
-M, --mark MARK        

# 보고서 모드를 사용하여 출력
-r, --report       

<strong># 출력 와이드 보고서
</strong>-w, --report-wide 

# 전송된 ping수 설정
-c, --report-cycles COUNT  

# 출력 json 
-j, --json

# 출력 XML
-x, --xml

# 쉼표로 구분된 값 출
-C, --csv
 
# 출력 원시 형식
-l, --raw
 
# 분할 출력
-p, --split

# curses 터미널 인터페이스 사용
-t, --curses  
<strong>
</strong><strong># 초기 디스플레이 모드 선택
</strong>--displaymode MODE

# 호스트 이름을 확인하지 마십시오
-n, --no-dns

# IP 번호 및 호스트 이름 표시 
-b, --show-ips

# 출력 필드 선택 
-o, --order FIELDS

# 출력에서 IP 정보 선택 
-y, --ipinfo NUMBER
 
# AS 번호 표시
-z, --aslookup 



</code></pre>
