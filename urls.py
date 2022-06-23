from django.urls import path,include
from app import views
urlpatterns = [
    path('',views.homeview.as_view()),
    path('about/',views.aboutview.as_view()),
    path('form/',views.formview.as_view()),
    path('recycle/',views.recycleview.as_view()),
    path('services/',views.servicesview.as_view()),
    path('about/',views.aboutview.as_view()),
    path('contacts/',views.contactsview.as_view()),
    path('appointment/',views.appointmentview.as_view()),
    path('blog/',views.blogview.as_view()),
    path('js/',views.jsview.as_view()),
    path('js1/',views.js1view.as_view()),
    path('js2/',views.js2view.as_view()),
    path('js3/',views.js3view.as_view()),
    path('jq1/',views.jq1view.as_view()),
    path('insertcontact/',views.insertcontact),
    path('insertschedule/',views.insertschedule),
    path('insertapt/',views.insertapt),
    path('insertmail/',views.insertmail),
]
