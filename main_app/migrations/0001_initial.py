# Generated by Django 4.1.7 on 2023-11-06 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_type', models.CharField(max_length=200, verbose_name='Тип контактной информации')),
            ],
        ),
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estate_number', models.CharField(max_length=200, unique=True, verbose_name='Номер')),
                ('floor', models.IntegerField(blank=True, null=True, verbose_name='Этаж')),
                ('length', models.FloatField(blank=True, null=True, verbose_name='Длина')),
                ('width', models.FloatField(blank=True, null=True, verbose_name='Ширина')),
                ('height', models.FloatField(blank=True, null=True, verbose_name='Высота')),
                ('area', models.FloatField(blank=True, null=True, verbose_name='Площадь')),
                ('observation_pit', models.BooleanField(blank=True, choices=[(True, 'Да'), (False, 'Нет'), (None, '')], null=True, verbose_name='Смотровая яма')),
                ('initial_cost', models.CharField(blank=True, max_length=200, null=True, verbose_name='Начальная стоимость')),
                ('build_date', models.DateField(blank=True, null=True, verbose_name='Дата постройки')),
                ('estimated_cost', models.CharField(blank=True, max_length=200, null=True, verbose_name='Оценочная стоимость')),
                ('estimated_cost_date', models.DateField(blank=True, null=True, verbose_name='Дата оценки')),
                ('for_rent', models.BooleanField(blank=True, choices=[(True, 'Да'), (False, 'Нет'), (None, '')], null=True, verbose_name='Сдается в аренду')),
                ('for_sale', models.BooleanField(blank=True, choices=[(True, 'Да'), (False, 'Нет'), (None, '')], null=True, verbose_name='Продается')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарии')),
                ('update_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Данные обновлены')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Estate',
                'verbose_name_plural': 'Estates',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('patronymic', models.CharField(blank=True, max_length=200, null=True, verbose_name='Отчество')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/', verbose_name='Фотография')),
                ('questions', models.TextField(blank=True, null=True, verbose_name='Вопросы')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарии')),
                ('update_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Данные обновлены')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('owner_id', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.person', verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Personalities',
                'ordering': ['surname', 'name', 'patronymic'],
            },
        ),
        migrations.CreateModel(
            name='RelationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation_type', models.CharField(max_length=200, verbose_name='Отношение к владельцу')),
            ],
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ownership_part', models.FloatField(blank=True, null=True, verbose_name='Доля собственности')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Дата возникновения отношения')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата прекращения отношения')),
                ('estate_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.estate')),
                ('person_id', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.person')),
                ('relation_type', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.relationtype')),
            ],
            options={
                'verbose_name': 'Relation',
                'verbose_name_plural': 'Relations',
            },
        ),
        migrations.CreateModel(
            name='Pass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pass_number', models.CharField(max_length=200, verbose_name='Номер пропуска')),
                ('car_model', models.CharField(blank=True, max_length=200, null=True, verbose_name='Модель ТС')),
                ('car_color', models.CharField(blank=True, max_length=200, null=True, verbose_name='Цвет ТС')),
                ('car_number', models.CharField(blank=True, max_length=200, null=True, verbose_name='Номерной знак ТС')),
                ('issue_date', models.DateField(blank=True, null=True, verbose_name='Дата выдачи')),
                ('expiration_date', models.DateField(blank=True, null=True, verbose_name='Действует до')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарии')),
                ('relation_id', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.relation')),
            ],
            options={
                'verbose_name': 'Pass',
                'verbose_name_plural': 'Passes',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_info', models.CharField(max_length=200, verbose_name='Контактная информация')),
                ('contact_type', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.contacttype')),
                ('person_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.person')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
                'ordering': ['contact_type', 'contact_info'],
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat_number', models.CharField(blank=True, max_length=200, null=True, verbose_name='Квартира')),
                ('house_number', models.CharField(blank=True, max_length=200, null=True, verbose_name='Дом')),
                ('street', models.CharField(blank=True, max_length=200, null=True, verbose_name='Улица')),
                ('city', models.CharField(blank=True, max_length=200, null=True, verbose_name='Населенный пункт')),
                ('region', models.CharField(blank=True, max_length=200, null=True, verbose_name='Область, район')),
                ('postal_code', models.CharField(blank=True, max_length=200, null=True, verbose_name='Почтовый индекс')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарии')),
                ('update_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Данные обновлены')),
                ('person_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.person')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
                'ordering': ['region', 'city', 'street', 'house_number', 'flat_number'],
            },
        ),
    ]
