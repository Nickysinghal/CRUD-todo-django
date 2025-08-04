from django.shortcuts import render,redirect
from .models import Todo
# Create your views here.
def todo_list(request):
    todos = Todo.objects.order_by('-id')
    return render(request,'todo/index.html',{'todos':todos})

#it renders an HTML template named index.html inside todo folder(inside your templates folder)

def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description =request.POST.get('description')
        Todo.objects.create(title=title,description=description)
    return redirect('todo_list') #this is the 'name' that we have defined in url.py 
                                #i.e path('todo/',views.todo_list,name="todo_list")
                                
def complete_todo(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed=True
    todo.save()                                
    return redirect('todo_list')

def delete_todo(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()                             
    return redirect('todo_list')