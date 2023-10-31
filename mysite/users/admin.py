from django.contrib import admin
from users.models import Profile, CusOrders, CusRatingFeedback

# Register your models here.

admin.site.register(Profile)
admin.site.register(CusOrders)
admin.site.register(CusRatingFeedback)
