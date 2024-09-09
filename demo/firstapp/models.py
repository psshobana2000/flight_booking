import os
import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Utility function for file upload
def get_file_name(instance, filename):
    now_time = datetime.datetime.now().strftime('%Y%m%d%X')
    new_filename = "{}{}".format(now_time, filename)
    return os.path.join('media/', new_filename)

class Flight(models.Model):
    airline_name = models.CharField(max_length=20)
    status = models.BooleanField(default=True)
    images = models.ImageField(upload_to=get_file_name, blank=True)

    def __str__(self):
        return self.airline_name


class Place(models.Model):
    city = models.CharField(max_length=30)
    airport = models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.city



GENDER_CHOICES = (
    ('male', 'MALE'),
    ('female', 'FEMALE')
)


class AdminLoginManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('User must have an email.')
        if not username:
            raise ValueError('User must have a username.')
        user = self.model(
            email=self.normalize_email(email)
,
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email)
,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class AdminLogin(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True, blank=False)
    email = models.EmailField(max_length=150, unique=True, blank=False)
    password = models.CharField(max_length=128)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = AdminLoginManager()

    def __str__(self):
        return self.username

class TourPackage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status_choices = [
        ('enabled', 'Enabled'),
        ('disabled', 'Disabled'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='enabled')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Account(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_name, null=True, blank=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    images = models.ImageField(upload_to='course_images/', blank=True, null=True)
    technologies = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Airport(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    image = models.ImageField(upload_to='airports/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.code})"



class FlightRoute(models.Model):
    SAVE_FARE = 'save'
    FLEXI_PLUS = 'flexi'
    SUPER_6E = 'super'

    FARE_OPTIONS = [
        (SAVE_FARE, 'Save Fare'),
        (FLEXI_PLUS, 'Flexi Plus'),
        (SUPER_6E, 'Super6E'),
    ]

    name = models.CharField(max_length=100, default='Some Default Value')
    departure = models.CharField(max_length=100, default='Some Default Value')
    arrival = models.CharField(max_length=100, default='Some Default Value')
    prize = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    distance = models.CharField(max_length=50)
    fare_option = models.CharField(
        max_length=5,
        choices=FARE_OPTIONS,
        default=SAVE_FARE,
    )

    def __str__(self):
        return f"{self.name} from {self.departure} to {self.arrival}"

class Arrival(models.Model):
    STATUS_CHOICES = [
        ('on_time', 'On Time'),
        ('delayed', 'Delayed'),
        ('cancelled', 'Cancelled'),
    ]

    arrival_date_time = models.DateTimeField()
    city = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.city} - {self.arrival_date_time} - {self.get_status_display()}"



class Passenger(models.Model):
    name = models.CharField(max_length=100)
    AGE_CATEGORY_CHOICES = [
        ('child', 'Child'),
        ('adult', 'Adult'),
        ('senior', 'Senior'),
    ]
    age_category = models.CharField(max_length=10, choices=AGE_CATEGORY_CHOICES)
    physically_challenged = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Traveller(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    seat_number = models.CharField(max_length=10)
    flight = models.CharField(max_length=20)    

class Trip(models.Model):
    ROUNDTRIP = 'roundtrip'
    MULTICITY = 'multicity'
    ONE_WAY = 'one_way'

    TRIP_TYPES = [
        (ROUNDTRIP, 'Roundtrip'),
        (MULTICITY, 'Multicity'),
        (ONE_WAY, 'One Way'),
    ]

    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    trip_type = models.CharField(max_length=10, choices=TRIP_TYPES)

    def __str__(self):
        return self.name

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=15)
    designation = models.CharField(max_length=100)
    password = models.CharField(max_length=100)



    def __str__(self):
        return self.name





