from django.db import models

# Create your models here.
class Story(models.Model) :
    str_id = models.CharField(max_length=100)
    str_title = models.CharField
    str_author = models.CharField
    str_create_date = models.DateField
    str_last_update_date = models.DateField

    def __str__(self) -> str :
        text_to_show = "[" + self.str_id + "," + self.str_title + "," + self.str_author + "," + str(self.str_create_date) + "," + str(self.str_last_update_date) + "]"
        return text_to_show

class Character(models.Model) :
    chr_id = models.CharField(max_length=100)
    chr_str_id = models.CharField
    chr_name = models.CharField
    chr_type = models.CharField
    chr_story = models.TextField
    chr_image = models.ImageField

    def __str__(self) -> str :
        text_to_show = "[" + self.chr_id + "," + self.chr_name + "," + self.chr_type + "," + self.chr_story + "]"
        return text_to_show

class Item(models.Model) :
    itm_id = models.CharField(max_length=100)
    itm_str_id = models.CharField
    itm_name = models.CharField
    itm_description = models.TextField
    itm_image = models.ImageField

    def __str__(self) -> str :
        text_to_show = "[" + self.itm_id + "," + self.itm_name + "," + self.itm_description + "]"
        return text_to_show

class Paragraph(models.Model) :
    par_id = models.CharField(max_length=100)
    par_str_id = models.CharField
    par_body = models.TextField()
    par_is_root = models.BooleanField(default=False)
    par_is_end = models.BooleanField(default=False)

    def __str__(self) -> str :
        text_to_show = "[" + self.par_id +";"+ self.par_body +";"+ str(self.par_is_root) +";"+ str(self.par_is_end) +"]"
        return text_to_show

    def getParBody(self) :
        return self.par_body

    def getParId(self) :
        return self.par_id

class ParagraphLinks(models.Model) :
    par_from_id = models.CharField(max_length=100)
    par_from_text = models.TextField
    par_to_id = models.CharField(max_length=100)

    def __str__(self) -> str :
        text_to_show = "["+ self.par_from_id +";"+ self.par_from_text +";"+ self.par_to_id +"]"
        return text_to_show

    def getFromText(self) :
        return self.par_from_text
    
