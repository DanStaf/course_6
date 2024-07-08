from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(null=True, blank=True, max_length=150, verbose_name='slug')
    content = models.TextField(verbose_name='Содержимое')
    photo = models.ImageField(null=True, blank = True, verbose_name='Изображение (превью)')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Признак публикации')
    views_qty = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        # Строковое отображение объекта
        return f'ARTICLE: {self.title}'

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'

##############
