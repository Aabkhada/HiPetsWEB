from django.forms import ModelForm
from AppHipets.models import Producto,Mascota,Tipo,Formulario

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create the form class.
class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class FormularioForm(ModelForm):
    class Meta:
        model = Formulario
        fields = '__all__'

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'