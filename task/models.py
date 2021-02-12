from django.db import models


# Create your models here.
class Task(models.Model):
    class Meta:
        ordering=['-id']
    name = models.TextField(max_length=200,blank=False,null=False)
    fromTime = models.DateTimeField()
    toTime = models.DateTimeField()
    detail = models.TextField(max_length=500,blank=True,null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
