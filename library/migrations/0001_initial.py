# Generated by Django 5.0.1 on 2024-02-01 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('available', models.CharField(choices=[('Available', 'Available'), ('Not Available', 'Not Available')], max_length=50)),
                ('front_page', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('book_genre', models.CharField(choices=[('Fairytales', 'Fairytales'), ('Historical Fiction', 'Historical Fiction'), ('Poetry', 'Poetry'), ('Picture Books', 'Picture Books')], max_length=50)),
                ('book_code', models.CharField(max_length=50, unique=True)),
                ('edition', models.CharField(max_length=100)),
                ('length', models.CharField(max_length=100)),
                ('chapter', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('copies', models.IntegerField()),
                ('published_date', models.DateField()),
                ('published_in', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=100)),
            ],
        ),
    ]
