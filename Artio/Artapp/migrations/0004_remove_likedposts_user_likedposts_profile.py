# Generated by Django 4.0.5 on 2022-06-26 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Artapp', '0003_remove_profile_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likedposts',
            name='User',
        ),
        migrations.AddField(
            model_name='likedposts',
            name='Profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Artapp.profile'),
        ),
    ]
