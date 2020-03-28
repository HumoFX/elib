# Generated by Django 3.0.4 on 2020-03-25 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('University', '0001_initial'),
        ('User', '0002_auto_20200326_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='university_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='Университет', to='University.University'),
            preserve_default=False,
        ),
    ]