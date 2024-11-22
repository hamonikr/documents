---
description: GIt 저장소에서 불필요하거나 민감한 데이터를 빠르게 제거하는데 사용하기 좋은 도구.
---

# BFG Repo-Cleaner

### BFG Repo-Cleaner이란.

Git 저장소에서 불필요하거나 민감한 데이터를 빠르게 제거하는 데 사용되는 도구입니다.&#x20;

대형 파일, 암호, 토큰, API 키와 같은 민감한 데이터가 과거의 커밋에 포함되어 있을 때, 이를 제거하기 위해 BFG Repo-Cleaner를 사용할 수 있습니다.

BFG는 `git filter-branch`와 유사한 작업을 수행하지만, 특히 대형 저장소에서는 훨씬 빠르게 동작합니다.



#### 주요 특징은 다음과 같습니다:

* 속도: BFG는 git-filter-branch보다 10\~720배 빠릅니다.
* 간단함: 특정 작업에 중점을 둬서 사용하기 쉽습니다.



### BFG Repo-Cleaner 설치하기

```
$ sudo apt-get update 또는 apu ( zsh alias )
$ sudo apt-get install -y bfg 또는 api bfg 
```

### BFG Repo-Cleaner 사용법

[**저장소 클론:**](https://github.com/hamonikr/bfg#%EC%A0%80%EC%9E%A5%EC%86%8C-%ED%81%B4%EB%A1%A0)

```
# bfg 명령어로 깃허브 리포지토리 복사합니다. 
$ bfg --clone https://github.com/example/repo.git

# 클론이 완료되면 해당 리포지토리 명으로 폴더가 생성됩니다. 
# ex) rego.git

```

[**큰 파일 찾기 (예: 10MB 이상):**](https://github.com/hamonikr/bfg#%ED%81%B0-%ED%8C%8C%EC%9D%BC-%EC%B0%BE%EA%B8%B0-%EC%98%88-10mb-%EC%9D%B4%EC%83%81)

```
# 리포지토리에서 큰 파일을 찾습니다. 
# ex) bfg --find-big-files 10M rego.git
$ bfg --find-big-filess 10M <PREPO_ATH>

```

[**큰 파일 삭제 (예: 100MB 이상):**](https://github.com/hamonikr/bfg#%ED%81%B0-%ED%8C%8C%EC%9D%BC-%EC%82%AD%EC%A0%9C-%EC%98%88-100mb-%EC%9D%B4%EC%83%81)

```
# 리포지토리에서 큰 파일을 삭제합니다.
# ex) bfg --remove-big-files 10M rego.git

bfg --remove-big-files 100M <PREPO_ATH>
```

[**변경 내용 원격 저장소에 푸시:**](https://github.com/hamonikr/bfg#%EB%B3%80%EA%B2%BD-%EB%82%B4%EC%9A%A9-%EC%9B%90%EA%B2%A9-%EC%A0%80%EC%9E%A5%EC%86%8C%EC%97%90-%ED%91%B8%EC%8B%9C)

```
# 정리한 리포지토리를 원격 저장소에 푸시합니다. 
# ex) bfg --push rego.git

bfg --push <PREPO_ATH>
```

[**모든 작업을 한 번에 수행:**](https://github.com/hamonikr/bfg#%EB%AA%A8%EB%93%A0-%EC%9E%91%EC%97%85%EC%9D%84-%ED%95%9C-%EB%B2%88%EC%97%90-%EC%88%98%ED%96%89)

```
./bfg --clone https://github.com/example/repo.git --remove-big-files 100 --push
```



