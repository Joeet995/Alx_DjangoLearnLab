from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password):
        if not email:
            raise ValueError("Users must have an Email")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email,password)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

        
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=False)
    profile_photo = models.ImageField()


class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
       return f"title = {self.title},author = {self.author}, publication_year = {self.publication_year}"
    


