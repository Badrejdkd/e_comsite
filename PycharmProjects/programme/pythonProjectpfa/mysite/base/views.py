
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import RegisterForm
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Produit
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')  # redirige vers une page après connexion
        else:
            messages.error(request, 'Nom d’utilisateur ou mot de passe invalide.')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Compte créé avec succès. Connectez-vous.')
            return redirect('login')
    return render(request, 'register.html', {'form': form})

class Productlist(View):
    def get(self,request):
        products = Produit.objects.all()
        return render(request,'ListProduit.html',{'products':products})


class ProductDetail(View):
    def get(self, request, pk, *args, **kwargs):  # Ensure 'pk' is accepted
        product = get_object_or_404(Produit, id=pk)
        return render(request, 'detailproduit.html', {'product': product})


def home(request):
    return render(request, 'home.html')