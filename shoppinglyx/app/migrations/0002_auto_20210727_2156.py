# Generated by Django 3.1.7 on 2021-07-27 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='zipcode',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('M', 'Mobile'), ('S', 'Shoes'), ('TW', 'Top Wear'), ('BW', 'Bottom Wear')], max_length=2),
        ),
    ]
