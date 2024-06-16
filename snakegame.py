import pygame
from snake import Snake
def main():
    print("In Main")
    pygame.init()
    clock = pygame.time.Clock()
    # Create the main screen
    screen = pygame.display.set_mode((256, 256))
    #Sets the background color
    screen.fill((0, 0, 255))
    direction = "RIGHT"
    snakepos = [64,64]
    
    input =""
    # Draws the base snakes body
    pygame.draw.rect(screen, (0, 255, 0), (snakepos[0], snakepos[1], 16, 16))
    #title the window
    pygame.display.set_caption("Snake Game by Taza")
    running = True
    while running:
        clock.tick(8)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                input = player_input(event)
        snakepos = player_movment(screen, input, snakepos)
                

        
        pygame.display.update()
    
def player_input(event):
    if event.key == pygame.K_LEFT:
        print("Left")
        return "LEFT"
    if event.key == pygame.K_RIGHT:
        print("Right")
        return "RIGHT"
    if event.key == pygame.K_UP:
        print("Up")
        return "UP"
    if event.key == pygame.K_DOWN:
        print("Down")
        return"DOWN"
def player_movment(screen, direction, snakepos):
    if direction == "RIGHT":
            screen.fill((0, 0, 255))
            snakepos[0] += 16
            pygame.draw.rect(screen, (0, 255, 0), (snakepos[0], snakepos[1], 16, 16))
            
    if direction == "LEFT":
            screen.fill((0, 0, 255))
            snakepos[0] -= 16
            pygame.draw.rect(screen, (0, 255, 0), (snakepos[0], snakepos[1], 16, 16))
            
    if direction == "UP":
            screen.fill((0, 0, 255))
            snakepos[1] -= 16
            pygame.draw.rect(screen, (0, 255, 0), (snakepos[0], snakepos[1], 16, 16))
            
    if direction == "DOWN":
            screen.fill((0, 0, 255))
            snakepos[1] += 16
            pygame.draw.rect(screen, (0, 255, 0), (snakepos[0], snakepos[1], 16, 16))
    return snakepos        

if __name__ == "__main__":
    main()
    