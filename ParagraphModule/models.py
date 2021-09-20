from django.db import models

# Create your models here.
class Paragraph(models.Model) :
    par_id = models.CharField(max_length=100)
    par_body = models.TextField()
    par_is_root = models.BooleanField(default=False)
    par_is_end = models.BooleanField(default=False)

    def __str__(self) -> str :
        text_to_show = "[" + self.par_id +";"+ self.par_body +";"+ self.par_is_root +";"+ self.par_is_end +"]"
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

class Character(models.Model) :
    char_id = models.CharField(max_length=100)

    # types of characters:
    # NPC - npc which interacts with our hero
    # HERO - a hero managed by palyer
    char_type = models.CharField(max_length=20)
    char_name = models.CharField(max_length=100)
    
