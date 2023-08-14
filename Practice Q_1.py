""" In a grocery shop, different varieties of biscuits are sold. The name of the biscuit,
stock(number of packets) in hand and price (per packet, in Rupees) are stored in the
system. Given a list of biscuits ordered by a customer, write an algorithm and the
subsequent Python code to find the total cost to be paid by the customer and update the
stock of biscuits available in the shop. If the order placed for a particular variety of
biscuit is greater than the stock in hand of that biscuit in the grocery shop then that
order is not accepted. The details of the biscuits available should be given as input and
the cost of biscuits will be given as integers. For example, if the grocery shop has five
varieties of biscuits and details are shown in the table below:"""

name = []
stock = []
price = []
n = int(input("Enter number of variety of biscuits: "))
print("\n")
for i in range(n):
    name.append(input("Enter name of Brand "+str(i+1)+" : "))
for i in range(n):
    stock.append(int(input("Enter number of Stock "+str(i+1)+" : ")))
for i in range(n):
    price.append(int(input("Enter price of Brand "+str(i+1)+" : ")))

a = []
sum = 0
for i in range(n):
    a.append(int(input("Enter quantity of biscuits for "+str(name[i])+" : ")))
    if(a[i]<=stock[i]):
        sum = sum + a[i]*price[i]
        stock[i] = stock[i]-a[i]
    else:
        a[i]=0
print("\n")
for i in range(n):
    print("Revised Stock for "+str(name[i])+" : "+str(stock[i]))
print("\n")
print("The total to be paid = "+str(sum))
