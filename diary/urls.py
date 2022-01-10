from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('detail/<post_id>', views.detail, name='detail'),
    path('edit/<post_id>', views.edit, name='edit'),
    path('update/<post_id>', views.update, name='update'),
    path('delete/<post_id>', views.delete, name='delete'),
]
