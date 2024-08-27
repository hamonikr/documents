# 하모니카 CLI tools

## hamonikr-cli-tools

`hamonikr-cli-tools` 는 하모니카OS에서 사용할 수 있는 유용한 CLI 프로그램을 설치하는 패키지입니다.

이 패키지는 CLI 에서 사용할 수 있는 아래와 같은 프로그램을 포함하고 있습니다.

### 포함 패키지

* [icdiff (color diff)](icdiff-color-diff.md)
* jq (json parser)
* [D2Coding Regular font (Korean font)](d2coding-regular-font-korean-font.md)
* remote-share-cli (easy file share to remote)
* [hamonikr-ff (fzf and bat features)](../../key-features/hamonikr-tui/hamonikr-ff-fzf-and-bat-features.md)
* speedtest-cli (network speed benchmark)
* w3m (terminal web browser)
* mtr (traceroute) : ex) mtr -t
* network-manager nmtui (network setting tui)
* systemd-tui (systemd service management tui)
* ncdu (disk usage analysis)
* [mc (terminal file manager)](mc-terminal-file-manager.md)
* [tldr (manual for command)](tldr-manual-for-command.md)
* [fsarchiver (partition backup and restore)](../../key-features/undefined-1/fsarchiver-partition-backup-and-restore.md)
* [starship (mordern prompt for shell)](starship-mordern-prompt-for-shell.md)
* [htop (process viewer)](htop-process-viewer.md)
* [glances (system monitoring tool)](glances-system-monitoring-tool.md)
* [lazydocker (TUI for both docker and docker-compose)](lazydocker-tui-for-both-docker-and-docker-compose.md)
* [tmux (terminal multiplexer)](tmux-terminal-multiplexer.md)
* [ttyd (Share terminal over the web) : ex) ttyd htop](ttyd-share-terminal-over-the-web.md)
* [aria2 (download utility - HTTP/HTTPS, FTP, SFTP, BitTorrent, Metalink)](aria2-download-utility-http-https-ftp-sftp-bittorrent-metalink.md)
* [asciinema (Record and share terminal sessions)](asciinema-record-and-share-terminal-sessions.md)
* [neofetch (show system infomation)](neofetch-show-system-infomation.md)
* [s-search (web-search-cli)](s-search-web-search-cli.md)

## **hamonikr-cli-tools** 설치하기

**HamoniKR(>=4.0)** 사용자는 아래 명령어로 프로그램을 설치할 수 있습니다.

```
$ sudo apt update
$ sudo apt install hamonikr-cli-tools
```

**Ubuntu, LinuxMint (>=Ubuntu 20.04)** 사용자는 아래 명령어로 프로그램을 설치할 수 있습니다.

```
$ wget -qO- https://pkg.hamonikr.org/add-hamonikr.apt | sudo -E bash -
$ sudo apt install hamonikr-cli-tools
```

{% hint style="info" %}
&#x20;프로젝트의 소스코드와 빌드 방법은 [Github 레포지토리](https://github.com/hamonikr/hamonikr-cli-tools)에서 확인하실 수 있습니다.
{% endhint %}

hamonikr-cli-tools 삭제 방법:

```bash
$ sudo apt purge -y hamonikr-cli-tools
$ sudo apt -y autoremove
```

