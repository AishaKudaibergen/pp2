import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Paint")
    clock = pygame.time.Clock()  #для контроля частоты кадров(FPS)

    radius = 5
    mode = 'brush'
    draw_color = (0, 0, 255)

    rect_start = None
    circle_start = None
    prev_pos = None

    while True:
        pressed = pygame.key.get_pressed()

        #Проверка, удерживаются ли клавиши
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():  #Обработка событий
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or (event.key == pygame.K_w and ctrl_held) or (event.key == pygame.K_F4 and alt_held):
                    return

                #Выбор цвета
                if event.key == pygame.K_r:
                    draw_color = (255, 0, 0)  # Красный
                elif event.key == pygame.K_g:
                    draw_color = (0, 255, 0)  # Зелёный
                elif event.key == pygame.K_b:
                    draw_color = (0, 0, 255)  # Синий
                elif event.key == pygame.K_y:
                    draw_color = (255, 255, 0)  # Жёлтый
                elif event.key == pygame.K_w:
                    draw_color = (255, 255, 255)  # Белый

                #Инструменты
                elif event.key == pygame.K_1:#кисть
                    mode = 'brush'
                elif event.key == pygame.K_2:#прямоугольник
                    mode = 'rect'
                elif event.key == pygame.K_3:# круг
                    mode = 'circle'
                elif event.key == pygame.K_4: #ластик
                    mode = 'eraser'
                elif event.key == pygame.K_5:  #очищаем холст полностью
                    screen.fill((0, 0, 0))
                    pygame.display.flip()  

            #Обработка нажатия мышки
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mode == 'rect':
                    rect_start = event.pos    #zапоминаем начальную позицию
                elif mode == 'circle':
                    circle_start = event.pos
            

            if event.type == pygame.MOUSEBUTTONUP:
                if mode == 'rect' and rect_start: # начальная(x1, y1)
                    end_pos = event.pos #конечная -(x2, y2)
                    width = end_pos[0] - rect_start[0]
                    height = end_pos[1] - rect_start[1]
                    pygame.draw.rect(screen, draw_color, (rect_start[0], rect_start[1], width, height), 5)
                    rect_start = None

                elif mode == 'circle' and circle_start:
                    end_pos = event.pos

                    # (√(Δx² + Δy²) формула расстояния между 2 точками
                    radius_circle = int(((end_pos[0] - circle_start[0]) ** 2 + (end_pos[1] - circle_start[1]) ** 2) ** 0.5)
                    pygame.draw.circle(screen, draw_color, circle_start, radius_circle, 2)
                    circle_start = None
 
            #для сглаживания
            if event.type == pygame.MOUSEMOTION:
                if event.buttons[0]:
                    pos = event.pos
                    if mode == 'brush':
                        if prev_pos:
                            pygame.draw.line(screen, draw_color, prev_pos, pos, radius * 2)
                        prev_pos = pos
                    elif mode == 'eraser':
                        if prev_pos:
                            pygame.draw.line(screen, (0, 0, 0), prev_pos, pos, (radius + 5) * 2) #Рисуем ластик
                        prev_pos = pos
                else:
                    prev_pos = None  #cброс, если мышка не нажата

        pygame.display.flip()
        clock.tick(60) #60 кадров в сек

main()