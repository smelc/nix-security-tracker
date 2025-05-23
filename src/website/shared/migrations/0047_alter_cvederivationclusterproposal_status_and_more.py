# Generated by Django 4.2.16 on 2025-04-16 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0046_alter_cachedsuggestions_proposal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvederivationclusterproposal',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('rejected', 'rejected'), ('accepted', 'accepted'), ('published', 'published')], default='pending', max_length=9),
        ),
        migrations.AlterField(
            model_name='cvederivationclusterproposalstatusevent',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('rejected', 'rejected'), ('accepted', 'accepted'), ('published', 'published')], default='pending', max_length=9),
        ),
    ]
