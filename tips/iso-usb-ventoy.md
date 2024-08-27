# 여러개 ISO 파일을 담는 부팅 USB 제작 프로그램 Ventoy

## Ventoy 설치하기

Ventoy는 윈도우, 리눅스 등 다양한 운영체제를 한 개의 USB에 넣어서 필요할때 부팅에 사용할 수 있는 기능을 제공하는 프로그램입니다.

HamoniKR 사용자는 아래 명령어로 Ventoy를 설치할 수 있습니다.

```
 $ sudo apt update
$ sudo apt install ventoy
```

HamoniKR 외의 사용자는 아래 명령어로 설치하실 수 있습니다.

```
$ curl -sL https://pkg.hamonikr.org/add-hamonikr.apt | sudo -E bash -
$ sudo apt install -y hamonikr-conky
```

{% hint style="info" %}
&#x20;[GitHub 링크](https://github.com/hamonikr/ventoy)에서 더 자세한 내용을 확인하실 수 있습니다.
{% endhint %}

프로그램 설치가 완료되면 시작 메뉴에 ventoy 를 검색하여 `ventoy 부팅 USB 제작` 을 클릭합니다.

![](<../.gitbook/assets/image (292).png>)

아래와 같이 실행되는 터미널에 사용자 비밀번호를 입력합니다.

![](<../.gitbook/assets/스크린샷, 2021-04-29 19-15-02.png>)

아래와 같이 Ventoy 프로그램이 실행됩니다.

![](<../.gitbook/assets/스크린샷, 2021-04-29 19-15-26 (1).png>)

## Ventoy 사용하기

### USB에 Ventoy 설치하기

PC에 USB를 꼽고 (포맷한 USB로 사용하세요),&#x20;

장치 항목에서 해당 USB를 선택 한 후 `설치`를 클릭하면 장치에 Ventoy 설치가 진행됩니다.

![](<../.gitbook/assets/스크린샷, 2021-04-29 19-15-26.png>)

![](<../.gitbook/assets/스크린샷, 2021-04-29 19-16-20.png>)

### USB에 ISO 파일 복사하기

USB에 Ventoy 설치가 완료되면 아래와 같이 해당 USB에 두 개의 파티션이 생성된 것을 확인할 수 있습니다.

이 중 `Ventoy` 파티션에  ISO 파일들을 복사해 둡니다.

![](<../.gitbook/assets/image (212).png>)



### ISO 이미지 선택하여 부팅하기

PC 재부팅, BIOS 화면에 진입하여 해당 USB로 부팅 되도록 설정하면, 아래와 같이 Ventoy가 실행됩니다.

USB에 넣어 둔 ISO 이미지들 중 부팅하고자 하는 이미지를 선택하여 부팅할 수 있습니다.

![](<../.gitbook/assets/image (220).png>)
