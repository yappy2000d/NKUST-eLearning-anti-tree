# NKUST-eLearning-anti-tree
繼學長於7年前的製作的[高應大學習平台刷登入次數](https://github.com/Xi-Plus/NKUST-ilearning-anti-tree)之後的 **「高科大教學平台刷登入次數」**。

## 免責聲明
1. 本程式僅提供交流，使用本程式所造成的任何行為皆為使用者所為，與開發者無關。
2. 不保證程式的正常運作，執行所造成的一切損失與開發者無關。
3. 使用本程式時禁止一切冒用帳號的行為。
4. 為避免造成伺服器承受更多流量壓力，請自行斟酌使用。
5. 其他未列載因使用本程式造成的事宜，均與本程式開發者無關。
6. 開發者有權隨時修正此免責聲明。

## 環境要求
需要額外安裝下方套件：
+ [beautifulSoup 4(bs4)](https://pypi.org/project/beautifulsoup4/)
+ [urlib3](https://pypi.org/project/urllib3/)
+ [requests](https://pypi.org/project/requests/)
+ [PyExecJS(execjs)](https://pypi.org/project/PyExecJS/)

## 使用方法
修改`main.py`末行的`loop()`函數的`重複次數`、`使用者名稱`、`使用者密碼`後，在與`base64.js`、`md5.js`和`des.js`同個資料夾內執行`main.py`。  
<sub>P.S 建議次數一次不要設太多，以免造成伺服器阻塞。</sub>
