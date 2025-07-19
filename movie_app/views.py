from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from .models import Movie_data
from .forms import Movie_form
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'movie_app/home.html')

@login_required
def create(request):
    if request.method == 'POST':
        frm = Movie_form(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect('list')  # Redirect to the list view after saving
    else:
        frm = Movie_form()
    return render(request, 'movie_app/create.html',{'form' : frm})

def list (request):
    movie_list_get = Movie_data.objects.all()
    return render(request, 'movie_app/list.html',{'movie_list' : movie_list_get})

@login_required
def edit(request,pk):
    instance_to_edit = get_object_or_404(Movie_data, pk=pk)
    if request.method == 'POST':
        frm = Movie_form(request.POST,instance=instance_to_edit)
        if frm.is_valid():
            frm.save()
            return redirect('list')  # Redirect to the list view after saving
    else:
        frm = Movie_form(instance=instance_to_edit)
    return render(request, 'movie_app/edit.html',{'form' : frm})

@login_required
def delete(request,pk):
    instance_to_delete = get_object_or_404(Movie_data,pk=pk)
    next_url = request.GET.get('next', 'list')  # Get the next URL to redirect after deletion
    if request.method == 'POST':
        instance_to_delete.delete()
        return redirect('list')
    return render(request, 'movie_app/delete_confirm.html', {'instance': instance_to_delete,'next_url': next_url})

@login_required
def edit_all(request):
    movie_list_get = Movie_data.objects.all()
    return render(request, 'movie_app/edit_all_page.html',{'movie_list': movie_list_get})

@login_required
def delete_all(request):
    movie_list_get = Movie_data.objects.all()
    return render(request, 'movie_app/delete_all_page.html',{'movie_list': movie_list_get})

def search(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        result=[]
        result = Movie_data.objects.filter(
                                            Q(name__icontains= query) |
                                            Q(year__icontains= query) |
                                            Q(director__icontains= query) |
                                            Q(genre__icontains= query)
                                           )       
        return render(request, 'movie_app/search.html', {'result': result,'query': query})


