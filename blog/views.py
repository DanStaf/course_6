from blog.models import Article
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify

"""def main_view(request):
    context = {"object": 'blog'}
    return render(request, 'main/test.html', context=context)
"""


class ArticleListView(ListView):
    model = Article

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_qty += 1
        self.object.save()

        if self.object.views_qty == 100:
            print(f'''C O N G R A T U L A T I O N S ! ! ! ! !
the Article "{self.object.title}" reached 100 views!
''')

        return self.object


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'content', 'photo',)
    success_url = reverse_lazy('blog:blog')

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()

        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'content', 'photo', 'is_published')
    # success_url = reverse_lazy('catalog:blog')

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view_article', args=[self.kwargs.get('pk')])


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:blog')

###########
