# Generated by Django 4.0.6 on 2023-03-16 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finanance', '0003_facturecl_devise_facturefr_devise_notes_devise'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='devise_compte',
        ),
        migrations.AddField(
            model_name='facturecl',
            name='compte',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='finanance.plan'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='facturefr',
            name='compte',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='finanance.plan'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notes',
            name='compte',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='finanance.plan'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='plan',
            name='code',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
