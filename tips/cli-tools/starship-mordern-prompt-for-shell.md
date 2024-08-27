# starship (mordern prompt for shell)

`starship` 은 쉘의 프롬프트를 유연하게 꾸밀 수 있도록 하는 프로그램입니다.

Bash, zsh 등 다양한 쉘에 호환되며, `hamonikr-cli-tools` 의 `starship` 에는 기본 설정이 포함되어 있습니다.

터미널 창에 `starship --help` 를 입력해 프로그램의 간단한 사용법을 확인할 수 있습니다.

![](<../../.gitbook/assets/image (139).png>)

위와 같이 `starship --help` 또는 `starship --version` 을 입력해 프로그램이 정상 설치된 것을 확인한 후, 새로운 터미널 창을 열면 `starship`이 적용된 것을 확인할 수 있습니다.

![](<../../.gitbook/assets/image (221).png>)

`hamonikr-cli-tools`의 `starship` 기본 설정은 다음과 같은 사항을 포함하고 있습니다.

* 현재 위치 정보 표시
* 명령어의 수행 시간 정보 표시
* git 정보 표시

## 현재 위치 정보

디렉토리 이동시 프롬프트에 기타 정보와 함께 자신의 현재 위치가 표시되는 것을 확인할 수 있습니다.

아래 이미지와 같이 tomcat 폴더 내부에서는 java의 버전도 함께 표시됩니다.

![](<../../.gitbook/assets/image (283).png>)

## 명령어 수행 시간 정보

어떤 명령어들은 수행되는데 오랜 시간이 소요되기도 하고, 그러한 경우 명령어가 수행되는데 걸린 시간을 알아야 합니다.

`starship`은 이러한 명령어 수행 시간 정보를 자동 출력합니다.

아래 이미지는 `apt update` 명령어 수행에 4초가 걸린 것을 알려주는 모습입니다.

![](<../../.gitbook/assets/image (184).png>)

## git 정보

`starship`은 현재 위치가 git 정보가 포함된 디렉토리일 경우, git 정보를 함께 표시합니다.

아래 이미지와 같이 git 프로젝트 내부에서 프로젝트 이름과 브랜치명이 함께 표시되는 것을 확인할 수 있습니다.

![](<../../.gitbook/assets/image (137).png>)

아래와 같이 커밋해야 할 사항이 생길 경우 `[!]` 로 이를 알리기도 합니다.

![](<../../.gitbook/assets/image (148).png>)

## 기타 기능

`starship`이 표시하는 사항이 어떤 의미인지 알고 싶다면 `starship explain` 을 입력해 해당 정보를 확인할 수도 있습니다.

![](<../../.gitbook/assets/image (225).png>)

`starship print-config` 를 입력하면 현재 `starship`의 설정 정보가 출력됩니다.

이를 통해 어떤 설정들이 적용된 상태인지 확인할 수 있습니다.

이러한 기본 설정에 원하는 설정을 추가하거나 수정하여 직접 자신의 프롬프트를 꾸밀 수 있습니다.

![](<../../.gitbook/assets/image (293).png>)
