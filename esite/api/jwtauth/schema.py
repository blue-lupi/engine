from django.contrib.auth import get_user_model
from wagtail.core.models import Page as wagtailPage

import graphene
import graphql_jwt
from graphene_django import DjangoObjectType
from graphql import GraphQLError

from graphql.execution.base import ResolveInfo
from ..types.core import Page

from esite.api.permissions import with_page_permissions

# Create your registration related graphql schemes here.

#class UserType(DjangoObjectType):
#    class Meta:
#        model = User
#        exclude_fields = ['password']

class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    home = graphene.Field(Page)
    survey = graphene.Field(Page)

    homequery = wagtailPage.objects.filter(slug="home")
    surveyquery = wagtailPage.objects.filter(slug="survey")

    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(home=with_page_permissions(info.context, cls.homequery.specific()).live().first(), survey=with_page_permissions(info.context, cls.surveyquery.specific()).live().first())
