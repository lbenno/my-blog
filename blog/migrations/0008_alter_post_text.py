# Generated by Django 3.2.25 on 2024-09-28 18:50

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=froala_editor.fields.FroalaField(),
        ),
    ]
