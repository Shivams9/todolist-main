from django.shortcuts import HttpResponse, render
import  datetime
from .forms import TodoForm
from .models import TodoModel





def delete(request):
    if request.POST:
        id = request.POST["id"]

        newtask = TodoModel.objects.filter(id=id)[0]
        newtask.delete()

        return render(request,"modal.html",{"message":"Deleted"})

    if request.GET:
        id = request.GET["id"]
        print(id)
        data = TodoModel.objects.filter(id=id)[0]
        print(data)
        data = {'dateoftask': data.dateoftask, 'task': data.task, "description": data.description,
                "status": data.status}

        return render(request, "update.html", {"id": id, "form": TodoForm(initial=data)})

    return render(request, "update.html")


# Create your views here.
def index(request):
    return render(request, "test.html")


def update(request):
    if request.POST:
        id = request.POST["id"]

        data = TodoForm(request.POST)
        print("Data ", data)
        newtask = TodoModel.objects.filter(id=id)[0]
        if data.is_valid():
            newtask.task = data.instance.task
            newtask.description = data.instance.description
            newtask.dateoftask = data.instance.dateoftask
            newtask.status = data.instance.status
            newtask.save()
        return HttpResponse("Updated")

    if request.GET:
        id = request.GET["id"]
        print(id)
        data = TodoModel.objects.filter(id=id)[0]
        print(data)
        data = {'dateoftask': data.dateoftask, 'task': data.task, "description": data.description,
                "status": data.status}
        return render(request, "update.html", {"id": id, "form": TodoForm(initial=data)})

    return render(request, "update.html")


def alltasks(request):
    data = TodoModel.objects.all().order_by('id').reverse()
    # data=TodoModel.objects.filter(id__gt=4)
    return render(request, "alltasks.html", {"tasks": data})


def previoustask(request):
    # data = TodoModel.objects.filter().order_by('id') dateoftask
    # data= TodoModel.objects.filter(id__gt=10)
    data = TodoModel.objects.filter(dateoftask__lt=datetime.datetime.now()).order_by('dateoftask').reverse()
    return render(request, "previoustasks.html", {"tasks": data})



def futuretask(request):

    data = TodoModel.objects.filter(dateoftask__gt=datetime.datetime.now()).order_by('dateoftask').reverse()
    return render(request, "future.html", {"tasks": data})



def between(request):
    previousdate=datetime.datetime(2022,12,11)
    futuredate=datetime.datetime(2022,12,14)

    data = TodoModel.objects.filter(dateoftask__gt=previousdate).filter(dateoftask__lt=futuredate).order_by('dateoftask').reverse()
    return render(request, "future.html", {"tasks": data})
  

def form(request):
    if request.POST:
        newtask = TodoForm(request.POST)
        if newtask.is_valid():
            newtask.save(commit=False)
            newtask.save()
            return HttpResponse("Saved")
        return HttpResponse("Not Saved")
    return render(request, "form.html", {"form": TodoForm()})




