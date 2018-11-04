from django.db import models

# Create your models here.
class Project(models.Model):
    image = models.ImageField(upload_to='images/') #data can saved as an Image, like a png
    summary = models.CharField(max_length=200)

    def __str__(self):
        message = ("{}. {}".format(str(self.id),(self.summary[:60]+"....")))
        return message
