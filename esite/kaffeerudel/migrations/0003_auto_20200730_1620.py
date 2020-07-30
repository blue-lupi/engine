# Generated by Django 2.2.13 on 2020-07-30 14:20

from django.db import migrations, models
import esite.kaffeerudel.models
import wagtail.core.blocks
import wagtail.core.blocks.static_block
import wagtail.core.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('kaffeerudel', '0002_auto_20200729_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='kaffeerudelpage',
            name='about',
            field=wagtail.core.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='kaffeerudelpage',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='kaffeerudelpage',
            name='cancellation_policy',
            field=wagtail.core.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='kaffeerudelpage',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='kaffeerudelpage',
            name='copyrightholder',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='kaffeerudelpage',
            name='court_of_registry',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='kaffeerudelpage',
            name='email',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='kaffeerudelpage',
            name='footers',
            field=wagtail.core.fields.StreamField([('f_partners', wagtail.core.blocks.StructBlock([('trusted_partner', wagtail.core.blocks.StreamBlock([('partner', wagtail.core.blocks.StructBlock([('partner_logo', wagtail.images.blocks.ImageChooserBlock(blank=False, help_text='Image fitting this step', null=True, required=False)), ('partner_link', wagtail.core.blocks.URLBlock(blank=False, help_text='Important! Format https://www.domain.tld/xyz', null=True, required=False))], blank=True, icon='fa-id-badge', null=True, required=True))], null=True, required=False))], blank=False, icon='fa-id-badge', null=True)), ('s_paymentmethods', wagtail.core.blocks.StructBlock([('trusted_paymentmethods', wagtail.core.blocks.StreamBlock([('paymentmethods', wagtail.core.blocks.StructBlock([('partner_logo', wagtail.images.blocks.ImageChooserBlock(blank=False, help_text='Image fitting this step', null=True, required=False)), ('partner_link', wagtail.core.blocks.URLBlock(blank=False, help_text='Important! Format https://www.domain.tld/xyz', null=True, required=False))], blank=True, icon='fa-id-badge', null=True, required=True))], null=True, required=False))], blank=False, icon='fa-credit-card', null=True))], null=True),
        ),
        migrations.AddField(
            model_name='kaffeerudelpage',
            name='gtc',
            field=wagtail.core.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='kaffeerudelpage',
            name='ownership',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='kaffeerudelpage',
            name='place_of_registry',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='kaffeerudelpage',
            name='privacy',
            field=wagtail.core.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='kaffeerudelpage',
            name='shipping',
            field=wagtail.core.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='kaffeerudelpage',
            name='sociallinks',
            field=wagtail.core.fields.StreamField([('link', wagtail.core.blocks.URLBlock(blank=False, help_text='Important! Format https://www.domain.tld/xyz', null=True))], null=True),
        ),
        migrations.AddField(
            model_name='kaffeerudelpage',
            name='tax_id',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='kaffeerudelpage',
            name='telefax',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='kaffeerudelpage',
            name='telephone',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='kaffeerudelpage',
            name='trade_register_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='kaffeerudelpage',
            name='vat_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='kaffeerudelpage',
            name='whatsapp_contactline',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='kaffeerudelpage',
            name='whatsapp_telephone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='kaffeerudelpage',
            name='zip_code',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='kaffeerudelpage',
            name='sections',
            field=wagtail.core.fields.StreamField([('s_head', wagtail.core.blocks.StructBlock([('head', wagtail.core.blocks.CharBlock(blank=False, classname='full title', help_text='Bold header text', null=True, required=True)), ('lead', wagtail.core.blocks.CharBlock(blank=False, help_text='The content of this element', null=True, required=False))], blank=False, icon='fa-columns', null=True)), ('s_feature', wagtail.core.blocks.StructBlock([('features', wagtail.core.blocks.StreamBlock([('feature', wagtail.core.blocks.StructBlock([('feature_image', wagtail.images.blocks.ImageChooserBlock(blank=False, help_text='Icon representating the below content', null=True, required=True)), ('feature_head', wagtail.core.blocks.CharBlock(blank=False, classname='full title', help_text='The bold header text', null=True, required=False)), ('feature_lead', wagtail.core.blocks.CharBlock(blank=False, help_text='The content of this element', null=True, required=False))], blank=False, icon='fa-info', null=True, required=False))], help_text='Add between 1 and 3 Features', max_num=3, null=True, required=True))], blank=False, icon='fa-info', null=True)), ('s_shop', wagtail.core.blocks.StructBlock([('shop', wagtail.core.blocks.static_block.StaticBlock(admin_text='Insert this block in order to display the shop on your website.', blank=True, icon='fa-shopping-basket', null=True))], blank=False, icon='fa-shopping-basket', null=True)), ('s_blue', wagtail.core.blocks.StructBlock([('blue_head', wagtail.core.blocks.CharBlock(blank=False, classname='full title', help_text='Bold header text', label='Head', null=True, required=True)), ('blue_lead', wagtail.core.blocks.CharBlock(blank=False, help_text='The content of this element', label='Lead', null=True, required=False)), ('blue_button', wagtail.snippets.blocks.SnippetChooserBlock(esite.kaffeerudel.models.Button, blank=False, help_text='Button at the Blue Section', label='Button', null=True, required=True))], blank=False, icon='home', null=True)), ('s_contentleft', wagtail.core.blocks.StructBlock([('cl_image', wagtail.images.blocks.ImageChooserBlock(blank=False, help_text='Select an image', label='Image', null=True, required=True)), ('cl_head', wagtail.core.blocks.CharBlock(blank=False, classname='full title', help_text='Bold header text', label='Head', null=True, required=True)), ('cl_lead', wagtail.core.blocks.CharBlock(blank=False, help_text='The content of this element', label='Lead', null=True, required=False)), ('cl_text', wagtail.core.blocks.RichTextBlock(blank=False, label='Text', null=True, required=True)), ('cl_button', wagtail.snippets.blocks.SnippetChooserBlock(esite.kaffeerudel.models.Button, blank=False, help_text='Button for Content Left', label='Button', null=True, required=False)), ('cl_center', wagtail.core.blocks.BooleanBlock(help_text='Align center', label='Align center', required=False))], blank=False, icon='fa-align-center', null=True)), ('s_contentright', wagtail.core.blocks.StructBlock([('cr_image', wagtail.images.blocks.ImageChooserBlock(blank=False, help_text='Select an image', label='Image', null=True, required=True)), ('cr_head', wagtail.core.blocks.CharBlock(blank=False, classname='full title', help_text='Bold header text', label='Head', null=True, required=True)), ('cr_lead', wagtail.core.blocks.CharBlock(blank=False, help_text='The content of this element', label='Lead', null=True, required=False)), ('cr_text', wagtail.core.blocks.RichTextBlock(blank=False, label='Text', null=True, required=True)), ('cr_button', wagtail.snippets.blocks.SnippetChooserBlock(esite.kaffeerudel.models.Button, blank=False, help_text='Button for Content Right', label='Button', null=True, required=False)), ('cr_center', wagtail.core.blocks.BooleanBlock(help_text='Align center', label='Align center', required=False))], blank=False, icon='fa-align-center', null=True)), ('s_images', wagtail.core.blocks.StructBlock([('images', wagtail.core.blocks.StreamBlock([('image', wagtail.core.blocks.StructBlock([('image_img', wagtail.images.blocks.ImageChooserBlock(blank=False, help_text='Select an image', label='Image', null=True, required=True)), ('image_link', wagtail.core.blocks.URLBlock(blank=False, help_text='Important! Format https://www.domain.tld/xyz', label='Link', null=True, required=False))], blank=False, icon='fa-picture-o', null=True, required=False))], help_text='Add between 1 and 20 Images', max_num=20, null=True, required=True))], blank=False, icon='fa-picture-o', null=True)), ('s_instagram', wagtail.core.blocks.StructBlock([('instagram_id', wagtail.core.blocks.CharBlock(blank=False, help_text='Instagram Account ID', null=True, required=False)), ('instagram_pc', wagtail.core.blocks.IntegerBlock(blank=False, help_text='Instagram Post Count', null=True, required=False))], blank=False, icon='fa-instagram', null=True)), ('s_faq', wagtail.core.blocks.StructBlock([('questions', wagtail.core.blocks.StreamBlock([('question', wagtail.core.blocks.StructBlock([('question_question', wagtail.core.blocks.CharBlock(blank=False, classname='full title', help_text='FAQ Question', label='Question', null=True, required=True)), ('question_answer', wagtail.core.blocks.RichTextBlock(blank=False, help_text='FAQ Answer', label='Answer', null=True, required=True))], blank=False, icon='fa-question', null=True, required=True))], null=True, required=False))], blank=False, icon='fa-question', null=True)), ('s_ratings', wagtail.core.blocks.StructBlock([('ratings_count', wagtail.core.blocks.IntegerBlock(blank=False, help_text='How many ratings will be displayed', null=True, required=False))], blank=False, icon='fa-star', null=True))], null=True),
        ),
    ]
