from django.urls import path 
from .views import *

urlpatterns = [
    path('reports/', reports_view.as_view(), name = 'reports'),
    path('area_waste/', area_waste_view.as_view(), name = 'area_waste'),
    # path('course/', course_view.as_view(), name = 'course'),
    # path('type/', type_view.as_view(), name = 'type'),
    # path('activity/', activity_view.as_view(), name = 'activity'),
    # path('area/', area_view.as_view(), name = 'area'),

]