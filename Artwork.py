#!/usr/bin/env python
# coding: utf-8

# In[2]:


from Catalog import Catalog
# class Artwork has been created here
class Artwork(Catalog):
    # constructor has been created to intialize parameters
    def __init__(self, artworkId, artworkTitle, artist, dateOfCreation, historicalSignificance, location):
        super().__init__()  # Initialize parent class
        self.artworkId = artworkId
        self.artworkTitle = artworkTitle
        self.artist = artist
        self.dateOfCreation = dateOfCreation
        self.historicalSignificance = historicalSignificance
        self.location = location
        
# function has been created to get the artwork id 
    def getArtworkId(self):
        return self.artworkId
    
# function has been created to get the artwork title
    def getArtworkTitle(self):
        return self.artworkTitle

# function has been created to get the artwork name
    def getArtist(self):
        return self.artist

# function has been created to get the date of creation of artwork 
    def getDateOfCreation(self):
        return self.dateOfCreation

# function has been created to get the historical significance of artwork 
    def getHistoricalSignificance(self):
        return self.historicalSignificance

# function has been created to get the location of artwork 
    def getLocation(self):
        return self.location

# function has been created to set the id of artwork 
    def setArtworkId(self, artworkId):
        self.artworkId = artworkId

# function has been created to set the title of artwork
    def setArtworkTitle(self, artworkTitle):
        self.artworkTitle = artworkTitle

# function has been created to set the artist
    def setArtist(self, artist):
        self.artist = artist

# function has been created to set the date of creation of artwork
    def setDateOfCreation(self, dateOfCreation):
        self.dateOfCreation = dateOfCreation

# function has been created to set the historical significance of artwork        
    def setHistoricalSignificance(self, historicalSignificance):
        self.historicalSignificance = historicalSignificance

# function has been created to set location of artwork        
    def setLocation(self, location):
        self.location = location


# In[ ]:





# In[ ]:




