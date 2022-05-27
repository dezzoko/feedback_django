from django.db import models
from pytils.translit import slugify
from django.urls import reverse


class Feedback(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    content = models.TextField(verbose_name='Текст')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='url')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('feed', kwargs={'slug_feed': self.slug})

    def save(self, *args, **kwargs):  # для создания слаг поля
        self.slug = slugify(self.title)
        super(Feedback, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-time_create', 'title']


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='url')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug_category': self.slug})

    def save(self, *args, **kwargs):  # для создания слаг поля
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
