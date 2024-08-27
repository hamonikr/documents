# 데스크톱 원문 검색 프로그램 recoll

## recoll 설치하기

recoll은 데스크톱 원문 검색 프로그램입니다. ppt, doc, xls, pdf, hwp 등 문서의 원문검색을 지원합니다.

**HamoniKR(>=4.0)** 사용자는 아래 명령어로 프로그램을 설치할 수 있습니다.

```
$ sudo apt update
$ sudo apt install -y recoll=1.31.0-1hamonikr5
```

**Ubuntu(>=20.04)** 사용자는 아래 명령어로 프로그램을 설치할 수 있습니다.

```
$ curl -sL https://pkg.hamonikr.org/add-hamonikr.apt | sudo -E bash -
$ sudo apt install -y recoll=1.31.0-1hamonikr5
```

{% hint style="info" %}
&#x20;프로젝트의 소스코드와 빌드 방법은 [Github 레포지토리](https://github.com/hamonikr/recoll)에서 확인하실 수 있습니다.
{% endhint %}

프로그램 설치가 완료되면 시작 메뉴에 recoll 을 검색하여 프로그램을 실행할 수 있습니다.

![](<../.gitbook/assets/image (394).png>)

![](<../.gitbook/assets/image (357).png>)



## 색인 구축하기

프로그램을 사용하기에 앞서, 가장 먼저 색인을 구축해야 합니다.

검색을 수행할 대상인 PC의 데이터들을 지정하는 과정입니다.

처음 프로그램 설치, 실행시 보여지는 `최초 색인 작성 설정` 창에서 지금 `색인 작성 시작`을 클릭합니다.

![](<../.gitbook/assets/image (373).png>)

아래와 같이 색인 작성이 진행됩니다. 일정 시간이 소요되니 색인 작성이 완료될 때까지 기다려 주세요.

![](<../.gitbook/assets/image (312).png>)

색인 구축이 완료되면 아래와 같이 정상적으로 검색되는 것을 확인할 수 있습니다.

![](<../.gitbook/assets/image (416).png>)



## 검색하기

상단의 표 아이콘을 클릭해 검색 결과를 표 형식으로 볼 수 있습니다.

![](<../.gitbook/assets/image (211).png>)

![](<../.gitbook/assets/image (353).png>)

검색된 문서의 `미리보기`를 클릭하면 해당 문서를 텍스트 형태로 볼 수 있습니다.

![](<../.gitbook/assets/image (179).png>)

보기 -> 결과 화면 글꼴 키우기/줄이기 를 클릭해 결과 화면의 글꼴을 키우고 줄일 수 있습니다.

![](<../.gitbook/assets/image (347).png>)

`도구` -> `고급검색` 을 통해 보다 복잡한 검색을 실행할 수 있습니다.

![](<../.gitbook/assets/image (400).png>)

## 환경설정

`환경설정` -> `GUI 환경설정` 을 통해 다양한 환경설정을 변경할 수 있습니다.

![](<../.gitbook/assets/image (358).png>)

`단축키` 항목을 통해 여러가지 단축키를 확인하고 변경할 수 있습니다.

![](<../.gitbook/assets/image (396).png>)



## 색인 구축 예약하기

계속해서 변경되는 PC의 데이터를 최신 상태로 검색하기 위해서는 주기적으로 색인을 업데이트 해야 합니다.

이러한 색인 업데이트 작업을 예약해 두면 작업이 자동으로 실행됩니다.

`환경설정` -> `색인 작성 예약` 을 클릭하면 색인 예약 설정 창이 열립니다.

![](<../.gitbook/assets/image (122).png>)

해당 창에서 `Cron 예약` 을 클릭해 예약을 등록하고, 활성화 합니다.

아래와 같이 입력 후 `활성화` 버튼을 클릭하면, 매일 12:00 에 색인 업데이트 작업이 자동 실행됩니다.

![](<../.gitbook/assets/image (360).png>)

