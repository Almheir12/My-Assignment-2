#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# class tour has been created 
class Tours:
    def __init__(self, date, groupcount, guideName):
     # attributes has been initialized here
        self.date = date
        self.groupcount = groupcount
        self.guideName = guideName

# fuction has been created to get date
    def getDate(self):
        return self.date
# fuction has been created to get groupcount
    def getGroupcount(self):
        return self.groupcount
# fuction has been created to get guide name
    def getGuideName(self):
        return self.guideName

# fuction has been created to set date
    def setDate(self, date):
        self.date = date
# fuction has been created to set groupcount
    def setGroupcount(self, groupcount):
        self.groupcount = groupcount
# fuction has been created to get guide name
    def setGuideName(self, guideName):
        self.guideName = guideName

