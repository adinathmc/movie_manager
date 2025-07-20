from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self,username,email, password=None,**extra_field):
        if not username:
            raise ValueError('username is required')
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(username = username,email=email, **extra_field)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,username,email, password=None, **extra_field):
        extra_field.setdefault('is_staff', True)
        extra_field.setdefault('is_superuser', True)
        return self.create_user(username,email, password, **extra_field)

class UserCreation(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100,blank=False, null=False)
    last_name = models.CharField(max_length=100,blank=False, null=False)
    username = models.CharField(max_length=100, unique=True,blank=False, null=False)
    email = models.EmailField(max_length=100, unique=True,blank=False, null=False)
    gender = models.CharField(max_length=10,
                              choices=[('Male','M'),('Female','F')],
                              blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=100,blank=True, null=True)
    phone_number = models.CharField(max_length=12, unique=True,blank=True, null=True)
    time_joined =models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    #profile_pic = models.ImageField(upload_to='profile_pics', default='default.jpg')
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = CustomUserManager()


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name','last_name']

    def __str__(self):
        return self.username

  
   













 #username = models.CharField(max_length=100)
    #email = models.EmailField(max_length=100)
    #password = models.CharField(max_length=100)
