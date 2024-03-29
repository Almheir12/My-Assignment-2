#!/usr/bin/env python
# coding: utf-8

# In[9]:


from Catalog import Catalog
from Exhibition import Exhibition  # Assuming you have an Exhibition class defined

# Create a Catalog object
catalog = Catalog()

# Create instances of Exhibition
exhibition1 = Exhibition(id=1, title="From Kalila wa Dimna to La Fontaine Travelling through Fables", startDate="2024-03-26", endDate="2024-07-21", location="Outdoor Spaces")
exhibition2 = Exhibition(id=2, title="Transparencies", startDate="2023-11-24", endDate="2024-03-31", location="Permanent Galleries")

# Add exhibitions to the catalog
catalog.addExhibition(exhibition1)
catalog.addExhibition(exhibition2)

# Test removal of an exhibition
catalog.removeExhibition(exhibition1)

# Verify if the removed exhibition is no longer in the catalog
print("Catalog Exhibitions after removal:")
for exhibition in catalog.exhibitions:
    print("Exhibitions List:", "Exhibition Title:", exhibition.title,"Exhibition Location:", exhibition.location)


# In[ ]:




