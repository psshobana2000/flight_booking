from django.shortcuts import render,redirect
from .forms import  Userform 
from firstapp.forms import Placeform,FlightRouteForm,PassengerForm,TravellerForm,ProfileForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .models import Passenger  
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import  MultiPartParser
from django.http import JsonResponse
from firstapp.serializers import AccountSerializer
from firstapp.models import Account
from firstapp.serializers import *
from rest_framework.decorators import parser_classes, api_view
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from rest_framework.response import Response
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import JsonResponse
from django.contrib.auth import authenticate
from .models import Course
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.shortcuts import render, get_object_or_404
from .models import FlightRoute,Traveller
from .forms import ProfileForm







def index(request):
    return render(request,"index.html")

def signup(request):
    return render(request,"signup.html")

def account(request):
    return render(request,"account.html")

def success(request):
    return render(request,"success.html")


def Form(request):
    form=Userform()
    if request.method == 'POST':
        form = Userform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"success.html")
    return render(request,'flight.html',{'form':form})

def place(request):
    form =Placeform()
    if request.method == 'POST':
        form = Placeform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"success.html")
    return render(request,'place.html',{'form':form})




@csrf_exempt
def admin_login_view(request):
    error_message = None  

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            # Log in the user
            login(request)
            
            if user.is_admin:
                return redirect('layout1')  # Redirect to admin home page
            else:
                return redirect('successs') 
        else:
            # Authentication failed
            error_message = 'Invalid username or password'
    return render(request, './panel.html', {'error': error_message})

def admin_logout_view(request):
    logout(request)
    return redirect('login_page')

def app(request):
    return render(request,"app.html")

def customer(request):
    return render(request,'customer.html')

def layout1(request):
    return render(request,'layout1.html')


def type(request):
    return render(request,'type.html')


def sec(request):
    return render(request,'sec.html')

def Economy(request):
    return render(request,'Economy.html')


def Airlines(request):
    return render(request,'Airlines.html')


@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@parser_classes([MultiPartParser])
def accountApi(request, id=0):
    if request.method == 'GET':
        account = Account.objects.all()
        account_serializer = AccountSerializer(account, many=True)
        return JsonResponse(account_serializer.data, safe=False)
    elif request.method == 'POST':
        data = request.data
        image = request.FILES.get('image')
        # Merge JSON data with uploaded image
        data['image'] = image
        account_serializer = AccountSerializer(data=data)
        if account_serializer.is_valid():
            account_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        emp_data = request.data
        emp = Account.objects.get(id=id)
        account_serializer = AccountSerializer(emp, data=emp_data)
        if account_serializer.is_valid():
            account_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        try:
            account = Account.objects.get(id=id)
            account.delete()
            return JsonResponse("Deleted Successfully", safe=False)
        except Account.DoesNotExist:
            return JsonResponse("Account does not exist", status=404, safe=False)

# Create your views here.

class ListUsers(APIView):

    auth_classes = [authentication.TokenAuthentication]
    perm_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        username = [user.username for user in User.objects.all()]
        return Response(username)


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args,**kwargs):
        serializer = self.serializer_class(data=request.data, context = {'request': request})
        serializer.is_valid(raise_exception=True)
        
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                'token': token.key,
                'user_id': user.pk,
                'email' : user.email,
            }
        )
    
def result(request):
    items_per_page = 5
    mydata=course.objects.filter(is_active=1).order_by('id')
    paginator = Paginator(mydata, items_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    reg_dict={'reg':mydata,'reg1':mydata,'page_obj': page_obj}
    return render(request,'app.html',reg_dict)


def course(request):
    # data = courses.objects.all()

    data =Course.objects.all().order_by('Title')
    if request.method == 'POST':
        try:
            title = request.POST.get('Title')
            description = request.POST.get('Description')
            technologies = request.POST.get('Technologies')
            images = request.FILES.get('images')
            status = request.POST.get('status')
            
            courses_data = Course(
                Title = title,
                Description = description,
                Technologies = technologies,
                Images = images,
                status = status,
            )
            courses_data.save()

            return redirect('course')
        
        except Exception as e:
            print("Error saving courses:", e)
    
    paginator = Paginator(data, 5)  # Show 5 contacts per page.

    page_number = request.GET.get("page")

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page_obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page_obj = paginator.page(paginator.num_pages)
    return render(request, 'course.html', {'page_obj': page_obj})

@api_view(['POST'])
def admin_login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user)

    return Response({
        'user_info': {
            'id' : user.id,
            'username' : user.username,
            'email' : user.email,
        },
        'token' : token
    })

