from django.urls import path

from parent import views
urlpatterns = [
    path('parent/update/<int:pk>/',views.parent_update),
    path('parent/',views.parent_list),
    path('parent/add',views.parent_add),
    path('parent/<int:pk>',views.parent),
    path('parent/delete/<int:pk>',views.parent_delete),
]
