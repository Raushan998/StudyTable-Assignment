from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.

def get_view(request):
    return render(request,'index.html',{'step_1':True})

def index(request):
    if request.method=="POST":
        
        name=request.POST.get('name')
        subject1=request.POST.get('subject1')
        subject2=request.POST.get('subject2')
        subject3=request.POST.get('subject3')
        subject4=request.POST.get('subject4')
        subject5=request.POST.get('subject5')
        subject6=request.POST.get('subject6')
        if name:
            user = request.session.get('user')
            if user:
                user['name']=name;
                request.session['user'] = user
            else:
                print(user)
                user={"name":name}
                request.session['user']=user;
            return render(request,'index.html',{'step_3':True,'step':True})
        elif subject1:
            user = request.session.get('user')
            print(user)
            if user:
                user['subject1'] = subject1
                request.session['user'] = user
            else:
                print(user)
                user = {"subject1":subject1}
                request.session['user'] = user
            return render(request, 'index.html', {'step_4': True,'step':True})
        elif subject2:
            user = request.session.get('user')
            print(user)
            if user:
                user['subject2'] = subject2
                request.session['user'] = user
            else:
                print(user)
                user = {"subject2": subject2}
                request.session['user'] = user
            return render(request, 'index.html', {'step_5': True,'step':True})
        elif subject3:
            user = request.session.get('user')
            print(user)
            if user:
                user['subject3'] = subject3
                request.session['user'] = user
            else:
                print(user)
                user = {"subject3": subject3}
                request.session['user'] = user
            return render(request, 'index.html', {'step_6': True,'step':True})
        elif subject4:
            user = request.session.get('user')
        
            if user:
                user['subject4'] = subject4
                request.session['user'] = user
            else:
                print(user)
                user = {"subject4": subject4}
                request.session['user'] = user
            return render(request,'index.html', {'step_7': True,'step':True})
        elif subject5:
            user = request.session.get('user')
            if user:
                user['subject5'] = subject5
                request.session['user'] = user
            else:
                print(user)
                user = {"subject5": subject5}
                request.session['user'] = user
            return render(request, 'index.html', {'step_8': True,'step':True})
        elif subject6:
            user = request.session.get('user')
            user['subject6']=subject6;
            request.session['user']=user;
            user = request.session.get('user')
            print(user)
            student={}
            for key,value in user.items():
                student[key]=value;
            context={
                'student':student
                }
            return render(request,'details.html',context)


    return render(request,'index.html',{'step_2':True,'step':True})
