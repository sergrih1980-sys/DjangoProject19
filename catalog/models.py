from django.db import models



class Product(models.Model):
    name =models.CharField(
        max_length=150,
        verbose_name="Наименование",
        help_text="Введите название")


    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание")

    image = models.ImageField(
            upload_to="products/",
            blank=True,
            null=True,
            verbose_name="Фото",
            help_text="Загрузите фото товара"
        )

    category = models.ForeignKey(
            "Category",
            on_delete=models.SET_NULL,
            null=True,
            blank=True,
            verbose_name="Категория",
            help_text="Выберите категорию из списка"
        )

    price = models.FloatField(
        verbose_name="Цена покупки",
        help_text="Введите цену")

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания")

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления")

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["-created_at"]


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(
    verbose_name="Описание", help_text="Введите описание"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name



