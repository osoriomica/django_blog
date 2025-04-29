from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Post
from .forms import CommentForm

# Create your views here.
class PostList(generic.ListView):
    # model = Post -now redundant by queryset
    queryset = Post.objects.filter(status=1)
    # template_name = 'post_list.html' - deleting post_list.html as we are using index.html
    # above line is redundant by django's default naming rule which is <app_name>/<model_name>_list.html
    template_name = 'blog/index.html'
    paginate_by = 6

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        print("Request method is POST")
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your comment is awaiting approval.",
            )

    comment_form = CommentForm()
    print("About to render template")
    
    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            
            },

    )