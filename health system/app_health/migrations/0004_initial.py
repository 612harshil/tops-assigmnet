# Generated by Django 4.2 on 2023-04-26 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_health', '0003_delete_doctor_user_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='disease_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.CharField(max_length=50)),
                ('diseasename', models.CharField(max_length=50)),
                ('symptoms', models.CharField(max_length=100)),
                ('precaution', models.CharField(max_length=100)),
                ('medicinename', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='doctor_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctorname', models.CharField(max_length=50)),
                ('specializations', models.CharField(max_length=50)),
                ('doctorpic', models.FileField(default='anonymous.jpg', upload_to='media/')),
                ('contact', models.CharField(max_length=10)),
                ('desc', models.CharField(max_length=500)),
                ('disease', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='medicine_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diseasename', models.CharField(max_length=50)),
                ('medicinename', models.CharField(max_length=50)),
                ('medprecaution', models.CharField(max_length=100)),
                ('meddesc', models.CharField(max_length=100)),
                ('medprice', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('username', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('profilepic', models.FileField(default='anonymous.jpg', upload_to='media/')),
                ('contact', models.CharField(max_length=10)),
            ],
        ),
    ]
