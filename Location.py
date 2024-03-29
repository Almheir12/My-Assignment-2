#!/usr/bin/env python
# coding: utf-8

# In[1]:


# class location has been created
class Location:
    def __init__(self, locationId, locationName):
        # attributes has been initialized here
        self.locationId = locationId
        self.locationName = locationName

    # function has been created to get location id
    def getLocationId(self):
        return self.locationId

     # function has been created to get location name
    def getLocationName(self):
        return self.locationName

# function has been created to set location id
    def setLocationId(self, locationId):
        self.locationId = locationId

   # function has been created to set location name
    def setLocationName(self, locationName):
        self.locationName = locationName


# In[ ]:




