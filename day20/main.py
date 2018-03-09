import sys

def extract_particles(buff):

    particles = []

    for particle in buff:
        p = particle.strip().split(" ")
        pos = p[0].split("<")[1].split(">")[0].split(",")
        vel = p[1].split("<")[1].split(">")[0].split(",")
        acc = p[2].split("<")[1].split(">")[0].split(",")
        particles.append((pos, vel, acc))

    return particles

if __name__ == '__main__':

    buff = sys.stdin.readlines()
    particles = extract_particles(buff)

    min_dist = sys.maxsize
    min_part = sys.maxsize

    # particle := (position, velocity, acceleration)
    # using 1000 ticks
    for _ in range(0, 1000):

        for i in range(0, len(particles)):

            # Increase the X velocity by the X acceleration.
            particles[i][1][0] = int(particles[i][1][0]) + int(particles[i][2][0])
            # Increase the Y velocity by the Y acceleration.
            particles[i][1][1] = int(particles[i][1][1]) + int(particles[i][2][1])
            # Increase the Z velocity by the Z acceleration.
            particles[i][1][2] = int(particles[i][1][2]) + int(particles[i][2][2])
            # Increase the X position by the X velocity.
            particles[i][0][0] = int(particles[i][0][0]) + int(particles[i][1][0])
            # Increase the Y position by the Y velocity.
            particles[i][0][1] = int(particles[i][0][1]) + int(particles[i][1][1])
            # Increase the Z position by the Z velocity.
            particles[i][0][2] = int(particles[i][0][2]) + int(particles[i][1][2])

    for i in range(0, len(particles)):
        dist = abs(int(particles[i][0][0])) + abs(int(particles[i][0][1])) + abs(int(particles[i][0][2]))

        if dist < min_dist:
            min_dist = dist
            min_part = i

    print("solution part1: particle {} with a distance of {}.".format(min_part, min_dist))
