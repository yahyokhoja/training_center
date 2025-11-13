from django.db import models
from django.conf import settings

def user_directory_path(instance, filename):
    # Файлы будут сохраняться в папке user_<id>/
    return f'user_{instance.user.id}/{filename}'

class Employer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='employer_profile'
    )
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255, blank=True, null=True)
    profile_image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    profile_video = models.FileField(upload_to=user_directory_path, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
