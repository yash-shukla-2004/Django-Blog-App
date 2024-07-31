from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(req):
    if req.method == 'POST':
        form = UserRegisterForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(req, f'Your Account has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(req,'users/register.html',{'form': form})

@login_required
def profile(req):
    if req.method == 'POST':
        u_form = UserUpdateForm(req.POST , instance = req.user)
        p_form = ProfileUpdateForm(req.POST , req.FILES , instance=req.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(req, f'Your Account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = req.user)
        p_form = ProfileUpdateForm(instance=req.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(req,'users/profile.html',context)

# message.debug
# message.info
# message.success
# message.warning
# message.error