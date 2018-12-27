# Generated by Django 2.1.3 on 2018-12-27 22:36

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('dzrip', '0002_auto_20181225_0945'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customermodel',
            options={'verbose_name': 'Профиль пользователей', 'verbose_name_plural': 'Профили пользователей'},
        ),
        migrations.AlterModelManagers(
            name='customermodel',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='customermodel',
            name='city',
        ),
        migrations.RemoveField(
            model_name='customermodel',
            name='name',
        ),
        migrations.RemoveField(
            model_name='customermodel',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='customermodel',
            name='surname',
        ),
        migrations.RemoveField(
            model_name='customermodel',
            name='user',
        ),
        migrations.AddField(
            model_name='customermodel',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/default_avatar.png', null=True, upload_to='avatars/', verbose_name='Аватар'),
        ),
        migrations.AddField(
            model_name='customermodel',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='customermodel',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='О себе'),
        ),
        migrations.AddField(
            model_name='customermodel',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AddField(
            model_name='customermodel',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='customermodel',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='customermodel',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AddField(
            model_name='customermodel',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.AddField(
            model_name='customermodel',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='customermodel',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='customermodel',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='customermodel',
            name='password',
            field=models.CharField(default=1111, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customermodel',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='customermodel',
            name='username',
            field=models.CharField(default='', error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='customermodel',
            table='Профиль',
        ),
    ]
