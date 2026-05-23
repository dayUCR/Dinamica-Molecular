import numpy as np
import random

class Particle:
    radius = 0.1
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel

    def move(self, dt):
        self.pos += dt*self.vel

    def edgeColision(self):
        for i in range(2):
            if (self.pos[i] <= self.radius or self.pos[i] >= 1-self.radius):
                self.vel[i] *= -1

# https://en.wikipedia.org/wiki/Elastic_collision#Two-dimensional_collision_with_two_moving_objects
def colision(particle1, particle2):
    a = np.dot(particle1.vel-particle2.vel, particle1.pos-particle2.pos)
    b = np.dot(particle1.pos-particle2.pos, particle1.pos-particle2.pos)
    particle1.vel -= (particle1.pos-particle2.pos)*a/b
    particle2.vel -= (particle2.pos-particle1.pos)*a/b

tf = 20 # Tiempo de la simulación
dt = 0.1
t = 0
particles = [Particle(np.array([0.25,0.25]), np.array([random.random() for _ in range(2)])),
             Particle(np.array([0.75,0.75]), np.array([random.random() for _ in range(2)]))]

print(f"{t:.2f}: p1 = {particles[0].pos}; p2 = {particles[1].pos}")
while (t <= tf):
    t += dt
    for p in particles:
        p.move(dt)

    for i in range(len(particles)):
        for j in range(i+1, len(particles)):
            if (np.sqrt(np.dot(particles[i].pos-particles[j].pos,particles[i].pos-particles[j].pos)) <= 2*particles[i].radius):
                colision(particles[i],particles[j])

    for p in particles:
        p.edgeColision()

    print(f"{t:.2f}: p1 = {particles[0].pos}; p2 = {particles[1].pos}")
