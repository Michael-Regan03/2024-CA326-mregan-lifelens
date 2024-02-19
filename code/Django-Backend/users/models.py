from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group, Permission
from django.core.validators import MinValueValidator, MaxValueValidator

class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None,  **extra_fields):
        if not email:
            raise ValueError("no email")
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name,**extra_fields)
        
        user.set_password(password)
        
        user.save()
        
        return user
   
    def create_superuser(self, email, name, password=None):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)

        user.set_password(password)
        user.is_superuser = True 
        user.is_staff = True  
        user.save(using=self._db)

        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length= 255, unique=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(120)])

    genders = [(0, "Male"), ( 1, "Female")]

    gender = models.IntegerField(choices=genders)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    groups = models.ManyToManyField(
        Group,
        related_name='custom_useraccount_groups',  # Unique related_name
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_useraccount_permissions',  # Unique related_name
        blank=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email
    
    def create_user(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)

        return self.create_user(email, name, password, **extra_fields)
