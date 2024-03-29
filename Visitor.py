#!/usr/bin/env python
# coding: utf-8

# In[1]:


# visitor class has been created here
class Visitor:
    def __init__(self, visitorId, visitorName, visitorAge, visitorCatagory):
        # attributes has been initialized here
        self.visitorId = visitorId
        self.visitorName = visitorName
        self.visitorAge = visitorAge
        self.visitorCatagory = visitorCatagory
        self.purchaseticket = None

     # fuction has been created to get visitor id
    def getVisitorId(self):
        return self.visitorId

     # fuction has been created to get visitor name
    def getVisitorName(self):
        return self.visitorName

     # fuction has been created to get visitor age
    def getVisitorAge(self):
        return self.visitorAge

     # fuction has been created to get visitor catagory
    def getVisitorCatagory(self):
        return self.visitorCatagory

# fuction has been created to set visitor id
    def setVisitorId(self, visitorId):
        self.visitorId = visitorId

        # fuction has been created to set visitor name
    def setVisitorName(self, visitorName):
        self.visitorName = visitorName

        # fuction has been created to set visitor age
    def setVisitorAge(self, visitorAge):
        self.visitorAge = visitorAge

        # fuction has been created to set visitor catagory
    def setVisitorCatagory(self, visitorCatagory):
        self.visitorCatagory = visitorCatagory

  # fuction has been created to purchase ticket online
    def purchase_ticket_online(self, event_type):
          # Creating a new PurchaseTicket object
        self.purchaseticket = PurchaseTicket(ticketId=None, event_type=event_type, price=None, dateOfPurchase=None, visitor=self)
        print("Ticket purchased online")

   # fuction has been created to purchase ticket offline (in person)
    def purchase_ticket_offline(self, event_type):
        # Creating a new PurchaseTicket object
        self.purchaseticket = PurchaseTicket(ticketId=None, event_type=event_type, price=None, dateOfPurchase=None, visitor=self)
        print("Ticket purchased offline")


# In[ ]:




