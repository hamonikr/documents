# tmux (terminal multiplexer)

tmux는 터미널의 멀티플렉서로, 하나의 창에서 여러개의 터미널을 session, window, 그리고 pane 단위로 관리할 수 있도록 하는 도구입니다.

## Session <a href="#tmux-terminalmultiplexer-session" id="tmux-terminalmultiplexer-session"></a>

session은 tmux를 실행하는 기본 단위로, 여러개의 window로 구성됩니다.&#x20;

tmux session은 영구적이기 때문에 tmux에서 실행되는 프로그램은 연결이 끊어져도 계속 실행됩니다.

### session 생성하기 <a href="#tmux-terminalmultiplexer-session" id="tmux-terminalmultiplexer-session"></a>

터미널 창에서 `tmux` 를 입력하면 새로운 tmux session이 생성되고, 해당 세션에 접속됩니다.

![](<../../.gitbook/assets/image (311).png>)

위 이미지의 하단에 초록색 바탕으로 출력되는 창에서 현재 tmux session 정보를 출력합니다.

이후, `tmux ls` 를 입력하면 해당 세션이 "0"이라는 이름으로 생성되었고, 한개의 윈도우가 존재하며, 해당 세션에 attach된 상태인 것을 알 수 있습니다.

![](<../../.gitbook/assets/image (411).png>)

세션에 이름을 지정해 생성하고 싶다면 `tmux new -s [이름]` 을 입력합니다.

기존에 생성한 세션이 attached 상태이므로 해당 세션 내에서가 아닌 새로운 터미널 창을 열어 해당 명령어를 입력해야 합니다.

이후, `tmux ls`를 입력하면 지정한 이름으로 새로운 세션이 생성되었고, attach 된 것을 확인할 수 있습니다.

![](<../../.gitbook/assets/image (135).png>)

### session 중단하기 <a href="#tmux-terminalmultiplexer-session" id="tmux-terminalmultiplexer-session"></a>

현재 attached 상태인 세션을 detach하기 위해서는 `Ctrl+b` 키를 누른 후 `d` 를 누릅니다.

![](<../../.gitbook/assets/image (409).png>)

위와 같이 해당 세션에서 빠져나온 것을 확인할 수 있습니다.

이후 `tmux ls`를 입력하면 test 세션은 attached 상태가 아닌 것을 확인할 수 있습니다.

다시 test 세션을 시작하기 위해서는 `tmux attach -t test` 를 입력합니다.

### session 종료하기 <a href="#tmux-terminalmultiplexer-session" id="tmux-terminalmultiplexer-session"></a>

`tmux kill-session -t [세션 명]` 명령어를 통해 생성한 세션을 완전히 종료할 수 있습니다.

이후, `tmux ls` 를 입력하면 test 세션이 삭제된 것을 확인할 수 있습니다.

![](<../../.gitbook/assets/image (202).png>)

## Window <a href="#tmux-terminalmultiplexer-window" id="tmux-terminalmultiplexer-window"></a>

window는 하나의 터미널 화면으로, session 내에서 탭과 같이 사용됩니다.

다음과 같이 현재 "0" 세션에는 1개의 윈도우가 존재합니다.

![](<../../.gitbook/assets/image (366).png>)

### Window 생성하기 <a href="#tmux-terminalmultiplexer-window" id="tmux-terminalmultiplexer-window"></a>

Ctrl+b 를 누른 후 C 를 누르면 새로운 윈도우가 생성됩니다.

이후 `tmux ls`를 입력하면 다음과 같이 두개의 윈도우가 존재하는 것을 확인할 수 있습니다.

하단의 탭에서는 두번째 윈도우인 **1:bash** 뒤에 \* 표시가 붙어있어, 현재 해당 윈도우에 위치함을 알 수 있습니다.

![](<../../.gitbook/assets/image (227).png>)

### Window 이동하기 <a href="#tmux-terminalmultiplexer-window" id="tmux-terminalmultiplexer-window"></a>

다시 첫번째 윈도우인 0:bash로 이동하기 위해서 Ctrl+b 를 누른후 해당 윈도우의 이름인 "0" 을 누릅니다.

![](<../../.gitbook/assets/image (162).png>)

위와 같이 첫번째 윈도우로 이동한 것을 확인할 수 있습니다.

### WIndow 삭제하기 <a href="#tmux-terminalmultiplexer-window" id="tmux-terminalmultiplexer-window"></a>

현재 윈도우를 삭제하려면 `Ctrl+d`를 누릅니다.

![](<../../.gitbook/assets/image (189).png>)

위 이미지와 같이 첫번째 윈도우인 0:bash가 삭제된 것을 확인할 수 있습니다.

## Pane <a href="#tmux-terminalmultiplexer-pane" id="tmux-terminalmultiplexer-pane"></a>

tmux는  하나의 화면을 여러개로 분할해 사용하는 기능 또한 제공합니다.

이때, Pane은 하나의 터미널 화면인 window를 분할한 단위입니다.

### 화면 분할하기 <a href="#tmux-terminalmultiplexer" id="tmux-terminalmultiplexer"></a>

`Ctrl+b` 를 누른 후 `Shift+%` 키를 누르면 현재의 window가 세로로 분할됩니다.

![](<../../.gitbook/assets/image (320).png>)

`Ctrl+b` 를 누른 후 `Shift+"` 키를 누르면 해당 pane이 다시 가로로 분할됩니다.

![](<../../.gitbook/assets/image (407).png>)

### pane 이동하기 <a href="#tmux-terminalmultiplexer-pane" id="tmux-terminalmultiplexer-pane"></a>

현재 위치한 pane은 우측 하단의 pane입니다.

Ctrl+b 를 누른 후 방향키를 통해 pane을 이동할 수 있습니다.

Ctrl+b 를 누른 후 **상** 방향키를 눌러 우측 상단 pane으로 이동한 모습입니다.

![](<../../.gitbook/assets/image (166).png>)

Ctrl+b 를 누른 후 **좌** 방향키를 눌러 우측 상단 pane으로 이동한 모습입니다.

![](<../../.gitbook/assets/image (196).png>)

### pane 크기 조정하기 <a href="#tmux-terminalmultiplexer-pane" id="tmux-terminalmultiplexer-pane"></a>

`Ctrl+b` 키를 누른 상태에서 방향키를 통해 분할된 화면의 크기를 조절할 수 있습니다.

우측 하단 pane에서 `Ctrl+b+`**`상 방향키`** 를 눌러 틀의 크기를 늘린 모습입니다.

![](<../../.gitbook/assets/image (165).png>)

### pane 삭제하기 <a href="#tmux-terminalmultiplexer-pane" id="tmux-terminalmultiplexer-pane"></a>

`Ctrl+d` 키를 누르면 아래 이미지와 같이 현재 pane이 삭제됩니다.

![](<../../.gitbook/assets/image (153).png>)
