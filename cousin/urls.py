from django.urls import path

from cousin import views

urlpatterns = [
#     #path('cousin',views.CousinListAPIView.as_view())
       path('cousin/update/<int:pk>/',views.CousinUpdate),
       path('cousin/',views.cousin_list),
       path('cousin/<int:pk>/',views.cousin_detail),
       #path('cousin/detail/<int:pk>/',views.cousin_detail),
       path('cousin/add/',views.cousin_add),
       path('cousin/delete/<int:pk>/',views.cousin_delete),
      

]

