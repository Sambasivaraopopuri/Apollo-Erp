from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from . models import *
# Create your views here.
def user_login(request):
    if request.method=="POST":
        admin = authenticate( username=request.POST["username"], password=request.POST["password"])
        if admin is not None:
            if admin.is_staff:
                login(request,admin)
                return redirect("administrator")
            elif admin is not None:
                login(request,admin)
                return redirect("evaluator")
        else:
            return HttpResponse("Check User Name & Password")
    return render(request,"login.html",{})

@login_required
def add_vender(request):
    if request.method=="POST":
        if request.user.is_staff!=False:
            vender=Vender.objects.create(admin_id=request.user.id,
            first_name=request.POST["fristname"],
            last_name=request.POST["lastname"],
            phone=request.POST["phone"],adders=request.POST["user_addres"],region_code_id=request.POST["region"],
            item_id=request.POST["items"])
            Vender_review.objects.create(vender_id=vender.id,evaluator_id=request.user.id)
            return redirect("administrator")
        else:
            return HttpResponse("<b>You don't have access</b>")
    return render(request,"add_vender.html",{"user":request.user,"regions":Region_code.objects.filter(user=request.user),
                                             "item":Items.objects.filter(admin=request.user)})

@login_required
def administrators(request):
    return render(request,"admin.html",{"user":request.user,"vender":Vender.objects.all()})
@login_required
def vender_edit(request,id):
    vender=Vender.objects.get(id=id)
    if request.method=="POST":
        vender.first_name=request.POST["fristname"]
        vender.last_name=request.POST["lastname"]
        vender.phone=request.POST["phone"]
        vender.adders=request.POST["user_addres"]
        vender.region_code_id=request.POST["region"]
        vender.item_id=request.POST["items"]
        vender.save()
        return redirect("administrator")
    return render(request,"add_vender.html",{"data":Vender.objects.get(id=id),"regions":Region_code.objects.filter(user=request.user),"item":Items.objects.filter(admin=request.user)})
@login_required
def add_item(request):
    if request.method=="POST":
        Items.objects.create(admin=request.user,name=request.POST["name"])
        return redirect("administrator")
    return render(request,"add_item.html",{})

@login_required
def add_region(request):
    if request.method=="POST":
        Region_code.objects.create(user=request.user,pincode=request.POST["name"])
        return redirect("administrator")
    return render(request,"add_item.html",{})
@login_required
def evaluator(request):
    vender=Vender.objects.all()
    vender_review=Vender_review.objects.all()
    return render(request,"evaluator.html",{"user":request.user,"vender":vender,"vender_review":vender_review})
@login_required
def comments_edit(request,id):

    return render(request,"comment.html",{"vender":Vender_review.objects.get(id=id)})
@login_required
def comments(request,id):
    vender=Vender.objects.get(id=id)
    vender_review=Vender_review.objects.filter(vender_id=vender.id).first()
    if request.method=="POST":
        vender_review.rating=request.POST["rating"]
        vender_review.comments=request.POST["comments"]
        vender_review.feedback=request.POST["test"]
        vender_review.save()
        return redirect("evaluator")
    return render(request,"comment.html",{"vender":vender})
@login_required
def fun_logout(request):
    logout(request)
    return redirect("login")
@login_required
def delete(request,id):
    vender=Vender.objects.get(id=id)
    vender__review=Vender_review.objects.filter(vender=vender.id)
    vender__review.delete()
    vender.delete()
    return redirect("administrator")