from django.db import models


# Create your models here.

class  Category(models.Model):
    cat_title= models.CharField(max_length=100)
    cat_description = models.CharField(max_length=100)


    def __str__(self):
        return self.cat_title
    


class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="newsblog/")
    content = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    date_of_published =  models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    


