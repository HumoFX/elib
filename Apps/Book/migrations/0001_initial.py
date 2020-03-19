# Generated by Django 3.0.4 on 2020-03-18 19:31

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('University', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='UDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(default='0', max_length=128)),
            ],
            options={
                'verbose_name': 'УДК',
                'verbose_name_plural': 'УДК',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='Book.Category')),
                ('udc_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Book.UDC')),
            ],
            options={
                'verbose_name': 'Категорий',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512, unique=True)),
                ('author', models.CharField(max_length=512, unique=True)),
                ('ключевые слова', models.TextField(default='')),
                ('img', models.ImageField(upload_to='img/books')),
                ('quantity', models.IntegerField()),
                ('Цена', models.FloatField()),
                ('Рейтинг', models.FloatField()),
                ('used', models.IntegerField()),
                ('Электроная версия', models.BooleanField(default=False)),
                ('file', models.FileField(blank=True, null=True, upload_to='file/e_books')),
                ('Печатная версия', models.BooleanField(default=False)),
                ('Спец книги', models.BooleanField()),
                ('Учебное пособие', models.BooleanField()),
                ('Дата публикации', models.DateField()),
                ('Дата получения', models.DateField()),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='University.Faculty')),
                ('udc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Book.Category')),
            ],
            options={
                'verbose_name': 'Книгу',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
