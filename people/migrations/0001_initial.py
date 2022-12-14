# Generated by Django 4.1 on 2022-08-15 23:13

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='SiteAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=250)),
                ('facebook_link', models.CharField(max_length=500)),
                ('twitter_link', models.CharField(max_length=500)),
                ('instagram_link', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500)),
                ('banner', django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=-1, scale=None, size=[1140, 650], upload_to='uploads/banner/')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, unique=True)),
                ('slug', models.SlugField(max_length=2000, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Publish', 'Publish')], max_length=250)),
                ('preview', models.ImageField(upload_to='uploads/preview/')),
                ('editor_pick', models.BooleanField(default=False)),
                ('post_image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[100, 80], upload_to='uploads/preview_sm/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cate', to='people.category')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
