from django.shortcuts import render,redirect
from django.contrib import messages
from tracker.models import * 

def index(request):
    if request.method=='POST':
        description=request.POST.get('description')
        amount=request.POST.get('amount')
        print(description,amount)

        if description == "":
            messages.info(request, "Description Cannot be blank")
            return redirect('/')
        elif not amount.isdigit():
            messages.info(request, "Enter a valid value Amount")
            return redirect('/')
        else:
            Transaction.objects.create(
                description=description,
                amount=amount
            )

    context={"transactions":Transaction.objects.all()}
    return render(request,'index.html',context)
