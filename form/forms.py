from django import forms
from .models import Values
from django.forms import ModelForm, TextInput, EmailInput, NumberInput, CharField


class add_data(forms.ModelForm):
    class Meta:
        model = Values
        fields = ["name", "reg", "dept", "domain", "email", "phone", "reason"]
        labels = {
            "name": ("Name"),
            "reason": ("Why do you want to join?"),
        }
        widgets = {
            "name": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 65%; min-width:50vw; background:#3C3C3C; margin-bottom:10px; border:none; font-size:20px;color: white; opacity:0.8; padding:10px",
                    "placeholder": "Name",
                }
            ),
            "domain": forms.Select(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 65%; background:#3C3C3C; margin-bottom:10px; border:none; font-size:16px;color: white; opacity:0.8; padding:10px",
                    "placeholder": "Registration Number",
                },
                choices=(
                    ("Robotics", "Robotics"),
                    ("Creatives", "Creatives"),
                    ("Content", "Content"),
                    ("Management", "Management"),
                    ("Public Relations", "Public Relations"),
                    ("Computer Vision", "Computer Vision"),
                    ("Natural Language Processing", "Natural Language Processing"),
                    (
                        "Machine Learing & Deep Learning",
                        "Machine Learing & Deep Learning",
                    ),
                    ("Cyber Security", "Cyber Security"),
                    ("Web & App Development", "Web & App Development"),
                    ("AR/VR", "AR/VR"),
                ),
            ),
            "reg": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 65%; min-width:50vw; background:#3C3C3C; margin-bottom:10px; border:none; font-size:20px;color: white; opacity:0.8; padding:10px",
                    "placeholder": "Registration Number",
                }
            ),
            "dept": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 65%; min-width:50vw; background:#3C3C3C; margin-bottom:10px; border:none; font-size:20px;color: white; opacity:0.8; padding:10px",
                    "placeholder": "Department",
                }
            ),
            "email": EmailInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 65%; min-width:50vw; background:#3C3C3C; margin-bottom:10px; border:none; font-size:20px;color: white; opacity:0.8; padding:10px",
                    "placeholder": "Email",
                }
            ),
            "phone": NumberInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 65%; min-width:50vw; background:#3C3C3C; margin-bottom:10px; border:none; font-size:20px;color: white; opacity:0.8; padding:10px",
                    "placeholder": "Phone",
                }
            ),
            "reason": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 65%; min-width:50vw; background:#3C3C3C; margin-bottom:10px; border:none; font-size:20px;color: white; opacity:0.8; padding:10px",
                    "placeholder": "Reason To Join",
                }
            ),
        }
