from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=225)

    class Meta:
        Ordering=('title')
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Post(models.Model):

    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS = {
        {ACTIVE,'active'},
        {DRAFT,'draft'}

    }

    Category= models.Foreignkey(Category, related_name='post',on_delete=models.CASCADE)
    title= models.CharField(max_length=225)
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status= models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    imagen = models.ImageField(upload_to='upload/', black=True, null=True)

    def __str__(self):
        return self.title

class comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
