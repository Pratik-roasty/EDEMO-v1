from django.contrib import admin
from django.urls import path
from edemoApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="homePage"),
    path('loginPage',views.login,name="loginPage"),
    path('loginCheck',views.loginCheck,name="loginCheck"),
    path('addInfo',views.addInfo,name="registerDone"),
    path('register',views.register,name="registerPage")
]
