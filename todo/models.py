from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models(Tables) here.

class Todo(models.Model):
    title = models.CharField(max_length=30)
    description =models.TextField()
    completed = models.BooleanField(default=False)
    email = models.EmailField(max_length=55,null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=True)
    #when we call Todo then it returns its title
    # def __str__(self) -> str:
    #     return self.title 
    