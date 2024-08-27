# asciinema (Record and share terminal sessions)

`asciinema`는 터미널 세션을 녹화하고 공유하는 도구입니다.

터미널 창에 `asciinema --help` 를 입력해 다양한 옵션과 간단한 사용법을 확인할 수 있습니다.

![](<../../.gitbook/assets/image (268).png>)

## asciinema 로 터미널창 녹화하기

asciinema의 사용법은 매우 간단합니다.

터미널창을 녹화하기 위해 `asciinema rec` 명령어를 입력합니다.

![](<../../.gitbook/assets/image (313).png>)

위 이미지와 같이 새로운 세션이 시작되며 녹화가 시각됩니다.

녹화하고자 하는 동작을 수행한 후 `ctrl-d` 키를 눌러 녹화를 종료합니다.

다음으로, 녹화 결과를 로컬에 저장하고자 한다면 `ctrl-c` 키를 누릅니다.

![](<../../.gitbook/assets/image (141).png>)

위 이미지와 같이 파일의 저장 경로가 출력됩니다.

`cat [filename]` 명령어를 통해 녹화된 모든 output을 출력할 수 있습니다.

녹화 결과를 재생하려면 `asciinema play [filename]` 명령어를 입력합니다.

![](<../../.gitbook/assets/image (289).png>)

## 터미널창 녹화 후 공유하기

`asciinema rec` 명령어로 녹화 시작, `ctrl+d` 키로 녹화 종료 후 `enter` 키를 누르면 녹화 결과를 외부에 공유할 수 있습니다.

![](<../../.gitbook/assets/image (127).png>)

위 이미지와 같이 `enter` 키를 누르면 녹화물의 링크가 출력됩니다.

해당 링크에 접속해 녹화영상을 확인할 수 있습니다.

![](<../../.gitbook/assets/image (426).png>)

asciinema.org에 가입, 로그인 하지 않았을 경우 해당 영상은 7일간 보관됩니다.

영상을 영구적으로 보관하고자 한다면 asciinema.org에 가입해야 합니다.

asciinema의 안내에 따라 아래 링크에 접속합니다.

![](<../../.gitbook/assets/image (223).png>)

이메일 입력, 이메일로 가입 인증 후 터미널 창에 `asciinema auth`를 입력하면 아래와 같이 링크가 출력됩니다.

![](<../../.gitbook/assets/image (355).png>)

해당 링크에 접속하면 아래 이미지와 같이 계정이 생성되고 업로드한 영상이 보관되는 것을 확인할 수 있습니다.

![](<../../.gitbook/assets/image (181).png>)
