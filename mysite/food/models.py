from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default='1'
    )
    prod_code = models.IntegerField(default=100)
    for_user = models.CharField(
        max_length=100, 
        default='xyz'
    )
    item_name = models.CharField(max_length=50)
    item_desc = models.CharField(
        max_length=500,
        default='''Lorem, ipsum dolor sit amet consectetur adipisicing elit. A nam voluptate assumenda recusandae officia et consequatur, 
                   nobis voluptatem incidunt laborum harum doloribus aspernatur iure aperiam adipisci quas alias ea delectus!'''
    )
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500,
        default="https://th.bing.com/th?id=OIP.N0JNvG4iu61u97rvu8FZWgHaFe&w=290&h=214&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2"
    )

    def __str__(self):
       return self.item_name
