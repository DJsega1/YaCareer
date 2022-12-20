# Generated by Django 3.2.16 on 2022-12-20 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('photo', models.ImageField(blank=True, upload_to='images/', verbose_name='фото')),
                ('first_name', models.CharField(blank=True, default='', max_length=150, verbose_name='имя')),
                ('last_name', models.CharField(blank=True, default='', max_length=150, verbose_name='фамилия')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='почта')),
                ('is_active', models.BooleanField(default=True, null=True, verbose_name='активная учетная запись')),
                ('is_staff', models.BooleanField(default=False, null=True, verbose_name='персонал')),
                ('is_superuser', models.BooleanField(default=False, null=True, verbose_name='админ')),
                ('is_open_to_work', models.BooleanField(default=False, null=True, verbose_name='в поисках работы')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('about', models.CharField(blank=True, max_length=1024, null=True, verbose_name='описание')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='дата рождения')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'пользователи',
                'default_related_name': 'users',
            },
        ),
        migrations.CreateModel(
            name='UserMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='название')),
                ('file', models.FileField(upload_to='files/', verbose_name='файл')),
                ('description', models.CharField(blank=True, max_length=1024, null=True, verbose_name='описание')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to=settings.AUTH_USER_MODEL, verbose_name='медиа')),
            ],
            options={
                'verbose_name': 'файл',
                'verbose_name_plural': 'файлы',
                'default_related_name': 'media',
            },
        ),
        migrations.CreateModel(
            name='UserLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=2048, verbose_name='ссылка')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='services.service', verbose_name='сервис')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to=settings.AUTH_USER_MODEL, verbose_name='ссылка на профиль')),
            ],
            options={
                'verbose_name': 'ссылка',
                'verbose_name_plural': 'ссылки',
                'default_related_name': 'links',
            },
        ),
    ]
