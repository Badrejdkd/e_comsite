
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import RegisterForm
from django.views import View
from django.shortcuts import get_object_or_404

from .models import Produit, Compagnie
from django.views import View
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .form import CustomLoginForm
from django.contrib import messages

def custom_login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Bienvenue {user.username} !')

            # Redirection selon le type d'utilisateur
            if user.is_staff:
                return redirect('data')  # À définir dans urls.py
            else:
                return redirect('home')   # À définir dans urls.py
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Compte créé avec succès. Vous pouvez maintenant vous connecter.')
            return redirect('login')  # Remplace 'login' par le nom correct de ta vue de connexion
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

class Productlist(View):
    def get(self,request):
        products = Produit.objects.all()
        return render(request,'ListProduit.html',{'products':products})

class PowerBIView(View):
    def get(self, request):
        return render(request, 'powerbi.html')

class ProductsByCompany(View):
    def get(self, request, compagnie_id):
        compagnie = get_object_or_404(Compagnie, id=compagnie_id)
        produits = Produit.objects.filter(compagnie=compagnie)
        return render(request, 'products_by_company.html', {
            'compagnie': compagnie,
            'produits': produits
        })
class complist(View):
    def get(self,request):
        comp = Compagnie.objects.all()
        return render(request,'home.html',{'comp':comp})

class ProductDetail(View):
    def get(self, request, pk, *args, **kwargs):  # Ensure 'pk' is accepted
        product = get_object_or_404(Produit, id=pk)
        return render(request, 'detailproduit.html', {'product': product})


def home(request):
    return render(request, 'home.html')