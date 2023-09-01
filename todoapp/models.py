from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=300)
    completed= models.BooleanField(default=False, blank=True, null=True)

    class Meta:        
        verbose_name_plural = 'todos'

    def __str__(self):
            return self.title
    