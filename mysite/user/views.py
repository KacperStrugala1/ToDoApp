from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from user.forms import UserForm

def register(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)  # NIE zapisujemy od razu
            raw_password = user_form.cleaned_data['password']
            user.set_password(raw_password)  # Teraz hasło będzie haszowane
            user.save()
            return redirect("/")
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, "user/register.html", {"user_form": user_form})