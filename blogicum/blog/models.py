from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Post(models.Model):
    title = models.CharField("Заголовок", max_length=256)
    text = models.TextField("Текст")
    pub_date = models.DateTimeField(
        "Дата и время публикации",
        help_text="Если установить дату и время в будущем — можно делать отложенные публикации.",
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Автор публикации"
    )
    location = models.ForeignKey(
        "Location", blank=True, null=True, on_delete=models.SET_NULL
    )
    category = models.ForeignKey(
        "Category", null=True, on_delete=models.SET_NULL, verbose_name="Категория"
    )
    is_published = models.BooleanField(
        "Опубликованно",
        default=True,
        help_text="Снимите галочку, чтобы скрыть публикацию.",
    )
    created_at = models.DateTimeField("Добавлено", auto_now_add=True)

    class Meta:
        verbose_name = "публикация"
        verbose_name_plural = "Публикации"

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField("Заголовок", max_length=256)
    description = models.TextField("Описание")
    slug = models.SlugField(
        "Индентификатор",
        help_text="Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.",
    )
    is_published = models.BooleanField(
        "Опубликованно",
        default=True,
        help_text="Снимите галочку, чтобы скрыть публикацию.",
    )
    created_at = models.DateTimeField("Добавлено", auto_now_add=True)

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class Location(models.Model):
    name = models.CharField("Название места", max_length=256)
    is_published = models.BooleanField(
        "Опубликованно",
        default=True,
        help_text="Снимите галочку, чтобы скрыть публикацию.",
    )
    created_at = models.DateTimeField("Добавлено", auto_now_add=True)

    class Meta:
        verbose_name = "местоположение"
        verbose_name_plural = "Местоположения"

    def __str__(self):
        return self.name
