from django.db import models
# Create your models here.
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default = 0)

MAX_INDEX_LEVEL = 99
NEGATIVE_ONE = -1
ZERO = 0
SEQUENCE_DEFAULT = ZERO

from django.db.models.fields import URLField
"""
class phrits(models.Model)
    usr_modify_by = models.CharField(max_length=255)
    txt_content = models.TextField(default = "")
class Section(phrits)
class Link(phrits)
class Paragraph(Section)
class Page(Section, Link)
class Heading(Paragraph, Link)
class ItemList(Paragraph)
class Rec_Ingredient(Section)
class Rec_IngredientList(ItemList)
"""

class Page(models.Model):
    title = models.CharField(max_length=255, default="Page Title")
    dt_create = models.DateTimeField(auto_now_add=True)
    def get_content():
        # query the child table
        return None
    def get_heading():
        # query the child table
        return None
    def get_paragraph():
        # query the child table
        return None

class Paragraph(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    int_index = models.IntegerField(default=MAX_INDEX_LEVEL)
    int_sequence = models.IntegerField(default=SEQUENCE_DEFAULT)
    content = models.TextField()




# class phrits(models.Model):
#     usr_modify_by = models.CharField(max_length=255)
#     txt_content = models.TextField(default = "")
#     # Included with Model, I think
#     # ****************************
#     # pk_id = 0
#     # usr_author = "Fritz Knack"
#     # dt_create = ''
#     # dt_modify = ''

#     # To Do
#     # ****************************
#     # def save():
#     #     # updated usr_modified_by
#     #     return None

# class Link(phrits):
#     url = URLField()
#     url_text = models.CharField(max_length=255, default = "link text")

# class Section(phrits):
#     int_sequence = models.IntegerField(default = -1)
#     s_title = models.CharField(max_length=255, default = "Title")
#     def __str__(self):
#         return self.s_title

# class Heading(Paragraph):
#     link = Link()
#     def __str__(self):
#         return self.s_title

# class ItemList(Paragraph):
#     def __str__(self):
#         return self.s_title

# class Rec_Ingredient(Section):
#     quantity = models.CharField(max_length=64, default = "quantity")
#     measure = models.CharField(max_length=64, default = "measure")
#     ingredient = models.CharField(max_length=64, default = "ingredient")
#     vegetarian = models.BooleanField(default = False)
#     vegan = models.BooleanField(default = False)
#     raw = models.BooleanField(default = False)
#     fat_free = models.BooleanField(default = False)
#     embellishment =  models.TextField()
#     def __str__(self):
#         return self.ingredient
#     def is_vegan(self):
#         # query the children
#         return False
#     # def __str__(self):
#     # def is_vegan(self):
#     # def is_vegetarian(self):
#     # def is_raw(self):
#     # def is_fat_free(self):
    
# class Rec_IngredientList(ItemList):
#     def get_sections():
#         # query the child table
#         return None
#     def is_vegan(self):
#         # query the children
#         return False
#     # def __str__(self):
#     # def is_vegan(self):
#     # def is_vegetarian(self):
#     # def is_raw(self):
#     # def is_fat_free(self):
