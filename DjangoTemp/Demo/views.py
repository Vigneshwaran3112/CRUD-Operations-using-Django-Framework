from django.shortcuts import render,redirect
from Demo.models import users

# Create your views here.

def create(request):
	if request.method == 'GET':
		return render(request, 'index.html')
	if request.method == 'POST':
		name = request.POST.get('name')
		mobile = request.POST.get('mobile')
		email = request.POST.get('email')

		data = users(name=name, mobile=mobile, email=email)
		data.save()

	return redirect('display/')

def display(request):
	user = ''
	user = users.objects.all()
	return render(request, 'display.html', {'users':user})

def delete(request, id):
	user = ''
	user = users.objects.get(id=id)
	user.delete()
	return redirect('/display/')

def edit(request,id):
	user = ''
	user = users.objects.get(id=id)
	return render(request, 'update.html', {'users':user})

def update(request, id):
	user = ''
	user = users.objects.get(id=id)
	if request.method == 'POST':
		name = request.POST.get('name')
		mobile = request.POST.get('mobile')
		email = request.POST.get('email')

		user.name = name
		user.mobile = mobile
		user.email = email
		user.save()
		return redirect('/display')
	return render(request, 'update.html', {'users':user})