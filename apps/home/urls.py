from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name = 'index'),
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('profile_edit/', profile_edit_view, name = 'profile_edit'),
    path('person_list/', person_list_view, name = 'person_list'),
    path('person_add/', person_add_view, name = 'person_add'),
    path('person_detail/<int:id_person>/', person_detail_view, name = 'person_detail'),
    path('person_edit/<int:id_person>/', person_edit_view, name = 'person_edit'),
    path('person_delete/<int:id_person>/', person_delete_view, name = 'person_delete'),
    path('person_status/<int:id_person>/', person_status_view, name = 'person_status'),
    
    
    path('my_sample_list/', my_sample_list_view, name = 'my_sample_list'),
    path('sample_list/', sample_list_view, name = 'sample_list'),
    path('sample_add/', sample_add_view, name = 'sample_add'),
    path('sample_detail/<int:id_sample>/', sample_detail_view, name = 'sample_detail'),
    path('sample_edit/<int:id_sample>/', sample_edit_view, name = 'sample_edit'),
    path('sample_delete/<int:id_sample>/', sample_delete_view, name = 'sample_delete'),

    # Courses,  Programs and Areas
    path('course_list/', course_list_view, name = 'course_list'),
    path('course_edit/<int:id_course>/', course_edit_view, name = 'course_edit'),
    path('course_delete/<int:id_course>/', course_delete_view, name = 'course_delete'),
    path('course_person/<int:id_person>/', course_person_view, name = 'course_person'),
    path('course_assign/<int:id_person>/<int:id_course>/', course_assign_view, name = 'course_assign'),

    # Programs
    # path('program_list/', program_list_view, name = 'program_list'),
    # path('program_edit/<int:id_program>/', program_edit_view, name = 'program_edit'),
    # path('program_delete/<int:id_program>/', program_delete_view, name = 'program_delete'),

    # Áreas and program 
    # str_view is  a variable  to program or area 
    path('<str:str_view>_list/', generic_list_view, name = 'generic_list'),
    path('<str:str_view>_add/', generic_add_view, name = 'generic_add'),
    path('<str:str_view>_edit/<int:id_view>/', generic_edit_view, name = 'generic_edit'),
    path('<str:str_view>_delete/<int:id_view>/', generic_delete_view, name = 'generic_delete'),
    
]
