# Generated by Django 3.1.1 on 2020-11-10 01:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=300)),
                ('imagen', models.ImageField(upload_to='')),
                ('texto', models.TextField()),
                ('fecha_publicacion', models.DateTimeField(blank=True, null=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historia',
                'verbose_name_plural': 'historias',
                'db_table': 'historia',
                'ordering': ['id'],
            },
        ),
    ]
