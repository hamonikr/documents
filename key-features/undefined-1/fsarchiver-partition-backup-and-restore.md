# fsarchiver (터미널 사용법) - 메뉴얼 제작성

`fsarchiver`는 파일시스템을 압축파일로 만들어 저장할 수 있도록 하는 파티션 백업/복구 툴입니다.

`partimage` 와 같은 기존의 오픈소스 파일시스템 백업 툴들은 파일시스템 블록 레벨에서 작동하기 때문에 생성한 백업을 보다 작은 파티션에 복구할 수 없고, 보다 큰 파티션에 복구하기 위해서는 파일시스템의 사이즈를 직접 조정해야 합니다.&#x20;

반면, `fsarchiver`는 데이터 공간만 충분하다면 생성한 백업 압축본을 보다 작은 파티션에 복구할 수 있고, 파일시스템 종류 (ReiserFS, ext3 등) 또한 지정할 수 있습니다.

터미널 창에 `fsarchiver --help` 를 입력해 간단한 사용법과 프로그램 옵션을 확인할 수 있습니다.

![](<../../.gitbook/assets/image (231).png>)

`commands` 항목을 보면 `fsarchiver`의 기능에는 크게 4가지가 있는 것을 알 수 있습니다.

`디스크의 파일시스템 정보 확인`, `파일시스템 백업과 복구`, `디렉토리 백업과 복구`, 그리고 `압축파일 정보 확인`입니다.

다음 목차에서 각 기능들의 사용법을 확인하세요.

## 파일시스템 정보 확인하기 <a href="#undefined-3" id="undefined-3"></a>

파일시스템 백업, 복구 작업을 진행하기에 앞서, 디스크의 파일시스템 정보를 확인해야 합니다.

`fsarchiver`의 다음 두 명령어를 통해 해당 정보를 확인할 수 있습니다.

`fsarchiver probe‌` - 디스크의 파일시스템 형식, 사이즈 등 확인

`fsarchiver probe detailed` - 각 파티션의 UUID 정보와 함께 확인

![](https://gblobscdn.gitbook.com/assets%2F-MOdedbke\_kpJqE1CY2X%2F-Me7olmWHvosfSCbUk1B%2F-Me8-JQwggc-N5PvA-93%2Fimage.png?alt=media\&token=416c96bf-b3b7-4d86-bd96-abe74c497d78)

## 파일시스템 백업, 복구하기

### 파일시스템 압축하기

`fsarchiver`는 `fsarchiver savefs` 명령어를 통해 파일시스템 전체를 하나의 파일로 압축해 백업할 수 있도록 합니다.

`fsarchiver`의 `help` 페이지 하단에서 제공하는 사용 예제는 아래와 같습니다.

![](<../../.gitbook/assets/image (305).png>)

위 예시와 같이 sdb2 파티션의 백업을 시도하면 아래와 같은 메시지가 출력됩니다.

![](<../../.gitbook/assets/image (424).png>)

백업하고자 하는 파티션이 `read/write` 에 마운트 된 상태라면 `-A` 옵션을 통해 라이브 백업을 생성하거나, `mount -o remount,ro /dev/sda1` 와 같은 명령을 통해 해당 파티션을 `read-only`에 마운트 한 후 백업을 진행해야 함을 의미합니다.

`read/write` 상태인 `sdb2`를 `read-only` 에 리마운트 한 후, 파일시스템 압축을 진행한 모습입니다.

![sudo mount - remount, ro /dev/sdb2](<../../.gitbook/assets/image (321).png>)

![sudo fsarchiver savefs -v -v -v /home/yeji/backup/myarchive2.fsa /dev/sdb2](<../../.gitbook/assets/image (169).png>)

#### 라이브 백업 생성하기

read/write 에 마운트 된 상태인 sda2 파티션의 라이브백업을 생성하기 위해 `-A` 옵션을 사용하고, 진행상태를 출력하기 위해 `-v` 옵션과 함께 수행한 모습입니다.

![sudo fsarchiver savefs -A -v -v -v /home/yeji/backup/livearchive1.fsa /dev/sdb2 ](<../../.gitbook/assets/image (302).png>)

### 파일시스템 압축 풀기

위에서 생성한 파일시스템 백업을 `fsarchiver restfs` 명령어로 복구합니다.

## 디렉토리 백업, 복구하기

`fsarchiver`는 `fsarchiver savedir` 명령어를 통해 디렉토리를 하나의 파일로 압축할 수 있도록 합니다.

아래 이미지는 git 폴더를 zstd 형식으로 압축한 모습입니다.

![sudo fsarchiver savedir ./git.zstd git](<../../.gitbook/assets/image (287).png>)

다음과 같이 현재 위치에 해당 압축 파일이 생성된 것을 확인할 수 있습니다.

![](<../../.gitbook/assets/image (207).png>)

`fsarchiver restdir` 명령어를 통해 위에서 생성한 압축 파일을 다른 위치에 푼 모습입니다.

![sudo fsarchiver restdir ./git.zstd.fsa /home/yeji/backup/ ](<../../.gitbook/assets/image (380).png>)

다음과 같이 해당 위치에 압축이 풀린 디렉토리가 생성된 것을 확인할 수 있습니다.

![](<../../.gitbook/assets/image (388).png>)

## 압축파일 정보 확인하기

`fsarchiver archinfo` 명령어를 통해 **fsarchiver**로 생성한 압축파일의 파일시스템 정보를 확인할 수 있습니다.

![sudo fsarchiver archinfo /home/yeji/backup/livearchive1.fsa](<../../.gitbook/assets/image (260).png>)
