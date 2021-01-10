from django.db import models

class Song(models.Model):
    name = models.CharField(max_length=80)
    album = models.CharField(max_length=80)
    artist = models.CharField(max_length=80)
    year = models.CharField(max_length=80)

    def getName(self):
        return self.name

    def getAlbum(self):
        return self.album

    def getArtist(self):
        return self.artist

    def getYear(self):
        return self.year