import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import os

# 8 vertices for a cube, (x, ,y, z) co-ordinate
vertices = (
    (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1),
    (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1)
)
# each vertex contains 3 edges in a cube
edges = (
    (0, 1), (0, 3), (0, 4), (2, 1), (2, 3), (2, 7),
    (6, 3), (6, 4), (6, 7), (5, 1), (5, 4), (5, 7)
)
surfaces = (
    (0, 1, 2, 3), (3, 2, 7, 6), (6, 7, 5, 4), (4, 5, 1, 0),
    (1, 5, 7, 2), (4, 0, 3, 6)
)
colors = (
    (1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 0, 0), (1, 1, 1), (0, 1, 1),
    (1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 0, 0), (1, 1, 1), (0, 1, 1),
)


def set_vertices(max_distance, min_distance=-20, camera_x=0, camera_y=0):
    camera_x = -1*int(camera_x)
    camera_y = -1 * int(camera_y)
    x_value_change = random.randrange(camera_x - 75, camera_x + 75)
    y_value_change = random.randrange(camera_y - 75, camera_y + 75)
    z_value_change = random.randrange(-1*max_distance, min_distance)
    new_vertices = []
    for vert in vertices:
        # new_vert = []
        new_x = vert[0] + x_value_change
        new_y = vert[1] + y_value_change
        new_z = vert[2] + z_value_change
        new_vertices.append((new_x, new_y, new_z))
    return new_vertices


def Cube(vertices):
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(colors[x])  # greenv v
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    os.environ['SDL_VIDEO_CENTERED'] = "1"
    pygame.init()
    # pygame.display.set_caption("SCREEN SAVER")
    # display = (1800, 1080)
    info = pygame.display.Info()  # You have to call this before pygame.display.set_mode()
    screen_width, screen_height = info.current_w, info.current_h
    window_width, window_height = screen_width-10, screen_height-20
    pygame.display.set_mode((window_width, window_height), DOUBLEBUF | OPENGL)
    max_distance = 100
    gluPerspective(45, (window_width/window_height), 0.1, max_distance)
    glTranslatef(0, 0, -30)
    cur_x = 0
    cur_y = 0
    x_move = 0
    y_move = 0
    game_speed = 1
    direction_speed = 1
    cube_dict = {}
    for x in range(70):
        cube_dict[x] = set_vertices(max_distance)
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_move = direction_speed
                if event.key == pygame.K_RIGHT:
                    x_move = -direction_speed
                if event.key == pygame.K_UP:
                    y_move = direction_speed
                if event.key == pygame.K_DOWN:
                    y_move = -direction_speed
            if event.type == pygame.K_UP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_move = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_move = 0
        # glRotatef(75, 1, 1, 30)
        x = glGetDoublev(GL_MODELVIEW_MATRIX)
        camera_x = x[3][0]
        camera_y = x[3][1]
        camera_z = x[3][2]
        cur_x += x_move
        cur_y += y_move
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glTranslatef(x_move, y_move, game_speed)
        for each_cube in cube_dict:
            Cube(cube_dict[each_cube])
        for each_cube in cube_dict:
            if camera_z <= cube_dict[each_cube][0][2]:
                new_max = int(-1*(camera_z - (max_distance * 2)))
                cube_dict[each_cube] = set_vertices(new_max, int(camera_z), cur_x, cur_y)
        pygame.display.flip()


main()
