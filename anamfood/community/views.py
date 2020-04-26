from django.shortcuts import render,get_object_or_404, redirect
from .models import Community, Comment
from .forms import CommunityForm, CommentForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    communities=Community.objects.all()
    context={
        'communities':communities
    }
    return render(request,'community/index.html',context)


def detail(request,pk):
    community=Community.objects.get(pk=pk)
    form=CommentForm()
    context={
        'community':community,
        'form':form
    }
    return render(request,'community/detail.html',context)

@login_required
@require_POST
def delete(request, pk):
    community=get_object_or_404(Community, pk=pk)
    community.delete()
    return redirect('community:index')


@login_required
def create(request):
    if request.method=='POST':
        form=CommunityForm(request.POST)
        if form.is_valid():
            community=form.save(commit=False)
            community.user=request.user
            community.save()
            return redirect('community:detail',community.pk)
    else:
        form=CommunityForm()
    context={
        'form':form
    }
    return render(request,'community/form.html',context)


@login_required
def update(request,pk):
    community=get_object_or_404(Community,pk=pk)
    if request.method=='POST':
        form=CommunityForm(request.POST,instance=community)
        if form.is_valid():
            community=form.save()
            return redirect('community:detail',community.pk)
    else:
        form=CommunityForm(instance=community)
    context={
        'form':form,
        'pk':pk
    }
    return render(request,'community/form.html',context)

def map(request,pk):
    community=get_object_or_404(Community,pk=pk)
    context={
        'community':community
    }
    return render(request,'community/map.html',context)

def map2(request,pk):
    community=get_object_or_404(Community,pk=pk)
    context={
        'community':community
    }
    return render(request,'community/map2.html',context)

@require_POST
@login_required
def create_comment(request,community_pk):
    community=get_object_or_404(Community, pk=community_pk)
    form=CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user=request.user
        comment.community = community
        comment.save()
        return redirect('community:detail', community_pk)


@require_POST
@login_required
def delete_comment(request, community_pk, comment_pk):
    comment=get_object_or_404(Comment, pk=comment_pk)
    if comment.user == request.user:
        comment.delete()
        return redirect('community:detail', community_pk)