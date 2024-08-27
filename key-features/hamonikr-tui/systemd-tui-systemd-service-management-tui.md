# systemd-tui (systemd service management tui)

`systemd-tui` 는 하모니카 OS 에서 시스템의 서비스를 관리하는 TUI 도구입니다

#### [프로그램 실행 화면](https://github.com/hamonikr/hamonikr-systemd-tui#%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8-%EC%8B%A4%ED%96%89-%ED%99%94%EB%A9%B4) <a href="#user-content" id="user-content"></a>

<figure><img src="../../.gitbook/assets/image (455).png" alt=""><figcaption></figcaption></figure>

#### [Installation](https://github.com/hamonikr/hamonikr-systemd-tui#installation) <a href="#user-content-installation" id="user-content-installation"></a>

```
$ sudo apt-get install -y systemd-tui

만약 종속성 문제로 설치가 실패한경우. 
$ sudo apt-get install -f
```

#### [Usage](https://github.com/hamonikr/hamonikr-systemd-tui#usage) <a href="#user-content-usage" id="user-content-usage"></a>

* systemd-tui 는 아래와 같이 `root 권한으로 실행`되어야 서비스를 관리할 수 있습니다.
* 터미널에서 아래 명령어를 실행하면 프로그램이 구동됩니다.

```
sudo systemd-tui
```

```
프로그램에서 표시되는 서비스 정보는 아래와 같습니다.

[x] - enabled unit.  [ ] - disabled unit
[s] - static unit.   -m- - masked unit

이동 키는 아래와 같습니다. 검색은 / 키를 이용하세요.

Up/k   - move cursor up. Down/j   - move cursor down.
PgUp/b - move page up.   PgDown/f - move page down.
/ - for search.\n\

서비스 관리 키는 아래와 같습니다.

r     - reload/update.   q - exit.\n\
Space - enable/disable.  s - start/stop unit.\n\
```

#### &#x20;<a href="#user-content-dependencies" id="user-content-dependencies"></a>

#### &#x20;<a href="#user-content-changelog" id="user-content-changelog"></a>
