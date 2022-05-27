from django.http import HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from .forms import AddPostForm
from .models import *
from .utils import DataMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class FeedbackHome(DataMixin, ListView):
    model = Feedback
    template_name = 'feedback/index.html'
    context_object_name = 'info'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return c_def | context

    def get_queryset(self):
        return Feedback.objects.filter(is_published=True)


class FeedbackDetail(DataMixin, DetailView):
    model = Feedback
    template_name = 'feedback/feed.html'
    context_object_name = 'feed'
    slug_url_kwarg = 'slug_feed'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['feed'])
        return c_def | context


class FeedbackCategory(DataMixin, ListView):
    model = Feedback
    template_name = 'feedback/index.html'
    context_object_name = 'info'
    slug_url_kwarg = 'slug_category'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['info'][0].cat),
                                      cat_selected=context['info'][0].cat_id)
        return c_def | context

    def get_queryset(self):
        return Feedback.objects.filter(cat__slug=self.kwargs['slug_category'], is_published=True)


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страницы не существует или она недоступна')


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'feedback/addpage.html'
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавить отзыв')
        return c_def | context


class DeletePage(DeleteView):
    model = Feedback
    template_name = 'feedback/delete_feedback.html'
    context_object_name = 'feed'
    slug_url_kwarg = 'slug_feed'
    success_url = reverse_lazy('home')


class UpdatePage(UpdateView):
    model = Feedback
    context_object_name = 'feed'
    form_class = AddPostForm
    template_name = 'feedback/update_page.html'
    slug_url_kwarg = 'slug_feed'


