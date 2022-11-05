# 適格請求書登録番号の登録状況確認スクリプト
# 国税庁の適格請求書発行事業者公表サイトをWebスクレイピングして確認する

import json
import os

from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

from mychrome import MyChrome

# 国税庁 適格請求書登録番号の公式検索サイト
SEARCH_INVOICE_NUMBER_URL = "https://www.invoice-kohyo.nta.go.jp/regno-search/detail?selRegNo="


# 適格請求書登録番号のスクレイピング
def scrape_invoice_number(invoiceNumber: int, outPath: str, headlessMode: bool = True):

    chrome = MyChrome(headlessMode).launch()

    url = SEARCH_INVOICE_NUMBER_URL + str(invoiceNumber)
    chrome.get(url)

    html = chrome.page_source.encode('utf-8')
    result_dict = _scrape_searched_page(html)

    chrome.close()
    chrome.quit()

    if result_dict:
        export_dict_to_json(outPath, result_dict)

def _scrape_searched_page(html: bytes):
    print("検索結果ページのスクレイピング")

    soup = BeautifulSoup(html, 'lxml')  # lxml はパーサ
    result_dict: dict = {}

    # エラー情報ページの場合
    err_box = soup.find('div', class_='err_box')
    if err_box:
        err_txt = err_box.find('li').text
        result_dict['error'] = err_box.find('li').text
        return result_dict

    # 適格請求書発行事業者登録情報
    detail = soup.find('div', class_='regno-search-detail_container')

    result_dict['number'] = detail.find('p', class_='itemdata sp_torokubango_data').text
    result_dict['name'] = detail.find('p', class_='itemdata sp_nmTsuushou_data').text
    # userInfo['timestamp_first'] = detail.find('p', class_='itemdata').text
    result_dict['timestamp_last'] = detail.find('p', class_='itemdata latestdate').text

    return result_dict


def export_dict_to_json(path: str, result_dict: dict):
    print("export_to_json() dict:" +  str(result_dict) + ", path:" + path)

    json_file = open(path, mode="w", encoding='utf-8', )
    json.dump(result_dict, json_file, indent=2, ensure_ascii=False)
    json_file.close()

