# 유튜브, Vimeo 동영상 파일 저장하기 - ClipGrab

유튜브 같은 동영상 공유 사이트들을 보고 있다 보면 마음에 드는 영상들을 자신의 PC로 다운로드 받고 싶을 때가 있습니다. 이럴 때 유용하게 사용할 수 있는 소프트웨어가 있습니다. 바로 ClipGrab 이라는 소프트웨어 입니다. 이번에는 저의 리눅스 민트에 설치를 해 볼거라 포스팅의 제목에 리눅스라는 단서를 붙였지만 ClipGrab은 윈도우, 맥, 리눅스를 모두 지원 합니다. 고로 설치법만 조금씩 차이가 있을 뿐이지 모든 OS에서 사용이 가능 합니다. 어쨋든 지금은 리눅스 버전을 설치하고 사용하는 방법에 대해서 알아보겠습니다.

다른 OS 버전으로 다운로드 받으시려면 아래의 링크에서 OS에 맞게 다운로드 받아서 사용하시면 됩니다.

■ ClipGrab 다운로드 (Windows , Mac OS X)\


[http://clipgrab.org/](http://clipgrab.org/) 에 들어가서 'Show all download options' 를 클릭하시면 됩니다.

리눅스의 경우는 터미널을 열고 아래의 명령어로 설치하면 됩니다. ClipGrab 은 소프트웨어 관리자에서 검색이 되지 않네요. \


■ ClipGrab 설치, ClipGrab 저장소를 추가해주고 설치\


sudo add-apt-repository ppa:clipgrab-team/ppa\
sudo apt-get update\
sudo apt-get install clipgrab

![](<../.gitbook/assets/image (336).png>)

설치가 끝나면 저렇게 인터넷 분류에 ClipGrab 이 들어가 있습니다. \


![](<../.gitbook/assets/image (377).png>)

우선 유튜브에 들어가서 마음에 드는 동영상을 찾아야 합니다. 저는 제가 좋아하는 토마스와 친구들 동영상을 하나 골랐습니다. ^^;  그리고 동영상의 주소를 복사 합니다.\


![](<../.gitbook/assets/image (198).png>)

ClipGrab을 실행하고 Downloads 탭을 누르고 위와 같이 URL 입력창에 붙여넣기 해 줍니다. 그리고 다운로드 받고 변환할 Format 을 지정해 줍니다. 보통 동영상은 MP4 를 많이 선택하죠. 여기서 중요한 것이 동영상이 아니라 음원만 추출도 가능 합니다. 어떤 가수의 뮤직비디오를 하나 고르고 저장 포맷을 MP3 로 지정하면 음원만 추출이 되어서 MP3 플레이어나 스마트폰에 넣어서 들을 수 있는 것이죠. 포맷을 골랐으면 저장할 영상의 품질을 골라 줍니다. 당연히 유튜브에 올라와 있는 화질보다 좋게는 저장이 안됩니다. 이렇게 포맷과 화질을 선택하고 'Grab this Clip!' 을 클릭합니다.\


![](<../.gitbook/assets/image (367).png>)

'Grab this Clip!' 을 클릭하면 파일을 저장할 위치를 선택합니다.\


![](<../.gitbook/assets/image (208).png>)

잠시 후 다운로드가 완료 됩니다.\


![](<../.gitbook/assets/image (327).png>)

제가 선택한 동영상이 다운로드 폴더에 잘 저장이 되었네요.\


![](<../.gitbook/assets/image (425).png>)

VLC 플레이어로 플레이 해 봤습니다. 잘 나옵니다. 이렇게 좋아하는 동영상 들을 스마트폰에 복사해서 가지고 다니면 데이터 걱정 없이 볼 수 있겠네요.\


![](<../.gitbook/assets/image (315).png>)

ClipGrab의 장점이 유튜브 뿐만 아니라 다양한 동영상 공유 사이트들을 지원한다는 것입니다. 현재 지원하는 사이트는 [YouTube](https://www.youtube.com/), [Vimeo](https://vimeo.com/), [Dailymotion](http://www.dailymotion.com/kr), [metacafe.com](http://www.metacafe.com/), [youku.com](http://www.youku.com/), [myspass.de](http://www.myspass.de/), [myvideo.de](http://myvideo.de/), [clipfish.de](http://www.clipfish.de/) 등이 있습니다. 이번엔 Vimeo 사이트에서 다운로드 해 봤습니다. 같은 방법으로 Vimeo 에서 마음에 드는 동영상을 찾아서 주소창에서 URL을 복사해서 ClipGrab 에 붙여넣기 하면 됩니다.\


![](<../.gitbook/assets/image (371).png>)

URL을 붙여넣고 포맷, 품질을 선택하고 Grab this clip! 을 클릭하고 저장할 폴더를 지정 합니다. 유튜브의 경우와 사용법은 같습니다. 다운로드가 잘 되었습니다.\


![](<../.gitbook/assets/image (168).png>)

토마스와 함께 Vimeo 에서 다운로드 한 강남스타일도 다운로드 폴더에 잘 들어가 있습니다.

ClipGrab은 동영상 수집하기에 참 괜찮은 소프트웨어 같습니다. 사용법도 간단하구요. 이상으로 동영상 다운로드 소프트웨어 ClipGrab 소개를 마칩니다

\
\
출처: [http://deneb21.tistory.com/376](http://deneb21.tistory.com/376)
