# 자막 편집 프로그램 Subtitld

## Subtitld 설치하기

subtitld 는 영상에 자막을 추가 또는 편집하는 프로그램입니다.

**HamoniKR(>=4.0)** 사용자는 아래 명령어로 프로그램을 설치할 수 있습니다.

```
$ sudo apt update
$ sudo apt install subtitld
```

다른 우분투 배포판 사용자는 아래 명령어로 프로그램을 설치할 수 있습니다.

```
$ wget -qO- https://pkg.hamonikr.org/add-hamonikr.apt | sudo -E bash -
$ sudo apt install subtitld
```

{% hint style="info" %}
&#x20;보다 자세한 설명과 소스코드는 [Github 레포지토리](https://github.com/hamonikr/subtitld)에서 확인하실 수 있습니다.
{% endhint %}

프로그램을 설치를 완료하면 아래 이미지와 같이 `시작 프로그램` 에 `자막 편집기 Subtitld` 가 추가된 것을 확인할 수 있습니다.

![](<../.gitbook/assets/image (190).png>)



{% hint style="info" %}
위 방법으로 설치시 프로그램이 정상 실행되지 않거나, 윈도우 사용자인 경우 [해당 링크](https://subtitld.jonata.org/install)에서 프로그램을 다운로드 받으세요.
{% endhint %}

## 영상 불러오기

`Subtitld` 프로그램을 처음 실행하면 아래 이미지와 같이 빈 화면이 나타납니다.

![](<../.gitbook/assets/image (150).png>)

하단의 `OPEN` 버튼을 클릭해 편집할 영상을 선택합니다.

![](<../.gitbook/assets/image (412).png>)

아래 이미지와 같이 하단의 `Files of type` 항목을 `Video files`로 변경하면 영상 파일을 선택할 수 있습니다.

![](<../.gitbook/assets/image (334).png>)

원하는 영상 파일을 선택하고, `Open` 버튼을 클릭합니다.

![](<../.gitbook/assets/image (175).png>)

아래 이미지와 같이 영상이 불러와 진 것을 확인할 수 있습니다.

![](<../.gitbook/assets/image (248).png>)

## 자막 추가하기

영상에 자막을 추가하기 위해 좌측 하단의 `ADD` 버튼을 클릭합니다.

![](<../.gitbook/assets/image (415).png>)

우측에 생성된 입력창에 원하는 자막을 입력합니다.

![](<../.gitbook/assets/image (354).png>)

하단에 생성된 자막의 위치와 길이를 조정해 자막이 보여질 시간과 길이를 변경할 수 있습니다.

![](<../.gitbook/assets/image (285).png>)

하단에서 자막을 생성할 위치를 선택 후 `ADD` 버튼을 클릭하면 해당 위치에 자막이 생성됩니다.

![](<../.gitbook/assets/image (232).png>)

아래 이미지와 같이 세개의 자막을 생성하였습니다.

![](<../.gitbook/assets/image (210).png>)

좌측 상단의 저장 버튼을 클릭해 자막 파일을 저장합니다.

![](<../.gitbook/assets/image (280).png>)

아래 이미지와 같이 지정한 위치에 원본 영상과 같은 이름으로 `usf` 파일과 `srt` 파일이 생성된 것을 확인할 수 있습니다.

![](<../.gitbook/assets/스크린샷, 2021-07-07 10-57-08.png>)

`srt` 파일의 이름이 **영상파일의 이름과 같고** 두 파일이 **같은 경로**에 위치할 경우,&#x20;

영상을 실행했을때 아래 이미지와 같이 자막과 함께 보여지는 것을 확인할 수 있습니다.

![](<../.gitbook/assets/image (333).png>)

