from django.urls import path
from contact import views

app_name='contact'

urlpatterns = [
    path('<int:contact_id>/', views.contact_met, name='contact'),
    path('', views.index, name='index'),
]