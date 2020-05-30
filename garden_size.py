### parameters ###
## basic parameters ##

# define initial (square) garden size in metres
x_range = 1
y_range = 1

# define social distancing radius in metres
radius = 2

# set occupancy we are interested in
min_occ = 6

## expert parameters

# set garden size increment
inc = 0.1

# set initial number of simulations to run
simulations = (x_range * y_range) * 20

# set reject:accept ratio for terminate
ratio = 9999

### end of parameters ###

# import packages
import random as rand
import matplotlib.pyplot as plt
from datetime import datetime
import timeit

# start runtime timer
start = timeit.default_timer()

# define function for neighbour checking
def has_neighbour(coords, trial_coord, radius):
    for coord in coords:
        test = (coord[0]-trial_coord[0])**2 + (coord[1]-trial_coord[1])**2
        if test < radius**2:
            #print(str(trial_coord) + " " + str(test) + " Neighbour")
            return True
        #else:
            #print(str(trial_coord) + " " + str(test) + " No neighbour")
    return False

# define function for picking best solution
def best_occ(dict):
    # 1) create a list of the dict's keys and values;
    # 2) return the key with the max value
    v = list(dict.values())
    k = list(dict.keys())
    return k[v.index(max(v))]


### simulations start here ###
min_occ = 0

while min_occ < 6:
    sim_occs = {}
    sim_coords = {}

    print("----- Start of garden size " + str(round(x_range,1)) + "x" + str(round(y_range,1)) + " metres -----")

    # iterate over simulations:
    for sim in range(1, simulations+1):
        print("--- Start of simulation " + str(sim) + " ---")

        # initialise accepted and rejected counts
        accepted = 1
        rejected = 0
        # seed random number generator with current time
        rand.seed(datetime.now())

        # generate initial random coordinate
        coords = []
        coords.append(((rand.uniform(0,x_range)),(rand.uniform(0,y_range))))
        print("First coordinate = " + str(coords[0]))

        # iterate over number of trials
        while rejected/accepted < ratio:
            # generate new random coordinate...
            trial_coord = (rand.uniform(0,x_range)),(rand.uniform(0,y_range))
            # print("Trial coordinate = " + str(trial_coord))

            # ...and test if it has any neighbours
            if not has_neighbour(coords, trial_coord, radius):
                # if it doesn't, add it to the coordinate list
                #print("Trial accepted!")
                accepted += 1
                coords.append(trial_coord)
            else:
                rejected += 1
                #print("Trial rejected")
            #print("Accepted " + str(len(coords)) + " coordinates")

        print("Total accepted coordinates = " + str(len(coords)))
        print("--- End of simulaton " + str(sim) + " ---")
        print("\n")

        # store occupancy and coords for this sumulation
        sim_occs[sim] = len(coords)
        sim_coords[sim] = coords

    # pick the best solution
    best_sim = best_occ(sim_occs)
    best_coords = sim_coords[best_sim]

    print("The best occupancy for garden size = " + str(round(x_range,1)) + " is " + str(sim_occs[best_sim]) + ", occuring at simulation " + str(best_sim))

    # if best solution does not meet minimum occupancy threshold, increment garden size
    min_occ = sim_occs[best_sim]
    x_range += inc
    y_range += inc
    # we need to update simulation number based on garden size
    simulations = int((x_range * y_range) * 20)

    print("Increasing garden size to " + str(round(x_range,1)) + "x" + str(round(y_range,1)) + " metres")
    print("\n")
    print("----- End of garden size " + str(round(x_range,1)) + "x" + str(round(y_range,1)) + " metres -----")

# end runtime timer
stop = timeit.default_timer()

print("\n \n")
print("########## SOLUTION ##########")
print("The minimum garden size required for " + str(min_occ) + " is " + str(round(x_range,1)) + "x" + str(round(y_range,1)) + " metres")
print("This solution was obtained in " + str(round(stop-start, 2)) + " seconds")

print("\n")
print("Thank you for using garden_distancing!")

# unpack coords for plotting
x_coords = []
y_coords = []

for coord in best_coords:
    x_coords.append(coord[0])
    y_coords.append(coord[1])

plt.axis([0, x_range, 0, y_range])
plt.xlabel("metres")
plt.ylabel("metres")
plt.plot(x_coords,y_coords, 'o')
plt.show()
plt.savefig("garden_size.png")
