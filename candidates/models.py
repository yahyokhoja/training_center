from django.db import models
from django.conf import settings


class CV(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="cv"
    )
    full_name = models.CharField(max_length=150)
    age = models.PositiveIntegerField(null=True, blank=True)
    experience = models.TextField(blank=True)
    education = models.TextField(blank=True)

    def __str__(self):
        return f"CV {self.full_name}"


class Skill(models.Model):
    cv = models.ForeignKey(
        CV,
        on_delete=models.CASCADE,
        related_name="skills"
    )
    name = models.CharField(max_length=100)
    level = models.CharField(
        max_length=20,
        choices=[
            ("beginner", "Начальный"),
            ("intermediate", "Средний"),
            ("advanced", "Продвинутый"),
            ("expert", "Эксперт"),
        ]
    )

    def __str__(self):
        return f"{self.name} ({self.level})"
