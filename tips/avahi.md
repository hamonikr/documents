# 로컬 네트워크 서비스 탐색 도구 avahi

## hamonikr-avahi-service 설치하기 <a href="#activitywatch" id="activitywatch"></a>

`avahi`는 로컬 네트워크에서 클라이언트가 IP를 모르는 경우에도 [Zero-configuration networking](https://en.wikipedia.org/wiki/Zero-configuration\_networking) 을 이용해서 로컬 네트워크의 다른 시스템이 ssh, aft, nfs, http, vnc 등의 서비스를 탐색할 수 있도록 지원하는 프로그램입니다.

`hamonikr-avahi-service`를 통해 서버의 IP주소를 몰라도 호스트명으로 서비스에 접속할 수 있습니다.

**HamoniKR(>=3.0)** 사용자는 아래 명령어로 프로그램을 설치할 수 있습니다.

```
$ sudo apt update
$ sudo apt install hamonikr-avahi-service
```

다른 우분투 배포판 사용자는 아래 명령어로 프로그램을 설치할 수 있습니다.

```
$ wget -qO- https://pkg.hamonikr.org/add-hamonikr.apt | sudo -E bash -
$ sudo apt install hamonikr-avahi-service
```

기본 제공되는 `ssh`와 `aft (Apple File Transfer)` 서비스 외에 다른 서비스를 추가하는 방법은

[Github 레포지토리](https://github.com/hamonikr/hamonikr-avahi-service)에서 확인하실 수 있습니다.‌

프로그램을 설치를 완료하면 아래 이미지와 같이 `시작 프로그램` 에&#x20;

`Avahi SSH Server Browser,` `Avahi VNC Server Browser`, `Avahi Zeroconf Browser`가 추가된 것을 확인할 수 있습니다.

![](<../.gitbook/assets/image (159).png>)



## 로컬 네트워크 서비스 탐색하기

`Avahi Zeroconf Browser`를 실행하면 아래 이미지와 같이

로컬 네트워크에서 서비스를 공급하고 있는 시스템을 확인할 수 있습니다.

![](<../.gitbook/assets/image (205).png>)

### 로컬 네트워크 시스템을 찾지 못한다면?

탐색하고자 하는 시스템의 방화벽이 `5353` 포트를 허용하지 않고 있다면 해당 시스템을 탐색하지 못합니다.

아래 명령어를 통해 방화벽에서 UDP `5353` 포트를 허용해주세요.

```
$ sudo ufw allow 5353/udp
```

## 시스템 이름으로 SSH 접속하기

`Avahi SSH Server Browser`를 실행하면 아래 이미지와 같이

로컬 네트워크에서 SSH 서비스를 공급하고 있는 시스템을 확인할 수 있습니다.

![](<../.gitbook/assets/image (399).png>)

접속하고자 하는 서비스를 선택한 후 `접속`을 클릭하면 아래와 같이 터미널 창이 열리며 해당 서버로의 SSH 접속이 수행됩니다.

![](<../.gitbook/assets/image (279).png>)

## SSH 접속이 수행되지 않는다면?

### DNS 서버 변경

로컬 네트워크의 시스템 접속 시도시 avahi는 `[호스트명].local` 로 해당 시스템의 IP주소를 찾습니다.

하지만 일부 DNS 서버에서는 이러한 검색에 정상적인 IP를 리턴하지 않습니다.

터미널 창에 `ping [호스트명].local` 을 입력했을 때 다른 IP를 리턴한다면, 아래와 같이 DNS 서버 정보를 변경하세요.

패널 우측의 `<->` 아이콘 클릭 > `네트워크 설정`클릭

![](<../.gitbook/assets/image (272).png>)

또는 `시작 프로그램` > `네트워크` 를 클릭해 네트워크 매니저를 실행합니다.

![](<../.gitbook/assets/image (428).png>)

우측 하단의 설정 버튼을 클릭합니다.

![](<../.gitbook/assets/스크린샷, 2021-06-08 18-54-44.png>)

아래 이미지와 같이 DNS 서버를 구글 퍼블릭 DNS로 설정합니다.

`IP4` 클릭 > `DNS` 항목의 자동설정을 비활성화 > `Server`에 `8.8.8.8` 입력

![](<../.gitbook/assets/image (193).png>)

### SSH  서비스 추가

접속하고자 하는 서버에 SSH 서비스가 구동 중이지 않으면 SSH 서비스를 구동시켜야 합니다.

`openssh-server`가 설치되어 있지 않다면 아래 명령어를 통해 설치하세요.

```
$ sudo apt install openssh-server
```

`openssh-server`가 설치되어 있지만 서비스가 비활성화 상태라면 아래 명령어를 통해 서비스를 활성화 하세요.

```
$ service sshd restart
```

## 주의사항

SSH 접속과 같은 서비스는 집이나 개발용 환경에서는 쉬운 서비스 공급을 위해서 사용될 수 있지만, 실제 운영환경에서는 보안상 취약점이 될 수 있으므로 사용을 권장하지 않습니다.
