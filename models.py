from django.db import models

class Book(models.Model):
    Bookid=models.IntegerField()
    Bookname=models.CharField(max_length=20)
    Bookauthor=models.CharField(max_length=50)
    Bookprice=models.IntegerField()