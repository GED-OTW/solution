import pygame as pg


# A clickable button whose label can change colour when the pointer hovers over it.
class Button():
    def __init__(self, image, pos, text_input, font, base_colour, hovering_colour):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_colour, self.hovering_colour = base_colour, hovering_colour
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_colour)
        # Use the rendered label as the button surface when no image is provided.
        if self.image == None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))


    def update(self, screen):
        # Draw the button surface first so the label appears on top of it.
        if self.image != None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def check_for_input(self, position):
        # The button is interactive only when the pointer is inside its rectangle.
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def change_colour(self, position):
        # Re-render the label using the hover or default colour based on pointer position.
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_colour)
        else:
            self.text = self.font.render(self.text_input, True, self.base_colour)