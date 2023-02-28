# Generated by Django 4.0 on 2023-02-21 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finanance', '0002_devises_immobe_taxes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.FloatField()),
                ('nom_compte', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('devise_compte', models.CharField(max_length=100)),
            ],
        ),
    ]
