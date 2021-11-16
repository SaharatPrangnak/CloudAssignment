# Generated by Django 3.2.9 on 2021-11-10 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boat',
            name='price',
            field=models.DecimalField(decimal_places=2, default=265.0, max_digits=7),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='boat',
            name='built',
            field=models.IntegerField(),
        ),
    ]