from django.db import models

class Post(models.Model):
    title = models.CharField('Title post', max_length=100)
    description = models.TextField('Description post')
    author = models.CharField('Name author',max_length=100)
    date = models.DateField('Data post')
    img = models.ImageField('Images', upload_to='image/%Y')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class Comments(models.Model):
    email = models.EmailField()
    name = models.CharField('Name', max_length=50)
    text_comments = models.TextField('Text comments', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Posts', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


class Likes(models.Model):
    ip = models.CharField('IP-address', max_length=100)
    pos = models.ForeignKey(Post, verbose_name='Posts', on_delete=models.CASCADE)