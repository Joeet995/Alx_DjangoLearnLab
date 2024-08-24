from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Permission, Group
from django.contrib.contenttypes.models import ContentType
from django import form


class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password, date_of_birth):
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
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()





class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
       return f"title = {self.title},author = {self.author}, publication_year = {self.publication_year}"
    
    class Meta:
        permissions = [
            ('can_view', 'Can View'),
            ('can_edit', 'Can Edit'),
            ('can_create', 'Can Create'),
            ('can_delete', 'Can Delete')
        ]

    # Viewers = Group.objects.get_or_create(name="Viewers")
    
    # Editors = Group.objects.get_or_create(name="Editors")

    # editing_permission = Permission.objects.create(code_name='can_edit',
    #                                                name= 'Can Edit'
    #                                                )
    # Editors.permissions.add(editing_permission)

    # Admins = Group.objects.get_or_create(name="Admins")
    
class Bookform(form.ModelForm):
        class Meta:
            model = Book
            fields = ['title', 'author', 'publication_year']

