# Generated by Django 2.2.1 on 2019-06-13 09:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Karshenas',
            fields=[
                ('karshenas_title', models.CharField(max_length=200)),
                ('karshenas_id', models.UUIDField(default=uuid.uuid4, help_text='Unique Id for this particular Karshenas', primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Modiriat',
            fields=[
                ('modiriat_title', models.CharField(max_length=200)),
                ('modiriat_id', models.UUIDField(default=uuid.uuid4, help_text='Unique Id for this particular Modiriat', primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Shobe',
            fields=[
                ('shobe_id', models.UUIDField(default=uuid.uuid4, help_text='Unique Id for this particular Shobe', primary_key=True, serialize=False)),
                ('shobe_title', models.CharField(max_length=200)),
                ('modiriat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Modiriat')),
            ],
        ),
        migrations.CreateModel(
            name='Madion',
            fields=[
                ('madion_id', models.UUIDField(default=uuid.uuid4, help_text='Unique Id for this particular Madion', primary_key=True, serialize=False)),
                ('madion_name', models.CharField(max_length=100)),
                ('madion_compani', models.CharField(max_length=100)),
                ('madion_zamen1', models.CharField(max_length=100)),
                ('madion_zamen2', models.CharField(max_length=100)),
                ('madion_zamen3', models.CharField(max_length=100)),
                ('date_erjae', models.DateField(blank=True, null=True)),
                ('kelase_asli', models.CharField(max_length=100)),
                ('kelase_niabati', models.CharField(max_length=100)),
                ('odat_banck', models.DateField(blank=True, null=True)),
                ('karshenas_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Karshenas')),
                ('modiriat_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Modiriat')),
                ('shobe_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Shobe')),
            ],
        ),
    ]
