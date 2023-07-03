from django.shortcuts import render, redirect

from .forms import SignupForm


# views contains functions which points towards the corresponding html files and passes required parameters to it.

def index(request):
    return render(request, 'todo/index.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'todo/signup.html', {
        'form': form
    })
