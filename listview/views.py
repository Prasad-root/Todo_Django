from django.shortcuts import render,redirect
from .models import TodoTable
from django.http import HttpResponse

def dashboard(request):
    current_user = request.user
    user_id = current_user.id
    todo_list = TodoTable.objects.filter(user_id=user_id)
    return render(request, "tableview.html", {'data': todo_list,'current_user_name':current_user.first_name})

def update_load(request,_update_id):
    data = TodoTable.objects.get(task_id = _update_id)
    return render(request,"update_page.html",{'data':data})

def update_task(request,update_id):
    try:
        if request.method == "POST":

            task_name = request.POST['taskname']
            task_disc = request.POST['taskdisc']
            date = request.POST['date']
            time = request.POST['time']

            chanage_row = TodoTable.objects.get(task_id = update_id)

            chanage_row.task_name = task_name
            chanage_row.task_disc = task_disc
            chanage_row.date = date
            chanage_row.time = time

            chanage_row.save()

            return redirect('/Dashboard')
    except:
        return redirect('/Dashboard')
        


def delete(request,delete_id):
    datarow = TodoTable.objects.get(task_id = delete_id)
    datarow.delete()
    return redirect("/Dashboard")

def changeStatus(request,changestate_id):
    should_chanage_row = TodoTable.objects.get(task_id = changestate_id)
    should_chanage_row.task_status = not should_chanage_row.task_status
    should_chanage_row.save()
    return redirect('/Dashboard')

def addTask(request):
    if request.method == "POST":
        taskname = request.POST['taskname']
        taskdisc = request.POST['taskdisc']
        date = request.POST['date']
        time = request.POST['time']

        current_user = request.user

        task = TodoTable.objects.create(task_name = taskname,task_disc = taskdisc,task_date = date,task_time = time,user_id_id = current_user.id)
        task.save()
        return redirect('/Dashboard')
    else:
        return render(request,"task_add_form.html")