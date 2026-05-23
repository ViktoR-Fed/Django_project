from django.contrib.auth.models import Group, Permission

moderators_group = Group.objects.create(name="Модератор продуктов")

can_unpublish_product = Permission.objects.get(codename="can_unpublish_product")
delete_product = Permission.objects.get(codename="delete_product")

moderators_group.permissions.add(can_unpublish_product, delete_product)
