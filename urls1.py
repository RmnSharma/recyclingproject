from django.urls import path,include
from app import views
urlpatterns = [
    path('',views.homeview.as_view()),
	path('about/',view.aboutview.as_view()),
]
