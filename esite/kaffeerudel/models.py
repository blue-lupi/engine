from django.http import HttpResponse
from django.db import models
from django.utils.safestring import mark_safe
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.admin.edit_handlers import PageChooserPanel, TabbedInterface, ObjectList, InlinePanel, StreamFieldPanel, MultiFieldPanel, FieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.forms.models import AbstractForm, AbstractFormField
from modelcluster.fields import ParentalKey

from esite.colorfield.fields import ColorField, ColorAlphaField
from esite.colorfield.blocks import ColorBlock, ColorAlphaBlock, GradientColorBlock

#from grapple.models import (
#    GraphQLField,
#    GraphQLString,
#    GraphQLStreamfield,
#)

# Create your homepage related models here.

@register_snippet
class Button(models.Model):
    button_title = models.CharField(null=True, blank=False, max_length=255)
    button_embed = models.CharField(null=True, blank=True, max_length=255)
    button_link = models.URLField(null=True, blank=True)
    button_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    panels = [
        FieldPanel('button_title'),
        FieldPanel('button_embed'),
        FieldPanel('button_link'),
        PageChooserPanel('button_page')
    ]

    def __str__(self):
        return self.button_title


class _S_HeadBlock(blocks.StructBlock):
    head = blocks.CharBlock(null=True, blank=False, required=True, classname="full title", help_text="Bold header text")
    lead = blocks.CharBlock(null=True, blank=False, required=False, help_text="The content of this element")

class FeatureFeatureBlock(blocks.StructBlock):
    feature_image = ImageChooserBlock(null=True, blank=False, required=True, help_text="Icon representating the below content")
    feature_head = blocks.CharBlock(null=True, blank=False, required=False, classname="full title", help_text="The bold header text")
    feature_lead = blocks.CharBlock(null=True, blank=False, required=False, help_text="The content of this element")

class _S_FeatureBlock(blocks.StructBlock):
    features = blocks.StreamBlock([
        ('feature', FeatureFeatureBlock(null=True, blank=False, required=False, icon='fa-info'))
    ], null=True, required=True, help_text='Add between 1 and 3 Features', max_num=3)

class _S_BlueBlock(blocks.StructBlock):
    #shop_background = ColorBlock(null=True, blank=False, required=False, help_text="Select background color that contrasts text")
    blue_head = blocks.CharBlock(label='Head', null=True, blank=False, required=True, classname="full title", help_text="Bold header text")
    blue_lead = blocks.CharBlock(label='Lead', null=True, blank=False, required=False, help_text="The content of this element")
    blue_button = SnippetChooserBlock(Button, label='Button', null=True, blank=False, required=True, help_text="Button at the Blue Section")

class _S_ContentRightBlock(blocks.StructBlock):
    cr_image = ImageChooserBlock(label='Image', null=True, blank=False, required=True, help_text="Select an image")
    cr_head = blocks.CharBlock(label='Head', null=True, blank=False, required=True, classname="full title", help_text="Bold header text")
    cr_lead = blocks.CharBlock(label='Lead', null=True, blank=False, required=False, help_text="The content of this element")
    cr_text = blocks.RichTextBlock(label='Text', null=True, blank=False, required=True)
    cr_button = SnippetChooserBlock(Button, label='Button', null=True, blank=False, required=False, help_text="Button for Content Right")
    cr_center = blocks.BooleanBlock(label='Align center', help_text='Align center', required=False)

class _S_ContentLeftBlock(blocks.StructBlock):
    cl_image = ImageChooserBlock(label='Image', null=True, blank=False, required=True, help_text="Select an image")
    cl_head = blocks.CharBlock(label='Head', null=True, blank=False, required=True, classname="full title", help_text="Bold header text")
    cl_lead = blocks.CharBlock(label='Lead', null=True, blank=False, required=False, help_text="The content of this element")
    cl_text = blocks.RichTextBlock(label='Text', null=True, blank=False, required=True)
    cl_button = SnippetChooserBlock(Button, label='Button', null=True, blank=False, required=False, help_text="Button for Content Left")
    cl_center = blocks.BooleanBlock(label='Align center', help_text='Align center', required=False)

