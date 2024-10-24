# Generated by Django 5.1.2 on 2024-10-23 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='posts/%Y/%m/'),
        ),
        migrations.AddField(
            model_name='post',
            name='cover_in_post_content',
            field=models.BooleanField(default=True, help_text='A capa somente será exibida dentro do post caso essa opção esteja marcada'),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
