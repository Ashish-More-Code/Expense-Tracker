from django.shortcuts import render,redirect
from django.contrib import messages
from tracker.models import * 
from django.db.models import Sum,Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


def index(request):
    if request.method=='POST':
        description=request.POST.get('description')
        amount=request.POST.get('amount')
        print(description,amount)

        if description == "":
            messages.info(request, "Description Cannot be blank")
            return redirect('/')
        else:
            Transaction.objects.create(
                description=description,
                amount=amount
            )
            return redirect('/',)
        
        try:
            amount=float(amount)
        except Exception as e:
            messages.info(request, "Enter a valid value Amount")
            return redirect('/')
    else:
        context={"transactions":Transaction.objects.all(),
                 "balance":Transaction.objects.aggregate(balance=Sum('amount'))['balance'] or 0,
                "income":Transaction.objects.filter(amount__gte=0).aggregate(income=Sum('amount'))['income'] or 0,
                "expense":Transaction.objects.filter(amount__lte=0).aggregate(expense=Sum('amount'))['expense'] or 0}
        print(context)
        return render(request,'index.html',context)

def deleteTransaction(request,uid):
    Transaction.objects.get(uuid=uid).delete()
    return  redirect("/")
     
def rigistration(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        user_name=request.POST['user_name']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(Q(username=user_name)| Q(email=email)).exists():
            messages.error(request, "Username already exists")
            return redirect('/register')
        elif Q(first_name=="")| Q(last_name=="") | Q(user_name=="") | Q(email=="") |Q(password==""):
            messages.error(request, "Fields cannot be blank")
            return redirect('/register')
        else:
            User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=user_name,
                email=email,
                password=password,
            )
            messages.success(request, "Registration successfull")
            return redirect('/register')
    else:
        return render(request,'registration.html')

def login_user(request):
    if request.method=='POST':
        user_name=request.POST['user_name']
        password=request.POST['password']

        if not user_name or not password:
            messages.error(request,'Fields cannot be empty')
            return redirect('/login')
        else:
            user = authenticate(username=user_name, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
             messages.error(request,'login failed')
             return redirect('/login')
    else:
        return render(request,'login.html')
    
def logot_user(request):
    logout(request)
    messages.error(request,"Logout successful")
    return redirect('/login')