from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

# Create your views here.
def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html',
        {'all_items': all_todo_items})

def addTodo(request):
    c = request.POST['content'] #find content in post request called "content"
    #create a new todo all_item
    new_item = TodoItem(content =c)
    # save
    new_item.save()
    # redirect the rowser to'/todo/'
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    # redirect the rowser to'/todo/'
    return HttpResponseRedirect('/todo/')
     
