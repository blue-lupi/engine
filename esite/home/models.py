from django.http import HttpResponse
from django.db import models
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


#> Header
class _H_HeroBlock(blocks.StructBlock):
    slide_image = ImageChooserBlock(null=True, blank=False, required=False, help_text="Big, high resolution slider image")
    slide_loadimage = blocks.BooleanBlock(null=True, blank=False, required=False, default=True, help_text="Whether or not to load the slide image from CMS (Unchecked is better for performance, only check if you want to test a new image)")
    slide_button = SnippetChooserBlock(Button, null=True, blank=False, required=False, help_text="The button displayed at the frontpage slider")

#> Why Section
class Why_ColumnBlock(blocks.StructBlock):
    Column_image = ImageChooserBlock(null=True, blank=False, required=False, help_text="Icon representating the below content")
    Column_head = blocks.CharBlock(null=True, blank=False, required=False, classname="full title", help_text="The bold header text at the frontpage slider")
    Column_subhead = blocks.RichTextBlock(null=True, blank=False, required=False, help_text="The content of the frontpage slider element", classname="full")
    Column_paragraph = blocks.RichTextBlock(null=True, blank=False, required=False, help_text="Formatted text", classname="full")

class _S_WhyBlock(blocks.StructBlock):
    why_head = blocks.CharBlock(null=True, blank=False, required=False, classname="full title", help_text="Bold header text")
    why_displayhead = blocks.BooleanBlock(null=True, blank=False, required=False, default=True, help_text="Whether or not to display the header")
    why_Columns = blocks.StreamBlock([
        ('why_Column', Why_ColumnBlock(null=True, blank=False, required=False, icon='fa-columns'))
    ], null=True, blank=False, required=False, max_num=8)

#> About Shop
class Shop_PricingcardBlock(blocks.StructBlock):
    shopcard_background = ColorBlock(null=True, blank=False, required=False, help_text="Select background color that contrasts text")
    shopcard_title = blocks.CharBlock(null=True, blank=False, required=False, classname="full title", help_text="Title of pricing card")
    shopcard_description = blocks.RichTextBlock(null=True, blank=False, required=False, help_text="Description of offer", classname="full")
    shopcard_price = blocks.DecimalBlock(null=True, blank=False, required=False, decimal_places=2, help="Price of the offer")
    shopcard_sucessmsg = blocks.RichTextBlock(null=True, blank=False, required=False, help_text="Success message", classname="full")
    shopcard_button = SnippetChooserBlock(Button, null=True, blank=False, required=False, help_text="Button displayed at the pricing-section")

class _S_ShopBlock(blocks.StructBlock):
    #shop_background = ColorBlock(null=True, blank=False, required=False, help_text="Select background color that contrasts text")
    shop_head = blocks.CharBlock(null=True, blank=False, required=False, classname="full title", help_text="Bold header text")
    shop_displayhead = blocks.BooleanBlock(null=True, blank=False, required=False, default=True, help_text="Whether or not to display the header")

#> About Section
class About_CardBlock(blocks.StructBlock):
    card_head = blocks.CharBlock(null=True, blank=False, required=False, classname="full title", help_text="The bold header text at the frontpage slider")
    card_paragraph = blocks.RichTextBlock(null=True, blank=False, required=False, help_text="Formatted text", classname="full")

class _S_AboutBlock(blocks.StructBlock):
    about_head = blocks.CharBlock(null=True, blank=False, required=False, classname="full title", help_text="Bold header text")
    about_displayhead = blocks.BooleanBlock(null=True, blank=False, required=False, default=True, help_text="Whether or not to display the header")
    about_cards = blocks.StreamBlock([
        ('aboutcard', About_CardBlock(null=True, blank=False, required=False, icon='fa-info'))
    ], null=True, blank=False, required=False, max_num=6)

#> Instagram Section
class _S_InstagramBlock(blocks.StructBlock):
    instagram_id = blocks.CharBlock(null=True, blank=False, required=False, classname="full", help_text="Instagram-Account id")
    instagram_pc = blocks.CharBlock(null=True, blank=False, required=False, classname="full", help_text="Instagram-Post count")

