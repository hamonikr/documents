# 하모니카 프린터 설정 가이드

이 문서의 내용은 다음과 같이 구성되었습니다.

* [방법1) 프로그램 > 프린터 실행](printers.md#id-하모니카프린터설정가이드-방법1\)프로그램%3E프린터실행)
  * [1.  시스템에서 제공하는 프린터 유틸리티를 실행.](printers.md#id-하모니카프린터설정가이드-1.시스템에서제공하는프린터유틸리티를실행.)
  * [2. 상단의 추가하기 버튼을 누릅니다.](printers.md#id-하모니카프린터설정가이드-2.상단의추가하기버튼을누릅니다.)
  * [3. USB 프린터의 경우](printers.md#id-하모니카프린터설정가이드-3.USB프린터의경우)
  * [4. 네트워크 연결 프린터인 경우](printers.md#id-하모니카프린터설정가이드-4.네트워크연결프린터인경우)
  * [5.  프린터 드라이버 설치](printers.md#id-하모니카프린터설정가이드-5.프린터드라이버설치)
    * [드라이버 설치 방법1 - 프린터 모델 선택](printers.md#id-하모니카프린터설정가이드-드라이버설치방법1-프린터모델선택)
    * [드라이버 설치 방법2 - 프린터 드라이버 파일을 수동으로 선택](printers.md#id-하모니카프린터설정가이드-드라이버설치방법2-프린터드라이버파일을수동으로선택)
    * [드라이버 설치 방법3 - 다운로드 가능한 프린터 드라이버 검색](printers.md#id-하모니카프린터설정가이드-드라이버설치방법3-다운로드가능한프린터드라이버검색)
    * [드라이버 설치 방법4 - Driverless IPP 선택](printers.md#id-하모니카프린터설정가이드-드라이버설치방법4-DriverlessIPP선택)
* [방법2) 웹브라우저로 프린터 추가 ](printers.md#id-하모니카프린터설정가이드-방법2\)웹브라우저로프린터추가method2)
  * [프린터 관리그룹으로 등록](printers.md#id-하모니카프린터설정가이드-프린터관리그룹으로등록)
  * [프린터 관리페이지 접속](printers.md#id-하모니카프린터설정가이드-프린터관리페이지접속)
    * [프린터 추가 메뉴](printers.md#id-하모니카프린터설정가이드-프린터추가메뉴)
    * [프린터 추가하기 - Step 1](printers.md#id-하모니카프린터설정가이드-프린터추가하기-Step1)
    * [프린터 추가하기 - Step 2](printers.md#id-하모니카프린터설정가이드-프린터추가하기-Step2)
    * [프린터 추가하기 - Step 3](printers.md#id-하모니카프린터설정가이드-프린터추가하기-Step3)
    * [프린터 추가하기 - Step 4](printers.md#id-하모니카프린터설정가이드-프린터추가하기-Step4)
    * [프린터 추가하기 - Step 5](printers.md#id-하모니카프린터설정가이드-프린터추가하기-Step5)
    * [프린터 추가하기 - Step 6](printers.md#id-하모니카프린터설정가이드-프린터추가하기-Step6)
* [방법3) 터미널 > lpadmin 으로 설정 ](printers.md#id-하모니카프린터설정가이드-방법3\)터미널%3Elpadmin으로설정method3)
  * [현재 설치된 프린터 보기](printers.md#id-하모니카프린터설정가이드-현재설치된프린터보기)
  * [프린터 추가하기](printers.md#id-하모니카프린터설정가이드-프린터추가하기)
  * [기본 프린터로 설정하기](printers.md#id-하모니카프린터설정가이드-기본프린터로설정하기)
  * [프린터 출력하기](printers.md#id-하모니카프린터설정가이드-프린터출력하기)
  * [Driverless 프린터 추가하기](printers.md#id-하모니카프린터설정가이드-Driverless프린터추가하기)
* [기타. 윈도우용 프린터를 공유해서 사용하는 방법(samba) ](printers.md#id-하모니카프린터설정가이드-기타.윈도우용프린터를공유해서사용하는방법\(samba\)share-printer)
  * [1) 삼바 설정 변경](printers.md#id-하모니카프린터설정가이드-1\)삼바설정변경)
  * [2) 삼바 재시작](printers.md#id-하모니카프린터설정가이드-2\)삼바재시작)
  * [3) 하모니카에서 프린터 설정](printers.md#id-하모니카프린터설정가이드-3\)하모니카에서프린터설정)

하모니카는 최근의 프린터는 대부분이 사용하는 usb 프린터를 지원하고 있으며

프린터의 전원을 키고 usb 를 꼽으면 자동으로 인식되어 설치됩니다.&#x20;

만약 자동으로 인식되지 않는 경우에는 다음의 4가지 방법으로 설치할 수 있습니다.

* 프로그램 > 프린터 실행
* 터미널 > lpadmin 으로 설정
* 웹브라우저 > [http://localhost:631](http://localhost:631)

프린터 제조사가 리눅스용 드라이버를 지원한다면 Ubuntu 용 드라이버를 다운로드 받아서 설치하면 됩니다.

프린터 드라이버의 경우 하모니카는 지원하는 드라이버가 없는 경우에도 자동으로 드라이버를 검색해서 찾아줍니다.

프린터 DB에 등록된 모델이 아닌 경우는 제조사에서 제공하는 프린터 드라이버(ppd)가 필요합니다.

일부 프린터는 하모니카에서 사용할 수 있는 드라이버 파일(ppd)이 제공되지 않는데, 이 경우는 다음과 같은 방법을 사용할 수 있습니다.

* 프린터 드라이버가 필요없는 [Driverless IPP](printers.md#id-하모니카프린터설정가이드-driverless)
* [윈도우용 프린터를 공유해서 사용하는 방법(samba)](printers.md#id-하모니카프린터설정가이드-share-printer)

## **방법1) 프로그램 > 프린터 실행** <a href="#id-1-greater-than" id="id-1-greater-than"></a>

### 1.  시스템에서 제공하는 프린터 유틸리티를 실행. <a href="#id-1.-." id="id-1.-."></a>

(프로그램 > 관리 > 프린터 메뉴 실행 또는 터미널에서 “system-config-printer” 명령어 입력)

### 2. 상단의 추가하기 버튼을 누릅니다. <a href="#id-2.-." id="id-2.-."></a>

![](../../.gitbook/assets/64357181.png)

### 3. USB 프린터의 경우 <a href="#id-3.usb" id="id-3.usb"></a>

모델명이 위에 표시됩니다. 모델명을 선택하고 다음 버튼을 누릅니다.

![](../../.gitbook/assets/64357182.png)

### 4. 네트워크 연결 프린터인 경우 <a href="#id-4." id="id-4."></a>

네트워크 프린터를 클릭하면 화면과 같이 여러가지 옵션이 제공되는데 프린터가 네트워크 자동설정을 지원하는 경우는 검색해서 보여주게 됩니다.

검색되지 않는 경우 아래의 AppSocket/HP JetDirect 를 선택하고 Host 칸에 프린터의 IP 주소를 입력합니다.

![](../../.gitbook/assets/64357183.png)

### 5.  프린터 드라이버 설치 <a href="#id-5." id="id-5."></a>

다음 버튼을 누르면 해당 프린터의 드라이버를 자동으로 찾아줍니다. (단, 해당 사이트에 등록된 모델에 한함).&#x20;

이 경우, 다음 버튼만 클릭해주면 해당 드라이버가 자동으로 설치됩니다.

만약 프린터 드라이버를 자동으로 찾지 못하는 경우 선택하는 방법은 4가지가 있습니다.

#### 드라이버 설치 방법1 - 프린터 모델 선택 <a href="#id-1" id="id-1"></a>

기본 제공하는 프린터 드라이버 목록에서 제조회사와 프린터 모델을 선택해서 입력

* 시스템에서 해당 프린터의 드라이버를 자동으로 찾지 못하는 경우, 데이터베이스 목록에서 해당 프린터의 모델명을 수동으로 선택해줍니다.

프린터 제조사 선택

![](../../.gitbook/assets/64357184.png)

프린터 모델 선택

![](../../.gitbook/assets/64357187.png)

* 설정가능한 옵션이 있는 프린터의 경우 옵션을 설정하는 화면이 나옵니다. (이 화면은 모델에 따라 나오지 않을 수 있습니다.)

![](../../.gitbook/assets/64357188.png)

* 프린터의 이름을 설정하고, 적용 버튼을 클릭하여 프린터를 추가합니다.

![](../../.gitbook/assets/64357189.png)

#### 드라이버 설치 방법2 - 프린터 드라이버 파일을 수동으로 선택 <a href="#id-2" id="id-2"></a>

제조사에서 공급하는 프린터 드라이버 파일을 직접 선택해줍니다.

프린터 드라이버 파일은 주로 파일 확장자가 ppd 로 제공되는 파일입니다.

![](../../.gitbook/assets/64357185.png)

#### 드라이버 설치 방법3 - 다운로드 가능한 프린터 드라이버 검색 <a href="#id-3" id="id-3"></a>

프린터 모델이나 제조사를 입력하고 검색합니다.

[http://www.openprinting.org/printers](http://www.openprinting.org/printers) 에 등록되지 않은 프린터의 경우 검색되지 않습니다.

![](../../.gitbook/assets/64357186.png)

#### 드라이버 설치 방법4 - Driverless IPP 선택 <a href="#id-4-driverlessipp" id="id-4-driverlessipp"></a>

Driverless IPP - 프린터 드라이버가 필요없는 프린팅 방식을 의미합니다.

이 방식은 프린터에서 보내주는 정보를 이용하여 프린터 드라이버가 없는 경우에도 인쇄할 수 있는 방법입니다.

프린터 사용자들이 관련 드라이버가 없어서 제대로 사용하지 못하는 경우가 있는데

하모니카의 CUPS 서비스는 프린터 관리를 위해 드라이버가 없는 프린터의 경우에도 자동으로 프린터 드라이버를 추가해서 사용할 수 있는 Driverless Printing 기능이 제공됩니다.

(CUPS 2.2.2 이상, cups-filters 1.13.0 이상 필요)

다만 기본적으로 활성화 되어 있지 않고, 이 기능을 사용하기 위해서는 /etc/cups/cups-browser.conf 파일의 제일 아래쪽에 아래의 내용을 추가합니다.

**sudo vi /etc/cups/cups-browser.conf**

CreateIPPPrinterQueues Driverless\
CreateIPPPrinterQueues All

\
설정 파일을 저장 후 다음과 같이 cups 서비스를 다시 재시작 해줍니다.

$ sudo systemctl restart cups cups-browsed

이제 **프로그램 > 프린터**를 실행하고 프린터 추가 버튼을 누르면 다음과 같은 화면이 나옵니다.

이때 아래 화면처럼 Driverless IPP 를 선택하시면 자동으로 프린터 드라이버를 추가해줍니다.

![](../../.gitbook/assets/64357208.png)

이 기능은 cups-filters PPD Generator 기능을 통해 자동으로 드라이버를 추가하는데 아래와 같은 과정으로 수행됩니다.

text -> texttopdf -> pdftopdf -> PDF -> gstoraster -> rastertopclm -> PCLm ---> Printer

참고문서 : [https://wiki.debian.org/CUPSDriverlessPrinting](https://wiki.debian.org/CUPSDriverlessPrinting)

## **방법2) 웹브라우저로 프린터 추가**  <a href="#id-2-method2" id="id-2-method2"></a>

### 프린터 관리그룹으로 등록 <a href="#id" id="id"></a>

먼저 현재 사용자를 프린터 관리그룹으로 등록해야 합니다.

터미널에서 아래의 명령을 실행하세요.&#x20;

```
sudo usermod -aG lpadmin $USER
sudo systemctl restart cups cups-browsed
```

### 프린터 관리페이지 접속 <a href="#id" id="id"></a>

이제 웹브라우저를 열고 주소창에 아래의 주소를 입력합니다.

[http://localhost:631](http://localhost:631)

다음과 같은 화면이 나오면 상단의 Administration 탭을 클릭합니다.

이때 사용자 인증을 요구한다면 위에서 설명한 프린터 관리그룹으로 등록하기를 먼저 해주세요.

![](../../.gitbook/assets/64357168.png)

#### 프린터 추가 메뉴 <a href="#id" id="id"></a>

화면에 보이는 Add Printer 버튼을 클릭하면 프린터 추가 화면이 나옵니다.

이때 Unauthorized 메세지가 나오는 경우 크롬이나 파이어폭스 등 다른 웹브라우저를 이용해서 다시 시도하세요. (firefox 권장)

![](../../.gitbook/assets/64357169.png)

#### 프린터 추가하기 - Step 1 <a href="#id-step1" id="id-step1"></a>

프린터의 위치에 따라서 두가지 선택지가 있습니다.

자신의 컴퓨터에 직접 연결된 프린터의 경우 Local Printers 메뉴를 이용할 수 있으며

네트워크 프린터를 추가하는 경우에는 설치할 프린터가 제공하는 기능에 따라 다양한 네트워크 연결방식을 사용할 수 있습니다.

일반적으로 대부분의 프린터가 지원하는 AppSocket/HP JetDirect 를 선택하면 됩니다.

![](../../.gitbook/assets/64357170.png)

#### 프린터 추가하기 - Step 2 <a href="#id-step2" id="id-step2"></a>

AppSocket/HP JetDirect 를 선택하면 다음과 같은 화면이 보입니다. Connection 입력란에 네트워크 프린터의 위치를 입력하세요.

ex) 프린터의 IP 주소가 192.168.0.10 인 경우 다음과 같이 입력

[socket://192.168.0.10:9100](socket://192.168.0.10:9100)

![](../../.gitbook/assets/64357171.png)

#### 프린터 추가하기 - Step 3 <a href="#id-step3" id="id-step3"></a>

프린터 이름 및 공유 여부 설정합니다.

![](../../.gitbook/assets/64357172.png)

#### 프린터 추가하기 - Step 4 <a href="#id-step4" id="id-step4"></a>

프린터 드라이버를 설정 합니다.

Make 옵션 박스에서 제조사를 선택하고 Continue 버튼을 클릭하면 다음 단계로 진행됩니다.

만약 제조사의 프린터 드라이버 PPD 파일을 가지고 있는 경우는 아래의 '찾아보기' 버튼을 클릭해서 ppd 파일을 선택해 주세요.

![](../../.gitbook/assets/64357173.png)

#### 프린터 추가하기 - Step 5 <a href="#id-step5" id="id-step5"></a>

이 단계에서는 자동으로 글로벌 프린터 데이터베이스를 검색하여 제조사의 모델을 보여줍니다.

검색 결과에서 자신의 프린터 선택하세요. 해당 사이트에 등록된 모델이 아닌 경우는 여기 나타나지 않습니다.

만약 자신의 프린터가 없는 경우에는 \`[윈도우 공유 프린터 이용하기](printers.md#id-하모니카프린터설정가이드-share-printer)\` 를 참고하세요.

자신의 프린터를 선택했으면 이제 가장 아래쪽의 Add Printer 버튼을 클릭하세요

![](../../.gitbook/assets/64357174.png)

#### 프린터 추가하기 - Step 6 <a href="#id-step6" id="id-step6"></a>

이제 프린터 추가되었다는 알림이 뜨고 프린터를 사용할 수 있습니다.

프린터의 설정을 할 수 있는 화면이 나오는데 특별한 조정값이 필요하지 않다면 그냥 \`Set Default Options\` 버튼을 클릭합니다.

![](../../.gitbook/assets/64357175.png)

프로그램 > 프린터 프로그램을 실행하면 화면과 같이 프린터가 추가된것을 볼 수 있습니다.

![](../../.gitbook/assets/64357176.png)

## **방법3) 터미널 > lpadmin 으로 설정**  <a href="#id-3-greater-than-lpadmin-method3" id="id-3-greater-than-lpadmin-method3"></a>

터미널에서 프린터를 추가하는 방법은 cups 패키지의 lpadmin, lpr, lpstat 명령어를 이용합니다.

보다 자세한 내용은 [https://docs.oracle.com/cd/E19455-01/805-7229/printsetup-42445/index.html](https://docs.oracle.com/cd/E19455-01/805-7229/printsetup-42445/index.html) 참고

[http://www.openprinting.org/download/kpfeifle/LinuxKongress2002/Tutorial/VI.CUPS-Connections/VI.tutorial-handout-cups-connections.html](http://www.openprinting.org/download/kpfeifle/LinuxKongress2002/Tutorial/VI.CUPS-Connections/VI.tutorial-handout-cups-connections.html)

### 현재 설치된 프린터 보기 <a href="#id" id="id"></a>

lpstat -s

### 프린터 추가하기 <a href="#id" id="id"></a>

`lpadmin \`

&#x20;`-E \`

&#x20;`-p p3005 \`

&#x20;`-v lpd://p3005.example.com/hp-p3005 \`

&#x20;`-m postscript-hp:0/ppd/hplip/HP/hp-laserjet_p3005-ps.ppd \`

&#x20;`-E`

* The first `-E` option forces to use encryption when connecting to the server. Note the last `-E` option which means something different entirely. We'll come back to it.
* The `-p` option expects the so-called _destination_, in other words the name of the printer to create.
* Relating to `lpinfo`, the `lpadmin -v` option is used for specifying the device URI, including the protocol – `lpd`, here. Note that it's not the entire line as `lpinfo` will normally print it out and you need to leave out the connection type, e.g. `file`, `direct`, `file`.
* Also relating to `lpinfo`, the `lpadmin -m` option lets you indicate the model. It can be referred to either with what `lpinfo -m` offers to you – and there's nothing to leave out there, this time. Or it can be referred to directly with a PPD file.
* The last `-E` option, this time supplied after `-p`, means _ena_

### 기본 프린터로 설정하기 <a href="#id" id="id"></a>

lpoptions -d <프린터이름>

### 프린터 출력하기 <a href="#id" id="id"></a>

lpr <파일명>

### Driverless 프린터 추가하기 <a href="#id-driverless" id="id-driverless"></a>

먼저 다음 명령어로 현재 사용가능한 driverlesss 프린터를 확인합니다.

driverless list

![](../../.gitbook/assets/64357215.png)

식별된 URI 를 이용하여 다음과 같이 드라이버 없는 프린터를 추가할 수 있습니다.

lpadmin -p Printer -v [ipp://FXD7B670.local:631/ipp/print](ipp://FXD7B670.local:631/ipp/print) -m driverless:[ipp://FXD7B670.local:631/ipp/print](ipp://FXD7B670.local:631/ipp/print)

![](../../.gitbook/assets/64357216.png)

![](../../.gitbook/assets/64357217.png)

## **기타. 윈도우용 프린터를 공유해서 사용하는 방법(samba)**  <a href="#id-.-samba-share-printer" id="id-.-samba-share-printer"></a>

### **1) 삼바 설정 변경** <a href="#id-1" id="id-1"></a>

sudo xed /etc/samba/smb.conf

\[global] 밑에 아래 3줄을 추가

dos charset=cp949

display charset = UTF8

unix charset=UTF8

### **2) 삼바 재시작** <a href="#id-2" id="id-2"></a>

sudo systemctl restart smbd

### **3) 하모니카에서 프린터 설정** <a href="#id-3" id="id-3"></a>

프로그램 > 관리 → 프린터 를 실행

상단의 추가하기 버튼을 클릭하면 다음과 같은 화면이 나옵니다.

공유프린터의 주소와 프린터 이름을 입력하고 정상적인 사용이 가능한지 확인 버튼을 클릭합니다.

예)

smb://공유컴퓨터 IP(예.192.168.0.1)/프린터이름(SamsungCLX-6220Series)

![](../../.gitbook/assets/64357193.png)

다음 버튼을 누르고 프린터 설정을 마칩니다.&#x20;
