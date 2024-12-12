from django.urls import path
from .views import *

urlpatterns = [
    #============= Class BASED VIEW CRUD URLS ================== #
    path('',ListViewBlog.as_view(),name="list_blog"),
    path('create/',CreateViewBlog.as_view(),name="add_blog"),
    path('<int:pk>/',DetailViewBlog.as_view(),name="detail_blog"),
    path('<int:pk>/update/',UpdateViewBlog.as_view(),name="update_blog"),
    path('<int:pk>/delete/',DeleteViewBlog.as_view(),name="delete_blog"),
    
    #============= FUNCTION BASED VIEW CRUD URLS ================== #
    """  path('',list_blog,name="list_blog"),
    path('create/',add_blog,name="add_blog"),
    path('<int:pk>/',detail_blog,name="detail_blog"),
    path('<int:pk>/update/',update_blog,name="update_blog"),
    path('<int:pk>/delete/',delete_blog,name="delete_blog") """,
   
    
    

]

