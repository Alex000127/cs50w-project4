from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from .models import User, Post, Follow, Like
import json

def index(request):
    allposts = Post.objects.all().order_by('-id')
    paginator = Paginator(allposts, 10)
    page_number = request.GET.get('page')
    postsPage = paginator.get_page(page_number)
    liked_dict = {}

    if request.user.is_authenticated:
        likes = Like.objects.filter(user=request.user)
        liked_dict = {like.post.id: True for like in likes}

    return render(request, "network/index.html", {
        "postsPage": postsPage,
        "liked": liked_dict
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def new_post(request):
    if request.method == "POST":
        cUser = User.objects.get(pk=request.user.id)
        content = request.POST["newpost-content"]
        newPost = Post(user=cUser, content=content)
        newPost.save()
        
        return HttpResponseRedirect(reverse(index))

def profile(request, user_id):
    cUser = get_object_or_404(User, pk=user_id)
    allposts = Post.objects.filter(user=cUser).order_by('-id')
    following = Follow.objects.filter(user=cUser)
    followers = Follow.objects.filter(userF=cUser)

    isfollowing = False
    if request.user.is_authenticated:
        try:
            isfollowing = Follow.objects.filter(user=request.user, userF=cUser).exists()
        except User.DoesNotExist:
            isfollowing = False

    paginator = Paginator(allposts, 10)
    page_number = request.GET.get('page')
    postsPage = paginator.get_page(page_number)
    
    return render(request, "network/profile.html", {
        "allposts": allposts,
        "postsPage": postsPage,
        "following": following,
        "followers": followers,
        "username": cUser.username,
        "isfollowing": isfollowing,
        "userP": cUser
    })

def following(request):
    cUser = User.objects.get(pk=request.user.id)
    peopleF = Follow.objects.filter(user=cUser)
    allposts = Post.objects.all().order_by('-id')
    postsF = []
    
    for post in allposts:
        for person in peopleF:
            if person.userF == post.user:
                postsF.append(post)
    #pagination
    paginator = Paginator(postsF, 10)
    page_number = request.GET.get('page')
    postsPage = paginator.get_page(page_number)
    
    return render(request, "network/following.html",{
        "postsPage":postsPage
    })

def follow(request):
    if request.method == 'POST':
        userfollow = request.POST.get('userfollow')
        cUser = request.user
        userfollowdata = get_object_or_404(User, username=userfollow)

        if cUser != userfollowdata:
            existing_follow = Follow.objects.filter(user=cUser, userF=userfollowdata).first()
            if not existing_follow:
                f = Follow(user=cUser, userF=userfollowdata)
                f.save()
        user_id = userfollowdata.id
        return HttpResponseRedirect(reverse('profile', kwargs={'user_id': user_id}))
    return redirect('index')

def unfollow(request):
    if request.method == 'POST':
        userfollow = request.POST.get('userfollow')
        cUser = request.user
        userfollowdata = get_object_or_404(User, username=userfollow)

        f = Follow.objects.filter(user=cUser, userF=userfollowdata).first()
        if f:
            f.delete()

        user_id = userfollowdata.id
        return HttpResponseRedirect(reverse('profile', kwargs={'user_id': user_id}))
    return redirect('home')

def edit(request, post_id):
    if request.method == "POST":
        data = json.loads(request.body)
        edit_post = Post.objects.get(pk=post_id)
        edit_post.content = data["content"]
        edit_post.save()
        return JsonResponse({"message": "change successful", "data":data["content"]})

def removeLIKE(request, post_id):
    post = Post.objects.get(pk=post_id)
    user = request.user
    Like.objects.filter(user=user, post=post).delete()
    
    like_count = Like.objects.filter(post=post).count()
    
    return JsonResponse({"message": "Like removed", "liked": False, "like_count": like_count})

def addLIKE(request, post_id):
    post = Post.objects.get(pk=post_id)
    user = request.user
    # Asegúrate de no agregar un like duplicado
    if not Like.objects.filter(user=user, post=post).exists():
        Like.objects.create(user=user, post=post)
    
    like_count = Like.objects.filter(post=post).count()
    
    return JsonResponse({"message": "Like added", "liked": True, "like_count": like_count})
