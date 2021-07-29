from django.forms import ModelForm
from .models import SeriesReviews
from .rules import nota_inteiro, campo_vazio
class ReviewForm(ModelForm):
    class Meta:
        """ Utiliza os inputs do models.py"""
        model = SeriesReviews
        fields = ['serie_name', 'serie_genre', 'serie_rating', 'serie_info', 'serie_note']
        labels = {
            'serie_name': 'Nome da série',
            'serie_genre': 'Gênero da série',
            'serie_rating': 'Nota para a série',
            'serie_info': 'Sinopse da série',
            'serie_note': 'Análise da série'
        }

    def clean(self):
        name = self.cleaned_data.get('serie_name')
        genre = self.cleaned_data.get('serie_genre')
        rating = self.cleaned_data.get('serie_rating')
        info = self.cleaned_data.get('serie_info')
        note = self.cleaned_data.get('serie_note')
        errors_list = {}
        nota_inteiro(rating, errors_list)
        campo_vazio(name, errors_list, 'serie_name')
        campo_vazio(genre, errors_list, 'serie_genre')
        campo_vazio(rating, errors_list, 'serie_rating')
        campo_vazio(info, errors_list, 'serie_info')
        campo_vazio(note, errors_list, 'serie_note')
        print(errors_list)
        print('oi')
        if errors_list is not None:
            for error in errors_list:
                massage_error = errors_list[error]
                self.add_error(error, massage_error)
        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        """ Adiciona classes nos imputs """
        super().__init__(*args, **kwargs)
        self.fields['serie_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['serie_genre'].widget.attrs.update({'class': 'form-control'})
        self.fields['serie_rating'].widget.attrs.update({'class': 'form-control'})
        self.fields['serie_info'].widget.attrs.update({'class': 'form-control'})
        self.fields['serie_note'].widget.attrs.update({'class': 'form-control'})