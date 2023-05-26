import pygame


class KeyInterface:
    def __init__(self, coord=(0, 0)):
        self.x, self.y = coord
        self.click = False
        self.start_pos = (0, 0)
        self.old_delta_x = 0
        self.old_delta_y = 0
        self.delta_x = 0
        self.delta_y = 0

    def set_xy(self, coord):
        self.x, self.y = coord

    def get_xy(self):
        return self.x, self.y

    @staticmethod
    def change_scale_scroll():
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    print("forward")
                elif event.button == 5:
                    print("backward")

    def moving_keys(self, speed=10):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.x -= speed
        elif keys[pygame.K_LEFT]:
            self.x += speed

        if keys[pygame.K_UP]:
            self.y += speed
        elif keys[pygame.K_DOWN]:
            self.y -= speed

        if keys[pygame.K_F1]:
            self.x, self.y = 0, 0
            self.delta_y = 0
            self.delta_x = 0
            self.old_delta_y = 0
            self.old_delta_x = 0

    def moving_mouse(self):
        pressed = pygame.mouse.get_pressed()

        if pressed[0] and not self.click:
            self.click = True
            self.start_pos = pygame.mouse.get_pos()
        elif self.click:
            pos = pygame.mouse.get_pos()
            self.delta_x = -1*(self.start_pos[0] - pos[0]) + self.old_delta_x
            self.delta_y = -1*(self.start_pos[1] - pos[1]) + self.old_delta_y
            self.x = self.delta_x
            self.y = self.delta_y
        if not pressed[0]:
            self.click = False
            self.old_delta_x = self.delta_x
            self.old_delta_y = self.delta_y
