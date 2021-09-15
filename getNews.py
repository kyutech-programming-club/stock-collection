from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='f08c6d20b4e547b2a3fd42657a63fdc6')

headlines = newsapi.get_top_headlines(sources='techcrunch')

# 取得したトップニュースの１件を表示
print(headlines['articles'][0])
