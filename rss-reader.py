import feedparser
from newspaper import Article
from kafka_manager import insert_kafka
import time
from datetime import datetime
from mongodb import get_rss
from progress_bar import progress
import elastic_python
import json

manage_elastic = elastic_python.ManageElasticsearch()
while True:
    try:
        rss_list = get_rss()
        for url in rss_list:
            print(url['link'])
            rss_link = url['link']

            NewsFeed = feedparser.parse(rss_link)
            print(NewsFeed)
            # entry = NewsFeed.entries[1]
            try:
                for news in NewsFeed.entries:
                    # print(news.published)
                    # print(news.title)
                    # print(news.link)
                    article = Article(news.link, language='fa')
                    article.download()
                    article.parse()
                    # # print(article.title)
                    # print(article.text)
                    # if article.has_top_image() is True:
                    #     print(article.top_image)
                    newses = {
                        'publish_date': news.published,
                        'title': news.title,
                        'news_text': article.text,
                        'link': news.link,
                        'image': article.top_image
                    }
                    print(newses)
                    insert_kafka(topic='news-rss', json_data=newses)
                    response_metadata = manage_elastic.metadata_from_prepossess_za_api(newses)
                    response_elastic = manage_elastic.insert_elastic(index_document=response_metadata)
                    print(response_elastic)
            except Exception as err:
                print(err)
    except Exception as err:
        print(err)
    print("I am in sleep... And time is :  " + datetime.now().strftime('%H:%M:%S'))
    progress(9000)
    time.sleep(1)
    print("Project Started... And time is :  " + datetime.now().strftime('%H:%M:%S'))

