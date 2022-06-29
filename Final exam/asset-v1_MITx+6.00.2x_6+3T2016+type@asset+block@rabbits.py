import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    for _ in range(CURRENTRABBITPOP):
        popDensity = CURRENTRABBITPOP / MAXRABBITPOP
        if random.random() < 1 - popDensity:
            CURRENTRABBITPOP += 1


def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    for _ in range(CURRENTFOXPOP):
        hunting_success = CURRENTRABBITPOP / MAXRABBITPOP
        if CURRENTRABBITPOP > 10 and random.random() < hunting_success:
            CURRENTRABBITPOP -= 1
            if random.random() < 1.0/3:
                CURRENTFOXPOP += 1
        else:
            if random.random() < 0.9:
                CURRENTFOXPOP -= 1
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_population = []
    fox_population = []
    for _ in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_population.append(CURRENTRABBITPOP)
        fox_population.append(CURRENTFOXPOP)
    return rabbit_population, fox_population


def plot_populations():
    populations = runSimulation(200)
    pylab.plot(populations[0], "-r", label="rabbits")
    pylab.plot(populations[1], "-b", label="foxes")
    pylab.xlabel("timestep")
    pylab.ylabel("population size")
    pylab.title("fox and rabbit population simulation")
    pylab.legend()

    pylab.figure()
    rabbit_coeff = pylab.polyfit(range(len(populations[0])), populations[0], 2)
    pylab.plot(pylab.polyval(rabbit_coeff, range(len(populations[0]))), "-r", label="rabbits")
    fox_coeff = pylab.polyfit(range(len(populations[1])), populations[1], 2)
    pylab.plot(pylab.polyval(fox_coeff, range(len(populations[1]))), "-b", label="foxes")
    pylab.xlabel("timestep")
    pylab.ylabel("population size")
    pylab.title("fox and rabbit population polyfit")
    pylab.legend()
    pylab.show()


plot_populations()