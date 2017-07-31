from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic

from staff.forms import LoginForm, EditForm, RegistrationForm
from staff.models import User


class LoginView(generic.FormView):
    template_name = 'account/login.html'
    model = User
    form_class = LoginForm
    success_url = 'edit'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            return redirect(".")
        else:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)


class EditView(generic.UpdateView):
    template_name = 'edit.html'
    model = User
    form_class = EditForm
    success_url = '/'

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        return super(EditView, self).form_valid(form)


class HomeView(generic.FormView):
    template_name = 'index.html'
    form_class = RegistrationForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(HomeView, self).form_valid(form)


class LogoutView(generic.RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
