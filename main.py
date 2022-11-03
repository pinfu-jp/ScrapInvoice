from scrapInvoice import scrap_invoice_number

invoiceNo = 1000020012131   # この番号は苫小牧市の番号
resultPath = 'result.json'

scrap_invoice_number(invoiceNo, resultPath, False)
