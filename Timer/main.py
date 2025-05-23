import time

def timer(n):
    if not n:
        return ValueError("Enter the time to start the timer!")
    print(f"The timer for {n} seconds starts now!")
    for i in range(n,0,-1):
        sec= i%60
        min=int(i/60)%60
        hr= int(i/3600)
        print(f"{hr:2}:{min:2}:{sec:2}")
        time.sleep(1)
    print("Time's Up!")


def get_val():
    hr=int(input("Enter the value for Hours: "))
    min=int(input("Enter the value for Minutes: "))
    sec=int(input("Enter the value for Seconds: "))
    val=hr*60*60 + min*60 + sec
    print(f"You entered the time to be {val} seconds.")
    timer(val)


if __name__=='__main__':
    get_val()