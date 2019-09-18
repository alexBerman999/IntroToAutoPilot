import pygame

from map import Map
from pathfind import pathfind

pygame.init()
screen = pygame.display.set_mode([600, 600])

map = Map(600, 600)
path = pathfind(map)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for obst in map.obstacles:
        pygame.draw.circle(screen, (255, 0, 0), (obst[0], obst[1]), obst[2], 2)

    for wp in map.waypoints:
        pygame.draw.circle(screen, (0, 255, 0), (wp[0], wp[1]), 5)

    for i in range(len(path) - 1):
        pygame.draw.line(screen, (0, 0, 255), path[i], path[i + 1])



    # Flip the display
    pygame.display.flip()

pygame.quit()
