import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Paint")
    clock = pygame.time.Clock()

    radius = 5
    mode = 'brush'
    draw_color = (0, 0, 255)

    rect_start = None
    circle_start = None
    prev_pos = None
    
    #новые переменные
    square_start = None
    right_triangle_start = None
    equilateral_triangle_start = None
    rhombus_start = None

    while True:
        pressed = pygame.key.get_pressed()

        # Проверка, удерживаются ли клавиши
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or (event.key == pygame.K_w and ctrl_held) or (event.key == pygame.K_F4 and alt_held):
                    return

                # Выбор цвета
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
                #1
                elif event.key == pygame.K_1:  # кисть
                    mode = 'brush'
                elif event.key == pygame.K_2:  # прямоугольник
                    mode = 'rect'
                elif event.key == pygame.K_3:  # круг
                    mode = 'circle'
                elif event.key == pygame.K_4:  # ластик
                    mode = 'eraser'
                elif event.key == pygame.K_5:  # очищаем холст полностью
                    screen.fill((0, 0, 0))
                    pygame.display.flip()

                #2   
                elif event.key == pygame.K_6:  # квадрат
                    mode = 'square'
                elif event.key == pygame.K_7:  # прямоугольный треугольник
                    mode = 'right_triangle'
                elif event.key == pygame.K_8:  # равносторонний треугольник
                    mode = 'equilateral_triangle'
                elif event.key == pygame.K_9:  # ромб
                    mode = 'rhombus'

            # Обработка нажатия мышки
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mode == 'rect':
                    rect_start = event.pos  # запоминаем начальную позицию
                elif mode == 'circle':
                    circle_start = event.pos

                #Начальные позиции новых форм
                elif mode == 'square':
                    square_start = event.pos
                elif mode == 'right_triangle':
                    right_triangle_start = event.pos
                elif mode == 'equilateral_triangle':
                    equilateral_triangle_start = event.pos
                elif mode == 'rhombus':
                    rhombus_start = event.pos

            if event.type == pygame.MOUSEBUTTONUP:
                if mode == 'rect' and rect_start:  # начальная -(x1, y1)
                    end_pos = event.pos  # конечная -(x2, y2)
                    width = end_pos[0] - rect_start[0]
                    height = end_pos[1] - rect_start[1]
                    pygame.draw.rect(screen, draw_color, (rect_start[0], rect_start[1], width, height), 5)
                    rect_start = None

                elif mode == 'circle' and circle_start:
                    end_pos = event.pos
                    radius_circle = int(((end_pos[0] - circle_start[0]) ** 2 + (end_pos[1] - circle_start[1]) ** 2) ** 0.5)
                    pygame.draw.circle(screen, draw_color, circle_start, radius_circle, 2)
                    circle_start = None


                elif mode == 'square' and square_start:
                    end_pos = event.pos
                    #Рассчитываем длину стороны как макс из ширины и высоты
                    side = max(abs(end_pos[0] - square_start[0]), abs(end_pos[1] - square_start[1]))
                    width = side if end_pos[0] > square_start[0] else -side
                    height = side if end_pos[1] > square_start[1] else -side
                    pygame.draw.rect(screen, draw_color, (square_start[0], square_start[1], width, height), 5)
                    square_start = None
                
                elif mode == 'right_triangle' and right_triangle_start:
                    end_pos = event.pos
                    #точки прямоугольного треугольника
                    points = [
                        right_triangle_start,
                        (right_triangle_start[0], end_pos[1]),  #Точка прямого угла
                        end_pos
                    ]
                    #Функция рисует треугольник, используя точки
                    pygame.draw.polygon(screen, draw_color, points, 5)
                    right_triangle_start = None
                
                elif mode == 'equilateral_triangle' and equilateral_triangle_start:
                    end_pos = event.pos
                    #сторона
                    side_length = math.sqrt((end_pos[0] - equilateral_triangle_start[0])**2 + (end_pos[1] - equilateral_triangle_start[1])**2)
                    #высота по формуле  (√3/2 * side)
                    height = (math.sqrt(3)/2) * side_length
                    #точки равностороннего треугольника
                    points = [
                            equilateral_triangle_start,
                            (equilateral_triangle_start[0] + side_length, equilateral_triangle_start[1]),
                            (equilateral_triangle_start[0] + side_length/2, equilateral_triangle_start[1] - height)
                    ]
                    pygame.draw.polygon(screen, draw_color, points, 5)
                    equilateral_triangle_start = None
                
                elif mode == 'rhombus' and rhombus_start:
                    end_pos = event.pos
                    #центральные точки
                    center_x = (rhombus_start[0] + end_pos[0]) / 2
                    center_y = (rhombus_start[1] + end_pos[1]) / 2
                    # горизонтальное и вертикальное расстояния
                    dx = end_pos[0] - rhombus_start[0]
                    dy = end_pos[1] - rhombus_start[1]
                    # Точки ромба: верхняя, правая, нижняя, левая
                    points = [
                        (center_x, rhombus_start[1]),
                        (end_pos[0], center_y),
                        (center_x, end_pos[1]),
                        (rhombus_start[0], center_y)
                    ]
                    pygame.draw.polygon(screen, draw_color, points, 5)
                    rhombus_start = None

            # для сглаживания
            if event.type == pygame.MOUSEMOTION:
                if event.buttons[0]:
                    pos = event.pos
                    if mode == 'brush':
                        if prev_pos:
                            pygame.draw.line(screen, draw_color, prev_pos, pos, radius * 2)
                        prev_pos = pos
                    elif mode == 'eraser':
                        if prev_pos:
                            pygame.draw.line(screen, (0, 0, 0), prev_pos, pos, (radius + 5) * 2)  # Рисуем ластик
                        prev_pos = pos
                else:
                    prev_pos = None  # сброс, если мышка не нажата

        pygame.display.flip()
        clock.tick(60)  # 60 кадров в сек

main()