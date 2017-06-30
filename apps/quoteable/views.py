from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Quote
from django.core.urlresolvers import reverse
from django.db.models import Count

# Create your views here.

def index(request):
	return render(request, 'quoteable/index.html')

def register(request):
	result = User.objects.register(request.POST)
	if isinstance(result, int):
		#validation successful
		request.session['userid'] = result
		return redirect(reverse('home'))
	else:
		#unsuccessful, flash messages
		for error in result:
			messages.add_message(request, messages.ERROR, error)
		return redirect(reverse('loginandres'))

def login(request):
	try:
		result = User.objects.login(request.POST)
		if isinstance(result, int):
			#login successful
			request.session['userid'] = result
			return redirect(reverse('home'))
		else:
			#unsuccessful, flash messages
			for error in result:
				messages.add_message(request, messages.ERROR, error)
			return redirect(reverse('loginandres'))
	except:
		messages.add_message(request, messages.ERROR, 'User authentication failed')
		return redirect(reverse('loginandres'))

def logout(request):
	request.session.clear()
	return redirect(reverse('loginandres'))
def home(request):
    user = User.objects.get(id=request.session['userid'])
    quotes = Quote.objects.all()
    #userquotes = Quote.objects.filter(poster=user)
    context = {
	   'user': user,
	   #'userquotes': userquotes,
	   'quotes': quotes,
	}
    return render(request, 'quoteable/home.html', context)
def addquote(request):
    Quote.objects.create(quotedby=request.POST['quotedby'], message=request.POST['message'], user=request.POST['user'])
    return redirect(reverse('home'))
def likequote(request, quoteid):
    this_user = User.objects.get(id=request.session['userid'])
    this_quote = Quote.objects.get(id=quoteid)
    this_quote.likes.add(this_user)
    return redirect(reverse('home'))
def mylikes(request):
    user = User.objects.get(id=request.session['userid'])
    quotes = Quote.objects.all()
    #userquotes = Quote.objects.filter(poster=user)
    context = {
	   'user': user,
	   #'userquotes': userquotes,
	   'quotes': quotes,
	}
    return render(request, 'quoteable/user.html', context)
def username(request):
    user = User.objects.get(id=request.session['userid'])
    quotes = Quote.objects.all()
    #userquotes = Quote.objects.filter(poster=user)
    context = {
	   'user': user,
	   #'userquotes': userquotes,
	   'quotes': quotes,
	}
    return render(request, 'quoteable/myposts.html', context)
def delete(request):
    Quote.objects.delete()
    return redirect(reverse('home'))
