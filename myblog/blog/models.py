from django.db import models

class Post(models.Model):
    title = models.CharField('Title post', max_length=100)
    description = models.TextField('Description post')
    author = models.CharField('Name author',max_length=100)
    date = models.DateField('Data post')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"