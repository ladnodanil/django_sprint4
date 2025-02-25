# Generated by Django 3.2.25 on 2024-07-13 06:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to='images',
                verbose_name='Изображение'
            ),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'is_published',
                    models.BooleanField(
                        default=True,
                        help_text='Снимите галочку, чтобы скрыть публикацию.',
                        verbose_name='Опубликовано',
                    ),
                ),
                ('text', models.TextField(verbose_name='Текст')),
                (
                    'created_at',
                    models.DateTimeField(
                        auto_now_add=True, verbose_name='Добавлено'),
                ),
                (
                    'author',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='comments',
                        to=settings.AUTH_USER_MODEL,
                        verbose_name='Автор',
                    ),
                ),
                (
                    'post',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='comments',
                        to='blog.post',
                        verbose_name='Комментарий',
                    ),
                ),
            ],
            options={
                'verbose_name': 'комментарий',
                'verbose_name_plural': 'Комментарий',
                'ordering': ('created_at',),
            },
        ),
    ]
