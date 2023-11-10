from django.urls import path
from. import views
from django.urls import path
from search_app.views import SearchResults

app_name='search_app'

urlpatterns=[
    path('',views.SearchResults,name='SearchResults'),

]