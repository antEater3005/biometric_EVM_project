# Generated by Django 4.1.7 on 2023-05-24 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0004_voter_delete_aadhar_election_iscompleted'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Voter',
            new_name='Voters',
        ),
    ]
