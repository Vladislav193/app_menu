from django.db import models
from django.urls import reverse

class Menu(models.Model):
    """
    Модель для хранения меню. Каждое меню имеет уникальное название.
    """
    name = models.CharField(max_length=100, unique=True, verbose_name="Название меню")

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    """
    Модель для хранения элементов меню. Каждый элемент может иметь родительский элемент
    (для построения древовидной структуры). Элементы могут быть отсортированы по порядку (order).
    URL для перехода может быть указан как явным образом (url), так и через named url.
    """
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE, verbose_name="Меню")
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE, verbose_name="Родительский элемент")
    title = models.CharField(max_length=100, verbose_name="Название пункта")
    url = models.CharField(max_length=255, blank=True, verbose_name="URL (если не указано, используется named url)")
    named_url = models.CharField(max_length=100, blank=True, verbose_name="Named URL")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок отображения")

    class Meta:
        verbose_name = "Элемент меню"
        verbose_name_plural = "Элементы меню"
        ordering = ['order']  # Определение порядка отображения элементов по полю order

    def __str__(self):
        return self.title

    def get_url(self):
        """
        Метод для получения URL элемента меню. Если указан named_url, возвращается
        URL по имени, иначе используется явный URL.
        """
        if self.named_url:
            return reverse(self.named_url)
        return self.url