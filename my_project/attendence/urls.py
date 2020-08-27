from django.urls import path

from attendence import views

urlpatterns = [
    path('view_show',views.view_show,name='records'),
    path('add',views.add),
    path('search',views.search,name='results'),
]