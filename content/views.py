from audioop import reverse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Content


class ContentBaseView(View):
    model = Content
    fields = '__all__'
    success_url = reverse_lazy('content:all')



class ContentListView(ContentBaseView, ListView):
     """ view to list all Contents, use the Content_
    list variable in the remplate to access all Content objects """
   
   
class ContentDetailView(ContentBaseView, DetailView):
    """ View to list details from one Content 
    use Content variable in template to acess specific Content here 
    and in the views bellow """

class ContentCreateView(ContentBaseView, CreateView):
    """ View to update Content """


   
class ContentUpdateView(ContentBaseView, UpdateView):
    """ View to update Content """


   
class ContentDeleteView(ContentBaseView, DeleteView):
    """View to delete a Content """