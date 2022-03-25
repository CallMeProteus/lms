from django.shortcuts import render

# Create your views here.
from audioop import reverse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Quizes


class QuizesBaseView(View):
    model = Quizes
    fields = '__all__'
    success_url = reverse_lazy('quizes:all')



class QuizesListView(QuizesBaseView, ListView):
     """ view to list all Quizess, use the Quizes_
    list variable in the remplate to access all Quizes objects """
   
   
class QuizesDetailView(QuizesBaseView, DetailView):
    """ View to list details from one Quizes 
    use Quizes variable in template to acess specific Quizes here 
    and in the views bellow """

class QuizesCreateView(QuizesBaseView, CreateView):
    """ View to update Quizes """


   
class QuizesUpdateView(QuizesBaseView, UpdateView):
    """ View to update Quizes """


   
class QuizesDeleteView(QuizesBaseView, DeleteView):
    """View to delete a Quizes """