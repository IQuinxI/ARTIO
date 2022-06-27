from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Comment(models.Model):
    Text = models.CharField(null=False, max_length=250, blank=False)
    LikeCount = models.IntegerField(null=True, default=0)
    # User = models.OneToOneField(User, on_delete=models.CASCADE)
# class UserAccountManager(BaseUserManager):
#     def create_user(self, email, name, password=None):
#         if not email:
#             raise ValueError('Enter Email Address')
#
#         email = self.normalize_email(email)
#         user = self.model(email=email, name=name)
#
#         user.set_password(password)
#         user.save()
#
#         return user

# class UserAccount(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_length=225, unique=True)
#     name = models.CharField(max_length=225)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     SubCount = models.IntegerField(default=0, null=False)

    # object =  UserAccountManager()
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['name']


class Profile(models.Model):
    user = models.CharField(max_length=20, null=False, blank=False, default="user")
    SubCount = models.IntegerField(default=0, null=False)
    # Comment = models.OneToOneField(Comment, on_delete=models.CASCADE, null=True, blank=True)
    state = models.CharField(max_length=20, null=False, blank=False)#Banned, Active
    password = models.CharField(max_length=20, null=False, blank=False)
    
    # def __str__(self):
    #     return self.user;

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()



class Poste(models.Model):
    Titre = models.CharField(max_length=250, null=False, blank=False)
    LikeCount = models.IntegerField(null=True, default=0)
    Comment = models.OneToOneField(Comment, on_delete=models.CASCADE, null=True, blank=True)
    Date = models.DateTimeField('date published')
    Art = models.ImageField(upload_to="media")
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # test = models.CharField(max_length=250, null=False, blank=False, default=None)

# class OwnedPosts(models.Model):
#     User = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
#     Poste = models.OneToOneField(Poste, on_delete=models.CASCADE, null=True)
#     test = models.CharField(max_length=250, null=False, blank=False, default=None)
class LikedPosts(models.Model):
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Poste = models.ForeignKey(Poste, on_delete=models.CASCADE)