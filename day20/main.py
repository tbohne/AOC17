import sys

def extract_particles(input):

    particles = []

    for particle in input:
        p = particle.strip().split(" ")
        pos = p[0].split("<")[1].split(">")[0].split(",")
        vel = p[1].split("<")[1].split(">")[0].split(",")
        acc = p[2].split("<")[1].split(">")[0].split(",")
        particles.append((pos, vel, acc))

    return particles

if __name__ == '__main__':

    input = sys.stdin.readlines()
    particles = extract_particles(input)
    min_dist = sys.maxsize
    min_part = sys.maxsize
    collisions = []

    # particle := (position, velocity, acceleration)
    # using 1000 ticks
    for _ in range(0, 1000):

        curr_positions = []
        tick_collisions = []

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

            curr_pos = [x[0] for x in curr_positions]

            if particles[i][0] in curr_pos and i not in collisions:
                tick_collisions.append(i)

                for pos, idx in curr_positions:
                    if pos == particles[i][0]:
                        if idx not in tick_collisions and particles[i][0] not in collisions:
                            tick_collisions.append(idx)
            else:
                curr_positions.append((particles[i][0], i))

        collisions += tick_collisions

    for i in range(0, len(particles)):
        dist = abs(
            int(particles[i][0][0])) + abs(int(particles[i][0][1])) + abs(int(particles[i][0][2])
        )

        if dist < min_dist:
            min_dist = dist
            min_part = i

    print("solution part1: {}".format(min_part))
    print("solution part2: {}".format(len(particles) - len(collisions)))
