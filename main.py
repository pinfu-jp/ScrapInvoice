from scrapeInvoice import scrape_invoice_number

invoiceNo = 1000020012131   # この番号は苫小牧市の番号
resultPath = 'result.json'

scrape_invoice_number(invoiceNo, resultPath, False)
