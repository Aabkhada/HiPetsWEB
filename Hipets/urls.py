"""Hipets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppHipets import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('catalogo/', views.catalogo, name='catalogo'),
    path('index/', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('formulario/', views.formulario, name='formulario'),

    #urls admin
    path('panelAdmin/',views.panelAdmin, name='panelAdmin'),
    
    path('productos/',views.productos, name='productos'),
    path('edit/<int:id>', views.editar),
    path('update/<int:id>', views.modificar),
    path('delete/<int:id>', views.eliminar),

    path('usuarios/',views.usuarios, name='usuarios'),
    path('eliminaruser/<int:id>', views.eliminaruser),
    path('editaruser/<int:id>', views.editaruser),
    path('modificaruser/<int:id>', views.modificaruser),
    
    path('formularios/',views.formularios, name='formularios'),
    path('eliminarform/<int:id>', views.eliminarform),
    path('editarform/<int:id>', views.editarformularios),
    path('modificarform/<int:id>', views.modificarform),    


    #urls users
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),

    #urls passwd
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html"), name='password_reset'),
    path('reset_password_enviado/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_send.html"), name='password_reset_done'),    
    path('reset_password_confirmar/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset_password_form.html"), name='password_reset_confirm'),
    path('reset_password_listo/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_confirm.html"), name='password_reset_complete'),    

] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

