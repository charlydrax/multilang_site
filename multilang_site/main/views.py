from django.views import generic
from .models import Post

#une class pour les articles en globale
class PostList(generic.ListView):
    queryset = Post.object.filter(status=1).order_by('created_on') #on affiche que les post qui on le status = 1 du plus récent au plus ancien
    template_name = 'index.html'
    
#une class pour avoir les détails des articles
class DetailView(generic.DetailView):
    model = Post
    template_name = 'post_details.html'