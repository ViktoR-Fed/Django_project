from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Добавление группы 'Менеджер продуктов'"

    def handle(self, *args, **options):

        Group.objects.all().delete()
        moderators_group = Group.objects.create(name="Модератор продуктов")

        can_unpublish_product = Permission.objects.get(codename="can_unpublish_product")
        delete_product = Permission.objects.get(codename="delete_product")

        moderators_group.permissions.add(can_unpublish_product, delete_product)

        self.stdout.write(
            self.style.SUCCESS("Успешное добавление группы: Менеджер продуктов")
        )
