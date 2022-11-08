import unittest
from scrapeInvoice import scrape_invoice_number

# ユニットテスト
class TestScrapInvoice(unittest.TestCase):

    _resultPath = 'result.json'

    def test_ScrapInvoiceNumber_true(self):
        print('登録済み番号でテスト')
        scrape_invoice_number(1000020012131, self._resultPath)

    def test_ScrapInvoiceNumber_false(self):
        print('未登録の登録番号でテスト')
        scrape_invoice_number(1234567890123, self._resultPath)

    def test_ScrapInvoiceNumber_err(self):
        print('桁数不正な登録番号でテスト')
        scrape_invoice_number(1234, self._resultPath)

if __name__ == '__main__':
    unittest.main()