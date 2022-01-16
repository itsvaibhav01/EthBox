from django.forms import ModelForm, fields
from .models import Client

# customer creation form 
class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'phone', 'email', 'aadhar', 'pan', 'address', 'profile']