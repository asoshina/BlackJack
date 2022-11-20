from const import *


def print_text(message, point, font_color='Black', font_type='./Other/OpenSans-Regular.ttf', font_size=20):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_size)
    display.blit(text, (point[0], point[1]))


def get_input():
    input_txt = ''
    input_rect = pygame.Rect(display_width // 2 - 30, display_height // 2 - 20, 70, 30)
    pygame.draw.rect(display, (255, 184, 0), input_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return input_txt.strip()
                elif event.key == pygame.K_BACKSPACE:
                    print(input_txt)
                    input_txt = input_txt[:-1:]
                    print(input_txt)
                else:
                    if len(input_txt) < 10:
                        input_txt += event.unicode
        pygame.draw.rect(display, (255, 184, 0), input_rect)
        print_text(message=input_txt, point=(input_rect.x+10, input_rect.y+5))
        pygame.display.update()
        clock.tick(60)


def clear(point, width, height):
    clear_rect = pygame.Rect(point[0], point[1], width, height)
    pygame.draw.rect(display, 'white', clear_rect)
    pygame.display.update()


def wait():
    flag = True
    while True and flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN :
                    flag = False
                    break
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            if event.type == pygame.MOUSEBUTTONUP:
                flag = False
                break
        pygame.display.update()
        clock.tick(60)

