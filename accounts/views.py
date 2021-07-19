from django.shortcuts import render, redirect
from accounts.forms import UserAdminCreationForm
from django.contrib.auth.decorators import login_required


def register(request):
    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'accounts/register.html', {'form': form})
    # return render(request, 'accounts/register.html')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
