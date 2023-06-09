from django.shortcuts import render
from .models import Newsletter
from django.contrib import messages
# Create your views here.


def home(request):
    if request.method == "GET":
        description = request.GET.get("description")
        if description:
            Newsletter.objects.create(description=description)
    messages.success(request, "Added Newsletter")
    return render(request, 'newsletter/addNewsletter.html')
