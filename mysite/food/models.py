from django.db import models

# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_desc = models.CharField(max_length=300)
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500,
        default="https://th.bing.com/th?id=OIP.N0JNvG4iu61u97rvu8FZWgHaFe&w=290&h=214&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2"
    )

    def __str__(self):
       return self.item_name
