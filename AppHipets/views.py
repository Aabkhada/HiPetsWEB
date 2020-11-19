from django.shortcuts import render, redirect
from AppHipets.models import *
from AppHipets.form import ProductoForm, CreateUserForm, FormularioForm
from django.template import Template,context,loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url='login')
@user_passes_test((lambda u: u.is_superuser),login_url='login')
def productos(request):
    form = ProductoForm()
    producto = Producto.objects.all()
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('/productos')
            except:
                pass
    else:
        form = ProductoForm()
    return render(request, 'productos.html',{'form':form, 'producto': producto})

@login_required(login_url='login')
def formulario(request):
    form = FormularioForm()
    if request.method == 'POST':
        form = FormularioForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('/index')
            except:
                pass
    else:
        form = FormularioForm()
    return render(request, 'formulario.html',{'form':form})



@login_required(login_url='login')
@user_passes_test(lambda u: u.is_superuser)
def panelAdmin(request):
    return render(request, 'panel.html')

def index(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')

def usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'usuarios.html',{'usuarios':usuarios})

def formularios(request):
    return render(request, 'formularios.html')


@login_required(login_url='login')    
def editar(request,id):
    pro = Producto.objects.get(id_producto=id)
    form = ProductoForm(instance=pro)
    return render(request,'edit.html',{'form':form,'id_producto':pro.id_producto})

@login_required(login_url='login')
def modificar(request,id):
    pro = Producto.objects.get(id_producto=id)

    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES, instance=pro)
        if form.is_valid():
            try:
                form.save()
                return redirect('/productos')
            except:
                pass    
    producto = Producto.objects.all()
    form = ProductoForm()
    return render(request, 'productos.html',{'form':form, 'producto': producto})

@login_required(login_url='login')
def eliminar(request,id):
    pro = Producto.objects.get(id_producto=id)
    pro.delete()
    return redirect('/productos')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/productos')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password=password)

            if user is not None:
                login(request,user)
                return redirect('/catalogo')
            else:
                messages.info(request,'Usuario o password incorrecto')
        return render(request,'login.html')
        

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/productos')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Se registró el usuario ' + user)
                return redirect('/login')
        return render(request,'register.html',{'form': form})

#    def listar(request):
#       producto = Producto.objects.all()
#       return render(request,"productos.html",{'producto':producto})
        

def catalogo(request):
    producto = Producto.objects.all()
    context = {'producto': producto}
    return render(request,'catalogo.html',context)

