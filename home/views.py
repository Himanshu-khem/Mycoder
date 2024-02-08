from django.shortcuts import render, HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
# Create your views here.

# home app function confegrations here
def about(request):
    #check for Authencate user
    if request.user.is_anonymous:
       messages.error(request,"Please Login To Access Content!")
       return render(request,'home/index.html')
    else:
       return render(request,'home/about.html')

def contact(request):
    
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<9 or len(phone)<3 or len(content)<3:
            messages.error(request, "Please fill the form correctly")
        else:
            
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request,"Form submitted sucessfully!")
    return render(request,'home/contact.html')

def home(request):
    # return HttpResponse("hiii im home app services page")
    return render(request,'home/index.html')
# fornt end function is here

def forntend(request):
    #check for Authencate user
    if request.user.is_anonymous:
       messages.error(request,"Please Login To Access Content!")
       return render(request,'home/index.html')
    else:
        return render(request,'home/forntend.html')
 
#courses of forntend tutorial
    # HTML course is here
def html1(request):
    if request.user.is_anonymous:
       messages.error(request,"Please Login To Access Content!")
       return render(request,'home/404handel.html')
    else:
       return render(request,'home/courses/HTMLcourse_1.html')
def htmlvideo(request):
    if request.user.is_anonymous:
       messages.error(request,"Please Login To Access Content!")
       return render(request,'home/404handel.html')
    else:
       return render(request,'home/courses/video.html')

# CSS course is here 
def css1(request):
    return render(request,'home/courses/CSScourse_1.html')

 
# online editor function is here

def onlineeditor(request):
    if request.user.is_anonymous:
       messages.error(request,"Please Login To Access Online Editor!")
       return render(request,'home/index.html')
    else:
       return render(request,'home/online_editor.html')

#signUp validation function is here

def handleSignup(request):
    if request.method == 'POST':
        # Getting the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous inputs
        if len(username) > 10:
            messages.error(request,"Username mustbe under 10 charecter!")
            return redirect("home")
        
        if pass1 != pass2:
            messages.error(request,"Password is Not Match!")
            return redirect("home")
            
        #creat user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your MYCoder Account has been Succsfully created!")
        return redirect("home")

    else:
        return render(request,'home/404handel.html')
    

# Login validation function is here
def handleLogin(request):

    if request.method == 'POST':
        # Getting the post parameters
        loginusername = request.POST['loginusername']
        logipass = request.POST['loginpass']
        
        user = authenticate(username = loginusername, password = logipass)

        if user is not None:
            login(request, user)
            messages.success(request,"Successfully Loggedin!")
            return redirect("home")
        else:
            messages.error(request,"Invalid Credntials! Please Try again!")
            return redirect("home")
    
    return render(request,'home/404handel.html')


# Logout validation function is here
def handleLogout(request):
    logout(request)
    messages.success(request,"Successfully LOGOUT!")
    return redirect("home")


#chaptcha validation 
def signuptest(request):
    import random
    num = random.randint(10000,99999)
    if request.method == 'POST':
        capcha = request.POST['captchauser']
        capenter = request.POST['capenter']
        # print(capcha)
        # print(capenter)
        if capcha == capenter:
            messages.success(request,'Capchasucessfull!')
        else:
            messages.error(request,"capcha doesnot match!")
    context = {"ran":num}
    return render(request,'home/Signup.html',context)



def newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = 'Hello, This is MyCoder'
        message = 'Thankyou For Subscribing newsletter of MyCoder. Form now You will be provided all the news and latest updates and many More!  '
        from_email = 'hchoudhary22012002@gmail.com'
        recipient_list = [email,]
        # print(email)
        send_mail(subject, message, from_email, recipient_list)
        messages.success(request,"Subsctiption sucessfull!")
        return render(request,'home/index.html')
    else:
        # return HttpResponse("Email faield")
        messages.error(request,"Email faild!")
        return render(request,'home/index.html')
      

