# 하모니카 OS 사용가능한 백신들

## ClamAV <a href="#id-os" id="id-os"></a>

* ClamAV 엔진을 기반으로 ClakTK 백신 사용가능

### 설치

```
sudo apt install clamav clamav-daemon clamtk
```

### 실행

시작메뉴에서 clamtk 실행

<figure><img src="../../.gitbook/assets/001 (2).png" alt=""><figcaption></figcaption></figure>

## 알약 (무료) <a href="#id-os" id="id-os"></a>

일반 사용자에게는 알약 리눅스 버전을 무료로 배포하고 있습니다.

패키지 버전이 아닌 설치 스크립트 형태이기 때문에 설치에 다소 어려움이 있지만 이스트시큐리티에서 제공하고 있는 매뉴얼대로 진행하면 문제없이 설치 가능합니다.

메뉴얼 : [알약 매뉴얼](https://cdn1.estsecurity.com/manual/alyacvms1/alyacforopenos1-manual\_ko.pdf)

### 설치

1. 시작메뉴에서 '환영합니다' 또는 welcome 입력 후 실행
2. 추천 프로그램에 있는 알약 다운로드\
   다운로드 경로는 /tmp/alyacdown 폴더입니다.
3. alyac.install 스크립트 실행\
   스크립트가 있는 위치에서 터미널을 열어서 진행\
   **sudo ./alyac.install**
4. 라이선스와 관련된 내용이 나오면 (하단에 --More-- 나오면) 스페이스바를 눌러 내용을 내린다.
5. 동의하는 내용이 나오면 y를 입력해줍니다.
6. input install path (default : /usr/local) : 설치 경로를 물어보는 것으로 따로 지정하지 않고 엔터를 누릅니다.
7. 설치가 완료되면 트레이 아이콘에 알약 아이콘이 표시됩니다.

<figure><img src="../../.gitbook/assets/002 (1).png" alt=""><figcaption></figcaption></figure>

### 제거

```
cd /usr/local/ALYac
sudo ./uninstall.sh
```

## 알약 (유료)

리눅스에서 알약을 상업적으로 사용하기 위해서는 이스트시큐리티에서 문의하셔야 합니다.

* [https://www.estsecurity.com/product/linux\_unix](https://www.estsecurity.com/product/linux\_unix)
* [알약 리눅스 버전(OL) 메뉴얼(171213).pdf](https://app.gitbook.com/s/-MOdedbke\_kpJqE1CY2X/tips/A1/attachments/24313947/24313948.pdf)
* 라이선스 : [Certificate.pdf](https://app.gitbook.com/s/-MOdedbke\_kpJqE1CY2X/tips/A1/attachments/24313947/24313960.pdf)

## V3 (유료) <a href="#id-os-v3" id="id-os-v3"></a>

* 2015년 부터 하모니카 OS 지원 하고 있음
* [https://www.ahnlab.com/kr/site/product/productView.do?prodSeq=58](https://www.ahnlab.com/kr/site/product/productView.do?prodSeq=58)

## 트렌드마이크로 (유료) <a href="#id-os" id="id-os"></a>

* 버전별로 지원 버전이 계속 업데이트 : [http://files.trendmicro.com/documentation/guides/deep\_security/Kernel%20Support/11.0/Deep\_Security\_11\_kernels\_EN.html](http://files.trendmicro.com/documentation/guides/deep\_security/Kernel%20Support/11.0/Deep\_Security\_11\_kernels\_EN.html)
* 트라이얼 다운로드 : [https://www.trendmicro.com/en\_us/business/products/hybrid-cloud/deep-security.html](https://www.trendmicro.com/en\_us/business/products/hybrid-cloud/deep-security.html)

## 이스캔 리눅스(eScan for Linux) <a href="#id-os-escanforlinux" id="id-os-escanforlinux"></a>

* [https://blog.naver.com/escankorea/221347827616](https://blog.naver.com/escankorea/221347827616)



## 구매관련 연락처 <a href="#id-os" id="id-os"></a>

* 안랩 우정사업본부 담당 협력사 / 인사이드프로 이승열상무님 / 010-2922-4521 / syl22@insidepro.co.kr
