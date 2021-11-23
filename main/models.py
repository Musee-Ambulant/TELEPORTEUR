from django.db import models

# Create your models here.


from django.db import models


# Create your models here.

class Ecole(models.Model):  # db object
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Groupe(models.Model):
    ecole = models.ForeignKey(Ecole, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photos_path = models.CharField(max_length=200)
    is_save = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Ami(models.Model):
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gif_path = models.CharField(max_length=200)
    stl_path = models.CharField(max_length=200)
    num_scan = models.IntegerField(default=0)
    is_save = models.BooleanField(default=False)

    def __str__(self):
        return self.name
