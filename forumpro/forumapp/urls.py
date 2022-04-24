from django.urls import path
from .views import home ,addInForum,addInDiscussion
urlpatterns=[
    path('',home,name='home'),
    
    path('addInForum/',addInForum,name='addInForum'),
    path('addInDiscussion/',addInDiscussion,name='addInDiscussion')
]