# 프린터 연결

HamoniKR OS에서는 네트워크 상에 존재하는 프린터를 자동으로 연결해서 프린터를 사용할 수 있습니다.&#x20;

즉, **사용자가 직접 프린터 드라이브를 설치할 필요가 없습니다.**&#x20;



만약 프린터 연결이 안된다면 하모니카팀에서 제공하는 프린터 지원 패키지를 설치해서 사용하시면됩니다.&#x20;



프린터 지원 패키지 설치.

```
# HamoniKR OS가 아닌 경우 
wget -qO- https://pkg.hamonikr.org/add-hamonikr.apt | sudo -E bash -
 
 
# HamoniKR OS인 경우.
sudo apt update
sudo apt install hamonikr-printer-drivers
```



## 프린터 프로그램 실행 <a href="#id" id="id"></a>

"**프로그램 메뉴 > 관리 > 프린터** " 또는 "**시스템 설정의 프린터**" 실행 (또는 터미널에서 “system-config-printer” 명령어 입력)

<figure><img src="../.gitbook/assets/image (510).png" alt=""><figcaption></figcaption></figure>

\


## 프린터 추가하기 버튼 클릭 <a href="#id" id="id"></a>

상단의 추가하기 버튼을 누릅니다.

<figure><img src="https://gblobscdn.gitbook.com/assets%2Fhamonikr%2F-MRTAMrEYrMhUJUpGoYQ%2F-MRTAd3jkX_6SeIeyQSa%2F64357181.png?alt=media" alt=""><figcaption></figcaption></figure>

\


### USB 프린터의 경우 <a href="#id-usb" id="id-usb"></a>

모델명이 위에 표시됩니다. 모델명을 선택하고 다음 버튼을 누릅니다.

<figure><img src="https://gblobscdn.gitbook.com/assets%2Fhamonikr%2F-MRTAMrEYrMhUJUpGoYQ%2F-MRTAd3kTfoMTiXp7bQG%2F64357182.png?alt=media" alt=""><figcaption></figcaption></figure>

\


### 네트워크 연결 프린터인 경우 <a href="#id" id="id"></a>

네트워크 프린터를 클릭하면 화면과 같이 여러가지 옵션이 제공되는데 프린터가 네트워크 자동설정을 지원하는 경우는 검색해서 보여주게 됩니다.

검색되지 않는 경우 아래의 AppSocket/HP JetDirect 를 선택하고 Host 칸에 프린터의 IP 주소를 입력합니다.

<figure><img src="https://gblobscdn.gitbook.com/assets%2Fhamonikr%2F-MRTAMrEYrMhUJUpGoYQ%2F-MRTAd3lIwsyPHXakZu9%2F64357183.png?alt=media" alt=""><figcaption></figcaption></figure>

\


## 프린터 드라이버 설치 <a href="#id" id="id"></a>

### 프린터 목록에서 추가할 프린터가 있는 경우 <a href="#id" id="id"></a>

기본 제공하는 프린터 드라이버 목록에서 추가할 프린터가 있는 경우에는 적합한 제조사와 프린터 모델을 선택합니다.

<img src="../.gitbook/assets/image (509).png" alt="" data-size="original">\


프린터 제조사 선택

<figure><img src="https://gblobscdn.gitbook.com/assets%2Fhamonikr%2F-MRTAMrEYrMhUJUpGoYQ%2F-MRTAd3m2EAxwHOBEMce%2F64357184.png?alt=media" alt=""><figcaption></figcaption></figure>

\


프린터 제품명 선택

<figure><img src="https://gblobscdn.gitbook.com/assets%2Fhamonikr%2F-MRTAMrEYrMhUJUpGoYQ%2F-MRTAd3pmX5xe2Pfg1xt%2F64357187.png?alt=media" alt=""><figcaption></figcaption></figure>

\


설정가능한 옵션이 있는 프린터의 경우 옵션을 설정하는 화면이 나옵니다. (이 화면은 모델에 따라 나오지 않을 수 있습니다.)

<figure><img src="https://gblobscdn.gitbook.com/assets%2Fhamonikr%2F-MRTAMrEYrMhUJUpGoYQ%2F-MRTAd3qnHS5P3Lubw7G%2F64357188.png?alt=media" alt=""><figcaption></figcaption></figure>

