from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Client
from .forms import ClientForm
from infura.infura_serve import contract


# Create your views here.

@login_required(login_url='/accounts/login/')
def homepage(request):
    form = ClientForm()
    query = Client.objects.filter(author=request.user)
    objs = list(set([x for x in query]))

    if request.method == "GET":
        context = {'form': form, 'clients': objs}
        return render(request=request,template_name="dashboard/index.html", context=context)

    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user

            # updating object status with blockchain
            obj_status = contract.getUser(int(obj.aadhar))
            print(obj_status)
            if obj_status == True:
                obj.source = 'blockchain'
            else:
                obj.source = 'self'
            obj.status = obj_status

            obj.save()

        context = {'form': form}
        return redirect('/dashboard')