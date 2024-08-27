# glances (system monitoring tool)

`glances`는 크로스 플랫폼 시스템 모니터링 툴입니다.

`glances`를 통해 PC의 상태와 시스템 정보를 웹으로도, 모바일로도, 로컬에서도 볼수있습니다.

터미널 창에 `glances --help` 를 입력해 간단한 사용법과 다양한 옵션을 확인할 수 있습니다.

![](<../../.gitbook/assets/image (144).png>)

`tldr glances` 를 입력해 `glances`의 기본 사용 예제를 확인할 수도 있습니다.

![](<../../.gitbook/assets/image (344).png>)

## 로컬 시스템 모니터링하기

터미널 창을 열고, `glances` 를 입력하면 아래와 같이 로컬 PC의 시스템 정보 모니터링 화면이 나타납니다.

![](<../../.gitbook/assets/image (376).png>)

## 웹을 통한 모니터링

터미널 창을 열고, `glances -w` 를 입력합니다.

다음과 같이 61280 포트에서 해당 웹이 실행된 것을 확인합니다.

![](<../../.gitbook/assets/image (352).png>)

위에서 출력된 주소인 [http://0.0.0.0:61208](http://0.0.0.0:61208) 에 접속하면 아래와 같이 웹으로 로컬 시스템 모니터링 페이지를 볼 수 있습니다.

![](<../../.gitbook/assets/image (245).png>)

{% hint style="info" %}
`UnicodeEncodeError` 가 발생한다면, `export LC_ALL='en_US.UTF-8'` 를 입력합니다.

해당 설정을 다시 되돌리려면 `export LC_ALL='ko_KR.UTF-8'` 를 입력합니다.
{% endhint %}

## 외부 시스템 모니터링

모니터링 대상 PC에서 터미널 창을 열고, `glances -s` 를 입력합니다.

디폴트 포트는 61209이며, 아래와 같이 -p 옵션으로 다른 포트를 지정해 실행할 수도 있습니다.

![glances -s -p 61210](<../../.gitbook/assets/image (309).png>)

다른 PC에서 터미널 창을 열고, `glances -c [대상 PC의 IP]` 를 입력합니다.

아래 이미지와 같이 외부에서 해당 PC의 시스템을 모니터링 할 수 있습니다.

![glances -c \[IP\] -p 61210](<../../.gitbook/assets/image (204).png>)
