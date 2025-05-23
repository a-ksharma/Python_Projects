#Compund Interest Formula : A=P(1+(r/n))^nt

# A	=	final amount
# P	=	initial principal balance
# r	=	interest rate
# n	=	number of times interest applied per time period
# t	=	number of time periods elapsed


def CI(P,r,t,n=1):
    if not P:
        raise ValueError("Enter the Principle Amount!")
    if not r:
        raise ValueError("Enter the Interest Rate!")
    if not t:
        raise ValueError("Enter the number of time periods elapsed!")
    else:
        
        A = P * ((1+(r/n)) ** (n*t))
        print(f"The Compund Interest for the Principle Amount {P} is {A-P:.2f}")
        print(f"The Final Amount is {A:.2f}")


P = input("Enter the Principle Amount: ")
r = input("Enter the Interest Rate(in %): ")
t = input("Enter the number of time periods elapsed(in Yrs): ")
n = input("Enter the number of times interest applied per time period: ")
P=float(P)
r=float(r)/100
n=float(n)
t=float(t)

if __name__=='__main__':
    while True:
        if P>=0 and r>=0 and t>=0:
            CI(P,r,t,n)
            break
        else:
            break