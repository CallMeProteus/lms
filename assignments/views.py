from django.shortcuts import render

# Create your views here.
from audioop import reverse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Assignments


class AssignmentsBaseView(View):
    model = Assignments
    fields = '__all__'
    success_url = reverse_lazy('assignments:all')



class AssignmentsListView(AssignmentsBaseView, ListView):
     """ view to list all Assignmentss, use the Assignments_
    list variable in the remplate to access all Assignments objects """
   
   
class AssignmentsDetailView(AssignmentsBaseView, DetailView):
    """ View to list details from one Assignments 
    use Assignments variable in template to acess specific Assignments here 
    and in the views bellow """

class AssignmentsCreateView(AssignmentsBaseView, CreateView):
    """ View to update Assignments """


   
class AssignmentsUpdateView(AssignmentsBaseView, UpdateView):
    """ View to update Assignments """


   
class AssignmentsDeleteView(AssignmentsBaseView, DeleteView):
    """View to delete a Assignments """