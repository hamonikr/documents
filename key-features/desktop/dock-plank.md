---
description: 하모니카OS의 바탕화면 독을 구성하는 프로그램
---

# 하단 메뉴바(dock) Plank

## Plank Dock?

"Plank"는 Linux 데스크톱 환경에서 사용되는 가벼운 도킹 애플리케이션입니다.

&#x20;Plank는 사용자가 자주 사용하는 애플리케이션 또는 폴더에 빠르게 액세스할 수 있도록 해주며,&#x20;

macOS의 독(Dock)과 유사한 기능을 제공합니다.



**Plank의 주요 특징은 다음과 같습니다:**

1. **간단한 설정**: Plank는 간단하고 미니멀한 설정 옵션을 제공합니다.
2. **자동 숨김**: 사용하지 않을 때 독을 자동으로 숨기는 기능을 제공합니다.
3. **테마 지원**: 다양한 테마를 적용하여 독의 모양을 사용자 지정할 수 있습니다.
4. **드래그 앤 드롭**: 애플리케이션 아이콘을 독에 드래그 앤 드롭하여 추가하거나 순서를 변경할 수 있습니다.



### 설치하기&#x20;

HamoniKR OS에서는 기본 프로그램으로 제공되고 있어 설치가 필요없습니다.&#x20;

### Ubuntu (>= 20.04), LinuxMint (>= 19.1)

```
wget -qO- https://pkg.hamonikr.org/add-hamonikr.apt | sudo -E bash -
sudo apt plank
```



### Plank 설정하기&#x20;

Albert (alt + space) 에  plank 또는 프로그램 메뉴에서 plank를 입력하면 plank와 plank Dock이 보여집니다.

( plank가 이미 실행된 상태라면 plank Dock를 통해 plank 설정이 가능합니다. )

<figure><img src="../../.gitbook/assets/4 (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/스크린샷, 2022-10-05 16-02-03.png" alt=""><figcaption></figcaption></figure>

### plank 설정 옵션

<figure><img src="../../.gitbook/assets/스크린샷, 2022-10-05 16-13-43.png" alt=""><figcaption></figcaption></figure>

테마 : 원하는 테마를 선택할 수 있습니다.

위치 : 화면 상에서 plank 위치를 설정합니다.&#x20;

정렬 : 위치를 정한 후 플랭크를 어느 방향에 위치시킬 것인지 설정합니다.

아이콘 크기 : 아이콘 크기를 설정합니다.

아이콘 줌 효과 : 아이콘 위에 마우스 오버 시 아이콘이 확대되는 효과를 설정합니다.&#x20;

### plank 동작 설정&#x20;

<figure><img src="../../.gitbook/assets/스크린샷, 2022-10-05 16-13-49.png" alt=""><figcaption></figcaption></figure>

Plank 숨기기 : Plank를 사용하지 않을 때 숨기는 방법을 설정합니다.

아이콘 관리 : Plank에 보여지는 아이콘을 설정합니다.



### 도크릿 설정&#x20;

<figure><img src="../../.gitbook/assets/스크린샷, 2022-10-05 16-13-53.png" alt=""><figcaption></figcaption></figure>

Plank에 위치시키고 싶은 아이콘을 더블클릭하면 해당 도크릿 Plank에 보여집니다.&#x20;

CPU 모니터 : plank에 위치시킨 후 아이콘에 마우스 오버 시 해당 PC의 CPU와 MEM이 표시됩니다.

바탕화면 : 아이콘을 클릭하면 바탕화면이 바로 보여집니다.

배터리 : 아이콘에 마우스 오버 시 배터리 잔량이 표시됩니다.

시계 : 시계 아이콘을 통한 시간 확인과, 아이콘 위에 마우스 오버 시 시간 확인이 가능합니다.??

클립보드 :   클립보드에 저장된 파일 확인이 가능합니다.

프로그램 : 아이콘에 마우스 우클릭을 하면 프로그램 목록이 보여지고 바로 실행이 가능합니다.

휴지통 : 아이콘을 클릭하면 휴지통이 보여집니다.&#x20;
