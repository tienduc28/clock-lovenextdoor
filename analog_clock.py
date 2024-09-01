import pygame
from math import pi, cos, sin
import datetime
from pygame import gfxdraw

WIDTH, HEIGHT = 1920, 1080
center = (WIDTH / 2, HEIGHT / 2)
clock_radius = 400

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Analog Clock")
clock = pygame.time.Clock()
FPS = 60

CLOCK = (33, 35, 37)
BACKGROUND = (217, 215, 211)
RED = (255, 0, 0)
YELLOW = (196, 166, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# fonts = pygame.font.get_fonts()
# print(fonts)

def numbers(number, size, position):
    font = pygame.font.Font("Dubai-Regular.ttf", size)
    text = font.render(number, True, CLOCK)
    text_rect = text.get_rect(center=(position))
    screen.blit(text, text_rect)

def write_text(text, size, position, font_file, text_rotate_degrees=0, align="center"):
    font = pygame.font.Font(font_file, size)
    text_surface = font.render(text, True, CLOCK)
    
    if text_rotate_degrees != 0:
        text_surface = pygame.transform.rotate(text_surface, text_rotate_degrees)
    
    text_rect = text_surface.get_rect()

    if align == "right":
        text_rect.topright = position
    elif align == "left":
        text_rect.topleft = position
    else:
        text_rect.center = position
    screen.blit(text_surface, text_rect)
def polar_to_cartesian(r, theta):
    x = r * sin(pi * theta / 180)
    y = r * cos(pi * theta / 180)
    return x + WIDTH / 2, -(y - HEIGHT / 2)


def main():
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        current_time = datetime.datetime.now()
        second = current_time.second
        minute = current_time.minute
        hour = current_time.hour

        day = current_time.day
        month = current_time.month
        year = current_time.year
        weekday = current_time.today().isoweekday()
        calendar = current_time.today().isocalendar()

        weekdays_abbr = {1: "Mo", 2: "Tu", 3: "We", 4: "Th", 5: "Fr", 6: "Sa", 7: "Su"}
        weekday_abbr = weekdays_abbr.get(weekday)

        months_abbr = {1: "JAN", 2: "FEB", 3: "MAR", 4: "APR", 5: "MAY", 6: "JUN", 7: "JUL",
                       8: "AUG", 9: "SEP", 10: "OCT", 11: "NOV", 12: "DEC"}
        month_abbr = months_abbr.get(month)

        if day < 10:
            day = "0" + str(day)

        screen.fill(BACKGROUND)

        #CIRCLES
        
        pygame.draw.circle(screen, CLOCK, center, clock_radius - 10, 5)

        outer_radius = clock_radius - 2
        pygame.draw.circle(screen, CLOCK, center, outer_radius, 2)
        gfxdraw.aacircle(screen, int(center[0]), int(center[1]), outer_radius + 1, CLOCK)
        gfxdraw.aacircle(screen, int(center[0]), int(center[1]), outer_radius, CLOCK)
        gfxdraw.aacircle(screen, int(center[0]), int(center[1]), outer_radius - 1, CLOCK)
        # pygame.draw.rect(screen, WHITE, [WIDTH / 2 - 260, HEIGHT / 2 - 30, 80, 60], 1)
        # pygame.draw.rect(screen, WHITE, [WIDTH / 2 - 180, HEIGHT / 2 - 30, 80, 60], 1)
        # pygame.draw.rect(screen, WHITE, [WIDTH / 2 + 100, HEIGHT / 2 - 30, 80, 60], 1)
        # pygame.draw.rect(screen, WHITE, [WIDTH / 2 + 180, HEIGHT / 2 - 30, 80, 60], 1)
        # pygame.draw.rect(screen, WHITE, [WIDTH / 2 - 50, HEIGHT / 2 - 30 + 160, 100, 60], 1)

        # numbers(str(weekday_abbr), 40, (WIDTH / 2 - 220, HEIGHT / 2))
        # numbers(str(calendar[1]), 40, (WIDTH / 2 - 140, HEIGHT / 2))
        # numbers(str(month_abbr), 40, (WIDTH / 2 + 140, HEIGHT / 2))
        # numbers(str(day), 40, (WIDTH / 2 + 220, HEIGHT / 2))
        # numbers(str(year), 40, (WIDTH / 2, HEIGHT / 2 + 160))

        for number in range(1, 25):
            numbers(str(number), 40, polar_to_cartesian(clock_radius + 30, number * 15))

        for number in range(0, 360, 15):
            width = 3
            if (number % 90 == 0):
                width = 6
            pygame.draw.line(screen, CLOCK, polar_to_cartesian(clock_radius + 8, number), polar_to_cartesian(clock_radius - 22, number), width)

        # draw dividing lines
        rb = 15
        thetas = [5*rb, 6*rb, 9*rb, 12*rb-6, 12*rb+6, 15*rb, 19*rb, 20*rb, 21*rb, 22*rb]
        for theta in thetas:
            pygame.draw.line(screen, CLOCK, polar_to_cartesian(clock_radius - 30, theta), polar_to_cartesian(clock_radius - 335, theta), 2)

        write_text("Ngủ", 50, (WIDTH / 2 + 100, HEIGHT / 2 - 150), "Dubai-Regular.ttf")
        write_text("Dậy", 40, (WIDTH / 2 + 350, HEIGHT / 2 - 60), "Dubai-Regular.ttf", 8, 'right')
        write_text("Ăn sáng", 40, (WIDTH / 2 + 330, HEIGHT / 2 + 60), "Dubai-Regular.ttf", 360 - 22, 'right')
        write_text("Chơi game", 40, (WIDTH / 2 + 160, HEIGHT / 2 + 155), "Dubai-Regular.ttf", 360 - 45, 'right')
        write_text("Ăn trưa", 40, (WIDTH / 2 + 22, HEIGHT / 2 + 225), "Dubai-Regular.ttf", 360 - 90, 'right')
        write_text("Xem TV", 40, (WIDTH / 2 - 165, HEIGHT / 2 + 133), "Dubai-Regular.ttf", 65, 'left')
        write_text("Hẹn hò", 40, (WIDTH / 2 - 330, HEIGHT / 2 + 75), "Dubai-Regular.ttf", 20, 'left')
        write_text("Code", 40, (WIDTH / 2 - 340, HEIGHT / 2 - 100), "Dubai-Regular.ttf", 360 - 15, 'left')
        write_text("Xem phim", 40, (WIDTH / 2 - 295, HEIGHT / 2 - 225), "Dubai-Regular.ttf", 360 - 35, 'left')
        write_text("Skin care", 40, (WIDTH / 2 - 235, HEIGHT / 2 - 280), "Dubai-Regular.ttf", 360 - 50, 'left')
        # Hour
        r = 130
        theta = (hour + minute / 60 + second / 3600) * (360 / 12)
        pygame.draw.line(screen, CLOCK, center, polar_to_cartesian(r, theta), 14)

        # Minute
        r = 280
        theta = (minute + second / 60) * (360 / 60)
        pygame.draw.line(screen, CLOCK, center, polar_to_cartesian(r, theta), 10)

        # Second
        r = 340
        theta = second * (360 / 60)
        pygame.draw.line(screen, RED, center, polar_to_cartesian(r, theta), 4)
        pygame.draw.line(screen, RED, center, polar_to_cartesian(r, theta), 4)

        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()


main()