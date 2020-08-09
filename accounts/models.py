from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.password_validation import validate_password
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.regions import TashkentRegions

from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):
    """
    Custom user manager to create and save a user with the given username and password.
    """

    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        # validate_password(password, user)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class CustomAbstractUser(AbstractUser):
    """
    A custom abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """

    class Types(models.TextChoices):
        ADMIN = "admin"
        MODERATOR = "moderator"
        DRIVER = "driver"
        CUSTOMER = "customer"
        SELLER = "seller"

    base_type = Types.CUSTOMER

    type = models.CharField(
        _("User type"), max_length=50, choices=Types.choices, default=base_type,
    )

    # email is required to activate user by email confirmation
    email = models.EmailField(
        _('Email address'),
        unique=True,
        error_messages={
            'unique': _("A user with email already exists."),
        },
    )
    phone_number = PhoneNumberField(
        _("Phone number of a customer"),
        unique=True,
        error_messages={
            'unique': _("A user with phone number already exists."),
        },
        null=True,
        blank=True
    )

    objects = UserManager()

    REQUIRED_FIELDS = ['email', 'type']

    class Meta:
        abstract = True
        ordering = ['username']

    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.base_type
        return super().save(*args, **kwargs)


class User(CustomAbstractUser):
    """
    Custom User model.

    Username and password are required. Other fields are optional.
    """

    class Meta(CustomAbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class CustomerManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.CUSTOMER)


class SellerManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.SELLER)


class DriverManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.DRIVER)


class ModeratorManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.MODERATOR)


class AdminManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.ADMIN)


class CustomerMore(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    birth_date = models.DateTimeField(verbose_name="Birth date of a customer", null=True, blank=True)
    image = models.ImageField(
        verbose_name="Image of a customer",
        upload_to='images/customers/',
        blank=True)

    def __str__(self):
        return f"{self.user.username}'s extra fields"

    class Meta:
        verbose_name_plural = 'Customers Extra Fields'
        verbose_name = 'Customer Extra Field'


class Customer(User):
    """Representation of a customer in online shop"""
    base_type = User.Types.CUSTOMER
    objects = CustomerManager()

    @property
    def more(self):
        return self.customermore

    def __str__(self):
        return self.get_full_name() or self.username

    class Meta:
        proxy = True


class SellerMore(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    company_name = models.CharField(max_length=64, verbose_name="Seller's company name", blank=True)
    image = models.ImageField(
        verbose_name="Image of a seller",
        upload_to='images/seller/', null=True,
        blank=True)

    def __str__(self):
        return f"{self.user.username}'s extra fields"

    class Meta:
        verbose_name_plural = 'Sellers\' Extra Fields'
        verbose_name = 'Seller\'s Extra Field'


class Seller(User):
    """Representation of seller in online shop"""
    base_type = User.Types.SELLER
    objects = SellerManager()

    @property
    def more(self):
        return self.sellermore

    class Meta:
        proxy = True

    def get_company_name(self):
        return self.more.company_name

    def __str__(self):
        return self.get_full_name() or self.username


class DriverMore(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    license_id = models.PositiveIntegerField(verbose_name="License number of a driver", blank=True, null=True)
    model = models.CharField(max_length=255, verbose_name="Model of a car", blank=True, null=True)
    country_number = models.CharField(max_length=31, verbose_name="Country number of a car", blank=True, null=True)
    region = models.CharField(
        max_length=64,
        choices=TashkentRegions.choices,
        verbose_name="Working region of a driver",
        default=TashkentRegions.BEKTEMIR
    )

    def __str__(self):
        return f"{self.user.username}'s extra fields"

    class Meta:
        verbose_name_plural = 'Drivers\' Extra Fields'
        verbose_name = 'Driver\'s Extra Fields'


class Driver(User):
    base_type = User.Types.DRIVER
    objects = DriverManager()

    @property
    def more(self):
        return self.drivermore

    class Meta:
        proxy = True


class ModeratorMore(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.user.username}'s extra fields"

    class Meta:
        verbose_name_plural = 'Moderators\' Extra Fields'
        verbose_name = 'Moderator\'s Extra Fields'


class Moderator(User):
    base_type = User.Types.MODERATOR
    objects = ModeratorManager()

    @property
    def more(self):
        return self.moderatormore

    class Meta:
        proxy = True


class AdminMore(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Admin'
        verbose_name = 'Admins'

    def __str__(self):
        return f"{self.user.username}'s extra fields"

    class Meta:
        verbose_name_plural = 'Admins\' Extra Fields'
        verbose_name = 'Admin\'s Extra Fields'


class Admin(User):
    base_type = User.Types.ADMIN
    objects = AdminManager()

    @property
    def more(self):
        return self.adminmore

    class Meta:
        proxy = True
