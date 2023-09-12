from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator

def index(request):
    ml = Movies.objects.all()

    movie_name = request.GET.get('movie_name')

    if movie_name != '' and movie_name is not None:
        ml = Movies.objects.filter(name__icontains=movie_name)

    paginator = Paginator(ml, 3)
    page = request.GET.get('page')
    ml = paginator.get_page(page)

    context = {'ml': ml}

    return render(request, 'index.html', context)