\


### 프린터 목록에서 추가할 프린터가 없는 경우 <a href="#id" id="id"></a>

만약 프린터 드라이버를 자동으로 찾지 못하는 경우에는 다음과 같은 방법으로 프린터 드라이버를 수동으로 추가할 수 있습니다.

리눅스를 지원하는 제품은 제조사에서 제공하는 드라이버 파일(파일 확장자가 ppd)을 다운로드 받아서 압축을 해제하면 포함되어 있습니다

\


![](http://confluence.invesume.com/download/attachments/2459478/image2021-7-13\_18-38-36.png?version=1\&modificationDate=1626140661725\&api=v2)

\


프린터의 이름을 설정하고, 적용 버튼을 클릭하여 프린터를 추가합니다.

<figure><img src="https://gblobscdn.gitbook.com/assets%2Fhamonikr%2F-MRTAMrEYrMhUJUpGoYQ%2F-MRTAd3rRXbf4_Su-YKe%2F64357189.png?alt=media" alt=""><figcaption></figcaption></figure>

\


### 프린터 드라이버가 필요 없는 인쇄 방식을 사용하는 경우 <a href="#id" id="id"></a>

\


하모니카는 프린터 관리를 위해 드라이버가 없는 프린터의 경우에도 자동으로 프린터 드라이버를 추가해서 사용할 수 있는 Driverless Printing 기능이 제공되는데

이 방식은 프린터에서 보내주는 정보를 이용하여 프린터 드라이버가 없는 경우에도 인쇄할 수 있는 방법입니다. (참고 문서 : [https://wiki.debian.org/CUPSDriverlessPrinting](https://wiki.debian.org/CUPSDriverlessPrinting) )

다만 이 방식은 제조사에서 제공하는 적합한 드라이버가 아니기 때문에 프린터의 일부 기능이 제한될 수 있습니다.

\


**프로그램 > 프린터**를 실행하고 프린터 추가 버튼을 누르면 다음과 같은 화면이 나옵니다.

이때 아래 화면처럼 Driverless IPP 를 선택하시면 자동으로 프린터 드라이버를 추가해줍니다.

\


<figure><img src="https://gblobscdn.gitbook.com/assets%2Fhamonikr%2F-MRTAMrEYrMhUJUpGoYQ%2F-MRTAd3vRFAiMYVn-lOT%2F64357208.png?alt=media" alt=""><figcaption></figcaption></figure>

\


## 다른 윈도우 PC 에서 공유한 프린터를 이용하는 방법 <a href="#id-pc" id="id-pc"></a>

이 방법은 윈도우를 사용하고 있는 다른 PC에서 공유한 프린터를 이용하여 인쇄하는 방법입니다.

### samba 설정 변경 <a href="#id-samba" id="id-samba"></a>

터미널을 열고 다음과 같이 입력합니다.

| `sudo xed /etc/samba/smb.conf` |
| ------------------------------ |

편집기에서 아래의 부분을 수정하고 저장합니다.

\


\[global] 밑에 아래 3줄을 추가

dos charset=cp949

display charset = UTF8

unix charset=UTF8

\


### samba 서비스 재시작 <a href="#id-samba" id="id-samba"></a>

터미널을 열고 다음과 같이 입력합니다.

| `sudo systemctl restart smbd` |
| ----------------------------- |

### 프린터 설정 <a href="#id" id="id"></a>

프로그램 > 관리 → 프린터 를 실행 후 상단의 추가하기 버튼을 클릭하면 다음과 같은 화면이 나옵니다.

공유프린터의 주소와 프린터 이름을 입력하고 정상적인 사용이 가능한지 확인 버튼을 클릭합니다.

예) smb://공유컴퓨터 IP(예.192.168.0.1)/프린터이름(SamsungCLX-6220Series)

\


<figure><img src="https://gblobscdn.gitbook.com/assets%2Fhamonikr%2F-MRTAMrEYrMhUJUpGoYQ%2F-MRTAd3uTzMvl4PxcEPh%2F64357193.png?alt=media" alt=""><figcaption></figcaption></figure>

다음 버튼을 누르고 프린터 설정을 마칩니다.
