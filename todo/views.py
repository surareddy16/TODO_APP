from django.shortcuts import render,redirect
from . models import Todo
from .forms import TodoForm,RegisterForm,LoginForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, TodoForm
from .models import Todo
from django.db.models import Q
from django.contrib import messages

# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('todo_list')
#     else:
#         form = RegisterForm()
#     return render(request, 'todo/register.html', {'form': form})

# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('todo_list')
@login_required
def todo_create(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)#savins form as temporary
            todo.user = request.user#comparing form with logged in user
            todo.save()#saving the form
        return redirect('todo_list')
        
    return render(request,'todo/todo_create.html',{'form':form})

@login_required
def todo_list(request):
    todo = Todo.objects.filter(user=request.user)
    query = request.GET.get('q')
    if query:
        todo = todo.filter(Q(title__icontains=query) | Q(description__icontains=query))
    return render(request,'todo/todo_list.html',{'todo':todo})

@login_required
def todo_update(request,pk):
    todo = Todo.objects.get(id = pk,user=request.user)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    return render(request,'todo/todo_create.html',{'form':form})

@login_required
def todo_delete(request,pk):
    todo =Todo.objects.get(id = pk,user = request.user)
    todo.delete()
    return redirect('todo_list')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todo_list')
    else:
        form = RegisterForm()
    return render(request, 'todo/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                # messages.success(request, "Login successful!")
                return redirect('todo_list')
        #     else:
        #         messages.error(request, "Invalid username or password.")
        # else:
        #     messages.error(request, "Invalid form submission. Please check your input.")
    else:
        form = LoginForm()
    return render(request, 'todo/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

# @login_required
# def todo_list(request):
#     todos = Todo.objects.filter(user=request.user)
#     query = request.GET.get('q')
#     if query:
#         todos = todos.filter(Q(title__icontains=query) | Q(description__icontains=query))
#     return render(request, 'todo/todo_list.html', {'todos': todos})

# @login_required
# def todo_create(request):
#     if request.method == 'POST':
#         form = TodoForm(request.POST)
#         if form.is_valid():
#             todo = form.save(commit=False)  # Don't save yet
#             todo.user = request.user  # Associate with current user
#             todo.save()  # Save to database
#             return redirect('todo_list')
#     else:
#         form = TodoForm()
#     return render(request, 'todo/todo_create.html', {'form': form})

# @login_required
# def todo_update(request, pk):
#     todo = Todo.objects.get(id=pk, user=request.user)
#     if request.method == 'POST':
#         form = TodoForm(request.POST, instance=todo)
#         if form.is_valid():
#             form.save()
#             return redirect('todo_list')
#     else:
#         form = TodoForm(instance=todo)
#     return render(request, 'todo/todo_create.html', {'form': form})

# @login_required
# def todo_delete(request, pk):
#     todo = Todo.objects.get(id=pk, user=request.user)
#     todo.delete()
#     return redirect('todo_list')