import typing_extensions
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from ganache.ganache_serve import contract
from dashboard.models import Client


# Create your views here.
@login_required(login_url='/accounts/login/')
def api(request):
    if request.method == 'GET':
        return HttpResponse('API blockchain')

    elif request.method == 'POST':
        print(request.POST['id'])
        return HttpResponse(request.POST['id'])


@login_required(login_url='/accounts/login/')
def get_doc(request):
    if request.method == 'GET':
        return HttpResponse('API blockchain')

    elif request.method == 'POST':
        print(request.POST)
        # user_id = request.POST['id']
        # user_bool = contract.getUser(user_id)
        return JsonResponse({'user_bool': request.POST['id']})


@login_required(login_url='/accounts/login/')
def put_doc(request):
    if request.method == 'GET':
        return HttpResponse('API blockchain')

    elif request.method == 'POST':
        # adding logic to dont transact if already verified by other and we are updating same value 
        user_id = int(request.POST['id'])
        user_bool = True if request.POST['bool'] == 'true' else False
        user_source = request.POST['source']

        print(user_id, user_bool, user_source)

        if (user_source != 'blockchain'):
            # update in blockchain 
            txn_hash = contract.addUser(user_id, user_bool)
            query = Client.objects.filter(aadhar=user_id)
            objs = list(set([x for x in query]))
            obj = objs[0]
            obj.status = user_bool 
            obj.source = 'self'
            obj.save()

            return JsonResponse({'return': txn_hash})

        elif (user_source == 'blockchain'):
            return JsonResponse({'return': 'already-exists-in-blockchain'})

