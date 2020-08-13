from django.db import models

# Create your models here.


class DB_tucao(models.Model):
    user = models.CharField(max_length=30, null=True)
    text = models.CharField(max_length=1000, null=True)
    ctime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text + str(self.ctime)