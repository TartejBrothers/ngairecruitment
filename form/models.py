from django.db import models

domains = (
    ("Robotics", "Robotics"),
    ("Creatives", "Creatives"),
    ("Content", "Content"),
    ("Management", "Management"),
    ("Public Relations", "Public Relations"),
    ("Computer Vision", "Computer Vision"),
    ("Natural Language Processing", "Natural Language Processing"),
    ("Machine Learing & Deep Learning", "Machine Learing & Deep Learning"),
    ("Cyber Security", "Cyber Security"),
    ("Web & App Development", "Web & App Development"),
    ("AR/VR", "AR/VR"),
)


class Values(models.Model):
    name = models.TextField()
    reg = models.TextField()
    dept = models.TextField()
    domain = models.CharField(max_length=40, choices=domains)
    email = models.TextField()
    phone = models.TextField()
    reason = models.TextField()


# Create your models here.
