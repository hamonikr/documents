# 모니터링 도구 Conky

## hamonikr-conky 설치하기

Conky는 바탕화면의 모니터링 도구입니다.

하모니카는 hamonikr-conky 를 통해 Conky 설정을 돕는 도구를 제공합니다.

**HamoniKR** 사용자는 아래 명령어를 통해 hamonikr-conky 를 설치할 수 있습니다.

```
# HamoniKR OS에서는 기본 프로그램으로 설치되어있습니다.
$ sudo apt update
$ sudo apt install -y hamonikr-conky
```

**Ubuntu**, **LinuxMint** 등 다른 배포판 사용자의 경우 아래 명령어를 통해 설치할 수 있습니다.

```bash
$ curl -sL https://pkg.hamonikr.org/add-hamonikr.apt | sudo -E bash -
$ sudo apt install -y hamonikr-conky
```

{% hint style="info" %}
&#x20;[GitHub 링크](https://github.com/hamonikr/hamonikr-conky)에서 더 자세한 내용을 확인하실 수 있습니다.
{% endhint %}

설치가 완료되면 아래와 같이 시작 메뉴에서 conky를 검색하여 `Conky 설정도구` 를 실행하고,

`Conky 온/오프`를 통해 conky 를 키고 끌 수 있습니다.

<figure><img src="../../.gitbook/assets/5 (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/스크린샷, 2023-10-31 12-54-26.png" alt=""><figcaption></figcaption></figure>

## Conky 사용하기

`Conky 설정도구`를 클릭하면, 아래와 같이 Conky Manager가 실행됩니다.

위젯 리스트 중 원하는 위젯을 체크하면 바탕화면에 해당 위젯이 추가됩니다.

<figure><img src="../../.gitbook/assets/스크린샷, 2023-10-31 12-57-45.png" alt=""><figcaption></figcaption></figure>



### 위젯 편집하기

편집을 원하는 테마를 선택 한 후 위의 아이콘을 클릭하여 해당 위젯의 위치, 크기 등을 편집할 수 있습니다.

<figure><img src="../../.gitbook/assets/image (28).png" alt=""><figcaption></figcaption></figure>

### Conky 키고 끄기

Albert (alt + space) 또는 시작 메뉴의 `Conky 온/오프` 를 클릭하여 Conky 를 키거나 끌 수 있습니다.

<figure><img src="../../.gitbook/assets/5 (2).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/6 (2).png" alt=""><figcaption></figcaption></figure>



## Conky 테마 추가하기

기본 제공되는 테마 외에도 자신이 원하는 테마를 탐색 또는 제작하여 추가할 수 있습니다.

### 테마 탐색하기

아래와 같은 사이트에서 다양한 conky 테마 오픈소스를 탐색할 수 있습니다.

* [devianart.com](https://www.deviantart.com/search?q=conky)
* [gnome-look.org](https://www.gnome-look.org/browse/cat/124/order/latest)
* [github.com](https://github.com/search?q=conky)

테마를 다운받고, 파일이 압축된 상태라면 압축을 풉니다.

보통 하나의 테마의 구성은 아래와 같습니다.

![](<../../.gitbook/assets/스크린샷, 2021-05-20 11-30-03.png>)

`start_conky.sh` 파일은 해당 테마를 실행시키는 스크립트 파일입니다.

`conkyrc`는 conky 테마의 설정파일입니다. 해당 파일에서 테마의 대부분을 그립니다.

`cups_n_saucers.lua` 파일은 테마의 심화 기능을 수행하는 스크립트 파일입니다. lua 파일은 테마에 따라 없을 수도 있습니다.



### 테마 추가, 적용하기

위 파일들이 포함된 폴더를 \~/.conky 폴더에 복사합니다.

![](<../../.gitbook/assets/스크린샷, 2021-05-20 11-43-04.png>)

아래와 같이 `Conky 설정도구`에 해당 테마가 추가된 것을 확인할 수 있습니다.

![](<../../.gitbook/assets/스크린샷, 2021-05-20 11-40-22.png>)

테마를 체크하여 실행시켜도 아래와 같이 테마가 완전히 출력되지 않을 수 있습니다.

![](<../../.gitbook/assets/image (264).png>)

테마를 에러 없이 호환시키기 위해 conkyrc 파일을 수정하겠습니다.

conkyrc 파일의 lua 파일을 로드하는 부분에 경로가 로컬의 경로와 다른것을 확인할 수 있습니다.

![](<../../.gitbook/assets/스크린샷, 2021-05-20 11-47-08.png>)

아래와 같이 로컬의 경로에 맞게 수정하고 저장하였습니다.

![](<../../.gitbook/assets/스크린샷, 2021-05-20 11-48-55.png>)

아래와 같이 정상 출력되는 것을 확인할 수 있습니다.

![](<../../.gitbook/assets/image (398).png>)

한글이 깨지는 문제를 해결하기 위해 한글이 깨지는 부분에 폰트 설정을 추가하겠습니다.

원하는 폰트를 다운받을 수도 있고, `~/.conky/fonts/` 에 있는 폰트 중 하나를 선택할 수도 있습니다.

![](<../../.gitbook/assets/스크린샷, 2021-05-20 11-52-21.png>)

아래와 같이 한글이 깨지지 않고 출력되는 것을 확인할 수 있습니다.

![](<../../.gitbook/assets/image (332).png>)



