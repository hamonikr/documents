# 쓰기 가능한 부팅 USB 제작 Live USB Creator

## Live USB Creator 설치하기

Live USB Creator는 ISO 이미지로 쓰기 가능한 라이브 USB를 제작하는 프로그램입니다.

[Github 레포지토리](https://github.com/hamonikr/live-usb-creator)에서 더 자세한 내용을 확인할 수 있습니다.

하모니카 OS 사용자의 경우 아래와 같은 방법으로 설치할 수 있습니다.

```
# Add APT
$ curl -sL https://pkg.hamonikr.org/add-hamonikr.apt | sudo -E bash-
$ sudo apt update
$ sudo apt install live-usb-creator
```

{% hint style="info" %}
&#x20; **우분투 18.04 이상, 하모니카 3.0 이상** 외의 OS 사용자는 [Github 레포지토리](https://github.com/hamonikr/live-usb-creator)에서 설치 방법을 확인하실 수 있습니다.
{% endhint %}

프로그램 설치가 완료되면, 시작메뉴에 `라이브 USB 제작` 이 추가된 것을 확인할 수 있습니다.

![](<../../.gitbook/assets/image (404).png>)

`라이브 USB 제작` 을 클릭하면 아래와 같이 Live USB Creator 프로그램이 실행됩니다.

![](<../../.gitbook/assets/image (427).png>)



## ISO 이미지로 쓰기 가능한 부팅 USB 제작하기

Live USB Creator를 통해 쓰기 가능한 부팅 USB를 제작할 수 있습니다.

우선, 아래 이미지와 같이 제작할 USB와 ISO 파일을 선택합니다.

`쓰기 가능한 Live USB 방식`을 선택하고, USB 장치에 사용할 크기를 설정하고, `다음으로`를 클릭하면 USB 제작이 진행됩니다.

`USB 장치에 사용할 크기 설정`에 설정한 나머지 부분은 아래 라이브 USB 부팅 후 데이터 저장 기능에서 사용됩니다.

![](<../../.gitbook/assets/image (265).png>)

![](<../../.gitbook/assets/image (356).png>)

제작된 USB 내부의 writable 디렉토리를 사용하여 데이터를 읽고 쓸 수 있습니다.

![](<../../.gitbook/assets/image (145).png>)

## 라이브 USB 부팅 후 데이터 저장

GParted와 같은 툴을 사용하여 제작한 USB의 파티션 구성을 확인하면 아래와 같이 나머지 부분이 `할당하지 않음`으로 표시되는 것을 확인할 수 있습니다.

![](<../../.gitbook/assets/image (379).png>)

해당 부분을 사용하기 위해 파티션을 할당해 줍니다. 아래는 fat32 형식으로 파티션을 할당한 이미지입니다.

![](<../../.gitbook/assets/image (413).png>)

해당 USB로 라이브 부팅을 하고, 아래 명령어로 생성한 mydata 폴더에 데이터를 저장합니다.

```
# 하모니카 라이브 USB로 부팅 후 터미널을 열고(Ctrl+Alt+T) 다음과 같이 실행
sudo mkdir /var/log/mydata
sudo chmod 777 /var/log/mydata
nemo /var/log/mydata
```

![](<../../.gitbook/assets/image (173).png>)

이후, 해당 USB로 다시 라이브 부팅을 진행해도 아래와 같이 데이터가 남아있는 것을 확인할 수 있습니다.

![](<../../.gitbook/assets/image (224).png>)

