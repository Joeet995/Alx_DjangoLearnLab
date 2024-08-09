from django.db import models

# Create your models here.

class Book:
    def __init__(self, title : str, author : str, publication_year: int):
        self.title = title
        self.author = author
        self.publication_year = publication_year

        if len(title) > 200:
            raise Exception("title given is more then 200 characters")
        
        if len(author) > 100:
            raise Exception("author name is more than 100 characters")
        
