# Generated by Django 4.0.6 on 2022-07-22 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pushcase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PushcaseNumeber', models.CharField(max_length=50)),
                ('IsDeleted', models.BooleanField(default=True)),
                ('CreateAt', models.DateField()),
                ('ModifiedAt', models.DateField()),
                ('DeletedAt', models.DateField()),
                ('PushcaseDate', models.DateField()),
            ],
            options={
                'verbose_name': 'Pushcase',
                'verbose_name_plural': 'Pushcase',
            },
        ),
        migrations.CreateModel(
            name='PushcaseDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodeP', models.CharField(max_length=50)),
                ('Desc', models.CharField(max_length=50)),
                ('Quality', models.IntegerField()),
                ('PriceP', models.IntegerField()),
                ('CostP', models.IntegerField()),
                ('UnitP', models.CharField(max_length=50)),
                ('Precentage', models.IntegerField()),
                ('PencetagePrice', models.IntegerField()),
                ('Total', models.IntegerField()),
                ('PushcaseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PushCase.pushcase')),
            ],
            options={
                'verbose_name': 'PushcaseDetail',
                'verbose_name_plural': 'PushcaseDetails',
            },
        ),
    ]
