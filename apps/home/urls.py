from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name = 'index'),
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('profile_edit/', profile_edit_view, name = 'profile_edit'),
    path('person_list/', person_list_view, name = 'person_list'),
    path('person_add/', person_add_view, name = 'person_add'),
    path('person_detail/<int:id_person>', person_detail_view, name = 'person_detail'),
    path('person_edit/<int:id_person>', person_edit_view, name = 'person_edit'),
    path('person_delete/<int:id_person>', person_delete_view, name = 'person_delete'),

    path('my_sample_list/', my_sample_list_view, name = 'my_sample_list'),
    path('sample_list/', sample_list_view, name = 'sample_list'),
    path('sample_add/', sample_add_view, name = 'sample_add'),
    path('sample_detail/<int:id_sample>', sample_detail_view, name = 'sample_detail'),
    path('sample_edit/<int:id_sample>', sample_edit_view, name = 'sample_edit'),
    path('sample_delete/<int:id_sample>', sample_delete_view, name = 'sample_delete'),
    
]
