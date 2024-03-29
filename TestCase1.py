#!/usr/bin/env python
# coding: utf-8

# In[3]:


from datetime import datetime

# Import the Artwork class
from Artwork import Artwork

# Create an instance of the Artwork class
artwork = Artwork(
    artworkId=123,
    artworkTitle="In Fontainebleau Forest: Pines and Birch Trees in the Rocks",
    artist="Camille Corot",
    dateOfCreation=datetime(1845, 6, 1),
    historicalSignificance="graphic arts ",
    location="Permanent Galleries"
)

# Access attributes of the artwork instance
print("New Artwork has been added here are the details")
print("Artwork ID:", artwork.artworkId)
print("Artwork Title:", artwork.artworkTitle)
print("Artist:", artwork.artist)
print("Date of Creation:", artwork.dateOfCreation)
print("Historical Significance:", artwork.historicalSignificance)
print("Location:", artwork.location)


# In[ ]:




