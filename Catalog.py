#!/usr/bin/env python
# coding: utf-8

# In[1]:


#class catalog has been created here
class Catalog:
    def __init__(self):
        # emptylists has been intialized to store artworks and exhibitions
        self.artworks = []
        self.exhibitions = []

    # function has been made to add artwork to the catalog
    def addArtwork(self, artwork):
        # Append the artwork to the artworks list
        self.artworks.append(artwork)
        print("Artwork added to the catalog")

    # function has been made to remove artwork to the catalog
    def removeArtwork(self, artwork):
        # Check if the artwork exists in the catalog
        if artwork in self.artworks:
            # Remove the artwork from the artworks list
            self.artworks.remove(artwork)
            print("Artwork removed from the catalog")
        else:
            print("Artwork not found in the catalog")

    # function has been made to add exhibition to the catalog
    def addExhibition(self, exhibition):
        # Append the exhibition to the exhibitions list
        self.exhibitions.append(exhibition)
        print("Exhibition added to the catalog")

     # function has been made to remove exhibition to the catalog
    def removeExhibition(self, exhibition):
        # Check if the exhibition exists in the catalog
        if exhibition in self.exhibitions:
            # Remove the exhibition from the exhibitions list
            self.exhibitions.remove(exhibition)
            print("Exhibition removed from the catalog")
        else:
            print("Exhibition not found in the catalog")


# In[ ]:




