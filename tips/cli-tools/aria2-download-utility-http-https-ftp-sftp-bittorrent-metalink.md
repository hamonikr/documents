# aria2 (download utility - HTTP/HTTPS, FTP, SFTP, BitTorrent, Metalink)

`aria2`는 다양한 프로토콜과 병렬 수행을 지원하는 다운로드 유틸리티입니다.

터미널 창에 `aria2c --help` 또는 `tldr aria2c`를 입력해 다양한 옵션과 간단한 사용법을 확인할 수 있습니다.

![](<../../.gitbook/assets/image (295).png>)

위 이미지의 설명과 같이 `aria2`는 HTTP(S), FTP, SFTP, BitTorrent, 그리고 Metalink 프로토콜을 지원하고, 여러개 파일을 병렬로 다운로드 받을 수 있으며, 다운로드 속도 등을 조절해 사용할 수 있습니다.

## aria2 로 파일 다운로드 받기

aria2 와 https 링크를 통해 영상을 다운로드 받기 위해 아래 명령어를 입력합니다.

`aria2c [file url]`

![](<../../.gitbook/assets/image (174).png>)

위 이미지와 같이 `aria2`가 다운로드 상태와 결과를 출력합니다.

다운로드 받을 파일의 이름을 지정하고자 한다면 아래 명령어를 입력합니다.

`aria2c --out=[filename] [file url]`

![](<../../.gitbook/assets/image (359).png>)

`aria2` 를 통해 여러개 파일을 병렬 다운로드 하는 방법은 아래와 같습니다.

`aria2c [file url] [file url]`

![](<../../.gitbook/assets/image (154).png>)

아래와 같이 -x 옵션을 통해 여러개 커넥션으로 하나의 파일을 다운로드 받을 수도 있습니다.

`aria2c -x2 [file url]`

![](<../../.gitbook/assets/image (335).png>)

BitTorrent 파일 또한 같은 방법으로 다운로드 받을 수 있습니다.

![](<../../.gitbook/assets/image (119).png>)

