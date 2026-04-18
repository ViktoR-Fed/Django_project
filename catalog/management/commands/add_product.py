from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Загрузка категорий и продуктов в базу данных"

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        Product.objects.all().delete()
        Category.objects.all().delete()
        # Загружаем данные
        call_command("loaddata", "data.json")
        self.stdout.write(self.style.SUCCESS("Успешное добавление данных из фикстуры"))
