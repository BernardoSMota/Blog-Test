from django.shortcuts import render, redirect
from blogUser.forms import customUserForm
from django.core.cache import cache


def newUser(request):
    form = customUserForm()
    
    if request.method == "POST":
        form = customUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            
            super_user_code = form.cleaned_data['super_user_code']
            current_code = cache.get('current_code') 
            if super_user_code == current_code:
                user.is_superuser = True
                user.is_staff = True
                
            user.set_password(form.cleaned_data['password1']) 
            user.save()
            return redirect('blog:index')
        
        
    return render(request, 'global/pages/form.html', context={'form': form} )

def userInfo(request):
    return render(request, 'blogUser/pages/user.html')