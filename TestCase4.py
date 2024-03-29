#!/usr/bin/env python
# coding: utf-8

# In[10]:


from PurchaseTicket import PurchaseTicket
from Tour import Tours  # Importing the Tours class assuming it contains the required information
from datetime import datetime

# Create a Tours object
tour = Tours(date=datetime.now(), groupcount=20, guideName="Abdullah")

# Create a PurchaseTicket object for a tour
ticket = PurchaseTicket(
    ticketId=1,
    event_type="Tour",
    price=63,  # Assuming the ticket price is 63 AED
    dateOfPurchase=datetime.now(),
    visitor=None,  # Assuming visitor information is not required for this test case
)

# Apply 50% discount for groups
group_discount = 0.5
ticket_price = ticket.getPrice()
if ticket.getEvent_type() == "Tour":
    ticket_price *= group_discount

# Calculate the final price including VAT
final_price = ticket.calculate_final_price()

# Print all details
print("Ticket ID:", ticket.getTicketId())
print("Event Type:", ticket.getEvent_type())
print("Price before discount:", ticket.getPrice())
print("Price after discount:", ticket_price)  # Print price after applying discount
print("Group Count:", tour.getGroupcount())  # Print group count using instance method
print("Guide Name:", tour.getGuideName())  # Print guide name using instance method
print("Final Price with VAT:", final_price)
print("Date of Purchase:", ticket.getDateOfPurchase())


# In[ ]:




