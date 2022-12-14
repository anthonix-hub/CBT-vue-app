# Generated by Django 2.1.8 on 2020-10-30 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ansChoosed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='QuestLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=50)),
                ('answers', models.CharField(max_length=50)),
                ('opts', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='anschoosed',
            name='quest',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='CBT_app.QuestLog'),
        ),
    ]
