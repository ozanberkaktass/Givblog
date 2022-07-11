from blog.models import navbar,Category

def index(request):
    return {
       "navbar": navbar.objects.all(),
       "categories": Category.objects.all(),
       "username": request.user.username
    }