from django.urls import path
from basic_app import views

# setting the name space for template tagging - this has to match the tag in the href
app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other')
]
