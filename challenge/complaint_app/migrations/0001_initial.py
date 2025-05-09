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
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_key', models.CharField(blank=True, default='', max_length=150)),
                ('account', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('opendate', models.DateField(blank=True, null=True)),
                ('complaint_type', models.CharField(blank=True, default='', max_length=150, null=True)),
                ('descriptor', models.CharField(blank=True, default='', max_length=150, null=True)),
                ('zip', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('borough', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('city', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('council_dist', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('community_board', models.CharField(blank=True, default='', max_length=150, null=True)),
                ('closedate', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, default='', max_length=150)),
                ('district', models.CharField(blank=True, default='', max_length=5)),
                ('party', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('borough', models.CharField(blank=True, default='', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
