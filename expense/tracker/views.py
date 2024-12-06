from django.shortcuts import render,redirect
from django.contrib import messages
from tracker.models import * 
from django.db.models import Sum

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
     
