import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3
    balls of the same color were drawn in the first 3 draws.
    '''
    results = 0
    balls = [True, True, True, True, False, False, False, False]
    for _ in range(numTrials):
        ballsCopy = balls[:]
        draw = []
        for _ in range(3):
            ball = random.choice(ballsCopy)
            draw.append(ball)
            ballsCopy.remove(ball)

        if True not in draw or False not in draw:
            results += 1
    return results/numTrials

print(drawing_without_replacement_sim(100))
