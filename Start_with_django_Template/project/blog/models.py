from django.db import models

# databse  contain two tables  Author & Blog

class Author(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Blog(models.Model):
    title=models.CharField(max_length=50)
    datetime=models.DateTimeField(auto_now_add=True,auto_created=True)
    content=models.TextField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    