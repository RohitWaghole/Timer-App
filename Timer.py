import time

def timer(t):

    while t:
        time.sleep(1)
        t -= 1
    for i in range(3):
        print("!!!! TIME UP !!!!")
        time.sleep(1)
    print()
    print("  READY TO ROCK  ")

def main():

    print("SET THE TIMER")
    h, m, s = map(int,input("Enter time in H:M:S : ").split())
    total_time = (h*60*60) + (m*60) + s
    print()
    timer(total_time)

if __name__ == "__main__":
    main()
