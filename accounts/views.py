from django.shortcuts import render,redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import View
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.
class SignUpView(UserPassesTestMixin,View):
    def get(self, request):
        return render(request, 'registration/signup.html', {'form':SignUpForm()})
    
    def post(self, request):
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account is successfully created.')
            return redirect('login')
        return render(request, 'registration/signup.html', {'form':form} ) 
    
    def test_func(self):
        user = self.request.user
        if user.is_authenticated:
            return False
        return True
