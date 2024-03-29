#!/usr/bin/env python
# coding: utf-8

# In[1]:


# here i have imported catalog class
from Catalog import Catalog
# class Exhibition has been created here
class Exhibition(Catalog):
     # constructor has been created to intialize parameters
    def __init__(self, id, title, startDate, endDate, location):
        # Call parent constructor
        super().__init__()
        
        # attributes has been initialized here
        self.id = id
        self.title = title
        self.startDate = startDate
        self.endDate = endDate
        self.location = location

    # function has been created to get exhibition id
    def getId(self):
        return self.id

# function has been created to get exhibition title
    def getTitle(self):
        return self.title

# function has been created to get exhibition start date
    def getStartDate(self):
        return self.startDate

# function has been created to get exhibition end date
    def getEndDate(self):
        return self.endDate

# function has been created to get exhibition location
    def getLocation(self):
        return self.location

# function has been created to set exhibition id
    def setId(self, id):
        self.id = id

# function has been created to set exhibition title
    def setTitle(self, title):
        self.title = title


# function has been created to set exhibition start date
    def setStartDate(self, startDate):
        self.startDate = startDate
        
# function has been created to set exhibition end date

    def setEndDate(self, endDate):
        self.endDate = endDate

# function has been created to set exhibition location
    def setLocation(self, location):
        self.location = location


# In[ ]:




