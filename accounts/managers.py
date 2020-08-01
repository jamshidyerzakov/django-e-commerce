# from django.contrib.auth.base_user import BaseUserManager
# from django.contrib.auth import get_user_model
#
#
# class UserManager(BaseUserManager):
#     """
#     Custom user manager to create and save a user with the given username and password.
#     """
#
#     def _create_user(self, username, email, password, **extra_fields):
#         if not username:
#             raise ValueError('The given username must be set')
#         if not email:
#             raise ValueError('Users must have an email address')
#         email = self.normalize_email(email)
#         username = self.model.normalize_username(username)
#         user = self.model(username=username, email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_user(self, username, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(username, email, password, **extra_fields)
#
#     def create_superuser(self, username, email=None, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#
#         return self._create_user(username, email, password, **extra_fields)
#
#
# class CustomerManager(UserManager):
#     def get_queryset(self, *args, **kwargs):
#         return super().get_queryset(*args, **kwargs).filter(type=User.Types.CUSTOMER)
#
#
# class SellerManager(UserManager):
#     def get_queryset(self, *args, **kwargs):
#         return super().get_queryset(*args, **kwargs).filter(type=User.Types.SELLER)
#
#
# class DriverManager(UserManager):
#     def get_queryset(self, *args, **kwargs):
#         return super().get_queryset(*args, **kwargs).filter(type=User.Types.DRIVER)
#
#
# class ModeratorManager(UserManager):
#     def get_queryset(self, *args, **kwargs):
#         return super().get_queryset(*args, **kwargs).filter(type=User.Types.MODERATOR)
#
#
# class AdminManager(UserManager):
#     def get_queryset(self, *args, **kwargs):
#         return super().get_queryset(*args, **kwargs).filter(type=User.Types.ADMIN)
