# Generated by Django 5.0 on 2023-12-11 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='comentario',
            field=models.TextField(),
        ),
    ]
