from django.shortcuts import render,redirect
from .forms import ApplicationForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ApplicationForm()
    return render(request, 'badmintonbooking/index.html',{"form": form})
    
    
def success(request):
    return render(request, 'badmintonbooking/success.html')
    