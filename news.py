from newspaper import Article


url = 'https://www.hamshahrionline.ir/news/464081/۸۰-درصد-جمعیت-قزوین-مشمول-دریافت-بسته-حمایت-معیشتی-هستند'
article = Article(url, language='fa')
article.download()
article.parse()
print(article.title)
print('====================================')
print(article.text)
print('====================================')
print(article.has_top_image())
print('====================================')
print(article.top_image)
print('====================================')


