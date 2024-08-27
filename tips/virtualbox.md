# VirtualBox 사용하기

윈도우가 필요한 경우 VirtualBox와 윈도우 무료 이미지를 이용하여 90일간 사용가능하다.

* VirtualBox 다운로드 : [https://download.virtualbox.org/virtualbox/6.0.10/virtualbox-6.0\_6.0.10-132072\~Ubuntu\~bionic\_amd64.deb](https://download.virtualbox.org/virtualbox/6.0.10/virtualbox-6.0\_6.0.10-132072\~Ubuntu\~bionic\_amd64.deb)
* VirtualBox 확장기능 다운로드 : [https://download.virtualbox.org/virtualbox/6.0.10/Oracle\_VM\_VirtualBox\_Extension\_Pack-6.0.10.vbox-extpack](https://download.virtualbox.org/virtualbox/6.0.10/Oracle\_VM\_VirtualBox\_Extension\_Pack-6.0.10.vbox-extpack)
* 윈도우 가상머신 이미지 (win 7 + ie11) 다운로드 : [https://az792536.vo.msecnd.net/vms/VMBuild\_20180102/VirtualBox/IE11/IE11.Win7.VirtualBox.zip](https://az792536.vo.msecnd.net/vms/VMBuild\_20180102/VirtualBox/IE11/IE11.Win7.VirtualBox.zip)

3개의 파일을 모두 다운로드 받아서 저장 (가상머신 이미지는 용량이 4.7G 정도)

## VirtualBox 설치 후 오류가 나는 경우 아래와 같이 권한을 변경 <a href="#id-6" id="id-6"></a>

$ sudo chown root:root /usr/lib/virtualbox

$ sudo chown root:root /usr/lib/

$ sudo chown root:root /usr

## VirtualBox CLI 제어 <a href="#id-6-cli" id="id-6-cli"></a>

* 참고문서 : [https://www.oracle.com/technical-resources/articles/it-infrastructure/admin-manage-vbox-cli.html](https://www.oracle.com/technical-resources/articles/it-infrastructure/admin-manage-vbox-cli.html)

가상머신 목록확인

$ vboxmanage list vms

가상머신 구동

$ vboxmanage start win10pe

가상머신 종료

$ vboxmanage shutdown win10pe

[https://www.techrepublic.com/article/how-to-run-virtualbox-virtual-machines-from-the-command-line/](https://www.techrepublic.com/article/how-to-run-virtualbox-virtual-machines-from-the-command-line/)

Say we want to run the "Ubuntu Server" VM as a headless instance. To do this, you would issue the command:

```
VBoxManage startvm "Ubuntu Server" --type headless
```

The VM will start up and hand you back your bash prompt. Your virtual server (if that's how you're using the VM) is now available to you.

If you need to pause that VM, issue the command:

```
VBoxManage controlvm "Ubuntu Server" pause --type headless
```

To restart that paused VM, issue the command:

```
VBoxManage controlvm "Ubuntu Server" resume --type headless
```

To shut down the VM, issue the command:

```
VBoxManage controlvm "Ubuntu Server" poweroff --type headless
```
