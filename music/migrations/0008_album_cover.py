# Generated by Django 4.2.1 on 2023-05-27 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_remove_album_track_remove_song_record_song_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='cover',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
