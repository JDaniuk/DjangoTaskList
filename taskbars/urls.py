from django.urls import path
from .views import( 
    index,
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskEditView,
    TaskDeleteView,
)

app_name = 'taskbars'

urlpatterns = [
    #path('', index, name='index'),
   # path('details', views.task_detail_view, name='details'),
    path('', TaskListView.as_view(), name='all-tasks'), # .as_view() essentialy converts class-based view into function based view
    path('addtask',TaskCreateView.as_view(),name='add-task'),
    path('<int:id>/',TaskDetailView.as_view(), name = 'details'),
    path('<int:id>/update',TaskEditView.as_view(),name= 'update'),
    path('<int:id>/delete/',TaskDeleteView.as_view(), name = 'delete'),
]