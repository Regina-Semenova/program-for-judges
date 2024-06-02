from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from law_app.forms import CreateQueryForm, EditQueryForm
from law_app.models import Query, Judge, Assistant
from django.forms.models import model_to_dict
from copy import copy

# Create your views here.
@login_required(login_url='login')
def index(request):
    if (request.user.groups.filter(name='judges').exists()):
        queries = Query.objects.filter(judge=Judge.objects.get(user=request.user.id))
        username = Judge.objects.get(user=request.user.id).judge_name
    if (request.user.groups.filter(name='assistants').exists()):
        queries = Query.objects.filter(judge=Judge.objects.get(assistant=Assistant.objects.get(user=request.user.id)))
        username = Assistant.objects.get(user=request.user.id).assistant_name

    context = {
        'queries': queries,
        'username': username,
    }

    return render(request, "law_app/index.html", context)

def login(request):
    return render(request, "law_app/login.html")

@login_required(login_url='login')
def create_new(request):
    if (request.user.groups.filter(name='judges').exists()):
        username = Judge.objects.get(user=request.user.id).judge_name
        if request.method == 'POST':
            form = CreateQueryForm(data=request.POST, id=request.user.id)
            if form.is_valid():
                qtype = form.cleaned_data['query_type']
                case_num = form.cleaned_data['case']
                pri = form.cleaned_data['priority']
                comm = form.cleaned_data['query_comments']
                judge = Judge.objects.get(user=request.user.id)
                new_q = Query(query_type = qtype, judge = judge, case = case_num, priority = pri, query_comments = comm)
                new_q.save()
                return HttpResponseRedirect('/')
        else:
            form = CreateQueryForm(id=request.user.id)

        context = {
            'form': form,
            'username': username,
        }

        return render(request, 'law_app/qnew.html', context)
    else:
        return HttpResponseRedirect('/')

@login_required(login_url='login')
def edit(request, qid):
    qry = Query.objects.get(query_id=qid)
    if (request.user.groups.filter(name='judges').exists()):
        username = Judge.objects.get(user=request.user.id).judge_name
        if (qry.judge != Judge.objects.get(user=request.user.id).judge_id):
            return HttpResponseRedirect('/')
    if (request.user.groups.filter(name='assistants').exists()):
        username = Assistant.objects.get(user=request.user.id).assistant_name
        if (qry.judge != Assistant.objects.get(user=request.user.id).judge_id):
            return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = EditQueryForm(data=UPOST(request.POST, qry), user=request.user)
        if form.is_valid():
            qry.query_type = form.cleaned_data['query_type']
            qry.case = form.cleaned_data['case']
            qry.priority = form.cleaned_data['priority']
            qry.assistant = form.cleaned_data['assistant']
            qry.status = form.cleaned_data['status']
            qry.query_comments = form.cleaned_data['query_comments']
            qry.save()
            
            return HttpResponseRedirect('/')
    else:
        form = EditQueryForm(instance=qry, user=request.user)

    context = {
        'form': form,
        'num': qry.query_id,
        'username': username,
    }

    return render(request, 'law_app/q.html', context)

    
def UPOST(post, obj):
    '''Updates request's POST dictionary with values from object, for update purposes'''
    post = copy(post)
    for k,v in model_to_dict(obj).items():
        if k not in post: post[k] = v
    return post