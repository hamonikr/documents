---
description: 터미널에서 전 세계와 빠르게 파일 공유
---

# remote-share-cli (easy file share to remote)

## remote-share-cli란?

remote-share-cli는 전 세계적으로 엑세스 가능한 프로그램입니다. stdin 또는 주어진 파일에서 https를 통해 단일 파일을 인터넷에 노출한 뒤 노출 주소가 자동으로 클립보드에 복사됩니다..?&#x20;

더 자세한 정보는 [https://github.com/marionebl/remote-share-cli](https://github.com/marionebl/remote-share-cli) 에서 확인할 수 있습니다.&#x20;



### remote-share-cli 설치하기.

```
npm install -g remote-share-cli
```

### remote-share-cli 사용하기.

```
 $ remote-share --help

  Quickly share files from command line with the world

  Usage
    $ remote-share [file]

  Options
    -n, --name Forced download name of the file

  Examples
    $ remote-share shared.png
    https://mysteriouswomen.localtunnel.me

    $ cat shared.png | remote-share --name=shared.png
    https://humbleappliance.localtunnel.me
```
