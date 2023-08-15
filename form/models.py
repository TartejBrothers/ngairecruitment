from django.db import models

domains = (("Robotics", "Robotics"), ("Creatives", "Creatives"), ("Content", "Content"))


class Values(models.Model):
    name = models.TextField()
    reg = models.TextField()
    dept = models.TextField()
    domain = models.CharField(max_length=20, choices=domains)
    email = models.TextField()
    phone = models.TextField()
    reason = models.TextField()


# Create your models here.
