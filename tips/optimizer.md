# 속도 최적화 및 디스크 정리

#### Speed Up your Mint <a href="#id-speedupyourmint" id="id-speedupyourmint"></a>

[https://easylinuxtipsproject.blogspot.com/p/speed-mint.html](https://easylinuxtipsproject.blogspot.com/p/speed-mint.html)

[https://easylinuxtipsproject.blogspot.com/p/ssd.html#ID12](https://easylinuxtipsproject.blogspot.com/p/ssd.html#ID12)

여러가지 방법이 링크에 제시되어 있지만 하모니카 리눅스에서 사용해볼만한 방법은 아래의 내용입니다.

### preload 설치 <a href="#id-preload" id="id-preload"></a>

sudo apt-get install preload

### apt-fast 설치 <a href="#id-apt-fast" id="id-apt-fast"></a>

sudo add-apt-repository ppa:apt-fast/stable

sudo apt-get update

sudo apt-get install apt-fast

### 파이어폭스 설정 변경 <a href="#id" id="id"></a>

### Limiting the disk write actions of Firefox <a href="#id-limitingthediskwriteactionsoffirefox" id="id-limitingthediskwriteactionsoffirefox"></a>

7\. By default, Firefox writes a lot to the hard disk. This reduces its speed. You can limit the disk write actions of Firefox, by putting the Firefox network cache into the RAM and by disabling sessionstore. Like this:\
\


#### Putting the Firefox network cache into the RAM <a href="#id-puttingthefirefoxnetworkcacheintotheram" id="id-puttingthefirefoxnetworkcacheintotheram"></a>

7.1. By moving the Firefox network cache from your hard disk to the RAM, you diminish the amount of disk writes. This'll probably make your Firefox noticeably faster. The price you pay is small: it'll only "cost" you 200 MB of your RAM.\
\
_**Note:**_ don't do this when your computer has less than 2 GB of RAM! Because with very little RAM, even 200 MB can't be missed.\
\
Proceed like this:\
\
a. Type in the URL bar of Firefox:\
about:config\
Press Enter.\
\
b. Now you're being presented with a warning. Ignore it and click on the button "I accept the risk!".\
\
c. [Copy/paste](https://easylinuxtipsproject.blogspot.com/p/copy-paste.html) the following into the filter bar (search bar):\
browser.cache.disk.enable\
Toggle its value to **false** by double-clicking it: this will disable "cache to disk" entirely.\
\
d. Now you're going to make sure that "cache to RAM" is enabled. [Copy/paste](https://easylinuxtipsproject.blogspot.com/p/copy-paste.html) the following into the filter bar (search bar):\
browser.cache.memory.enable\
This should already be set to **true**; if not, toggle it to true by double-clicking it.\
\
e. Then you're going to determine how much memory can be used as RAM cache. [Copy/paste](https://easylinuxtipsproject.blogspot.com/p/copy-paste.html) this into the filter bar (search bar):\
browser.cache.memory.capacity\
You'll probably won't find an existing instance. If (as expected) nothing was found, create it like this:\
\
_**Right-**_click on the blank area in Firefox, then select New - Integer.\
Make this the **preference name**:\
browser.cache.memory.capacity\
Enter the **integer value** in KB; I advise 204800 (which equals 200 MB). That's usually more than enough.\
\
f. Close Firefox and launch it again. You're done! Check it like this:\
\
Type in the URL bar:\
**about:cache**\
Press Enter.\
\
By the way: you'll then also see a mention of an "appcache" which is still present on the disk, but there's no need to move that (much less frequently used) cache to the RAM as well.\
\
_**Note:**_ This is a user preference. Repeat this hack in each user account.\
\


#### Disabling sessionstore <a href="#id-disablingsessionstore" id="id-disablingsessionstore"></a>

7.2. Firefox has a session restore feature, which remembers what pages were opened if Firefox experiences an unexpected shutdown (read: crashes). This feature is neat, but causes many disk writes. Disable it like this:\
\
a. Type in the URL bar of Firefox:\
\
about:config\
\
Press Enter.

\
\
b. Now you're being presented with a warning. Ignore it and click on the button "I accept the risk!".\
\
c. Type in the filter bar: sessionstore\
\
c. Double-click on the item called **browser.sessionstore.interval**. The default interval is **15000**, which means 15 seconds. Add three zeros to the existing value, so that it becomes: **15000000** and click the OK button.\
\
d. Close Firefox and launch it again. Now you've practically disabled the session restore feature.\
\
_**Note (1):**_ Leave the other cache and sessionstore settings as they are: usually, the less invasive a hack is, the better. Because this reduces the risk of unexpected unwanted side effects.\
\
_**Note (2):**_ This is a user preference. Repeat this hack in each user account.\
\


### Firefox: optimize the Places database from time to time <a href="#id-firefox-optimizetheplacesdatabasefromtimetotime" id="id-firefox-optimizetheplacesdatabasefromtimetotime"></a>

8\. In your Firefox profile there's an sqlite database called Places, which after a while starts resembling a swollen Swiss cheese with holes. That might slow your Firefox down.\
\
You can speed your Firefox up a bit, by optimizing (vacuuming) that database: you can namely deflate that swollen Swiss cheese into a compact smaller cheese. As follows:\
\
Type the following _**in the URL bar**_ of Firefox:\
\
about:support\
\
Press Enter.\
\
Almost at the bottom of the page you get to see then, there's a header called Places Database. Click there on the button called Verify Integrity.\
\
You're done! Repeat this on a monthly basis, so that your Firefox won't lose speed again because of a swollen database.

## 다스크 용량이 부족한 경우 안전하게 정리하는 방법 <a href="#id" id="id"></a>

### How to Clean Linux Mint Safely <a href="#id-howtocleanlinuxmintsafely" id="id-howtocleanlinuxmintsafely"></a>

[https://easylinuxtipsproject.blogspot.com/p/clean-mint.html](https://easylinuxtipsproject.blogspot.com/p/clean-mint.html)
