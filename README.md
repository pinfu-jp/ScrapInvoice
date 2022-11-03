# ScrapInvoice:適格請求書登録状況スクレイピング

- Webスクレイピングの学習用コードです
- 適格請求書登録番号が実在するかを調査できるスクリプトです
- [適格請求書発行事業者公表サイト](https://www.invoice-kohyo.nta.go.jp/)をWebスクレイピングしてhtmlから情報を取得しています

# サンプルコード

```python
from scrapInvoice import scrap_invoice_number

invoiceNo = 1234567890123
resultPath = 'result.json'

# スクレイピング
scrap_invoice_number(invoiceNo, resultPath, False)

# 結果は 'result.json' に出力されます
```

# 実行環境

- Python Ver.3.9.7 で動作確認
- selenium, bs4(BeautifulSoup) が必要です

- Chrome Driver が必要です
  - https://chromedriver.chromium.org/downloads からダウンロードして以下に配置してください
    - C:\\devtool\\chromedriver_win32\\chromedriver.exe
    
- 