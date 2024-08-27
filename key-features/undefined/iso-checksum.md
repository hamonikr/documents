# ISO 파일 - checksum 확인

파일의 무결성 검증은 중요한 과정입니다. 특히 운영 체제 ISO 파일과 같이 큰 파일을 다운로드할 때 중간에 오류나 손상이 발생할 수 있기 때문에 체크섬을 통해 파일의 무결성을 확인하는 것이 좋습니다.



파일 체크섬을 하는 방법은 터미널에서 명령어로 확인을 할 수 있지만 HamoniKR OS에서는 파일 탐색기에서 파일 체크섬을 할 수 있는 기능을 제공하고 있습니다.&#x20;



### 파일탐색기에서 ISO 파일 체크섬하기.

iso 파일에서 마우스 우측 버튼을 클릭하고, "검증"을 선택합니다.&#x20;

<figure><img src="../../.gitbook/assets/image (516).png" alt=""><figcaption></figcaption></figure>

"ISO 검증" 창이 활성화되고 파일 체크섬을 자동으로 계산합니다.&#x20;

<figure><img src="../../.gitbook/assets/7 (7).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/8 (9).png" alt=""><figcaption></figcaption></figure>



터미널에서 ISO파일 체크섬하기.

```
$ sha5sum iso-file.iso
# 결과값 :
# 239a3ed3de39c67b05f1e2783cb1735501158d46faaef30ef0c27c89f4e9b4d  ./iso-file.iso
```





