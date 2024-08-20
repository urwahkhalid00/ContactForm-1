
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('submit')  
        else:
            print(form.errors)  # print errors to the console
            return render(request, 'contact.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
def submit(request):
    # Your view logic here
    return render(request, 'submit.html')
