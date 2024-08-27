# ffmpeg 사용법 - 동영상에서 음성추출하기, 동영상 변환

하모니카에서는 기본으로 제공되는 ffmpeg 를 이용하여 아래와 같이 다양한 미디어 편집작업이 가능합니다.

* [Converting Audio into Different Formats / Sample Rates](ffmpeg.md#ffmpeg사용법-동영상에서음성추출하기,동영상변환-ConvertingAudiointoDifferentFormats/SampleRates)
* [Extract Audio](ffmpeg.md#ffmpeg사용법-동영상에서음성추출하기,동영상변환-ExtractAudio)
* [Replace Audio on a Video without re-encoding.](ffmpeg.md#ffmpeg사용법-동영상에서음성추출하기,동영상변환-ReplaceAudioonaVideowithoutre-encoding.)
* [Extract Single Image from a Video at Specified Frame](ffmpeg.md#ffmpeg사용법-동영상에서음성추출하기,동영상변환-ExtractSingleImagefromaVideoatSpecifiedFrame)
* [Merge Multiple Videos](ffmpeg.md#ffmpeg사용법-동영상에서음성추출하기,동영상변환-MergeMultipleVideos)
* [Split a Video into Images](ffmpeg.md#ffmpeg사용법-동영상에서음성추출하기,동영상변환-SplitaVideointoImages)
* [Convert Images into a Video](ffmpeg.md#ffmpeg사용법-동영상에서음성추출하기,동영상변환-ConvertImagesintoaVideo)
* [Convert Single Image into a Video](ffmpeg.md#ffmpeg사용법-동영상에서음성추출하기,동영상변환-ConvertSingleImageintoaVideo)
* [Convert non-sequentially named Images in a directory](ffmpeg.md#ffmpeg사용법-동영상에서음성추출하기,동영상변환-Convertnon-sequentiallynamedImagesinadirectory)
* [Convert .mov (JPEG-A or other codec) to H264 .mp4](ffmpeg.md#ffmpeg사용법-동영상에서음성추출하기,동영상변환-Convert.mov\(JPEG-Aorothercodec\)toH264.mp4)
* [Convert mp4 to webm](ffmpeg.md#ffmpeg사용법-동영상에서음성추출하기,동영상변환-Convertmp4towebm)
* [Simple FLAC convert](ffmpeg.md#ffmpeg사용법-동영상에서음성추출하기,동영상변환-SimpleFLACconvert)
* [Mix Stereo to Mono](ffmpeg.md#ffmpeg사용법-동영상에서음성추출하기,동영상변환-MixStereotoMono)
* [Trim End of file (mp3)](ffmpeg.md#ffmpeg사용법-동영상에서음성추출하기,동영상변환-TrimEndoffile\(mp3\))
* [To Encode or Re-encode ?](ffmpeg.md#ffmpeg사용법-동영상에서음성추출하기,동영상변환-ToEncodeorRe-encode?)
  *
    * [use ffmpeg cut mp4 video without re-encoding](ffmpeg.md#ffmpeg사용법-동영상에서음성추출하기,동영상변환-useffmpegcutmp4videowithoutre-encoding)
    * [use ffmpeg cut mp4 video with re-encoding](ffmpeg.md#ffmpeg사용법-동영상에서음성추출하기,동영상변환-useffmpegcutmp4videowithre-encoding)
    * [reduce filesize](ffmpeg.md#ffmpeg사용법-동영상에서음성추출하기,동영상변환-reducefilesize)
  * [Convert MKV to MP4](ffmpeg.md#ffmpeg사용법-동영상에서음성추출하기,동영상변환-ConvertMKVtoMP4)
  * [Add Watermark overlay (png) to the center of a video](ffmpeg.md#ffmpeg사용법-동영상에서음성추출하기,동영상변환-AddWatermarkoverlay\(png\)tothecenterofavideo)

## Converting Audio into Different Formats / Sample Rates <a href="#ffmpeg-convertingaudiointodifferentformats-samplerates" id="ffmpeg-convertingaudiointodifferentformats-samplerates"></a>

Minimal example: transcode from MP3 to WMA:\
`ffmpeg -i input.mp3 output.wma`

You can get the list of supported formats with:\
`ffmpeg -formats`

Convert WAV to MP3, mix down to mono (use 1 audio channel), set bit rate to 64 kbps and sample rate to 22050 Hz:\
`ffmpeg -i input.wav -ac 1 -ab 64000 -ar 22050 output.mp3`

Convert any MP3 file to WAV 16khz mono 16bit:\
`ffmpeg -i 111.mp3 -acodec pcm_s16le -ac 1 -ar 16000 out.wav`

Convert any MP3 file to WAV 20khz mono 16bit for ADDAC WAV Player:\
`ffmpeg -i 111.mp3 -acodec pcm_s16le -ac 1 -ar 22050 out.wav`\
cd into dir for batch process:\
`for i in *.mp3; do ffmpeg -i "$i" -acodec pcm_s16le -ac 1 -ar 22050 "${i%.mp3}-encoded.wav"; done`

Picking the 30 seconds fragment at an offset of 1 minute:\
In seconds\
`ffmpeg -i input.mp3 -ss 60 -t 30 output.wav`

In HH:MM:SS format\
`ffmpeg -i input.mp3 -ss 0:01:00 -t 0:00:30 output.wav`

Split an audio stream at specified segment rate (e.g. 3 seconds)\
`ffmpeg -i somefile.mp3 -f segment -segment_time 3 -c copy out%03d.mp3`

## Extract Audio <a href="#ffmpeg-extractaudio" id="ffmpeg-extractaudio"></a>

`ffmpeg -i input-video.avi -vn -acodec copy output-audio.aac`

`vn` is no video.\
`acodec` copy says use the same audio stream that's already in there.

`ffmpeg -i video.mp4 -f mp3 -ab 192000 -vn music.mp3`

The -i option in the above command is simple: it is the path to the input file. The second option -f mp3 tells ffmpeg that the ouput is in mp3 format. The third option i.e -ab 192000 tells ffmpeg that we want the output to be encoded at 192Kbps and -vn tells ffmpeg that we dont want video. The last param is the name of the output file.

## Replace Audio on a Video without re-encoding. <a href="#ffmpeg-replaceaudioonavideowithoutre-encoding." id="ffmpeg-replaceaudioonavideowithoutre-encoding."></a>

strip audio stream away from video\
`ffmpeg -i INPUT.mp4 -codec copy -an OUTPUT.mp4`

combine the two streams together (new audio with originally exisiting video)\
`ffmpeg -i 36.MOV -i 36.wav -map 0:v -map 1:a -c copy -y 36-encoded.mov`\
or add an offset to audio\
`ffmpeg -i 36.MOV -itsoffset -0.25 -i 36.wav -map 0:v -map 1:a -c copy -y 36-encoded.mov`\
or\
`ffmpeg -i INPUT.mp4 -i AUDIO.wav -shortest -c:v copy -c:a aac -b:a 256k OUTPUT.mp4`

You say you want to "extract audio from them (mp3 or ogg)". But what if the audio in the mp4 file is not one of those? you'd have to transcode anyway. So why not leave the audio format detection up to ffmpeg?

To convert one file:

`ffmpeg -i videofile.mp4 -vn -acodec libvorbis audiofile.ogg`

To convert many files:

`for vid in *.mp4; do ffmpeg -i "$vid" -vn -acodec libvorbis "${vid%.mp4}.ogg"; done`

You can of course select any ffmpeg parameters for audio encoding that you like, to set things like bitrate and so on.

Use `-acodec libmp3lame` and change the extension from `.ogg` to `.mp3` for mp3 encoding.

If what you want is to really extract the audio, you can simply "copy" the audio track to a file using -acodec copy. Of course, the main difference is that transcoding is slow and cpu-intensive, while copying is really quick as you're just moving bytes from one file to another. Here's how to copy just the audio track (assuming it's in mp3 format):

`ffmpeg -i videofile.mp4 -vn -acodec copy audiofile.mp3`

Note that in this case, the audiofile format has to be consistent with what the container has (i.e. if the audio is AAC format, you have to say audiofile.aac). You can use the ffprobe command to see which formats you have, this may provide some information:

`for file in *; do ffprobe $file 2>&1 |grep Audio; done`

A possible way to automatically parse the audio codec and name the audio file accordingly would be:

`for file in *mp4 *avi; do ffmpeg -i "$file" -vn -acodec copy "$file".`ffprobe "$file" 2>&1 |sed -rn 's/._Audio: (...), ._/\1/p'`; done`

Note that this command uses sed to parse output from ffprobe for each file, it assumes a 3-letter audio codec name (e.g. mp3, ogg, aac) and will break with anything different.

Encoding multiple files

You can use a Bash "for loop" to encode all files in a directory:

`$ mkdir newfiles`\
`$ for f in *.m4a; do ffmpeg -i "$f" -codec:v copy -codec:a libmp3lame -q:a 2 newfiles/"${f%.m4a}.mp3"; done`

`ffmpeg -i input.m4a -acodec libmp3lame -ab 128k output.mp3`\
m4a to mp3 conversion with ffmpeg and lame

A batch file version of the same command would be:\
`for f in *.m4a; do ffmpeg -i "$f" -acodec libmp3lame -ab 256k "${f%.m4a}.mp3"; done`

## Extract Single Image from a Video at Specified Frame <a href="#ffmpeg-extractsingleimagefromavideoatspecifiedframe" id="ffmpeg-extractsingleimagefromavideoatspecifiedframe"></a>

`$ vf [ss][filename][outputFileName]`\
where `vf` is a custom bash script as follows:\
`$ ffmpeg -ss $1 -i $2 -qmin 1 -q:v 1 -qscale:v 2 -frames:v 1 -huffman optimal $3.jpg`\
\
ss offset = frame number divided by FPS of video = the decimal (in milliseconds) ffmpeg needs i.e. 130.5

## Merge Multiple Videos <a href="#ffmpeg-mergemultiplevideos" id="ffmpeg-mergemultiplevideos"></a>

file names in folder, if they contain spaces, must be properly escaped\
`ls * | perl -ne 'print "file $_"' | ffmpeg -f concat -i - -c copy merged.mp4`

## Split a Video into Images <a href="#ffmpeg-splitavideointoimages" id="ffmpeg-splitavideointoimages"></a>

`$ ffmpeg -i video.flv image%d.jpg`

## Convert Images into a Video <a href="#ffmpeg-convertimagesintoavideo" id="ffmpeg-convertimagesintoavideo"></a>

`$ ffmpeg -f image2 -i image%d.jpg imagestovideo.mp4`\
`$ ffmpeg -i image-%03d.png -c:v libx264 -pix_fmt yuv420p test.mp4`\
`$ ffmpeg -r 1/5 -i image-%03d.png -c:v libx264 -vf fps=25 -pix_fmt yuv420p test.mp4`

## Convert Single Image into a Video <a href="#ffmpeg-convertsingleimageintoavideo" id="ffmpeg-convertsingleimageintoavideo"></a>

`$ ffmpeg -loop 1 -i image.png -c:v libx264 -t 60 -pix_fmt yuv420p -vf scale=1920:1080 out.mp4`

## Convert non-sequentially named Images in a directory <a href="#ffmpeg-convertnon-sequentiallynamedimagesinadirectory" id="ffmpeg-convertnon-sequentiallynamedimagesinadirectory"></a>

`$ ffmpeg -framerate 30 -pattern_type glob -i '*.jpeg' -c:v libx264 -pix_fmt yuv420p gan-1.mov`

## Convert .mov (JPEG-A or other codec) to H264 .mp4 <a href="#ffmpeg-convert.mov-jpeg-aorothercodec-toh264.mp4" id="ffmpeg-convert.mov-jpeg-aorothercodec-toh264.mp4"></a>

`ffmpeg -i input.mov -vcodec libx264 -pix_fmt yuv420p output.mp4`

## Convert mp4 to webm <a href="#ffmpeg-convertmp4towebm" id="ffmpeg-convertmp4towebm"></a>

`$ ffmpeg -i example.mp4 -f webm -c:v libvpx -b:v 1M -acodec libvorbis example.webm -hide_banner`\
[more info](http://www.bugcodemaster.com/article/convert-videos-webm-format-using-ffmpeg)

## Simple FLAC convert <a href="#ffmpeg-simpleflacconvert" id="ffmpeg-simpleflacconvert"></a>

`ffmpeg -i audio.xxx -c:a flac audio.flac`

## Mix Stereo to Mono <a href="#ffmpeg-mixstereotomono" id="ffmpeg-mixstereotomono"></a>

You can modify a video file directly without having to re-encode the video stream. However the audio stream will have to be re-encoded.\
Left channel to mono: `ffmpeg -i video.mp4 -map_channel 0.1.0 -c:v copy mono.mp4`\
\
Left channel to stereo:\
`ffmpeg -i video.mp4 -map_channel 0.1.0 -map_channel 0.1.0 -c:v copy stereo.mp4`\
\
If you want to use the right channel, write `0.1.1` instead of `0.1.0.`

## Trim End of file (mp3) <a href="#ffmpeg-trimendoffile-mp3" id="ffmpeg-trimendoffile-mp3"></a>

Here's a command line that will slice to 30 seconds without transcoding:\
`ffmpeg -t 30 -i inputfile.mp3 -acodec copy outputfile.mp3`

## To Encode or Re-encode ? <a href="#ffmpeg-toencodeorre-encode" id="ffmpeg-toencodeorre-encode"></a>

Do you need to cut video with re-encoding or without re-encoding mode? You can try to following below command.\
Synopsis: ffmpeg -i \[input\_file] -ss \[start\_seconds] -t \[duration\_seconds] \[output\_file]

#### use ffmpeg cut mp4 video without re-encoding <a href="#ffmpeg-useffmpegcutmp4videowithoutre-encoding" id="ffmpeg-useffmpegcutmp4videowithoutre-encoding"></a>

Example:\
`ffmpeg -i source.mp4 -ss 00:00:05 -t 00:00:10 -c copy cut_video.mp4`

#### use ffmpeg cut mp4 video with re-encoding <a href="#ffmpeg-useffmpegcutmp4videowithre-encoding" id="ffmpeg-useffmpegcutmp4videowithre-encoding"></a>

Example:\
`ffmpeg -i source.mp4 -ss 00:00:05 -t 00:00:10 -async 1 -strict -2 cut_video.mp4`

If you want to cut off section from the beginning, simply drop -t 00:00:10 from the command

#### reduce filesize <a href="#ffmpeg-reducefilesize" id="ffmpeg-reducefilesize"></a>

Example:\
`ffmpeg -i input.mov -vcodec libx264 -crf 24 output.mp4`\
\
It reduced a 100mb video to 9mb.. Very little change in video quality.

Example:\
`ffmpeg -i video.mov -vf eq=saturation=0 -s 640x480 -c:v libx264 -crf 24 output.mp4`\
\
make a grayscale version and scale to 640x480

### Convert MKV to MP4 <a href="#ffmpeg-convertmkvtomp4" id="ffmpeg-convertmkvtomp4"></a>

`ffmpeg -i file.mkv`\
\
check for streams that you want (video/audio). be sure to convert/specify DTS 6 channel audio stream\
\
`ffmpeg -i input.mkv -strict experimental -map 0:0 -map 0:1 -c:v copy -c:a:1 libmp3lame -b:a 192k -ac 6 output.mp4`

### Add Watermark overlay (png) to the center of a video <a href="#ffmpeg-addwatermarkoverlay-png-tothecenterofavideo" id="ffmpeg-addwatermarkoverlay-png-tothecenterofavideo"></a>

`ffmpeg -i source.mov -i watermark.png -filter_complex "overlay=x=(main_w-overlay_w)/2:y=(main_h-overlay_h)/2" output.mp4`

more commands\
[http://www.catswhocode.com/blog/19-ffmpeg-commands-for-all-needs](http://www.catswhocode.com/blog/19-ffmpeg-commands-for-all-needs)
