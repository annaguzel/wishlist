# Generated by Django 3.0.3 on 2020-02-19 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wishes', '0003_auto_20200219_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishes', to='wishes.List'),
        ),
    ]
