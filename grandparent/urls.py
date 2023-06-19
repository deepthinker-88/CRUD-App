from django.urls import path
from . import views

urlpatterns = [
    #path('grandparent/',views.GrandparentListView.as_view())
    path('grandparent/',views.grandparent_list,name='grandparent_list'),
    path('grandparent/<int:pk>',views.grandparent_detail),
    path('grandparent/add',views.grandparent_add),
    path('grandparent/update/<int:pk>',views.grandparent_update),
    path('grandparent/delete/<int:pk>',views.grandparent_delete)
]
