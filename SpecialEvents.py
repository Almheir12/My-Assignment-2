#!/usr/bin/env python
# coding: utf-8

# In[1]:


# specialevents class has been created here
class SpecialEvents:
    def __init__(self, id, title, startDate, endDate, location):
        # attributes has been initialized here
        self.id = id
        self.title = title
        self.startDate = startDate
        self.endDate = endDate
        self.location = location

    # fuction has been created to get id
    def getId(self):
        return self.id

     # fuction has been created to get title
    def getTitle(self):
        return self.title

     # fuction has been created to get start date
    def getStartDate(self):
        return self.startDate

     # fuction has been created to get end date
    def getEndDate(self):
        return self.endDate

     # fuction has been created to get location
    def getLocation(self):
        return self.location

 # fuction has been created to set id
    def setId(self, id):
        self.id = id

     # fuction has been created to set title
    def setTitle(self, title):
        self.title = title

         # fuction has been created to set start date
    def setStartDate(self, startDate):
        self.startDate = startDate

         # fuction has been created to set end date
    def setEndDate(self, endDate):
        self.endDate = endDate

         # fuction has been created to set location
    def setLocation(self, location):
        self.location = location


# In[ ]:




