# Generated by Django 4.1.4 on 2023-01-17 00:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('livro', '0007_alter_livros_doador_id_alter_livros_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='doador_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='livros',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]