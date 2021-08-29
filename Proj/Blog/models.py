from django.db import models

# Create your models here.

# class BlogPost(models.Model):
#     text = ...
#     category = ..


    # def __str__(self):    # be jaye adad esme music ro mizare   object(1) --> iran
    #     return self.music

class books_user(models.Model):
    name = models.TextField(max_length=100,null = True,blank = True)
    book = models.TextField(max_length=100,null = True,blank = True)
    author = models.TextField(max_length=100,null = True,blank = True)

    def __str__(self):
        return self.name #dar jaee ke ina save mishan esmeshono esm username mizare be jaye 1,2,3,...


class poems_user(models.Model):
    name = models.TextField(max_length=100,null = True,blank = True)
    poem = models.TextField(max_length=300,null = True,blank = True)
    poet = models.TextField(max_length=100,null = True,blank = True)

    def __str__(self):
        return self.name

class musics_user(models.Model):
    name = models.TextField(max_length=100,null = True,blank = True)
    music = models.TextField(max_length=100,null = True,blank = True)
    singer = models.TextField(max_length=100,null = True,blank = True)

    def __str__(self):
        return self.name
