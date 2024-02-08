from django.shortcuts import render, HttpResponse
#added manually
from django.contrib import messages
# Create your views here.

# blog app function confegrations here
def bloghome(request):
    if request.user.is_anonymous:
       messages.error(request,"Please Login To Access Content!")
       return render(request,'home/index.html')
    else:
       return render(request,'blog/blog.html') 

def blogpost(request, slug):
    return HttpResponse(f"this is blog post {slug}") 