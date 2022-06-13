# Generated by Django 4.0.5 on 2022-06-13 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devinfo', '0004_alter_tag_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='thumbnail')),
                ('tags', models.ManyToManyField(to='devinfo.tag')),
            ],
        ),
    ]
