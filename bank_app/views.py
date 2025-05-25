from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.
def index(request):
	context = {

	}
	return render(request, 'index.html', context)

def signin(request):
	context = {
	}
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ("Login Successful"))
			return redirect("index")
		else:
			messages.success(request, ("Incorrect username or password"))
			return redirect(request.META.get("HTTP_REFERER"))
	return render(request, 'login.html', context)