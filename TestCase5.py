#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PurchaseTicket import PurchaseTicket  
from Visitor import Visitor  
from datetime import datetime

# Test case for purchasing ticket online
print("Test Case: Purchase Ticket Online")
visitor = Visitor(visitorId=1, visitorName="Amnah", visitorAge=20, visitorCatagory="Student")
purchase_date_online = datetime.now()
ticket_online = PurchaseTicket(ticketId=1, event_type=None, price=None, dateOfPurchase=None, visitor=None)
ticket_online.purchase_ticket_online(event_type="Special Event", price=100, dateOfPurchase=purchase_date_online, visitor=visitor)
print(f"Ticket ID: {ticket_online.getTicketId()}")
print(f"Event Type: {ticket_online.getEvent_type()}")
print(f"Price: {ticket_online.getPrice()}")
print(f"Date of Purchase: {ticket_online.getDateOfPurchase()}")
print(f"Visitor Name: {ticket_online.visitor.getVisitorName()}")
print(f"Visitor Age: {ticket_online.visitor.getVisitorAge()}")
print(f"Visitor Category: {ticket_online.visitor.getVisitorCatagory()}")

# Test case for purchasing ticket offline
print("\nTest Case: Purchase Ticket Offline")
visitor = Visitor(visitorId=2, visitorName="Mariam", visitorAge=25, visitorCatagory="Adult")
purchase_date_offline = datetime.now()
ticket_offline = PurchaseTicket(ticketId=2, event_type=None, price=None, dateOfPurchase=None, visitor=None)
ticket_offline.purchase_ticket_offline(event_type="Guided Tour", price=50, dateOfPurchase=purchase_date_offline, visitor=visitor)
print(f"Ticket ID: {ticket_offline.getTicketId()}")
print(f"Event Type: {ticket_offline.getEvent_type()}")
print(f"Price: {ticket_offline.getPrice()}")
print(f"Date of Purchase: {ticket_offline.getDateOfPurchase()}")
print(f"Visitor Name: {ticket_offline.visitor.getVisitorName()}")
print(f"Visitor Age: {ticket_offline.visitor.getVisitorAge()}")
print(f"Visitor Category: {ticket_offline.visitor.getVisitorCatagory()}")


# In[ ]:




