import datetime

class Article():
    def __init__(self,title,subtitle,body,author):
        self.title = title
        self.subtitle = subtitle
        self.body = body
        self.author = author
        self.date = datetime.datetime.now()