class ImageImageBlock(blocks.StructBlock):
    image_img = ImageChooserBlock(label='Image', null=True, blank=False, required=True, help_text="Select an image")
    image_link = blocks.URLBlock(label='Link', null=True, blank=False, required=False, help_text="Important! Format https://www.domain.tld/xyz")

class _S_ImagesBlock(blocks.StructBlock):
    images = blocks.StreamBlock([
        ('image', ImageImageBlock(null=True, blank=False, required=False, icon='fa-picture-o'))
    ], null=True, required=True, help_text='Add between 1 and 20 Images', max_num=20)

#> Instagram Section
class _S_InstagramBlock(blocks.StructBlock):
    instagram_id = blocks.CharBlock(null=True, blank=False, required=False, help_text="Instagram Account ID")
    instagram_pc = blocks.IntegerBlock(null=True, blank=False, required=False, help_text="Instagram Post Count")

#> Trusted Section
class FAQ_QuestionBlock(blocks.StructBlock):
    question_question = blocks.CharBlock(label='Question', null=True, blank=False, required=True, classname="full title", help_text="FAQ Question")
    question_answer = blocks.RichTextBlock(label='Answer', null=True, blank=False, required=True, help_text="FAQ Answer")

class _S_FAQBlock(blocks.StructBlock):
    # header = blocks.CharBlock(null=True, blank=False, required=False, classname="full title", help_text="Bold header text")
    questions = blocks.StreamBlock([
        ('question', FAQ_QuestionBlock(null=True, blank=False, required=True, icon='fa-question'))
    ], null=True, required=False)


class _S_RatingsBlock(blocks.StructBlock):
    ratings_count = blocks.IntegerBlock(null=True, blank=False, required=False, help_text="How many ratings will be displayed")


#> Trusted Section
class Trusted_PartnerBlock(blocks.StructBlock):
    partner_logo = ImageChooserBlock(null=True, blank=False, required=False, help_text="Image fitting this step")
    partner_link = blocks.URLBlock(null=True, blank=False, required=False, help_text="Important! Format https://www.domain.tld/xyz")

class _S_TrustedBlock(blocks.StructBlock):
    trusted_partner = blocks.StreamBlock([
        ('partner', Trusted_PartnerBlock(null=True, blank=True, required=True, icon='fa-id-card'))
    ], null=True, required=False)

class _S_SmallTrustedBlock(blocks.StructBlock):
    trusted_partner = blocks.StreamBlock([
        ('partner', Trusted_PartnerBlock(null=True, blank=True, required=True, icon='fa-id-badge'))
    ], null=True, required=False)

class _S_SmallTrustedPBlock(blocks.StructBlock):
    trusted_paymentmethods = blocks.StreamBlock([
        ('paymentmethods', Trusted_PartnerBlock(null=True, blank=True, required=True, icon='fa-id-badge'))
    ], null=True, required=False)

class _S_ShopBlock(blocks.StructBlock):
    shop = blocks.StaticBlock(
        admin_text=mark_safe('Insert this block in order to display the shop on your website.'),
        null=True, blank=True, icon='fa-shopping-basket')


