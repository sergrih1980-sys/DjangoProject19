from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from django.utils import timezone

class Command(BaseCommand):
    help = 'Удаляет все существующие данные и создаёт тестовые категории и продукты'

    def handle(self, *args, **options):
        self.stdout.write('Начинаем очистку базы данных...')

        # Удаляем все продукты
        deleted_products, _ = Product.objects.all().delete()
        self.stdout.write(
            self.style.SUCCESS(f'Удалено продуктов: {deleted_products}')
        )

        # Удаляем все категории
        deleted_categories, _ = Category.objects.all().delete()
        self.stdout.write(
            self.style.SUCCESS(f'Удалено категорий: {deleted_categories}')
        )

        self.stdout.write('Создаём тестовые данные...')

        # Создаём категории
        categories_data = [
            {'name': 'Электроника', 'description': 'Электронные устройства и гаджеты'},
            {'name': 'Одежда', 'description': 'Мужская, женская и детская одежда'},
            {'name': 'Книги', 'description': 'Художественная и научная литература'},
        ]

        created_categories = []
        for cat_data in categories_data:
            category = Category.objects.create(**cat_data)
            created_categories.append(category)
            self.stdout.write(
                self.style.NOTICE(f'Создана категория: {category.name}')
            )

        # Создаём продукты
        products_data = [
            {
                'name': 'Смартфон Galaxy S23',
                'description': 'Флагманский смартфон с отличной камерой',
                'image': 'products/galaxy_s23.jpg',
                'category': created_categories[0],
                'price': 69999.99,
            },
            {
                'name': 'Футболка хлопковая',
                'description': 'Удобная футболка из 100% хлопка',
                'image': 'products/tshirt.jpg',
                'category': created_categories[1],
                'price': 1999.50,
            },
            {
                'name': 'Ноутбук Dell XPS 13',
                'description': 'Ультрабук с процессором Intel i7',
                'image': 'products/dell_xps.jpg',
                'category': created_categories[0],
                'price': 89999.00,
            },
            {
                'name': 'Война и мир',
                'description': 'Роман-эпопея Льва Толстого',
                'image': 'products/war_and_peace.jpg',
                'category': created_categories[2],
                'price': 999.00,
            },
        ]

        for prod_data in products_data:
            product = Product.objects.create(
                **prod_data,
                created_at=timezone.now(),
                updated_at=timezone.now()
            )
            self.stdout.write(
                self.style.SUCCESS(f'Создан продукт: {product.name}')
            )

        self.stdout.write(self.style.SUCCESS('Все тестовые данные успешно созданы!'))