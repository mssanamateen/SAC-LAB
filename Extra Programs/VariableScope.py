#ticket counter
total_tickets=0
def sell_ticket(counter_id,n):
    global total_tickets# to modify the global variable
    total_tickets+=n
    print(f"Counter {counter_id} sold {n} tickets")
sell_ticket(1,3)
sell_ticket(2,6)
print("Total tickets sold:",total_tickets)