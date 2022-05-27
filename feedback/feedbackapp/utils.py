from django.db.models import Count

from .models import Category, Feedback

menu = [
    {'title': "Главная страница", 'url_name': 'home'},
    {'title': "Добавить отзыв", 'url_name': 'add_page'},
]


class DataMixin:
    def get_user_context(self, *, object_list=None, **kwargs):
        paginate_by = 4
        context = kwargs
        cats = Category.objects.annotate(Count('feedback'))
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu
        context['cats'] = cats
        return context
