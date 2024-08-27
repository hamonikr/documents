# s-search (web-search-cli)

S (s-search) 는 터미널에서 명령어를 입력해 웹 검색을 하는 도구입니다.

터미널 창에 `s --help` 를 입력해 간단한 사용법과 다양한 옵션을 확인할 수 있습니다.

## s-search 기본 사용법 <a href="#id-2021.074-s-search" id="id-2021.074-s-search"></a>

s-search의 기본 사용법은 다음과 같습니다.

`s -p [provider] <키워드>`

이때, provider는 google, naver와 같은 검색 사이트를 의미합니다.

`s <키워드>` 와 같이 provider를 명시하지 않으면 기본 검색 사이트인 구글 검색이 수행됩니다.

아래 이미지는 터미널 창에 `s golang` 를 입력해 google에 "golang"을 검색한 결과가 웹 브라우저로 열린 모습입니다.

아래 이미지는 터미널 창에 `s -p naver hamonikr` 를 입력해 naver에 "hamonikr"를 검색한 결과가 웹 브라우저로 열린 모습입니다.

터미널 창에 `s --list-providers` 를 입력해 s-search가 제공하는 provider 리스트를 확인할 수 있습니다.

google, naver 외에도 amazon, archwiki, bing, facebook, github, gmail, instagram, medium, netflix, soundcloud, spotify, stackoverflow, youtube 등 다양한 검색 사이트를 지원합니다.

## 웹 검색 결과를 터미널 창에서 보기 <a href="#id-2021.074" id="id-2021.074"></a>

**w3m**은 무료 오픈 소스 텍스트 기반 웹 브라우저입니다.

웹브라우저가 아닌 터미널창에 검색 결과를 출력하기 위해서는 `-b` 옵션으로 w3m 을 입력합니다.

아래 이미지는 `s -b w3m golang` 을 입력해 구글에 "golang"을 검색한 결과를 터미널창에 출력한 모습입니다.

## 웹 서버로 열기 <a href="#id-2021.074" id="id-2021.074"></a>

s-search의 `-s` 옵션을 통해 s-search를 터미널 창에서가 아닌 웹 인터페이스로도 사용할 수 있습니다.

터미널창에 `s -s` 라고 입력하면 기본포트인 8080에서 웹서버가 실행됩니다.

아래 이미지는 터미널창에 `s -s` 를 입력한 후 localhost:8080에 접속해 웹서버가 실행된 모습을 확인한 결과입니다.

## s-search 의 설정 변경하기 <a href="#id-2021.074-s-search" id="id-2021.074-s-search"></a>

s-search의 설정파일인 \~/.config/s/config 파일을 생성해 s-search의 설정을 직접 custom 할 수 있습니다.

특정 provider 제외, 특정 provider 포함, 직접 provider 추가 등 다양한 기능이 제공됩니다.

자세한 사항을 s-search 레포지토리([https://github.com/zquestz/s](https://github.com/zquestz/s)) 리드미의 Configuration 항목에서 확인하세요.
