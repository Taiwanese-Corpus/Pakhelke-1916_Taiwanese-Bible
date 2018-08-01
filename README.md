# Pakhelke巴克禮聖經

- 信望愛線頂[閱讀經文](http://taigi.fhl.net/list.html)

## 資料說明
文字檔khǹg佇github，音檔用[Dropbox](https://www.dropbox.com/sh/d8im0w9xin3sdmi/AACxK89PXCeXRr3DKeGyJj9Ma?dl=0)
- json:`pkl.json`。整理`pklcl.txt`, `pklhl.txt`佮`低品質一段mp3`
- 全羅:`pklcl.txt`
- 漢羅:`pklhl.txt`
- 低品質一段mp3:
- 低品質一章mp3:`wget -m ftp://ftp.fhl.net/pub/FHL/audio/Taiwanese64k/`
  - 攏總300575秒
- 高品質一章mp3:`wget -m ftp://ftp.fhl.net/pub/FHL/audio/taisource/`

## 音檔授權
節錄自[信望愛網頁](http://bible.fhl.net/new/audio.html)
```
台語有聲聖經，由何姊妹(錄製人希望匿名)錄製、剪接提供給信望愛資訊中心，歡迎廣傳使用，並允許做不影響原意之修改。她更進一步開放著作權，同意所有人可以將他的錄音散佈、重製、配樂用於商業與非商業用途，不收費，也不需要進一步取得她的同意，只願福音廣傳。信望愛資訊中心很榮幸把她的錄音原始檔案放置於台灣與北美供大家下載使用。檔案很大，請耐心下載。
 ```

## 統計音檔時間
```
find .  -name '*.mp3' -exec bash -c "avconv -i {} -loglevel panic -f wav - | sox -t wav -  -n stat"  \; 2>&1 | \
  grep Length | sed -n 's#^Length (seconds):[^0-9]*\([0-9.]*\)$#\1#p' | \
  paste -sd+ | bc
```