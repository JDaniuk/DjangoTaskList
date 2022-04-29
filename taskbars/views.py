from django.shortcuts import render, get_object_or_404

from django.urls import reverse

from .models import Task

from django.views.generic import ( #import build in views from django
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
    )
from .forms import TaskCreateForm, TaskEditForm
# Create your views here.
def index(request):
    return render(request, "index.html" )

#def task_detail_view(request): Too complicated, Use build in functions
 #   obj = Task.objects.all().values_list()
  #  context = {
   #     'object':obj,
    #    }
    #return render(request, "details.html",context)

    #this is better and simpler:
class TaskListView(ListView):
    queryset = Task.objects.all() #queryset is required, Task.objects.all() returns all Task objects from database
    # by default it looks for a template in <app_name>/modelname_list.html
    template_name = 'index.html'


#def task_create_view(request):
 #   form = TaskCreateForm(request.POST or None)
 #   if form.is_valid():
  #      form.save()
   # context = {
    #    'form' : form
     #   }
    #return render(request,'addtask.html',context)

class TaskDetailView(DetailView):
    #queryset = Task.objects.all() #optional, simply limits the choices and options
    template_name = 'details.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Task, id=id_)


class TaskCreateView(CreateView):
    template_name = 'addtask.html'
    queryset = Task.objects.all()
    form_class = TaskCreateForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class TaskEditView(UpdateView):
    template_name = 'edit.html'
    queryset = Task.objects.all()
    form_class = TaskEditForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Task, id=id_)
  

class TaskDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Task
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Task, id=id_)

    def get_success_url(self):
        return reverse('taskbars:all-tasks')
    
