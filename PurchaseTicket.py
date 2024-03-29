#!/usr/bin/env python
# coding: utf-8

# In[3]:


#purchaseticket class has been created
class PurchaseTicket:
    def __init__(self, ticketId, event_type, price, dateOfPurchase, visitor):
      # attributes has been initialized here
        self.ticketId = ticketId
        self.event_type = event_type
        self.price = price
        self.dateOfPurchase = dateOfPurchase
        self.visitor = visitor

  # fuction has been created to get ticket id
    def getTicketId(self):
        return self.ticketId

    # fuction has been created to get event type
    def getEvent_type(self):
        return self.event_type

    # fuction has been created to get price
    def getPrice(self):
        return self.price

    # fuction has been created to get date of purchase
    def getDateOfPurchase(self):
        return self.dateOfPurchase

  # fuction has been created to set ticket id
    def setTicketId(self, ticketId):
        self.ticketId = ticketId

    # fuction has been created to set event type
    def setEvent_type(self, event_type):
        self.event_type = event_type

 # fuction has been created to set price
    def setPrice(self, price):
        self.price = price

        # fuction has been created to get date of purchase
    def setDateOfPurchase(self, dateOfPurchase):
        self.dateOfPurchase = dateOfPurchase

    # function has been created to calculate final price with VAT
    def calculate_final_price(self):
        # Assuming VAT is 5%
        vat_rate = 0.05
        final_price = self.price * (1 + vat_rate)
        return final_price
    
     # function to purchase ticket online
    def purchase_ticket_online(self, event_type, price, dateOfPurchase, visitor):
        self.event_type = event_type
        self.price = price
        self.dateOfPurchase = dateOfPurchase
        self.visitor = visitor
        print("Ticket purchased online.")

    # function to purchase ticket offline
    def purchase_ticket_offline(self, event_type, price, dateOfPurchase, visitor):
        self.event_type = event_type
        self.price = price
        self.dateOfPurchase = dateOfPurchase
        self.visitor = visitor
        print("Ticket purchased offline.")


# In[ ]:





# In[ ]:




