# Generated by Django 5.0.6 on 2024-07-20 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Unidades', '0004_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vulcanche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('cabaña', models.IntegerField()),
                ('fechaEstadia', models.DateField()),
            ],
        ),
    ]
