from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Author(models.Model):
    def __init__(self, name):
        self.name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    #name = models.CharField(max_length=100)
    
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='title')
    class Meta(models.Model):
        permissions = [
            ('can_add_book', 'Can add book'),
            ('can_change_book', 'Can change book'),
            ('can_delete_book', 'Can delete book'),
        ]
    
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin')
        ('librarian', 'Librarian'),
        ('member', 'Member'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    
    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
    
    @receiver(post_save, sender=UserProfile)
def assign_permissions(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        if instance.role == 'Admin':
            user.user_permissions.add(
                Permission.objects.get(codename='can_add_book'),
                Permission.objects.get(codename='can_change_book'),
                Permission.objects.get(codename='can_delete_book'),
            )
        elif instance.role == 'Librarian':
            user.user_permissions.add(
                Permission.objects.get(codename='can_add_book'),
                Permission.objects.get(codename='can_change_book'),
            )
        elif instance.role == 'Member':
            # Typically, Members wouldn't have book permissions
            pass

    
