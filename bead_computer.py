file = open("Bead trajectory.txt", "r")

AMOUNT_TO_COMPUTE = 10
"""
HELPER FUNCTIONS
"""


def multiply(array, val):
    for i in range(len(array)):
        array[i] *= val
    return array

def subtract(array, val):
    for i in range(len(array)):
        array[i] -= val
    return array
"""
times is the times array
N is the len(times)
position is i

lag time = 1/(N-i) * summation from 1 to N-i of 
"""
def lag_time(times, index):
    lag = 0
    lag_times = []
    denom = float(len(times)-index)
    for n in range(len(times)-index):
        lag += (times[n+index]-times[n])/denom
    return lag

def mean(positions):
    mean = 0
    denom = len(positions)
    for n in range(len(positions)):
        mean += positions[n]/denom
    return mean

def variance(positions, mean_value):
    var = 0
    denom = len(positions)
    for n in range(len(positions)):
        var += ((positions[n] - mean_value)**2)/denom
    return var
    
def mean_squared_disp(positions, variance, index):
    mean_squared = 0
    denom = 2*(len(positions)-index)*variance
    for n in range(len(positions)-index):
        mean_squared += ((positions[n+index]-positions[n])**2)/denom
    return mean_squared

def autocorrelation(positions, variance, index):
    auto = 0
    denom = (len(positions)-index)*variance
    for n in range(len(positions)-index):
        auto += (positions[n+index]*positions[n])/denom
    return auto
"""
START

"""
# create 2 arrays for the time and positions
time = []
position = []

# read the first line
line = file.readline()
# so long as its valid
while line and len(time) < AMOUNT_TO_COMPUTE:
    # split by a space
    splt = line.split()
    # if the split length isn't two, skip
    if len(splt) < 2:
        line = file.readline()
        continue
    # load into array
    time.append(float(splt[0]))
    position.append(float(splt[1]))
    # read next line
    line = file.readline()

print("File Loaded!")


# input the date of birth and reemove the / and spaces
dob = input("Please enter your date of birth, format DD/MM/YYYY: ").strip().replace("/","").replace(" ", "")

dob_integer = -1
try:
    # convert to integer and add decimal at correct location
    dob_integer = int(dob)*(10**-7)
except exception as e:
    print("invalid date of birth input")
    quit()
    
# 1
multiplied_dob = position
multiply(multiplied_dob, dob_integer)

# 2
lag_times = []
for i in range(AMOUNT_TO_COMPUTE):
    print("Lag Times %", 100*float(i+1)/AMOUNT_TO_COMPUTE)
    lag_times.append(lag_time(time, i))
    
    
mean_pos = mean(position)

# 3
subtracted_mean_pos = position
subtract(subtracted_mean_pos, mean_pos)

# 4     of new second column
variance_pos = variance(subtracted_mean_pos, mean_pos)

mean_sqared_disp_pos = []
for i in range(AMOUNT_TO_COMPUTE):
    print("mean squared %:", 100*float(i+1)/AMOUNT_TO_COMPUTE)
    mean_sqared_disp_pos.append(mean_squared_disp(subtracted_mean_pos, variance_pos, i))

auto_corr_pos = []
for i in range(AMOUNT_TO_COMPUTE):
    print("auto corr %:", 100*float(i+1)/AMOUNT_TO_COMPUTE)
    auto_corr_pos.append(autocorrelation(subtracted_mean_pos, variance_pos, i))
    

print("\n\nCalculations Done! Saving to calculated_functions.csv\n\n")
file = open("calculated_functions.csv", "w+")
file.write("Time,Position,Lag Time,Mean Subtracted Position,Mean squared Displacement,Autocorrelation\n")

for i in range(AMOUNT_TO_COMPUTE):
    file.write(str(time[i]) + "," + str(position[i])+"," +str(lag_times[i])+","+str(subtracted_mean_pos[i])+","+str(mean_sqared_disp_pos[i])+","+str(auto_corr_pos[i]) + "\n")

