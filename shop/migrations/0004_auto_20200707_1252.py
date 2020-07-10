# Generated by Django 3.0.7 on 2020-07-07 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20200707_1119'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'ordering': ('id',), 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(blank=True, upload_to='articles/'),
        ),
        migrations.AlterIndexTogether(
            name='articles',
            index_together={('id', 'slug')},
        ),
    ]
