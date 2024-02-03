from django.db import models

# Create your models here.

class EmergencyCategory(models.Model):
    name = models.CharField(max_length=225)
    image = models.ImageField(upload_to='images')


class Emergency(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    phone = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images')
    category = models.ForeignKey(EmergencyCategory, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Emergency'
        verbose_name_plural = "Emergencies"
