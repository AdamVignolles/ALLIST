from django.shortcuts import render, redirect, HttpResponse
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

            m = ManageUser()
            users = m.get_user_by_email_and_password(request.GET.get('email'), request.GET.get('pswd'))
            for user in users:
                if user['email'] == request.GET.get('email') and user['password'] == request.GET.get('pswd'):
                    context = {'error_login': 'user found'}
                    # create cookie
                    response = render(request, 'app/index.html')
                    print(response)
                    print(request.GET.get('email'))
                    response.set_cookie('email', request.GET.get('email'), samesite='Lax')
                    print(response.set_cookie('email', request.GET.get('email'), samesite='Lax'))
                    print(request.COOKIES.get('email'))
                    print(response.cookies)
                    return redirect('/app/')
                
            context = {"error_login": "email or password incorrect"}
            
        elif request.GET.get('signup') == 'signup':
            m = ManageUser()
            users = m.get_user_by_email(request.GET.get('email'))
            for user in users:
                if user['email'] == request.GET.get('email'):
                    context = {"error_sign_up": "email already used"}
                    return render(request, 'login/index.html', context=context)
            m.insert_user(request.GET.get('txt'), request.GET.get('pswd'), request.GET.get('email'))
            context = {'error_sign_up': 'user inserted'}
            # create cookie
            response = render(request, 'app/index.html')
            response.set_cookie('email', request.GET.get('email'))
            print(request.GET.get('email'))
            return redirect('/app/')

    return render(request, 'login/index.html', context=context)

def app(request):
    # get cookie
    if request.COOKIES.get('email') == None:
        return redirect('/login/')
    
    users = ManageUser().get_user_by_email(request.COOKIES.get('email'))
    len_user = 0
    for user in users:
        len_user += 1
        user = user
    if len_user == 1:
        print(user)
        context = {'user': user, 'all_listes': ManageUser().get_user_listes(user)}
        return render(request, 'app/index.html', context=context)
    else:
        return redirect('/login/')