from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

DEPART_CHOICES = [
    ("R&I", "R&I"),
    ("전략마케팅", "전략마케팅")
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=10, choices=DEPART_CHOICES, verbose_name="소속")
    image = models.ImageField(default='default_image.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        
        img = Image.open(self.image.path)

        if img.height > 300 or img.width >300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
