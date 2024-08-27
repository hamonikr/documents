# 부팅 메뉴 선택기 boot-select

## 1. boot-select란?

PC에 여러개의 다른 운영체제나 여러개의 커널을 설치한 경우, 기본으로 부팅 될 메뉴를 선택하는 프로그램입니다.

boot-select의 더 자세한 설명은 [https://github.com/hamonikr/boot-select](https://github.com/hamonikr/boot-select) 에서 확인할 수 있습니다.

\


## 2. boot-select 설치

&#x20;ubuntu 22.04이상, HamoniKR 6.0 이상은 아래와 같이 설치가 가능합니다.&#x20;

`$ wget -qO-` [`https://repo.hamonikr.org/hamonikr-app.apt`](https://repo.hamonikr.org/hamonikr-app.apt) `| sudo -E bash -`

`$ sudo apt install neofetch`



ubuntu 20.04 이하, HamoniKR 5.0 이하는 아래와 같이 설치가 가능합니다.

`$ curl -sL` [`https://pkg.hamonikr.org/add-hamonikr.apt`](https://pkg.hamonikr.org/add-hamonikr.apt) `| sudo -E bash -`\
`$ sudo apt update`\
`$ sudo apt install -y boot-select`

\


## boot-select &#x20;

프로그램 설치가 완료되면 시작 프로그램에  boot-select 또는 부팅메뉴 선택기를 검색하거나

터미널에서 sudo boot-select를 입력하면 프로그램을 실행할 수 있습니다.&#x20;

<figure><img src="../../.gitbook/assets/1 (15).png" alt=""><figcaption></figcaption></figure>

\


boot-select를 실행하기 위해서는 관리자 권한이 필요하며, 로그인한 계정의 비밀번호를 입력해주셔야 합니다.

<figure><img src="../../.gitbook/assets/2 (9).png" alt=""><figcaption></figcaption></figure>

\


암호를 입력하면 아래와 같이 부팅을 원하는 메뉴를 선택할 수 있는 화면이 보여집니다.&#x20;

<figure><img src="../../.gitbook/assets/3 (10).png" alt=""><figcaption></figcaption></figure>

\


원하는 메뉴를 화살표 키로 선택하신 후 엔터를 입력하면 시스템이 재시작된다는 알람창이 뜨고 yes 버튼을 누르면 시스템이 자동으로 재시작됩니다.&#x20;

<figure><img src="../../.gitbook/assets/4 (10).png" alt=""><figcaption><p><br></p></figcaption></figure>

시스템이 재시작되면 부팅 목록에서 선택한 부팅 메뉴가 우선으로 선택되어 있는 것을 확인할 수 있습니다.&#x20;
