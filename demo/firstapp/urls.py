
from django.urls import path
from firstapp import views
from django.conf import settings
from .views import CustomAuthToken


urlpatterns = [
    path('index/',views.index,name='index'),
    path('login',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('account/',views.account,name='account'),
    path('Form/',views.Form,name='Form'), 
    path('place/',views.place,name='place'), 
    path('app/',views.app,name='app'),  
    path('customer/',views.customer,name='customer'),
    path('layout1/',views.layout1, name='layout1'),
    path('sec/',views.sec, name='sec'),
    path('',views.admin_login_view, name='admin_login'), 
    path('emp/', views.accountApi),
    path('emp/<int:id>', views.accountApi),
    path('api/token/', CustomAuthToken.as_view(), name='api-token'),
    path('result/', views.result, name='result'),
    path('course/',views.course,name='course'),
    path('Economy/',views.Economy,name='Economy'),
    path('Airlines/',views.Airlines,name='Airlines'), 
    path('success/',views.success,name='success'), 
    path('routes/',views.routes,name='routes'),
    path('manage_routes/',views.manage_routes,name='manage_routes'),
    path('card/',views.card,name='card'),
    path('manage_routes/edit/<int:pk>/', views.route_edit, name='route_edit'),
    path('manage_routes/delete/<int:pk>/', views.route_delete, name='route_delete'),
    path('manage_type/',views.manage_type,name='manage_type'),
    path('manage_trip/',views.manage_trip,name='manage_trip'),
    path('type/',views.type,name='type'),
    path('manage_type/edit/<int:pk>/', views.type_edit, name='type_edit'),
    path('manage_type/delete/<int:pk>/', views.type_delete, name='type_delete'),
    path('nav/',views.nav,name='nav'),
    path('Traveller/',views.traveller,name='Traveller'),
    path('manage_traveller/',views.manage_traveller,name='manage_traveller'),
    path('traveller/edit/<int:pk>/', views.traveller_edit, name='traveller_edit'),
    path('traveller/delete/<int:pk>/', views.traveller_delete, name='traveller_delete'),
    path('manage_seat/',views.manage_seat,name='manage_seat'), 
    path('manage_users/',views.manage_users,name='manage_users'),
    path('panel/', views.panel, name='panel'),
    path('Profile/', views.Profile, name='Profile'),
    path('dashboard/', views.dashboard, name='dashboard')
    

]
    


    




