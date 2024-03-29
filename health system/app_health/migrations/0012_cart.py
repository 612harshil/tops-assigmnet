# Generated by Django 4.1.7 on 2023-05-08 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_health', '0011_medicine_user_medpic'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_health.medicine_user')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_health.user')),
            ],
        ),
    ]
