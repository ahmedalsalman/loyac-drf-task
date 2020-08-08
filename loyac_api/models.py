from django.db import models
from django.contrib.auth.models import (
	UserManager, AbstractBaseUser
)
from datetime import datetime


class CustomUserManager(UserManager):
	def create_user(self, email, date_of_birth, first_name, last_name, password=None):
		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(
			email=self.normalize_email(email),
			date_of_birth=date_of_birth,
			first_name=first_name, 
			last_name=last_name,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, date_of_birth, first_name, last_name, password):
		user = self.create_user(
			email,
			password=password,
			date_of_birth=date_of_birth,
			first_name=first_name, 
			last_name=last_name,
		)
		user.is_superuser = True
		user.is_staff = True
		user.save(using=self._db)
		return user


class CustomUser(AbstractBaseUser):
	email = models.EmailField(
		verbose_name='email address',
		max_length=255,
		unique=True,
	)
	date_of_birth = models.DateField()
	first_name = models.CharField(max_length=150)
	last_name = models.CharField(max_length=150)
	is_active = models.BooleanField(default=True)
	is_superuser = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	employeeID = models.CharField(blank=True, null=True, max_length=150)

	objects = CustomUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['date_of_birth', 'first_name', 'last_name',]

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		return True


AGE_GROUPS = (
			('5-9','5-9'),
			('10-17','10-17'),
			('18-26','18-26'),
			('27-35','27-35'),
			)

class Program(models.Model):
	name = models.CharField(max_length=150)
	image = models.ImageField(null=True, blank=True)
	description = models.TextField()
	age_group = models.CharField(choices=AGE_GROUPS,max_length=5)
	date_created = models.DateTimeField(default=datetime.now())
	points = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	supervisor = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name="supervising")


	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Program"


class Application(models.Model):
	program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="applications")
	applicant = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, related_name="applications")
	points = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	application_date = models.DateTimeField(default=datetime.now())
	
	def __str__(self):
		return "%s: %s" % (self.applicant.email, str(self.program.name))

#To create a signal and send an email to the superuser to give the request.user is_staff permissions.
class StaffUserRequest(models.Model):
	pass