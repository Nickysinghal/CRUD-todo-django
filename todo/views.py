from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from .models import Todo
from django.contrib import messages
# Create your views here.
def todo_list(request):
    todos = Todo.objects.order_by('-id')
    return render(request,'todo/index.html',{'todos':todos})

#it renders an HTML template named index.html inside todo folder(inside your templates folder)

def create_todo(request):
    if request.method == 'POST':
        langs = request.POST.getlist('lang') 
        title = request.POST.get('title')   
        description =request.POST.get('description')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        priority = request.POST.get('priority')
        languages = ','.join(langs)
        Todo.objects.create(title=title,description=description, email=email, phone=phone, priority=priority, languages=languages)
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

def update_todo(request,todo_id):
    t = get_object_or_404(Todo,id=todo_id)
    if request.method=='POST':
        data = request.POST
        title = data.get('title')
        description = data.get('description')
        email = data.get('email')
        phone= data.get('phone')
        priority = data.get('priority')
        langs = data.getlist('lang')
        languages = ','.join(langs)
        
        t.title = title
        t.description= description
        t.email=email
        t.phone = phone
        t.priority= priority
        t.languages= languages
        
        t.save()
        return redirect('/')
    context = { 'todo' : t}
    return render(request, 'todo/update.html', context)
    # return HttpResponse("update page")