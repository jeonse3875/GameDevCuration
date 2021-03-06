# Generated by Django 4.0.5 on 2022-06-13 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devinfo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='children',
        ),
        migrations.AddField(
            model_name='tag',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='thumbnail'),
        ),
        migrations.CreateModel(
            name='TagRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_tag', to='devinfo.tag')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_tag', to='devinfo.tag')),
            ],
        ),
    ]