#> Steps Section
class Steps_StepBlock(blocks.StructBlock):
    step_image = ImageChooserBlock(null=True, blank=False, required=False, help_text="Image fitting this step")
    step_head = blocks.CharBlock(null=True, blank=False, required=False, classname="full title", help_text="Bold header text")
    step_subhead = blocks.RichTextBlock(null=True, blank=False, required=False, help_text="Short introduction to the following paragraph", classname="full")
    step_paragraph = blocks.RichTextBlock(null=True, blank=False, required=False, help_text="Step paragraph", classname="full")

class _S_StepsBlock(blocks.StructBlock):
    steps_head = blocks.CharBlock(null=True, blank=False, required=False, classname="full title", help_text="Bold header text")
    steps_displayhead = blocks.BooleanBlock(null=True, blank=False, required=False, default=True, help_text="Whether or not to display the header")
    steps_steps = blocks.StreamBlock([
        ('step', Steps_StepBlock(null=True, blank=False, required=False, icon='fa-list-ol'))
    ], null=True, blank=False, required=False, max_num=4)

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

#> Instagram Section
class _S_WolfBlock(blocks.StructBlock):
    wolf_head = blocks.CharBlock(null=True, blank=False, required=False, classname="full", help_text="Bold header text")
    wolf_subhead = blocks.RichTextBlock(null=True, blank=False, required=False, help_text="The content of the black wolf coffee intro", classname="full")

#> Trusted Section
class FAQ_QuestionBlock(blocks.StructBlock):
    question_icon = blocks.CharBlock(null=True, blank=True, required=True, help_text="Font Awesome icon name (e.g. facebook-f) from https://fontawesome.com/icons?d=gallery&s=solid&m=free")
    question_head = blocks.CharBlock(null=True, blank=False, required=False, classname="full title", help_text="Bold header text")
    question_paragraph = blocks.RichTextBlock(null=True, blank=False, required=False, help_text="Formatted text", classname="full")
    question_link = blocks.URLBlock(null=True, blank=True, required=True, help_text="Important! Format https://www.domain.tld/xyz")

class _S_FAQBlock(blocks.StructBlock):
    header = blocks.CharBlock(null=True, blank=False, required=False, classname="full title", help_text="Bold header text")
    questions = blocks.StreamBlock([
        ('question', FAQ_QuestionBlock(null=True, blank=False, required=False, icon='fa-question'))
    ], null=True, required=False)

#> Homepage
class HomePage(Page):
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
        ('link', blocks.URLBlock(help_text="Important! Format https://www.domain.tld/xyz"))
    ])

    array = []
    def sociallink_company(self):
        for link in self.sociallinks:
            self.array.append(str(link).split(".")[1])
        return self.array


    headers = StreamField([
        ('h_hero', _H_HeroBlock(null=True, blank=False, icon='image')),
        ('code', blocks.RawHTMLBlock(null=True, blank=True, classname="full", icon='code'))
    ], null=True, blank=False)

    sections = StreamField([
        ('s_why', _S_WhyBlock(null=True, blank=False, icon='fa-columns')),
        ('s_about', _S_AboutBlock(null=True, blank=False, icon='fa-info')),
        ('s_instagram', _S_InstagramBlock(null=True, blank=False, icon='fa-instagram')),
        ('s_steps', _S_StepsBlock(null=True, blank=False, icon='fa-list-ol')),
        ('s_shop', _S_ShopBlock(null=True, blank=False, icon='home')),
        ('s_trusted', _S_TrustedBlock(null=True, blank=False, icon='fa-id-card-o')),
        ('s_wolf', _S_WolfBlock(null=True, blank=False, icon='fa-coffee')),
        ('s_faq', _S_FAQBlock(null=True, blank=False, icon='fa-question')),
        ('code', blocks.RawHTMLBlock(null=True, blank=True, classname="full", icon='code'))
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
        StreamFieldPanel('headers'),
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