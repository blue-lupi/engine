# Generated by Django 2.1.7 on 2019-03-24 10:21

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20190323_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personpage',
            name='biography',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title', icon='title', template='patterns/molecules/streamfield/blocks/heading_block.html')), ('paragraph', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'bold', 'italic', 'link', 'ol', 'ul'])), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.CharBlock(classname='title')), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('citation_link', wagtail.core.blocks.URLBlock(required=False))])), ('embed', wagtail.embeds.blocks.EmbedBlock()), ('document', wagtail.core.blocks.StructBlock([('document', wagtail.documents.blocks.DocumentChooserBlock()), ('title', wagtail.core.blocks.CharBlock(required=False))]))], blank=True),
        ),
    ]
