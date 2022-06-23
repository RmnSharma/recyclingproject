from django.shortcuts import render, redirect
from django.views.generic import TemplateView,ListView
from app.forms import contactform,scheduleform,aptform,mailform
from app.models import blog
# Create your views here.

class homeview(TemplateView):
    template_name="home.html" 
class aboutview(TemplateView):
	template_name="about.html"
class formview(TemplateView):
    template_name="form.html"
class recycleview(TemplateView):
    template_name="recycle.html"
class servicesview(TemplateView):
    template_name="services.html"
class aboutview(TemplateView):
    template_name="about.html"
class contactsview(TemplateView):
    template_name="contacts.html"
class appointmentview(TemplateView):
    template_name="appointment.html"
class blogview(TemplateView):
    template_name="blog.html"
class jsview(TemplateView):
    template_name="js.html"
class js1view(TemplateView):
    template_name="js1.html"
class js2view(TemplateView):
    template_name="js2.html"
class js3view(TemplateView):
    template_name="js3.html"
class jq1view(TemplateView):
    template_name="jq1.html"
class blogview(ListView):
    template_name='blog.html'
    def get_queryset(self):
        return blog.objects.all()
    
    
def insertcontact(request):
    if request.method=='POST':
        form=contactform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contacts/')
        else:
            form=contactform()
            return render(request,"contacts.html",{'form':form})

def insertschedule(request):
    if request.method=='POST':
        form=scheduleform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/recycle/')
        else:
            form=scheduleform()
            return render(request,"recycle.html",{'form':form})
    
def insertapt(request):
    if request.method=='POST':
        form=aptform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/appointment/')
        else:
            form=aptform()
            return render(request,"appointment.html",{'form':form})
    
def insertmail(request):
    if request.method=='POST':
        form=mailform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/recycle/')
        else:
            form=mailform()
            return render(request,"recycle.html",{'form':form})
    