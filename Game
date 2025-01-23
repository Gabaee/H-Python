import pygame

# Initialize pygame
pygame.init()

# Set the window size
window_size = (400, 400)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title
pygame.display.set_caption("Ping Pong")

# Set the font
font = pygame.font.Font(None, 36)

# Set the ball properties
ball_radius = 20
ball_color = (255, 255, 255)
ball_position = [200, 200]
ball_velocity = [2, 2]

# Set the paddle properties
paddle_width = 15
paddle_height = 100
paddle_color = (255, 255, 255)
left_paddle_position = [25, 150]
right_paddle_position = [375, 150]

# Set the score properties
left_score = 0
right_score = 0

# Set the game properties
game_over = False

# Main game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Update the ball position
    ball_position[0] += ball_velocity[0]
    ball_position[1] += ball_velocity[1]

    # Check for ball collision with the top and bottom of the window
    if ball_position[1] > window_size[1] - ball_radius or ball_position[1] < ball_radius:
        ball_velocity[1] = -ball_velocity[1]

    # Check for ball collision with the left paddle
    if ball_position[0] < paddle_width + ball_radius:
        if (
            ball_position[1] < left_paddle_position[1] + paddle_height / 2
            and ball_position[1] > left_paddle_position[1] - paddle_height / 2
        ):
            ball_velocity[0] = -ball_velocity[0]
        else:
            right_score += 1
            ball_position = [200, 200]
            ball_velocity = [2, 2]

    # Check for ball collision with the right paddle
    if ball_position[0] > window_size[0] - paddle_width - ball_radius:
        if (
            ball_position[1] < right_paddle_position[1] + paddle_height / 2
            and ball_position[1] > right_paddle_position[1] - paddle_height / 2
        ):
            ball_velocity[0] = -ball_velocity[0]
        else:
            left_score += 1
            ball_position = [200, 200]
            ball_velocity = [2, 2]

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the ball
    pygame.draw.circle(screen, ball_color, ball_position, ball_radius)

    # Draw the left paddle
    pygame.draw.rect()
