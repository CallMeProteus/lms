from django.shortcuts import render

# Create your views here.
from audioop import reverse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Announcements


class AnnouncementsBaseView(View):
    model = Announcements
    fields = '__all__'
    success_url = reverse_lazy('announcements:all')



class AnnouncementsListView(AnnouncementsBaseView, ListView):
     """ view to list all Announcementss, use the Announcements_
    list variable in the remplate to access all Announcements objects """
   
   
class AnnouncementsDetailView(AnnouncementsBaseView, DetailView):
    """ View to list details from one Announcements 
    use Announcements variable in template to acess specific Announcements here 
    and in the views bellow """

class AnnouncementsCreateView(AnnouncementsBaseView, CreateView):
    """ View to update Announcements """


   
class AnnouncementsUpdateView(AnnouncementsBaseView, UpdateView):
    """ View to update Announcements """


   
class AnnouncementsDeleteView(AnnouncementsBaseView, DeleteView):
    """View to delete a Announcements """