from django.db import models


class Blog(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок",
        help_text="Введите заголовок поста",
    )

    content = models.TextField(
        verbose_name="Содержимое", help_text="Введите контент блога"
    )

    photo = models.ImageField(
        upload_to="blog/photo",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Вставьте фото",
    )

    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата создания",
        help_text="Укажите дату создания поста",
    )

    is_publication = models.BooleanField(
        default=True,
        verbose_name="Признак публикации",
        help_text="Укажите признак публикации (булевое поле)",
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
        ordering = ["title", "content", "views_counter"]

    def __str__(self):
        return self.title
