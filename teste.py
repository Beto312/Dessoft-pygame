import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fireboy and Watergirl")

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LAVA = (255, 100, 0)
WATER = (0, 100, 255)
PLATFORM_COLOR = (100, 100, 100)
FINISH_COLOR = (0, 255, 0)
CRYSTAL_COLOR = (255, 255, 0)

# Character settings
fireboy_pos = pygame.Rect(100, HEIGHT - 60, 40, 40)
watergirl_pos = pygame.Rect(200, HEIGHT - 60, 40, 40)
SPEED = 5
GRAVITY = 1
JUMP_STRENGTH = 15

# Platform, obstacle, and finish settings
ground = pygame.Rect(0, HEIGHT - 40, WIDTH, 40)  # Ground platform at the bottom of the screen
platforms = [
    pygame.Rect(50, HEIGHT - 150, 200, 20),
    pygame.Rect(300, HEIGHT - 300, 200, 20),
    pygame.Rect(550, HEIGHT - 450, 200, 20)
]
lava = pygame.Rect(50, HEIGHT - 100, WIDTH // 2, 20)
water = pygame.Rect(WIDTH // 2, HEIGHT - 100, WIDTH // 2, 20)
finish_area = pygame.Rect(WIDTH - 100, HEIGHT - 60, 80, 40)

# Collectibles (crystals)
fireboy_crystals = [pygame.Rect(200, HEIGHT - 200, 20, 20), pygame.Rect(600, HEIGHT - 500, 20, 20)]
watergirl_crystals = [pygame.Rect(300, HEIGHT - 200, 20, 20), pygame.Rect(400, HEIGHT - 500, 20, 20)]

# Player states
fireboy_velocity_y = 0
watergirl_velocity_y = 0
fireboy_on_ground = False
watergirl_on_ground = False
fireboy_collected_crystals = 0
watergirl_collected_crystals = 0

# Game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Fireboy controls
    if keys[pygame.K_LEFT]:
        fireboy_pos.x -= SPEED
    if keys[pygame.K_RIGHT]:
        fireboy_pos.x += SPEED
    if keys[pygame.K_UP] and fireboy_on_ground:
        fireboy_velocity_y = -JUMP_STRENGTH
        fireboy_on_ground = False

    # Watergirl controls
    if keys[pygame.K_a]:
        watergirl_pos.x -= SPEED
    if keys[pygame.K_d]:
        watergirl_pos.x += SPEED
    if keys[pygame.K_w] and watergirl_on_ground:
        watergirl_velocity_y = -JUMP_STRENGTH
        watergirl_on_ground = False

    # Apply gravity
    fireboy_velocity_y += GRAVITY
    fireboy_pos.y += fireboy_velocity_y
    watergirl_velocity_y += GRAVITY
    watergirl_pos.y += watergirl_velocity_y

    # Check for collisions with platforms and ground
    fireboy_on_ground = False
    watergirl_on_ground = False

    # Ground collision
    if fireboy_pos.colliderect(ground):
        fireboy_pos.bottom = ground.top
        fireboy_velocity_y = 0
        fireboy_on_ground = True
    if watergirl_pos.colliderect(ground):
        watergirl_pos.bottom = ground.top
        watergirl_velocity_y = 0
        watergirl_on_ground = True

    # Platform collisions
    for platform in platforms:
        # Fireboy platform collision
        if fireboy_pos.colliderect(platform) and fireboy_velocity_y > 0:
            fireboy_pos.bottom = platform.top
            fireboy_velocity_y = 0
            fireboy_on_ground = True
        # Watergirl platform collision
        if watergirl_pos.colliderect(platform) and watergirl_velocity_y > 0:
            watergirl_pos.bottom = platform.top
            watergirl_velocity_y = 0
            watergirl_on_ground = True

    # Check for collisions with lava and water
    if fireboy_pos.colliderect(water):
        print("Game Over! Fireboy cannot touch water!")
        running = False
    if watergirl_pos.colliderect(lava):
        print("Game Over! Watergirl cannot touch lava!")
        running = False

    # Check for collectible crystals
    for crystal in fireboy_crystals[:]:
        if fireboy_pos.colliderect(crystal):
            fireboy_crystals.remove(crystal)
            fireboy_collected_crystals += 1
    for crystal in watergirl_crystals[:]:
        if watergirl_pos.colliderect(crystal):
            watergirl_crystals.remove(crystal)
            watergirl_collected_crystals += 1

    # Check if both players reached the finish line and collected all crystals
    if (fireboy_pos.colliderect(finish_area) and watergirl_pos.colliderect(finish_area) and
            fireboy_collected_crystals == len(fireboy_crystals) + 2 and
            watergirl_collected_crystals == len(watergirl_crystals) + 2):
        print("Level Complete!")
        running = False

    # Draw ground, platforms, lava, water, and finish area
    pygame.draw.rect(screen, PLATFORM_COLOR, ground)
    for platform in platforms:
        pygame.draw.rect(screen, PLATFORM_COLOR, platform)

    pygame.draw.rect(screen, LAVA, lava)
    pygame.draw.rect(screen, WATER, water)
    pygame.draw.rect(screen, FINISH_COLOR, finish_area)

    # Draw collectibles (crystals)
    for crystal in fireboy_crystals:
        pygame.draw.rect(screen, CRYSTAL_COLOR, crystal)
    for crystal in watergirl_crystals:
        pygame.draw.rect(screen, CRYSTAL_COLOR, crystal)

    # Draw characters
    pygame.draw.rect(screen, RED, fireboy_pos)  # Fireboy
    pygame.draw.rect(screen, BLUE, watergirl_pos)  # Watergirl

    pygame.display.flip()
    pygame.time.Clock().tick(30)  # 30 FPS

pygame.quit()
