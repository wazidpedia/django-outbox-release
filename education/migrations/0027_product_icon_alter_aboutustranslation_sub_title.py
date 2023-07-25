# Generated by Django 4.1.2 on 2023-07-22 15:00

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0026_aboutus_aboutustranslation'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='icon',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='aboutustranslation',
            name='sub_title',
            field=django_cryptography.fields.encrypt(models.CharField(max_length=100, verbose_name='sub title')),
        ),
    ]
