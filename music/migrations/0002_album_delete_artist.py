# Generated by Django 4.2.1 on 2023-05-22 18:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('songs', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
    ]
