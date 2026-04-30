from django.core.management.base import BaseCommand
from tours.models import Tour

class Command(BaseCommand):
    help = 'Populate database with sample tours'

    def handle(self, *args, **kwargs):
        tours_data = [
            {
                'name': 'Романтический Париж',
                'destination': 'EU',
                'country': 'Франция',
                'city': 'Париж',
                'tour_type': 'excursion',
                'duration_days': 7,
                'price': 85000,
                'description': 'Незабываемое путешествие в город любви. Эйфелева башня, Лувр, круиз по Сене и прогулки по Монмартру.',
                'includes': 'Перелет, проживание 4*, экскурсии, завтраки',
                'rating': 4.8,
            },
            {
                'name': 'Пляжи Мальдив',
                'destination': 'AS',
                'country': 'Мальдивы',
                'city': 'Мале',
                'tour_type': 'beach',
                'duration_days': 10,
                'price': 150000,
                'description': 'Райский отдых на белоснежных пляжах. Кристально чистая вода, подводное плавание и максимальный релакс.',
                'includes': 'Перелет, проживание 5*, все включено, трансфер',
                'rating': 5.0,
            },
            {
                'name': 'Сафари в Кении',
                'destination': 'AF',
                'country': 'Кения',
                'city': 'Найроби',
                'tour_type': 'active',
                'duration_days': 8,
                'price': 120000,
                'description': 'Приключение в дикой природе Африки. Наблюдение за животными в их естественной среде обитания.',
                'includes': 'Перелет, проживание в лоджах, сафари-туры, гид',
                'rating': 4.7,
            },
            {
                'name': 'Великая Китайская стена',
                'destination': 'AS',
                'country': 'Китай',
                'city': 'Пекин',
                'tour_type': 'excursion',
                'duration_days': 9,
                'price': 95000,
                'description': 'Исследование древних чудес Китая. Великая стена, Запретный город и традиционная китайская культура.',
                'includes': 'Перелет, проживание 4*, экскурсии, полупансион',
                'rating': 4.6,
            },
            {
                'name': 'Карибский круиз',
                'destination': 'NA',
                'country': 'США',
                'city': 'Майами',
                'tour_type': 'cruise',
                'duration_days': 14,
                'price': 180000,
                'description': 'Роскошный круиз по Карибским островам. Посещение нескольких стран, развлечения на лайнере класса люкс.',
                'includes': 'Круиз на лайнере 5*, питание, развлечения, экскурсии',
                'rating': 4.9,
            },
            {
                'name': 'Спа-курорт в Баден-Бадене',
                'destination': 'EU',
                'country': 'Германия',
                'city': 'Баден-Баден',
                'tour_type': 'wellness',
                'duration_days': 7,
                'price': 110000,
                'description': 'Оздоровление в знаменитом термальном курорте. Spa-процедуры, минеральные источники и живописная природа.',
                'includes': 'Перелет, проживание в спа-отеле 5*, процедуры, питание',
                'rating': 4.7,
            },
            {
                'name': 'Экзотический Бали',
                'destination': 'AS',
                'country': 'Индонезия',
                'city': 'Денпасар',
                'tour_type': 'beach',
                'duration_days': 12,
                'price': 98000,
                'description': 'Тропический рай с храмами, рисовыми террасами и чудесными пляжами. Йога, серфинг и балийский массаж.',
                'includes': 'Перелет, проживание 4*, завтраки, экскурсии',
                'rating': 4.8,
            },
            {
                'name': 'Горы Швейцарии',
                'destination': 'EU',
                'country': 'Швейцария',
                'city': 'Цюрих',
                'tour_type': 'active',
                'duration_days': 8,
                'price': 135000,
                'description': 'Альпийские приключения: горные лыжи, походы и посещение живописных деревень.',
                'includes': 'Перелет, проживание в шале 4*, ски-пасс, полупансион',
                'rating': 4.9,
            },
        ]

        for tour_data in tours_data:
            tour, created = Tour.objects.get_or_create(
                name=tour_data['name'],
                defaults=tour_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Создан тур: {tour.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Тур уже существует: {tour.name}'))

        self.stdout.write(self.style.SUCCESS('Готово! База данных заполнена тестовыми турами.'))
