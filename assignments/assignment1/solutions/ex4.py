from random import random

#Generate point (x, y)
#If point in hitzone increment n_hits
#Increment n_tot
#Circle inscribed within 1x1 square with top-right corner (1,1)
#Satisfies (x-0.5)^2 + (y-0.5)^2 = 0.25
#For points (x, y) within circle (x-0.5)^2 + (y-0.5)^2 < 0.25

def estimate_pi(precision):
    n_hits = 0
    n_tot = 0

    for i in range(100000000):
        x = random()
        y = random()
        if ((x-0.5)**2 + (y-0.5)**2) < 0.25:
            n_hits += 1
        n_tot += 1
    #pi/4 is approximately n_hits/n_tot
    pi_approx = n_hits / n_tot * 4
    return round(pi_approx, precision)

print(estimate_pi(4))