---
description: 키보드 & 마우스하나로 여러개 컴퓨터에 사용하기.
---

# Barrier

"Barrier"는 오픈 소스 소프트웨어로, 여러 컴퓨터의 키보드와 마우스를 단일 컴퓨터의 입력 장치로 사용할 수 있게 해주는 KVM (Keyboard, Video, Mouse) 스위치의 소프트웨어 버전입니다.

Barrier의 주요 특징은 다음과 같습니다:

1. **다중 플랫폼 지원**: Barrier는 Windows, macOS, 그리고 Linux에서 동작합니다.
2. **클립보드 공유**: 한 컴퓨터에서 텍스트 복사하고 다른 컴퓨터에 붙여넣을 수 있습니다.
3. **오픈 소스**: Barrier는 GPL 라이선스로 배포되는 오픈 소스 프로젝트입니다.

Barrier를 사용하면 여러 컴퓨터를 사용하는 작업 공간에서 키보드와 마우스 스위칭 장치를 구입할 필요 없이 효율적으로 작업할 수 있습니다.



### Barrier 설치하기.

```
$ sudo apt install -y barrier
```



### Barrier 실행하기.

프로그램 메뉴> "barrier" 또는 Albert(Ctrl + Space) barrier로 실행합니다.&#x20;

<div>

<figure><img src="../.gitbook/assets/스크린샷, 2023-10-26 15-49-07 (1).png" alt=""><figcaption></figcaption></figure>

 

<figure><img src="../.gitbook/assets/스크린샷, 2023-10-26 15-50-18.png" alt=""><figcaption></figcaption></figure>

</div>

<figure><img src="../.gitbook/assets/스크린샷, 2023-10-26 15-51-17.png" alt=""><figcaption></figcaption></figure>



### Barrier 설정하기

Barrier는 서버와 클리아언트로 설정을 합니다.&#x20;

* 서버는 마우스와 키보드를 사용하실 컴퓨터를 의미하며,
* 클라이언트는 사용하실 여러대의 컴퓨터입니다.&#x20;



### Barrier 서버 설정하기

1. 아래 그림과 같이 Barrier를 실행하신 후,  서버에 체크를 하시고 "서버설정" 버튼을 클릭합니다.

<figure><img src="../.gitbook/assets/image (460).png" alt=""><figcaption></figcaption></figure>

2. Barrier 서버 구성과 레이어 설정을 진행합니다.&#x20;
   1. 우측 상단의 모니터를 마우스로 선택하여 드래그로 끌어다 놓습니다.&#x20;
   2. "이름없음" 지정된 모니터가 생성됩니다.

<figure><img src="../.gitbook/assets/image (464).png" alt=""><figcaption></figcaption></figure>

3.  "이름없음" 모니터를 마우스 더블클릭을 하고, 화면 이름에 컴퓨터의 화면 이름(장치 이름)을 입력하고 OK버튼을 클릭합니다.

    &#x20;<mark style="color:red;">**- 잠깐!. 컴퓨터의 화면이름을 몰르시겠다고요??**</mark>&#x20;

    &#x20;<mark style="color:red;">**- 그러면 클라이언트로 사용하실 컴퓨터에 Barrier를 실행하신 후 "F4"를 눌르시면 확인할 수 있어요..**</mark>

<figure><img src="../.gitbook/assets/image (465).png" alt=""><figcaption></figcaption></figure>

4. "이름없음"에서 입력하신 화면이름으로 변경됩니다.&#x20;

<figure><img src="../.gitbook/assets/image (466).png" alt=""><figcaption></figcaption></figure>

5. 그리고 간편 사용을 위해 단축키 설정을 진행합니다.&#x20;
   1. 그림에서 "1 단축키" 탭을 눌리시고,  "2 생성" 버튼을 클릭하면, "3. 단축키" 설정창이 나옵니다.&#x20;
   2. 사용하실 키보드 단축키를 지정하고 "ok"버튼을 클릭하세요.

<figure><img src="../.gitbook/assets/image (467).png" alt=""><figcaption></figcaption></figure>

6.  좌측 단축키 레이어에서 지정하신 단축키를 클릭하시고,  우측 행동 레이어에서 "1. 생성" 버튼을 클릭합니다.&#x20;

    &#x20;\- 동작 설정창에서 원하시는 수행 동작을 선택하시면 됩니다.&#x20;

    &#x20;\- 전 동작 설정의 옵션에서 Toggle Screen을 선택하겠습니다.&#x20;

<figure><img src="../.gitbook/assets/image (469).png" alt=""><figcaption></figcaption></figure>

7. Barrier를 사용하기 위한 서버 설정이 완료된것이며, "OK" 버튼을 클릭하여 "서버설정" 창을 닫으시고  Barrier의 "시작" 버튼을 클릭합니다.

<div>

<figure><img src="../.gitbook/assets/선택 영역_018 (1).png" alt=""><figcaption></figcaption></figure>

 

<figure><img src="../.gitbook/assets/선택 영역_019 (1).png" alt=""><figcaption></figcaption></figure>

</div>

<figure><img src="../.gitbook/assets/image (471).png" alt=""><figcaption></figcaption></figure>

### Barrier 클라이언트 설정하기.

1. Barrier 실행 후 클라이언트 체크를 하시고 "시작" 버튼을 클릭합니다.&#x20;

<figure><img src="../.gitbook/assets/image (472).png" alt=""><figcaption></figcaption></figure>

2. Security question 창이 나오는데 여기에서 "Yes" 버튼을 클릭합니다.&#x20;

<figure><img src="../.gitbook/assets/image (473).png" alt=""><figcaption></figcaption></figure>

3.  클라이언트 설정이 완료되었습니다. Barrier창을 닫아주세요... 창을 닫는다고 종료되는게 아니니 문제 없습니다.&#x20;

    &#x20;\- Barrier 종료는 작업표시줄에 Barrier 아이콘으로 종료하시면됩니다.&#x20;

<figure><img src="../.gitbook/assets/3 (11).png" alt=""><figcaption></figcaption></figure>



#### 이로써 서버와 클라이언트 설정이 완료되었습니다.&#x20;

#### 지정하신 단축키를 이용해서 하나의 키보드와 마우스로 여러개의 컴퓨터를 관리해 보세요...

#### 아주 아주 좋\~습니다.&#x20;
