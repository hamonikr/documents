# 시스템 사용시간 모니터링 ActivityWatch

## ActivityWatch 설치하기

ActivityWatch는 시스템 및 프로그램의 사용시간을 모니터링 해서 얼마나 많은 시간을 사용하는지 알 수 있게 보여주는 프로그램입니다.

**HamoniKR(>=4.0)** 사용자는 아래 명령어로 프로그램을 설치할 수 있습니다.

```
$ sudo apt update
$ sudo apt install hamonikr-activitywatch
```

**Ubuntu(>=18.04), LinuxMint(>=19)** 사용자는 아래 명령어로 프로그램을 설치할 수 있습니다.

```
$ wget -qO- https://pkg.hamonikr.org/add-hamonikr.apt | sudo -E bash -
$ sudo apt install hamonikr-activitywatch
```

{% hint style="info" %}
&#x20;기타 OS (**Windows**, **Mac**)에서의 설치 방법, 프로젝트의 소스코드와 빌드 방법은 [Github 레포지토리](https://github.com/hamonikr/hamonikr-activitywatch)에서 확인하실 수 있습니다.
{% endhint %}

프로그램 설치 후 시스템을 **재시작**하면 자동으로 프로그램이 시작되어 시스템 트레이에 아이콘이 나타납니다.

`프로그램 메뉴` > `보조프로그램` > `시스템 사용시간 보기` 를 클릭합니다.

![](<../.gitbook/assets/image (234).png>)

![](<../.gitbook/assets/image (384).png>)



### 브라우저 확장기능 설치하기

웹사이트 분석을 사용하고 싶은 경우, 사용하는 브라우저에 맞는 확장 기능을 추가로 설치해야 합니다.

확장 기능을 설치하기 위해 아래 링크에 접속합니다.

#### Naver Whale, Chrome 사용자 :&#x20;

{% embed url="https://chrome.google.com/webstore/detail/nglaklhklhcoonedhgnpgddginnjdadi/" %}

#### Firefox 사용자 :&#x20;

{% embed url="https://addons.mozilla.org/en-US/firefox/addon/aw-watcher-web/" %}

Chrome 사용자의 경우 아래 이미지와 같이 `Chrome에 추가` 버튼을 클릭해 해당 확장 프로그램을 설치합니다.

![](<../.gitbook/assets/스크린샷, 2021-06-07 15-24-59.png>)

이와 같이 확장 프로그램을 추가하고 나면, `ActivityWatch` 프로그램의 `Browser` 항목에 인터넷 사용 기록이 표시되는 것을 확인할 수 있습니다.

![](<../.gitbook/assets/image (252).png>)



## 시스템 사용 시간 분석

상단 메뉴의 `보고서`를 클릭하면 내 PC의 시스템 사용 시간을 확인할 수 있습니다.

![](<../.gitbook/assets/image (417).png>)

`Summary` 항목은 아래와 같이 프로그램과 윈도우의 사용 시간, 분야별 그래프 등을 확인할 수 있습니다.

![](<../.gitbook/assets/image (259).png>)



### 카테고리 설정 변경하기

카테고리 설정을 통해 보고서에 기록할 작업을 직접 분류하고, 각각의 설정을 변경할 수 있습니다.

상단 메뉴의 `설정` 을 클릭합니다.

![](<../.gitbook/assets/스크린샷, 2021-06-07 14-54-55.png>)

스크롤을 내려 아래의 `카테고리 설정` 항목을 보면 아래와 같이 기본 설정되어 있는 것을 확인할 수 있습니다.

![](<../.gitbook/assets/image (374).png>)

직접 분류를 추가하기 위해 아래의 `+ 분류 추가` 버튼을 클릭합니다.

![](<../.gitbook/assets/image (419).png>)

화상회의 프로그램인 Zoom과 Google Meet의 사용을 기록하기 위해 아래와 같이 값을 입력하였습니다.

`Name`에는 카테고리 이름을 지정하고,&#x20;

`Pattern` 에 `Zoom|Google Meet` 라고 입력해 두 프로그램의 사용을 기록하도록 설정하고,&#x20;

해당 카테고리의 표시 색을 설정하기 위해 `Inherit parent color` 버튼을 해제한 후 원하는 색상으로 지정해 주었습니다.

![](<../.gitbook/assets/image (206).png>)

`OK` 버튼을 클릭해 설정을 저장하면 아래와 같이 해당 카테고리가 추가된 것을 확인할 수 있습니다.

`저장`을 클릭해 변경 사항을 저장합니다.

![](<../.gitbook/assets/image (267).png>)

아래 이미지와 같이 해당 카테고리가 추가되고 지정한 색으로 표시되는 것을 확인할 수 있습니다.

![](<../.gitbook/assets/스크린샷, 2021-06-07 15-16-28.png>)



### 뷰 추가하기

기본으로 제공되는 `Summary`, `Window`, `Browser`, `Editor` 뷰 외에 추가적으로 필요한 뷰가 있다면 직접 추가하여 커스텀 할 수 있습니다.

뷰를 추가하기 위해 항목 우측의 `+New view`를 클릭합니다.&#x20;

![](<../.gitbook/assets/image (422).png>)

뷰의 ID와 이름을 지정해 줍니다.

![](<../.gitbook/assets/image (155).png>)

다음과 뷰가 추가된 것을 확인할 수 있습니다. 해당 뷰에 표시할 항목을 추가하기 위해 `+Add visualization`을 클릭합니다.

![](<../.gitbook/assets/image (318).png>)

추가된 프로그램 항목의 설정 아이콘을 클릭합니다.

![](<../.gitbook/assets/image (378).png>)

다음과 같이 추가할 수 있는 항목의 리스트 중 원하는 것을 선택합니다.

![](<../.gitbook/assets/image (233).png>)

아래 이미지는 `사용시간 그래프`와 `Sunburst clock`을 추가한 모습입니다.&#x20;

항목 추가를 완료하였다면 `Save` 버튼을 클릭해 해당 뷰를 저장합니다.

![](<../.gitbook/assets/image (183).png>)



## 수집된 데이터 내보내기

내 PC에서 수집한 데이터를 JSON 파일로 저장해 이를 외부와 공유할 수 있습니다.

&#x20;상단 메뉴의 `데이터베이스`를 클릭합니다.

![](<../.gitbook/assets/스크린샷, 2021-06-07 14-49-18.png>)

`JSON으로 모든 데이터베이스 내보내기`  클릭합니다.

![](<../.gitbook/assets/image (133).png>)

해당 파일을 저장할 폴더와 파일 이름을 지정하고 저장합니다.

![](<../.gitbook/assets/image (351).png>)

아래와 같이 파일이 저장된 것을 확인할 수 있습니다.

![](<../.gitbook/assets/image (343).png>)
