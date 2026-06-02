from django.db import models

# Create your models here.
class Contacts(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank = True)
    phone_number = models.CharField(max_length = 11)
    email = models.EmailField(blank=True)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        )
    def __str__(self):
        return self.phone_number