from django.db import models

# Create your models(Tables) here.

class Todo(models.Model):
    title = models.CharField(max_length=30)
    description =models.TextField()
    completed = models.BooleanField(default=False)
    
    #when we call Todo then it returns its title
    # def __str__(self) -> str:
    #     return self.title 
    