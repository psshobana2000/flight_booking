from .models import  Place, Flight, Airport, FlightRoute, Passenger, Traveller, Profile
from django import forms
from django.contrib.auth.models import User


class Flightform(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['airline_name','status','images']
        
class Userform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email']

class Placeform(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['city','airport','code','country']


# models.py

from django.db import models

def get_file_name(instance, filename):
    # Your logic to generate a file path for ImageField upload_to
    pass  # Replace with your logic

class Airline(models.Model):
    image = models.ImageField(upload_to=get_file_name)
    logo = models.ImageField(upload_to=get_file_name)
    # Other fields in your Airline model

class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = ['code', 'name', 'city', 'country', 'image']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }



class FlightRouteForm(forms.ModelForm):
    class Meta:
        model = FlightRoute
        fields = ['name', 'departure', 'arrival', 'distance', 'prize', 'fare_option']
       
class PassengerForm(forms.ModelForm):
    class Meta: 
        model = Passenger
        fields = ['name', 'age_category', 'physically_challenged']

       
class TravellerForm(forms.ModelForm):
    class Meta: 
        model = Traveller
        fields = ['first_name', 'last_name','gender','date_of_birth','seat_number','flight']
    



class ProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Profile
        fields = ['name', 'email', 'contact', 'designation', 'password']
        
