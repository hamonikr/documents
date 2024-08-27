# lazydocker (TUI for both docker and docker-compose)

`lazydocker`는 docker와 docker-compose의 터미널 UI 를 제공하는 도구입니다.

터미널 창에 `lazydocker --help` 를 입력해 간단한 옵션을 확인할 수 있습니다.

![](<../../.gitbook/assets/image (215).png>)

## 실행중인 컨테이너 모니터링하기

터미널창에 `lazydocker` 를 입력하면 lazydocker가 실행됩니다.

아래 이미지와 같이 좌측에 컨테이너와 이미지, 볼륨 리스트를 보여줍니다.

우측에는 현재 실행중인 컨테이너의 로그가 출력됩니다.

![](<../../.gitbook/assets/image (393).png>)

우측 상단의 `Stats` 를 클릭하면 해당 컨테이너의 상태를 모니터링 할 수 있는 화면이 보여집니다.

CPU와 메모리 실시간 사용량, 트래픽 등의 정보를 제공합니다.

![](<../../.gitbook/assets/image (160).png>)

우측 상단의 `Config`를 클릭하면 해당 컨테이너의 설정 정보를 보여줍니다.

컨테이너의 ID, 이름 이름 등 기본 설정 뿐만 아니라 네트워크 설정, 마운트 설정 등 모든 설정 정보를 확인할 수 있습니다.

![](<../../.gitbook/assets/image (147).png>)

마지막으로 우측 상단의 `Top`을 클릭하면 도커 내에서 동작하는 프로세스를 확인할 수 있습니다.

![](<../../.gitbook/assets/image (418).png>)

## 이미지 설정 정보 확인하기

좌측 이미지 항목 내의 이미지를 클릭하면 해당 이미지의 설정 정보를 확인할 수 있습니다.

이미지의 이름, id, 태그, 사이즈, 레이어 등을 확인할 수 있습니다.

![](<../../.gitbook/assets/image (241).png>)

## docker 명령어 사용하기

docker 명령을 실행하고자 하는 컨테이너를 클릭한 상태에서 키보드에서 `b`를 누르면 Bulk Command 창이 보여집니다.

해당 창을 통해 컨테이너 일괄 정지, 삭제, prune 등 명령어를 쉽게 사용할 수 있습니다.

![](<../../.gitbook/assets/image (429).png>)

접속하고자 하는 컨테이너를 선택한 후, 키보드에서 `c`를 누르면 Custom Command 창이 보여집니다.

해당 창을 통해 컨테이너 접속 명령을 쉽게 사용할 수 있습니다.

![](<../../.gitbook/assets/image (308).png>)

## docker-compose 명령어 사용하기

docker-compose로 실행되는 컨테이너들은 좌측의 `Services` 항목에 출력됩니다.&#x20;

docker-compose 관련 명령을 실행하고자 하는 컨테이너를 클릭한 상태에서 키보드에서 b를 누르면 Bulk Command 창이 보여집니다.

![](<../../.gitbook/assets/image (392).png>)

해당 창을 통해 docker-compose up, stop, pull build 등 명령어를 쉽게 사용할 수 있습니다.

![](<../../.gitbook/assets/image (328).png>)
