from django.test import TestCase
from taskbars.models import Task
# Create your tests here.
class TaskTestCase(TestCase):
    def setUp(self):
        #use descripton as a kind of key, it is returned by most queries, instead of title, so '[<Task: completed task>]>', not '[<Task: test1 Task>]>'
        Task.objects.create(title = 'test1',description = 'completed task',completed = True )
        Task.objects.create(title = 'test2',description = 'incomplete task',completed = False )
        pass

    def test_task_creation(self):
      "Tasks are properly created"
      tasks = Task.objects.all()
      self.assertTrue(tasks)

    #def test_task_removal(self):
     #   "Tasks are properly removed"
      #  tasks = Task.objects.all().delete()
       # print(tasks)
        #self.assertFalse(tasks)
         