# Generated by Django 4.1.7 on 2023-03-23 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0002_alter_candidates_candidate_symbol_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aadhar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('UID_No', models.IntegerField(max_length=12)),
                ('photo', models.ImageField(upload_to='image')),
            ],
        ),
    ]
