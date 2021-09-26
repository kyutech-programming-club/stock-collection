from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='02c24d46025f4edbb582b1d50555788c')
all_articles = newsapi.get_everything(q='google', sources='techcrunch', from_param="2021-08-15", to="2021-08-31")

if( all_articles['totalResults'] > 0 ):
    print("ニュース件数： {}".format(all_articles['totalResults']))
    print(all_articles['articles'][0])
else:
    print("条件に合致したニュースはありません。")