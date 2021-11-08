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
    path("dataview/<int:pk>", views.dataview, name='dataview'),
    path("intmCPproject", views.intmCPproject, name='intmCPproject'),
    path("advCPproject", views.advCPproject, name='advCPproject'),
    path("easyCproject", views.easyCproject, name='easyCproject'),
    path("intmCproject", views.intmCproject, name='intmCproject'),
    path("advCproject", views.advCproject, name='advCproject'),
    path("easyJproject", views.easyJproject, name='easyJproject'),
    path("intmJproject", views.intmJproject, name='intmJproject'),
    path("advJproject", views.advJproject, name='advJproject'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)