# Generated by Django 3.2.9 on 2022-11-26 11:30

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rankme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steam', models.CharField(blank=True, max_length=40, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('lastip', models.TextField(blank=True, null=True)),
                ('score', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('kills', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('deaths', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('assists', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('suicides', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('tk', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('shots', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('hits', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('headshots', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('connected', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('rounds_tr', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('rounds_ct', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('lastconnect', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('knife', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('glock', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('hkp2000', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('usp_silencer', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('p250', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('deagle', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('elite', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('fiveseven', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('tec9', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('cz75a', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('revolver', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('nova', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('xm1014', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('mag7', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('sawedoff', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('bizon', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('mac10', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('mp9', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('mp7', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('ump45', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('p90', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('galilar', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('ak47', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('scar20', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('famas', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('m4a1', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('m4a1_silencer', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('aug', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('ssg08', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('sg556', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('awp', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('g3sg1', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('m249', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('negev', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('hegrenade', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('flashbang', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('smokegrenade', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('inferno', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('decoy', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('taser', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('mp5sd', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('breachcharge', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('head', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('chest', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('stomach', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('left_arm', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('right_arm', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('left_leg', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('right_leg', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('c4_planted', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('c4_exploded', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('c4_defused', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('ct_win', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('tr_win', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('hostages_rescued', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('vip_killed', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('vip_escaped', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('vip_played', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('mvp', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('damage', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('match_win', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('match_draw', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('match_lose', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('first_blood', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('no_scope', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('no_scope_dis', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('thru_smoke', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('blind', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('assist_flash', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('assist_team_flash', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('assist_team_kill', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('wallbang', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'rankme',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='address')),
                ('city', models.CharField(blank=True, max_length=60, null=True, verbose_name='city')),
                ('zipcode', models.CharField(blank=True, max_length=12, null=True, verbose_name='zip code')),
                ('phonenumber', models.CharField(blank=True, max_length=25, null=True, verbose_name='first name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=254, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid email address. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], verbose_name='email address')),
                ('dark_theme', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_customer', models.BooleanField(default=False, help_text='Designates whether the user is a customer site.', verbose_name='staff status')),
                ('is_admin', models.BooleanField(default=False, help_text='Designates whether the user is a customer admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
