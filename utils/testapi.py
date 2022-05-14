from newsapi.newsapi_client import NewsApiClient

newsapi = NewsApiClient(api_key='d657b3284e804e5582bb31c3b6b777fc')


req_data = {"id": [], "publishedAt": [], "name": [], "title": [], "description": [] }

titledata=[]
descdata=[]

def informationgather(input) :
    all_articles = newsapi.get_everything(q=input,
                                          from_param='2022-04-14',
                                          to='2022-05-14',
                                          language='en',
                                          sort_by='relevancy')
    x = len(all_articles['articles'])
    for i in range(5):
        titledata.append(all_articles['articles'][i]['title'])
        descdata.append(all_articles['articles'][i]['description'])
    return (titledata , descdata)