#> Homepage
class KaffeerudelPage(Page):
    city = models.CharField(null=True, blank=False, max_length=255)
    zip_code = models.CharField(null=True, blank=False, max_length=255)
    address = models.CharField(null=True, blank=False, max_length=255)
    telephone = models.CharField(null=True, blank=False, max_length=255)
    telefax = models.CharField(null=True, blank=False, max_length=255)
    vat_number = models.CharField(null=True, blank=False, max_length=255)
    whatsapp_telephone = models.CharField(null=True, blank=True, max_length=255)
    whatsapp_contactline = models.CharField(null=True, blank=True, max_length=255)
    tax_id = models.CharField(null=True, blank=False, max_length=255)
    trade_register_number = models.CharField(null=True, blank=False, max_length=255)
    court_of_registry = models.CharField(null=True, blank=False, max_length=255)
    place_of_registry = models.CharField(null=True, blank=False, max_length=255)
    trade_register_number = models.CharField(null=True, blank=False, max_length=255)
    ownership = models.CharField(null=True, blank=False, max_length=255)
    email = models.CharField(null=True, blank=False, max_length=255)

    copyrightholder = models.CharField(null=True, blank=False, max_length=255)

    about = RichTextField(null=True, blank=False)
    privacy = RichTextField(null=True, blank=False)
    shipping = RichTextField(null=True, blank=False)
    gtc = RichTextField(null=True, blank=False)
    cancellation_policy = RichTextField(null=True, blank=False)

    sociallinks = StreamField([
        ('link', blocks.URLBlock(null=True, blank=False, help_text="Important! Format https://www.domain.tld/xyz"))
    ], null=True, blank=False)

    array = []
    def sociallink_company(self):
        for link in self.sociallinks:
            self.array.append(str(link).split(".")[1])
        return self.array


    sections = StreamField([
        ('s_head', _S_HeadBlock(null=True, blank=False, icon='fa-columns')),
        ('s_feature', _S_FeatureBlock(null=True, blank=False, icon='fa-info')),
        ('s_shop', _S_ShopBlock(null=True, blank=False, icon='fa-shopping-basket')),
        ('s_blue', _S_BlueBlock(null=True, blank=False, icon='home')),
        ('s_contentleft', _S_ContentLeftBlock(null=True, blank=False, icon='fa-align-center')),
        ('s_contentright', _S_ContentRightBlock(null=True, blank=False, icon='fa-align-center')),
        ('s_images', _S_ImagesBlock(null=True, blank=False, icon='fa-picture-o')),
        ('s_instagram', _S_InstagramBlock(null=True, blank=False, icon='fa-instagram')),
        ('s_faq', _S_FAQBlock(null=True, blank=False, icon='fa-question')),
        ('s_ratings', _S_RatingsBlock(null=True, blank=False, icon='fa-star')),
        # ('code', blocks.RawHTMLBlock(null=True, blank=True, classname="full", icon='code'))
    ], null=True, blank=False)

    footers = StreamField([
        ('f_partners', _S_SmallTrustedBlock(null=True, blank=False, icon='fa-id-badge')),
        ('s_paymentmethods', _S_SmallTrustedPBlock(null=True, blank=False, icon='fa-credit-card')),
    ], null=True, blank=False)

    token = models.CharField(null=True, blank=True, max_length=255)

    #graphql_fields = [
    #    GraphQLStreamfield("headers"),
    #    GraphQLStreamfield("sections"),
    #]

    main_content_panels = [
        StreamFieldPanel('sections'),
        StreamFieldPanel('footers')
    ]

    imprint_panels = [
        MultiFieldPanel(
            [
            FieldPanel('city'),
            FieldPanel('zip_code'),
            FieldPanel('address'),
            FieldPanel('telephone'),
            FieldPanel('telefax'),
            FieldPanel('whatsapp_telephone'),
            FieldPanel('whatsapp_contactline'),
            FieldPanel('email'),
            FieldPanel('copyrightholder')
            ],
            heading="contact",
        ),
        MultiFieldPanel(
            [
            FieldPanel('vat_number'),
            FieldPanel('tax_id'),
            FieldPanel('trade_register_number'),
            FieldPanel('court_of_registry'),
            FieldPanel('place_of_registry'),
            FieldPanel('trade_register_number'),
            FieldPanel('ownership')
            ],
            heading="legal",
        ),
        StreamFieldPanel('sociallinks'),
        MultiFieldPanel(
            [
            FieldPanel('about'),
            FieldPanel('privacy'),
            FieldPanel('shipping'),
            FieldPanel('gtc'),
            FieldPanel('cancellation_policy'),
            ],
            heading="terms",
        )
    ]

    token_panel = [
        FieldPanel('token')
    ]

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels + main_content_panels, heading='Main'),
        ObjectList(imprint_panels, heading='Imprint'),
        ObjectList(Page.promote_panels + token_panel + Page.settings_panels, heading='Settings', classname="settings")
    ])

    preview_modes = []