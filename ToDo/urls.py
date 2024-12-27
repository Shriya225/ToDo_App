from django.urls import path
from .import views

urlpatterns = [
    path('addTask/',views.addTask,name="addTask"),
    path("",views.ViewTasks,name="viewTasks"),
    path("task/<int:pk>/edit/",views.editView,name="edit"),
 path('delete-item/<int:item_id>/', views.delete_item, name='delete_item'),
 path('profile/',views.profile,name="profile"),
]
