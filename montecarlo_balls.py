def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    import random
    # red ball = true, green ball = false
    same_color = []
    for _ in range(numTrials):
        balls = [True, True, True, False, False, False]
        balls_picked = []
        for _ in range(3):
            ball = random.choice(balls)
            balls.remove(ball)
            balls_picked.append(ball)
        if True not in balls_picked or False not in balls_picked:
            same_color.append(True)
        else:
            same_color.append(False)
    return float(same_color.count(True))/len(same_color)


print(noReplacementSimulation(10000))