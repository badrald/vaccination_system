from django.urls import path
from . import views


urlpatterns = [
    path('',views.index_view,name="index_view"),
    path('JobPlaces/',views.job_place,name="job_places"),
    path('Vaccination/',views.vacciantion,name="vaccination"),
]