@api_view(['GET'])
def get_user_data(request):
    user = request.user

    if user.is_authenticated:
        return Response({
            'user_info': {
                'id' : user.id,
                'username' : user.username,
                'email' : user.email,
            },
        })

    return Response({'error': 'not authenticated'}, status=400)

def login(request):
    print("coming here")
    return render(request,"login.html")

@csrf_exempt
def admin_login_api(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            # Log in the user
            login(request)
            
        return JsonResponse({'id':'1','username': 'demoadmin','password':'demopass'}) 
    else:
        return JsonResponse({'error': 'Invalid username or password'}, status=400)  # Return JsonResponse with error message and status code
    

def card(request):
    return render(request,"card.html")

def routes(request):
    if request.method == 'POST':
        form = FlightRouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = FlightRouteForm()
    return render(request, 'routes.html', {'form': form})

def manage_routes(request):
   routes = FlightRoute.objects.all()
   return render(request, 'manage_routes.html', {'routes': routes})

def route_edit(request, pk):
    flight_route = get_object_or_404(FlightRoute, pk=pk)
    if request.method == 'POST':
        form = FlightRouteForm(request.POST, instance=flight_route)
        if form.is_valid():
            form.save()
            return redirect('manage_routes')  
    else:
        form = FlightRouteForm(instance=flight_route)
    return render(request, 'route_edit.html', {'form': form})

def route_delete(request, pk):
    route = get_object_or_404(FlightRoute, pk=pk)
    if request.method == "POST":
        route.delete()
        return redirect('manage_routes.html', pk=pk)
    return render(request, 'route_delete.html', {'route': route})



def manage_trip(request):
    return render(request,"manage_trip.html")


def manage_type(request):
    types = Passenger.objects.all()
    return render(request, 'manage_type.html', {'types': types})


def type(request):
    if request.method == 'POST':
        form = PassengerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  
    else:
        form = PassengerForm()
    return render(request, 'type.html', {'form': form})

def type_edit(request, pk):
    type = get_object_or_404(Passenger, pk=pk)
    if request.method == 'POST':
        form = PassengerForm(request.POST, instance=type)
        if form.is_valid():
            form.save()
            return redirect('manage_type')  
    else:
        form = PassengerForm(instance=type)
    return render(request, 'type_edit.html', {'form': form})



def type_delete(request, pk):
    type = get_object_or_404(Passenger, pk=pk)
    if request.method == 'POST':
        type.delete()
        return redirect('manage_type.html',pk=pk)
    return render(request, 'confirm_delete.html', {'type': type})



def nav(request):
    return render(request,"nav.html")

def traveller(request,id):
    if request.method == 'POST':
        form = TravellerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success') 
    else:
        form = TravellerForm()
    return render(request, 'traveller.html', {'form': form})


def manage_traveller(request):
    travellers = Traveller.objects.all()
    return render(request, 'manage_traveller.html', {'travellers': travellers})



def traveller_edit(request, id):
    travellers = get_object_or_404(travellers, id=id)
    if request.method == 'POST':
        form = TravellerForm(request.POST, instance=traveller)
        if form.is_valid():
            form.save()
            return redirect('manage_traveller') 
    else:
        form = TravellerForm(instance=traveller)
    return render(request, 'traveller_edit.html', {'form': form})



def traveller_delete(request, id):
    travellers = get_object_or_404(travellers, id=id)
    if request.method == 'POST':
        travellers.delete()
        return redirect('manage_traveller.html')
    return render(request, 'Traveller_delete.html', {'traveller': traveller})

def manage_seat(request):
    return render(request,"manage_seat.html")

def sec(request):
    return render(request,"sec.html")
 


def manage_users(request):
    return render(request,"manage_users.html")

def panel(request):
    return render(request,"panel.html")


from django.shortcuts import render, redirect
from .forms import ProfileForm

def Profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  
        else:    
            return render(request, 'Profile.html', {'form': form})
    else:
        form = ProfileForm()
    return render(request, 'Profile.html', {'form': form})

from .models import Profile
def manage_users(request):
    profiles = Profile.objects.all()  
    return render(request, 'manage_users.html', {'profiles': profiles})


def edit_profile(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('manage_users')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})




def delete_profile(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    if request.method == 'POST':
        profile.delete()
        return redirect('manage_users')
    return render(request, 'delete_profile.html', {'profile': profile})
