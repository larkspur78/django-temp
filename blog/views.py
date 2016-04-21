from django.shortcuts import render
from .models import Post
#every view function takes in a request object as its argument
def post_list(request):
    #based on this request, we can render our page
    #in second positional arg, we specify position of template
    #it will look in templates folder automatically
    #giving it a python dictionary thirs positional arg
    return render(request, 'blog/post_list.html', {
        'posts': Post.objects.all()
    })
    #what steps do we still need to get it to show up on website?
    #we need an endpoint
# Create your views here.
