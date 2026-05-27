from particle import Particle
import numpy as np

def distance(particle1, particle2):
    '''Returns the distance between 2 particles

    Args:
        particle1: First particle
        particle1: Second particle
    '''
    return np.sqrt((particles[i].posX-particles[j].posX)**2
                  +(particles[i].posY-particles[j].posY)**2)

def colision(particle1, particle2):
    '''Modifies the velocity of 2 colliding particles

    The calculation is based on the equation found in:
    https://en.wikipedia.org/wiki/Elastic_collision#Two-dimensional_collision_with_two_moving_objects

    Args:
        particle1: First particle whose velocity to modify
        particle1: Second particle whose velocity to modify
    '''

    # Constants required for calculation
    a = (particle1.velX-particle2.velX)*(particle1.posX-particle2.posX) \
        + (particle1.velY-particle2.velY)*(particle1.posY-particle2.posY)
    b = (particle1.posX-particle2.posX)**2 + (particle1.posY-particle2.posY)**2

    particle1.velX -= (particle1.posX-particle2.posX)*a/b
    particle1.velY -= (particle1.posY-particle2.posY)*a/b
    particle2.velX -= (particle2.posX-particle1.posX)*a/b
    particle2.velY -= (particle2.posY-particle1.posY)*a/b


t = 0
tf = 20
dt = 0.1
particles = [Particle([0.25,0.25]), Particle([0.75,0.75])]

print(f"{t:.2f}:")
print(f"p1 = {particles[0].posX},{particles[0].posY}")
print(f"p2 = {particles[1].posX},{particles[1].posY}")

while (t <= tf):
    t += dt
    for p in particles:
        p.move(dt)

    # Runs over all pairs without duplicates
    for i in range(len(particles)):
        for j in range(i+1, len(particles)):
            if (distance(particles[i],particles[j]) <= 2*particles[i].radius):
                colision(particles[i],particles[j])

    for p in particles:
        p.edgeColision()

    print(f"{t:.2f}:")
    print(f"p1 = {particles[0].posX},{particles[0].posY}")
    print(f"p2 = {particles[1].posX},{particles[1].posY}")
