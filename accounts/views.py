from django.shortcuts import render
from django.views.generic import CreateView
from .models import CustomUser
from .  import forms
from django.urls import reverse_lazy
class SignUpPage(CreateView):
    form_class = forms.CustomUserForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

