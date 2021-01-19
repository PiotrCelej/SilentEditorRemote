from django.db import models
import hashlib

# Create your models here.
class MainTextBody(models.Model) :
    text_id = models.IntegerField(default=0)
    name = models.CharField(max_length=512)
    body_text = models.TextField()
    last_update_date = models.DateTimeField('last update')
    author = models.CharField(max_length=512)

    def __str__(self) -> str:
        text_to_show = self.author + " last updated: " + str(self.last_update_date) + "\n\n" + self.body_text
        return text_to_show

    def getTextBody(self) :
        return self.body_text
    
    def getTextMetadata(self) :
        return [self.text_id, self.name, str(self.last_update_date), self.author]

class UserProfile(models.Model) :
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_pass = models.CharField(max_length=100)

    def getUserProfile(self) :
        return [self.user_name, self.user_email]

    def changePass(self, passPhase) :
        self.user_pass = passPhase.encode()
    
    def checkPass(self, passPhase) :
        hashed_pass= passPhase.encode()
        if hashed_pass == self.user_pass :
            return True
        else :
            return False