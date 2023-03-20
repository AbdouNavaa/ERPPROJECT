# Generated by Django 4.0.6 on 2023-03-15 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finanance', '0002_paiementsfr'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturecl',
            name='Devise',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='finanance.devises'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='facturefr',
            name='Devise',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='finanance.devises'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notes',
            name='Devise',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='finanance.devises'),
            preserve_default=False,
        ),
    ]
