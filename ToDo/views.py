from django.shortcuts import render,redirect,get_object_or_404
from ToDo.forms import AddTask,editForm,UserProfileForm,UserForm
from .models import Task,UserProfile
from django.http import JsonResponse, HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


# from .signals import task_done
# Create your views here.
@login_required
def addTask(req):
    if req.method=='POST':
        form=AddTask(req.POST)
        if form.is_valid():
            print("task done!!")

            # task_done.send(sender=req.user,message="hello",user=req.user,form=form)

            form = form.save(commit=False)
            form.user = req.user  # Assign the logged-in user to the task
            form.save()
        else:
            print("invalid form")
        return redirect("viewTasks")
    else:
        form=AddTask()
    return render(req,"addTask.html",{'form':form})

    

@login_required
def ViewTasks(request):
    query = request.GET.get('q', '')  # Get the search query from the request
    sortby = request.GET.get('sortby', '')  # Get the search query from the request
    if query:
       all_objs = Task.objects.filter(
    user=request.user
).filter(
    Q(title__icontains=query) | Q(description__icontains=query)
)
    else:
        all_objs = Task.objects.filter(user=request.user)  # Show all tasks for the logged-in user

    if sortby=="Time":
        all_objs=all_objs.order_by("due_date")
    elif sortby=="Title":
        all_objs=all_objs.order_by("title")

    return render(request, 'ToDo.html', {'all_objs':all_objs, 'query': query})



@login_required
def editView(request,pk):
    task=get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
        form = editForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('viewTasks')  # Redirect to your task list or desired page
    else:
        form = editForm(instance=task)
    return render(request,"editForm.html",{'form':form})

@login_required
def delete_item(request,item_id):
    if request.method =="DELETE":
        task=get_object_or_404(Task,pk=item_id)
        task.delete()
        return JsonResponse({'message': 'Task deleted successfully!'})
    return HttpResponseNotAllowed(['DELETE'])

@login_required
def profile(request):
    user = request.user  # Get the logged-in user
   
    try:
        profile = user.userprofile  # Access the related UserProfile
    except ObjectDoesNotExist:
        profile = UserProfile.objects.create(user=user)
    # Create the forms for User and UserProfile
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)  # To handle file uploads (e.g. profile picture)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserForm(instance=user)
        profile_form = UserProfileForm(instance=profile)

    return render(request, "profile.html", {
        'user_form': user_form,
        'profile_form': profile_form,
        "user":user
    })



