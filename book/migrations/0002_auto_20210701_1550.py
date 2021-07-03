# Generated by Django 3.2.4 on 2021-07-01 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authar',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='long_describtion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='no_of_reads',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='page_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='short_describtion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(default='Publish', max_length=20),
        ),
        migrations.AddField(
            model_name='book',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnail/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('no_of_reading_books', models.IntegerField(default=0)),
                ('books', models.ManyToManyField(related_name='book_readers', to='book.Book')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='authars',
            field=models.ManyToManyField(blank=True, null=True, related_name='books', to='book.Authar'),
        ),
    ]
