from django.contrib import admin
from django.urls import path
from CreditCardFD import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("",views.index,name='index'),
    path("home",views.home,name='home'),
    path("about",views.about,name='about'),
    path("signin",views.signin,name='signin'),
    path("contact",views.contact,name='contact'),
    path("home1",views.home1,name='home1'),
    path("dashboard",views.dashboard,name='dashboard'),
    path("deleteupload/<int:pk>",views.deleteupload,name="deleteupload"),
    path("dataview/<int:pk>/", views.dataview, name='dataview'),
     path("dataview/home1", views.home1, name='dataview/home1'),
  
    path("easyCproject", views.easyCproject, name='easyCproject'),
  
    path("easyJproject", views.easyJproject, name='easyJproject'),
    path("intmJproject", views.intmJproject, name='intmJproject'),
    path("advJproject", views.advJproject, name='advJproject'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)