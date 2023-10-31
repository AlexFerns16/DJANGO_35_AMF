from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profilepic.jpg', upload_to='profile_pictures')
    location = models.CharField(max_length=100)
    user_type = models.CharField(max_length=200, default='users')

    def __str__(self):
        return self.user.username


class CusOrders(models.Model):

    order_id = models.AutoField(primary_key=True)
    prod_code = models.IntegerField()
    quantity = models.IntegerField(default=1)
    user = models.CharField(max_length=200)

    def __str__(self):
        return str(
            (
                str(self.order_id),
                str(self.prod_code),
                str(self.quantity),
                str(self.user)
            )
        )


class CusRatingFeedback(models.Model):
    prod_code = models.IntegerField(default=1)
    ratings = models.FloatField()
    feedback = models.CharField(max_length=200)
    username  = models.CharField(max_length=200, default='username')
    user_type = models.CharField(max_length=200, default='Cust')

    def __str__(self):
        return str(
            (
                str(self.prod_code),
                str(self.ratings),
                str(self.feedback),
                str(self.username),
                str(self.user_type)
            )
        )
