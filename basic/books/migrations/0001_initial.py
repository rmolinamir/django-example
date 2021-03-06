# Generated by Django 2.2.4 on 2020-01-08 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0002_author_created_at'),
        ('publishers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.SmallIntegerField(choices=[(0, 'Fantasy'), (1, 'Horror'), (2, 'Sci-fi'), (3, 'Sci-fi')], default=None, null=False)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('created_at', models.DateField(auto_now=True)),
                ('authors', models.ManyToManyField(related_name='books', to='authors.Author')),
                ('genre', models.ManyToManyField(related_name='books', to='books.BookGenre')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='publishers.Publisher')),
            ],
        ),
    ]
