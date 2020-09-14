from django.shortcuts import render
import random 


def password_generate(request):
    characters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if request.GET.get('lowercase'):
        characters.extend(list('abcdefghijklmnopqrstuvwxyz'))

    if request.GET.get('numbers'):
        characters.extend(list('9876543210'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*-+{(])}<?>['))

    password = ''
    length = int(request.GET.get('length'))

    i=0
    while i < length:
        password += random.choice(characters)
        i += 1
        context_var = {'password':password}
    return render(request,'password_generate.html',context_var)

    

