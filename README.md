# ScrapeInvoice:適格請求書登録状況スクレイピング

- Webスクレイピングの学習用コードです
- 適格請求書登録番号が実在するかを調査できるスクリプトです
- [適格請求書発行事業者公表サイト](https://www.invoice-kohyo.nta.go.jp/)をWebスクレイピングしてhtmlから情報を取得しています

# サンプルコード

## 実行コード

```python
from scrapeInvoice import scrape_invoice_number

invoiceNo = 1234567890123
resultPath = 'result.json'

# スクレイピング
scrape_invoice_number(invoiceNo, resultPath)

# 結果は 'result.json' に出力されます
```

## 出力結果

- 成功
```json
{
  "number": "T1234567890123",
  "timestamp_last": "令和4年6月13日"
}
```

- 失敗
```json
{
  "error": "検索対象の登録番号は存在しません。内容をお確かめのうえ、入力してください。"
}
```


# 実行環境

- Python Ver.3.9.7 で動作確認
- selenium, bs4(BeautifulSoup) が必要です

- Chrome Driver が必要です
  - https://chromedriver.chromium.org/downloads からダウンロードして以下に配置してください
    - C:\\devtool\\chromedriver_win32\\chromedriver.exe
     
