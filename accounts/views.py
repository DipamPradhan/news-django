from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import CustomUserCreationForm, ProfileUpdateForm
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = ProfileUpdateForm
    template_name = "registration/profile_edit.html"
    success_url = reverse_lazy("home")

    def get_object(self):
        return self.request.user
