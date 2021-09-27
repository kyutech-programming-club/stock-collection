import requests
import bs4

# キーワードを使って検索してhtmlを取得する
keyword = 'TOYOTA'
response = requests.get('https://www.google.co.jp/search?q=' + keyword)

# ステータスコードが200以外なら例外を発生させる
response.raise_for_status()

# 取得したHTMLをパースする
bs = bs4.BeautifulSoup(response.text, "html.parser")

# 検索結果のタイトルとリンクを取得
element = bs.select('.r > a')

title_list = []
url_list = []

for i in range(len(element)):
    # タイトルのテキスト部分のみ取得
    title = element[i].get_text()    
    # リンクのみを取得し、余分な部分を削除する
    url = element[i].get('href').replace('/url?q=','')

    title_list.append(title)
    url_list.append(url)

# 出力
for i in range(len(title_list)):
    print(title_list[i])
    print('['+ url_list[i] +']')
    print('')