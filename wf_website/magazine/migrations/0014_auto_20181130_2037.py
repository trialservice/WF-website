# Generated by Django 2.1.3 on 2018-11-30 20:37

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('magazine', '0013_auto_20181112_2249'),
    ]

    operations = [
        migrations.CreateModel(
            name='MagazineArticleTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='magazine.MagazineArticle')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='magazine_magazinearticletag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='magazinearticle',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='magazine.MagazineArticleTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
