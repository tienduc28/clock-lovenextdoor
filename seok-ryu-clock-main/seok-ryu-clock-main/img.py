import pygame

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Image Example')

# Load image
image = pygame.image.load('moonandcloud.png')

# Check if the image loaded correctly
if image:
    print("Image loaded successfully!")

# Set new dimensions for the image (e.g., reduce to 100x100 pixels)
new_width = 100
new_height = 100
scaled_image = pygame.transform.scale(image, (new_width, new_height))

# Define position for the scaled image
image_position = (100, 100)  # You can change the position as needed

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Blit the scaled image to the screen
    screen.blit(scaled_image, image_position)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
