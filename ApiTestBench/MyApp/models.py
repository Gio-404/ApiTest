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


class DB_apis(models.Model):
    project_id = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=100, null=True)
    api_method = models.CharField(max_length=10, null=True)
    api_url = models.CharField(max_length=1000, null=True)
    api_header = models.CharField(max_length=1000, null=True)
    api_login = models.CharField(max_length=10, null=True)
    api_host = models.CharField(max_length=100, null=True)
    desc = models.CharField(max_length=100, null=True)
    body_method = models.CharField(max_length=1000, null=True)
    api_body = models.CharField(max_length=1000, null=True)
    result = models.TextField(null=True)
    sign = models.CharField(max_length=10, null=True)
    file_key = models.CharField(max_length=50, null=True)
    file_name = models.CharField(max_length=50, null=True)
    public_header = models.CharField(max_length=1000, null=True)

    last_body_method = models.CharField(max_length=20, null=True, blank=True)
    last_api_body = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name

class DB_apis_log(models.Model):
    user_id = models.CharField(max_length=10,null=True)
    api_method = models.CharField(max_length=10, null=True)
    api_url = models.CharField(max_length=1000, null=True)
    api_header = models.CharField(max_length=1000, null=True)
    api_login = models.CharField(max_length=10, null=True)
    api_host = models.CharField(max_length=100, null=True)
    body_method = models.CharField(max_length=1000, null=True)
    api_body = models.CharField(max_length=1000, null=True)
    sign = models.CharField(max_length=10, null=True)
    file_key = models.CharField(max_length=50, null=True)
    file_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.api_url

