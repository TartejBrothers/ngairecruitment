from django.db import models

domains = (
    ("Robotics", "Robotics"),
    ("Creatives", "Creatives"),
    ("Content", "Content"),
    ("Management", "Management"),
    ("Public Relations", "Public Relations"),
    ("Computer Vision", "Computer Vision"),
    ("NLP", "NLP"),
    ("Machine Learning","Machine Learning"),
    ("Cyber Security", "Cyber Security"),
    ("Web & App", "Web & App"),
    ("AR/VR", "AR/VR"),
)


class Values(models.Model):
    name = models.TextField()
    reg = models.TextField()
    dept = models.TextField()
    domain = models.CharField(max_length=35, choices=domains)
    email = models.TextField()
    phone = models.TextField()
    reason = models.TextField()


# Create your models here.
