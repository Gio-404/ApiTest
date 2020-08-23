from django.db import models

# Create your models here.


class DB_tucao(models.Model):
    user = models.CharField(max_length=30, null=True)
    text = models.CharField(max_length=1000, null=True)
    ctime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text + str(self.ctime)


class DB_home_href(models.Model):
    name = models.CharField(max_length=30, null=True)
    href = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return self.name


class DB_project(models.Model):
    name = models.CharField(max_length=100, null=True)
    remark = models.CharField(max_length=1000, null=True)
    user = models.CharField(max_length=200, null=True)
    other_user = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
