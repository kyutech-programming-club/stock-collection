import os
import datetime
import json
import getTodaysStock
import makeSearchList

from time import sleep
from googleapiclient.discovery import build

GOOGLE_API_KEY = "AIzaSyAwz1kET7wZc4uz420f6tg__xftWMXI9H8"
CUSTOM_SEARCH_ENGINE_ID = "d5f69bbec694913dc"

DATA_DIR = 'data'

def makeDir(path):
    if not os.path.isdir(path):
        os.mkdir(path)

def getSearchResponse(keyword):
    today = datetime.datetime.today().strftime("%Y%m%d")
    timestamp = datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")

    makeDir(DATA_DIR)

    service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)

    page_limit = 2
    start_index = 1
    response = []
    for n_page in range(0, page_limit):
        try:
            sleep(1)
            response.append(service.cse().list(
                q=target_keyword,
                cx=CUSTOM_SEARCH_ENGINE_ID,
                lr='lang_ja',
                num=1,
                start=start_index
            ).execute())
            start_index = response[n_page].get("queries").get("nextPage")[
                0].get("startIndex")
        except Exception as e:
            print(e)
            break

    # レスポンスをjson形式で保存
    save_response_dir = os.path.join(DATA_DIR, 'response')
    makeDir(save_response_dir)
    out = {'snapshot_ymd': today, 'snapshot_timestamp': timestamp, 'response': []}
    out['response'] = response
    jsonstr = json.dumps(out, ensure_ascii=False)
    with open(os.path.join(save_response_dir, 'response_' + keyword + '.json'), mode='w', encoding='utf-8') as response_file:
        response_file.write(jsonstr)

if __name__ == '__main__':
    dates_list = getTodaysStock.search_dates()
    print("会社名を入力してください")
    target_company = input()
    for num in range(len(dates_list)):
        target_keyword = target_company + " " + dates_list[num]
        print(target_keyword)
        getSearchResponse(target_keyword)
        makeSearchList.makeSearchResults(target_keyword)