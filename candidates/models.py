from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    profile = models.TextField()
    image = models.ImageField(upload_to='candidate_images/', null=True, blank=True)
    address = models.CharField(max_length=255)  # Corrected spelling from 'adres' to 'address'
    skills = models.JSONField()  # Changed to JSONField for better structure
    languages = models.JSONField()  # Changed to JSONField for better structure
    payment_status = models.CharField(max_length=50)  # Limited to a fixed length for better validation

    class Meta:
        verbose_name = "Candidate"
        verbose_name_plural = "Candidates"

    def __str__(self):
        return self.name

# Create your models here.
