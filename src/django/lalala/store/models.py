from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registrated_at = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(
        default="https://www.google.com/url?sa=i&url=https%3A%2F%2Fsteamcommunity.com%2Fsharedfiles%2Ffiledetails%2F%3Fid%3D1790762888&psig=AOvVaw0wJRjJqYKIVcmCp5etldO-&ust=1675584755288000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCJjBu-O1-_wCFQAAAAAdAAAAABAF",
        upload_to="buyer/", blank=True, null=True)


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Product(models.Model):
    pass


# class Category(models.Model):
#     name = models.TextField(default='All')
#     product = models.ManyToOneRel(Product)

# Create your models here.
