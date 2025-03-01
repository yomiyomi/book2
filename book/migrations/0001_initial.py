# Generated by Django 5.1.2 on 2024-11-19 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('is_borrowed', models.BooleanField(default=False)),
                ('borrower_name', models.CharField(blank=True, max_length=100, null=True)),
                ('borrowed_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
