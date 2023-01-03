import pygame

def main():
    print("In Main")
    pygame.init()
    clock = pygame.time.Clock()
    # Create the main screen
    screen = pygame.display.set_mode((320, 320))
    #Sets the background color
    screen.fill((0, 0, 255))
    direction = "RIGHT"
    xsnakepos = 100
    ysnakepos = 100
    # Draws the base snakes body
    pygame.draw.rect(screen, (0, 255, 0), (xsnakepos, ysnakepos, 15, 15))
    #title the window
    pygame.display.set_caption("Snake Game by Taza")
    running = True
    while running:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("Left")
                    direction = "LEFT"
                if event.key == pygame.K_RIGHT:
                    print("Right")
                    direction = "RIGHT"
                if event.key == pygame.K_UP:
                    print("Up")
                    direction = "UP"
                if event.key == pygame.K_DOWN:
                    print("Down")
                    direction = "DOWN"
        if direction == "RIGHT":
            screen.fill((0, 0, 255))
            xsnakepos += 15
            pygame.draw.rect(screen, (0, 255, 0), (xsnakepos, ysnakepos, 15, 15))
            if xsnakepos > 320:
                print("Game Over")
        if direction == "LEFT":
            screen.fill((0, 0, 255))
            xsnakepos -= 15
            pygame.draw.rect(screen, (0, 255, 0), (xsnakepos, ysnakepos, 15, 15))
            if xsnakepos < 0:
                print("Game Over")
        if direction == "UP":
            screen.fill((0, 0, 255))
            ysnakepos -= 15
            pygame.draw.rect(screen, (0, 255, 0), (xsnakepos, ysnakepos, 15, 15))
            if ysnakepos < 0:
                print("Game Over")
        if direction == "DOWN":
            screen.fill((0, 0, 255))
            ysnakepos += 15
            pygame.draw.rect(screen, (0, 255, 0), (xsnakepos, ysnakepos, 15, 15))
            if ysnakepos > 320:
                print("Game Over")

        
        pygame.display.update()
    

if __name__ == "__main__":
    main()
    