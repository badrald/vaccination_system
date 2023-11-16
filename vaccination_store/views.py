from django.shortcuts import render
from django.http import JsonResponse
from .models import JobPlace,Vaccination
from .form import JobPlaceForm,VaccinationForm
from django.contrib.auth.decorators import user_passes_test,login_required


def is_superuser(user):
    return user.is_superuser
def superuser_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)

# Create your views here.
def index_view(request):
    return render(request,"vaccination_store/index.html")

@login_required
@superuser_required
def vacciantion(request):
    if request.method == "POST":
        form= VaccinationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"message":"success"},status=201)
        else :
            return JsonResponse({"error":"there's error"},status=400)
    form = VaccinationForm()
    vaccinations=Vaccination.objects.all()
    context= {"form":form,"vaccinations":vaccinations}
    return render(request, "vaccination_store/vaccination.html",context)

@login_required
@superuser_required
def job_place(request):
    if 'id' in  request.POST:
        id = request.POST['id']
        obj = JobPlace.objects.get(pk=id)
        obj.delete()
        return JsonResponse({"success":"the job deleted successfuly "},status=200)
    if request.method == "POST":
        form = JobPlaceForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success":"the job place added successfuly "},status=200)
    job_places = JobPlace.objects.all()
    form = JobPlaceForm()
    return render(request,"vaccination_store/job_place.html",{"job_places":job_places,"form":form})
