from django.shortcuts import render
from .manage_user import ManageUser

# Create your views here.

def acceuil(request):
    return render(request, 'acceuil/index.html')

def about(request):
    return render(request, 'about/index.html')

def contact(request):
    return render(request, 'contact/index.html')

def conditions_utilisation(request):
    return render(request, 'conditions_utilisation/index.html')

def politique_confidentialite(request):
    return render(request, 'politique_confidentialite/index.html')


def login(request):

    context = {}

    # form get method
    if request.method == 'GET': 
        if request.GET.get('login') == 'login':
            print(request.GET.get('email'))
            print(request.GET.get('pswd'))
            m = ManageUser()
            users = m.get_user_by_email_and_password(request.GET.get('email'), request.GET.get('pswd'))
            for user in users:
                if user['email'] == request.GET.get('email') and user['password'] == request.GET.get('pswd'):
                    context = {'error_login': 'user found'}
                    return render(request, 'login/index.html', context=context)
            context = {"error_login": "email or password incorrect"}
            
        elif request.GET.get('signup') == 'signup':
            print(request.GET.get('login'))
            print(request.GET.get('pswd'))
            print(request.GET.get('email'))
            print(request.GET.get('txt'))
            m = ManageUser()
            users = m.get_user_by_email(request.GET.get('email'))
            for user in users:
                if user['email'] == request.GET.get('email'):
                    context = {"error_sign_up": "email already used"}
                    return render(request, 'login/index.html', context=context)
            m.insert_user(request.GET.get('txt'), request.GET.get('pswd'), request.GET.get('email'))
            context = {'error_sign_up': 'user inserted'}

    return render(request, 'login/index.html', context=context)