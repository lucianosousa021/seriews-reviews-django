from django.shortcuts import render, redirect, get_object_or_404
from .models import SeriesReviews
from .forms import ReviewForm

# Create your views here.


def index(request):
    reviews = SeriesReviews.objects.all().order_by('-id')
    data = {
        'reviews': reviews
    }
    return render(request, 'index.html', data)


def vizualizar(request, review_id):
    review = get_object_or_404(SeriesReviews, pk=review_id)
    exibir_review = {
        'review': review
    }
    return render(request, 'vizualizar.html', exibir_review)


def criar(request):
    form = ReviewForm()
    criar_review = {
        'form': form
    }
    return render(request, 'criar.html', criar_review)


def salvar(request):
    form = ReviewForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        serie_name = request.POST['serie_name']
        serie_genre = request.POST['serie_genre']
        serie_rating = request.POST['serie_rating']
        serie_info = request.POST['serie_info']
        serie_note = request.POST['serie_note']
        serie = SeriesReviews(serie_name=serie_name, serie_genre=serie_genre,
                              serie_rating=serie_rating, serie_info=serie_info, serie_note=serie_note)
        serie.save()
        return redirect('index')
    else:
        context = {
            'form': form,
        }
        return render(request, 'criar.html', context)


def deletar(request, review_id):
    review = SeriesReviews.objects.all().filter(pk=review_id)
    review.delete()
    return redirect('index')


def editar(request, review_id):
    field = ReviewForm(request.POST or None)
    if request.method == 'POST' and field.is_valid():
        serie_name = request.POST['serie_name']
        serie_genre = request.POST['serie_genre']
        serie_rating = request.POST['serie_rating']
        serie_info = request.POST['serie_info']
        serie_note = request.POST['serie_note']
        serie = SeriesReviews(pk=review_id, serie_name=serie_name, serie_genre=serie_genre,
                              serie_rating=serie_rating, serie_info=serie_info, serie_note=serie_note)
        serie.save()
        return redirect('index')
    update_form = SeriesReviews.objects.get(pk=review_id)
    editar = {
        'field': field,
        'update_form': update_form,

    }
    return render(request, 'editar.html', editar)


def buscar(request):
    review = SeriesReviews.objects.all().order_by('-id')
    if 'buscar' in request.GET:
        nome_buscar = request.GET['buscar']

        review = review.filter(serie_name__icontains=nome_buscar)

    dados = {
        'reviews': review
    }
    return render(request, 'buscar.html', dados)
