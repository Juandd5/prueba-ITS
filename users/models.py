from django.db import models


class User(models.Model):

    gender = models.CharField('Gender', max_length=50)
    full_name = models.CharField('Full Name', max_length=50)
    email = models.EmailField('Email', max_length=100)
    age = models.PositiveIntegerField('Age')
    city = models.CharField('City', max_length=50)
    country = models.CharField('Country', max_length=50)
    picture = models.CharField('Picture', max_length=50)

    def __str__(self) -> str:
        return self.full_name
    
    class Meta():
        verbose_name_plural = 'Users'
        db_table = 'users'
