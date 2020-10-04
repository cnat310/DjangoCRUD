from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm, DateForm
from django.http import HttpResponseRedirect
from django import forms
from django.contrib import messages
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.decorators import login_required

def home(request):
	date_filter = datetime.today().strftime('%Y-%m-%d')
	yesterday = (datetime.today() - timedelta(days = 1)).strftime('%Y-%m-%d')
	yesterday_header = (datetime.today() - timedelta(days = 1))
	today_header = datetime.today()
	tomorrow = (datetime.today() + timedelta(days = 1)).strftime('%Y-%m-%d')
	tomorrow_header = (datetime.today() + timedelta(days = 1))
	all_items = List.objects.filter(date = date_filter)
	yesterday_items = List.objects.filter(date = yesterday)
	tomorrow_items = List.objects.filter(date = tomorrow)
	return render(request, 'home.html', {'all_items':all_items, 'today_header': today_header, 'yesterday_header': yesterday_header, 'tomorrow_header': tomorrow_header,'date_filter':date_filter, 'yesterday': yesterday, 'tomorrow': tomorrow, 'yesterday_items': yesterday_items, 'tomorrow_items': tomorrow_items})

def about(request):
	
	return render(request, 'about.html', {})

@login_required
def add(request):
	if not request.user.is_authenticated:
		return render(request, 'myapp/login_error.html')	
	if request.method == 'POST':
		form = ListForm(request.POST or None)
		if form.is_valid():
			form.save()
			all_items = List.objects.all
			return redirect('home')
		else:
			all_items = List.objects.all
			return render(request, 'add.html', {'all_items':all_items})
	else:
		all_items = List.objects.all
		return render(request, 'add.html', {'all_items':all_items})

def search(request):
	if request.method == 'POST':
		date_filter = request.POST['date']
		form = DateForm(request.POST or None)
		if form.is_valid():
			all_items = List.objects.filter(date = date_filter)
			return render(request, 'search.html', context = {'all_items': all_items, 'date_filter': date_filter})
		else:
			all_items = List.objects.all
			return redirect('home')

	else:
		return redirect('home')

@login_required
def delete(request, list_id):
	item = List.objects.get(pk=list_id)
	item.delete()
	date = item.date
	all_items = List.objects.filter(date = date)
	return render(request, 'search.html', context = {'all_items': all_items, 'date': date})

@login_required
def edit(request, list_id):
	if request.method == 'POST':
		item = List.objects.get(pk=list_id)
		date = item.date
		print(date)
		form = ListForm(request.POST or None, instance=item)

		if form.is_valid():
			form.save()
			all_items = List.objects.filter(date = date)
			return render(request, 'search.html', context = {'all_items': all_items, 'date': date})
	else:
		item = List.objects.get(pk=list_id)
		return render(request, 'edit.html', {'item': item})
