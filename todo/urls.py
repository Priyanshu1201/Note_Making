from django.urls import path
from .views import insert,delete,show_data,edit

app_name = 'todo'

urlpatterns = [
    path('', insert, name='insert'),
    path('show/<str:id>', show_data, name='show'),
    path('edit/<str:id>', edit, name='edit'),
    path('delete/<str:id>', delete, name='delete')
]