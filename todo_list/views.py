from django.shortcuts import render, redirect
from .models import List
#Add forms.
from .forms import ListForm
#Django has a messaging system.
from django.contrib import messages
#To re-direct after deleting entry:
from django.http import HttpResponseRedirect


def home(request): 

	if request.method == 'POST':
	#POST request is something sent from input box in base.html.
		#IF the post request is made (someone fills out the forms), populate with the request POST or if none is made, NONE.	
		form = ListForm(request.POST or None)

		#IF the form is valid, then save it.
		if form.is_valid():
			form.save()
			#Re-drect to home page, and show the changes.
			all_items = List.objects.all
			#Add message.
			messages.success(request, ('Item Has Been Added To List!'))
			return render(request, 'home.html', {'all_items': all_items})
	
	else:
		#Just show home page.
		all_items = List.objects.all
		return render(request, 'home.html', {'all_items': all_items})

def about(request): 
	my_name = "John Elder"
	number = 2+2
	context = {'name': my_name, "number": number}
	return render(request, 'about.html', context)	

def delete(request, list_id):
	#When we delete something, we make the item variable equal to this list_id.
	item = List.objects.get(pk=list_id)
	#Here we delete this item.
	item.delete()
	#Send message.
	messages.success(request, ('Item Has Been Deleted From List!'))
	return redirect('home')

def cross_off(request, list_id):
	item = List.objects.get(pk=list_id)
	#Change to TRUE when crossed off.
	item.completed = True 
	item.save()
	return redirect('home')

def uncross(request, list_id):
	item = List.objects.get(pk=list_id)
	#Change to TRUE when crossed off.
	item.completed = False  
	item.save()
	return redirect('home')	

def edit(request, list_id):	
	if request.method == 'POST':
		item = List.objects.get(pk=list_id)	
	#POST request is something sent from input box in base.html.
		#IF the post request is made (someone fills out the forms), populate with the request POST or if none is made, NONE.	
		form = ListForm(request.POST or None, instance=item)

		#IF the form is valid, then save it.
		if form.is_valid():
			form.save()
			#Add message.
			messages.success(request, ('Item Has Been Edited!'))
			return redirect('home')
	
	else:
		#Just show home page.
		item = List.objects.get(pk=list_id)
		return render(request, 'edit.html', {'item': item})