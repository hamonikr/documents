# 백업 및 복구

하모니카 OS는 **Timeshift**, **Qt-fsarchiver**, 그리고 **Systemback**이라는 다양한 도구를 제공하여 사용자가 시스템 및 데이터를 안전하게 백업하고 복구할 수 있도록 지원합니다. 각 도구는 사용 목적과 특징이 다르므로 필요에 맞게 선택하여 사용할 수 있습니다.



|   **Timeshift**   |      시스템 설정 및 파일 스냅샷 생성      |  시스템 파일 및 설정  |    시스템 파일   |  O  |  쉬움 |
| :---------------: | :--------------------------: | :-----------: | :---------: | :-: | :-: |
| **Qt-fsarchiver** |     전체 디스크 또는 파티션 백업 및 복구    |  디스크/파티션 이미지  |    전체 시스템   |  O  |  중간 |
|   **Systemback**  | 시스템 및 사용자 데이터 백업 및 복구, 설치 지원 | 시스템 및 사용자 데이터 | 시스템/사용자 데이터 |  O  |  쉬움 |



## **Timeshift를 이용한 시스템 백업 및 복구**

**Timeshift 개요**

* **Timeshift**는 주로 시스템 설정 및 파일 백업에 사용되는 도구로, 스냅샷을 통해 쉽게 이전 상태로 복원할 수 있습니다.

**주요 사용 방법**

1. **설치 및 실행**: 하모니카 OS의 \*\*"시작 메뉴 > 관리 > Timeshift"\*\*에서 실행.
2. **스냅샷 생성**:
   * **백업 유형**: RSYNC 또는 BTRFS 중 선택.
   * **저장 위치**: 외장 드라이브 또는 로컬 디스크.
   * **일정 설정**: 자동 스냅샷 생성을 위한 일정 지정.
   * **"생성(Create)"** 버튼 클릭.
3. **복구**:
   * **스냅샷 선택** 후 **"복원(Restore)"** 클릭.
   * 재부팅 후 시스템 복구 완료.

{% content-ref url="startmenu/management/timeshift.md" %}
[timeshift.md](startmenu/management/timeshift.md)
{% endcontent-ref %}

## **Qt-fsarchiver를 이용한 전체 디스크 및 파티션 백업**

**Qt-fsarchiver 개요**

* 디스크 또는 특정 파티션을 백업하고 복원할 수 있는 GUI 기반 도구입니다. 전체 시스템 복원이 필요한 상황에서 유용합니다.

**주요 사용 방법**

1. **설치 및 실행**: \*\*"시작 메뉴 > 관리 > Qt-fsarchiver"\*\*에서 실행.
2. **백업 생성**:
   * **"Save partition"** 메뉴 선택.
   * 백업할 디스크/파티션 및 저장 경로 지정.
   * **"Start"** 클릭으로 백업 진행.
3. **복구**:
   * **"Restore partition"** 메뉴 선택.
   * 백업 파일 및 대상 디스크 선택 후 복원 시작.

{% content-ref url="key-features/undefined-1/qt-fsarchive.md" %}
[qt-fsarchive.md](key-features/undefined-1/qt-fsarchive.md)
{% endcontent-ref %}

## **Systemback을 이용한 시스템 백업 및 복구**

**Systemback 개요**

* **Systemback**은 시스템 및 사용자 데이터의 백업과 복원을 모두 지원하며, 시스템 설치 및 재설정 기능도 제공합니다.

**주요 사용 방법**

1. **설치 및 실행**: 하모니카 OS의 \*\*"추천 소프트웨어 > Systemback"\*\*에서 실행.
2. **백업 생성**:
   * **"Create New Backup"** 메뉴 선택.
   * 백업할 디렉토리 및 설정 지정.
   * **"Create New"** 버튼 클릭.
3. **복구**:
   * \*\*"Restore Points"\*\*에서 복원 지점 선택.
   * **"Restore System"** 클릭 후 재부팅.

{% content-ref url="recommendation/systemback.md" %}
[systemback.md](recommendation/systemback.md)
{% endcontent-ref %}
