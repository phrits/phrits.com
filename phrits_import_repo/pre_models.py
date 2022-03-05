
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default = 0)

from django.db import models
from django.db.models.fields import URLField

"""
class phrits(models.Model):
    id = 0
    usr_author = "Fritz Knack"
    dt_create = models.DateTimeField(auto_now=True)
    dt_modify = dt_create
    usr_modify_by = usr_author
class Section(phrits):
class Heading(Section):
class Paragraph(Section):
class Rec_Ingredient(Section):
"""
class phrits(models.Model):
    usr_modify_by = models.CharField(max_length=255)
    txt_content = models.TextField(default = "")
    # Included with Model, I think
    # ****************************
    # pk_id = 0
    # usr_author = "Fritz Knack"
    # dt_create = ''
    # dt_modify = ''

    # To Do
    # ****************************
    # def save():
    #     # updated usr_modified_by
    #     return None

class Link(phrits):
    url = URLField()
    url_text = models.CharField(max_length=255, default = "link text")

class Section(phrits):
    int_sequence = models.IntegerField(default = -1)
    s_title = models.CharField(max_length=255, default = "Section Title")
    def __str__(self):
        return self.s_title

class HPage(Section, Link):
    # Included
    # ********
    # int_sequence = 0
    # url = URLField()
    # url_text = models.CharField(max_length=255, default = "link text")
    s_title = models.CharField(max_length=255, default = "Page Title")
    def get_sections():
        # query the child table
        return None
    arr_sections = [Section]

class Paragraph(Section):
    fk_parent = models.ForeignKey(Section, on_delete=models.CASCADE)
    s_title = models.CharField(max_length=255, default = "")
    def __str__(self):
        return self.txt_content.split()[:8]

class Heading(Paragraph, Link):
    fk_parent = fk_parent = models.ForeignKey(Section, on_delete=models.CASCADE)
    s_title = models.CharField(max_length=255, default = "Heading")
    def __str__(self):
        return self.s_title

class ItemList(Paragraph):
    fk_parent = fk_parent = models.ForeignKey(Section, on_delete=models.CASCADE)


class Rec_Ingredient(Section):
    fk_parent = fk_parent = models.ForeignKey(Section, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=64, default = "quantity")
    measure = models.CharField(max_length=64, default = "measure")
    ingredient = models.CharField(max_length=64, default = "ingredient")
    vegetarian = models.BooleanField(default = False)
    vegan = models.BooleanField(default = False)
    raw = models.BooleanField(default = False)
    fat_free = models.BooleanField(default = False)
    embellishment =  models.TextField()
    def __str__(self):
        return self.ingredient
    def is_vegan(self):
        # query the children
        return False
    # def __str__(self):
    # def is_vegan(self):
    # def is_vegetarian(self):
    # def is_raw(self):
    # def is_fat_free(self):
    
class Rec_IngredientList(ItemList):
    fk_parent = fk_parent = models.ForeignKey(Section, on_delete=models.CASCADE)
    def get_sections():
        # query the child table
        return None
    def is_vegan(self):
        # query the children
        return False
    # def __str__(self):
    # def is_vegan(self):
    # def is_vegetarian(self):
    # def is_raw(self):
    # def is_fat_free(self):
