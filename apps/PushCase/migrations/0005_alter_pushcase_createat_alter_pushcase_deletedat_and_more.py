# Generated by Django 4.0.6 on 2022-07-26 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PushCase', '0004_rename_isdeleted_pushcase_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pushcase',
            name='CreateAt',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='pushcase',
            name='DeletedAt',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='pushcase',
            name='ModifiedAt',
            field=models.DateField(auto_now=True),
        ),
    ]
