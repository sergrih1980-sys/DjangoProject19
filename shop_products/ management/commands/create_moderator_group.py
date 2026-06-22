from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from shop_products.models import Product

class Command(BaseCommand):
    help = 'Создаёт группу "Модератор продуктов" с необходимыми разрешениями'

    def handle(self, *args, **options):
        # Получаем контент‑тип для модели Product
        content_type = ContentType.objects.get_for_model(Product)

        # Создаём группу
        moderator_group, created = Group.objects.get_or_create(
            name='Модератор продуктов'
        )

        if created:
            self.stdout.write(
                self.style.SUCCESS('Группа "Модератор продуктов" успешно создана')
            )
        else:
            self.stdout.write('Группа "Модератор продуктов" уже существует')

        # Получаем кастомное разрешение
        try:
            unpublish_perm = Permission.objects.get(
                codename='can_unpublish_product',
                content_type=content_type
            )
            moderator_group.permissions.add(unpublish_perm)
            self.stdout.write('Разрешение can_unpublish_product назначено группе')
        except Permission.DoesNotExist:
            self.stdout.write(
                self.style.WARNING('Разрешение can_unpublish_product не найдено')
            )

        # Добавляем разрешение на удаление
        try:
            delete_perm = Permission.objects.get(
                codename='delete_product',
                content_type=content_type
            )
            moderator_group.permissions.add(delete_perm)
            self.stdout.write('Разрешение на удаление продуктов назначено группе')
        except Permission.DoesNotExist:
            self.stdout.write(
                self.style.WARNING('Разрешение delete_product не найдено')
            )