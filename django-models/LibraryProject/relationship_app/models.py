from django.db import models

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
    
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    
class Admin(models.Model):
    name = models.CharField(max_length=100)
    related_admin = models.OneToOneField('self', on_delete=models.CASCADE, related_name='admin_detail', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Member(models.Model):
    name = models.CharField(max_length=100)
    related_member = models.OneToOneField('self', on_delete=models.CASCADE, related_name='member_detail', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
# class UserProfile(models.Model):
#     username = models.CharField(max_length=50)
    
#       def __str__(self):
#         return self.username
    
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     role = models.CharField(max_length=50)
    
#     def __str__(self):
# return f"{self.user.username} - {self.role}"