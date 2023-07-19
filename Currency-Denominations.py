Withdrawn_amt = int(input('Enter the Amount to be Withdrawn: '))

d500 = Withdrawn_amt//500
d_500 = Withdrawn_amt%500

d200 = d_500//200
d_200 = d_500%200

d100 = d_200//100
d_100 = d_200%100

d50 = d_100//50
d_50 = d_100%50

d20 = d_50//20
d_20 = d_50%20

d10 = d_20//10
d_10 = d_20%10

d5 = d_10//5
d_5 = d_10%5

d2 = d_5//2
d_2 = d_5%2

d1 = d_2//1
d_1 = d_2%1

total_denominations = d500+d200+d100+d50+d20+d10+d5+d2+d1

Pandiyarajan = print('The denominations are: ',total_denominations) 
