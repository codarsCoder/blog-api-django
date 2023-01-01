from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    
    
    def __str__(self):
        return f"{self.category_name}"


class Blog(models.Model):
    STATUS = (
        (1, 'Public'),
        (2, 'Draf')
    )
    category = models.ForeignKey(Category, related_name='categories', on_delete=models.CASCADE)  ## category yazdık ama category_id olarak kaydedecek
    title = models.CharField(max_length=50)
    content = models.TextField()
    status = models.SmallIntegerField(choices=STATUS, default=1)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    user_id = models.IntegerField()   ## serializere eklemeyeceğiz   sonradan create metodunu override ederek alıp ekleyeceğiz 
    def __str__(self):
      return f"{self.title}"