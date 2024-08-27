# ttyd (Share terminal over the web)

`ttyd`는 터미널에서 명령어를 입력한 결과를 웹으로 공유하는 도구입니다.

터미널 창에 `ttyd --help` 를 입력해 간단한 사용법과 다양한 옵션을 확인할 수 있습니다.

![](<../../.gitbook/assets/image (125).png>)

## 로컬의 파일 내용 공유하기

파일 내용을 터미널창에 출력하는 명령어로 `cat` 이 있습니다.

ttyd를 통해 해당 내용을 다른 사람들과 웹으로 공유할 수 있습니다.

터미널 창에 `ttyd cat [공요하고자 하는 파일명]` 을 입력하면 아래와 같이 ttyd가 실행되고 연결된 포트를 출력합니다.

![](<../../.gitbook/assets/image (247).png>)

[http://localhost:7681/](http://localhost:7681/) 에 접속하면 다음과 같이 해당 명령어의 결과인 파일 내용 출력이 보여집니다.

![](<../../.gitbook/assets/image (240).png>)

## Docker 모니터링 화면 공유하기

docker 모니터링 도구인 `lazydocker`의 실행창을 공유하고자 한다면 `ttyd lazydocker`를 입력합니다.

![](<../../.gitbook/assets/image (258).png>)

[http://localhost:7681/](http://localhost:7681/) 에서 `lazydocker` 화면이 공유되는 것을 확인할 수 있습니다.

![](<../../.gitbook/assets/image (142).png>)

## 여러개 창 동시에 띄우기

ttyd의 기본 포트인 7681과 다른 포트를 지정해 동시에 여러개의 ttyd 창을 공유할 수 있습니다.

위에서 실행한 `lazydocker` 창이 7681 포트에서 실행 중인 상태에서 `htop` 명령어의 결과창을 7682 포트로 공유합니다.

![](<../../.gitbook/assets/image (177).png>)

다음과 같이 [http://localhost:7682/](http://localhost:7682/) 에서 `htop` 창을 확인할 수 있습니다.

![](<../../.gitbook/assets/image (431).png>)

