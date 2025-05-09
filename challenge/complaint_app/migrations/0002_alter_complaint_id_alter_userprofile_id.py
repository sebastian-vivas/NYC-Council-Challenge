from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
