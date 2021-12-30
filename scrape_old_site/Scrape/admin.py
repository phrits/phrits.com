from django.contrib import admin

# Register your models here.

from django.contrib import admin

#from .models import Heading, ItemList, Link, Page, Paragraph, Rec_Ingredient, Rec_IngredientList, Section
from .models import Page, Paragraph

admin.site.register(Page)
admin.site.register(Paragraph)
# admin.site.register(Heading)
# admin.site.register(ItemList)
# admin.site.register(Link)
# admin.site.register(Rec_Ingredient)
# admin.site.register(Rec_IngredientList)
# admin.site.register(Section)