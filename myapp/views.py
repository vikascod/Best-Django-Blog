from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import Post, Comment
from django.contrib import messages
from myapp.templatetags import extras



# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    context = {
        'posts':allPosts
    }
    return render(request, 'myapp/bloghome.html', context)

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments =  Comment.objects.filter(post=post, parent=None)
    replies =  Comment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.sno].append(reply)
    print(replyDict)
    context = {'post':post, 'comments':comments, 'user':request.user, 'replyDict':replyDict}
    return render(request, 'myapp/blogpost.html', context)

def postComment(request):
    if request.method=="POST":
        blog_comment = request.POST.get('blog_comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get("parentSno")

        if parentSno == "":
            user_comment = Comment(blog_comment=blog_comment, user=user, post=post)
            user_comment.save()
            messages.success(request, 'Your comment successfully has been posted')
    
        else:
            parent = Comment.objects.get(sno=parentSno)
            user_comment = Comment(blog_comment=blog_comment, user=user, post=post, parent=parent)
            user_comment.save()
            messages.success(request, 'Your reply successfully has been posted')

    
    return redirect(f'/blog/{post.slug}')


