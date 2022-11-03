import unittest
from scrapInvoice import scrap_invoice_number

# ユニットテスト
class TestScrapInvoice(unittest.TestCase):

    _resultPath = 'result.json'

    def test_ScrapInvoiceNumber_true(self):
        print('正常な登録番号でテスト')
        tomakomaiNo = 1000020012131
        scrap_invoice_number(tomakomaiNo, self._resultPath)

    def test_ScrapInvoiceNumber_false(self):
        print('未登録の登録番号でテスト')
        scrap_invoice_number(1234567890123, self._resultPath)

    def test_ScrapInvoiceNumber_err(self):
        print('桁数不正な登録番号でテスト')
        scrap_invoice_number(1234, self._resultPath)

if __name__ == '__main__':
    unittest.main()