import numpy as np
import matplotlib.pyplot as plt

# умова варіанту №27
x1_coef, x2_coef = 4,8

minimize = True
left_side_coefs = np.array([[2,1],
                            [1,3],
                            [3,2]])
right_side_coefs = np.array([8,9,13])
signs =[">=", ">=", ">="]



# знаходжу точки де перетинаються лінії за допомогою linalg.solve вирішення системи лінійних рівнянь
line_intersections = []
for line_a_ind in range(len(left_side_coefs)):
    for line_b_ind in range(line_a_ind+1, len(left_side_coefs)):
        system_of_two_lines_l_side = np.vstack((left_side_coefs[line_a_ind,:], left_side_coefs[line_b_ind,:]))
        system_of_two_lines_r_side = np.array([right_side_coefs[line_a_ind], right_side_coefs[line_b_ind]])

        point = np.linalg.solve(system_of_two_lines_l_side, system_of_two_lines_r_side)

        line_intersections.append(point)

        print(f"Лінії перетинаються у точці: {point}")
    


# знаходжу перетини з вісями
x_intersections = []
y_intersections = []
for line_ind in range(len(left_side_coefs)):
    x1_c = left_side_coefs[line_ind, 0]
    x2_c = left_side_coefs[line_ind, 1]
    b = right_side_coefs[line_ind]
    x_intersection = (b/x1_c,0)
    y_intersection = (0,b/x2_c)
    x_intersections.append(x_intersection)
    y_intersections.append(y_intersection)

    print(f"Перетин з віссю x: {x_intersection}")
    print(f"Перетин з віссю y: {y_intersection}")


# перевірка чи підходить точка під обмеження
def point_in_domain(point):
    x, y = point[0], point[1]
    for i, sign in enumerate(signs):
        if sign == ">=":
            if x*left_side_coefs[i, 0] + y*left_side_coefs[i,1] >= right_side_coefs[i]:
                pass
            else:
                return False
        else:
            if x * left_side_coefs[i, 0] + y * left_side_coefs[i, 1] <= right_side_coefs[i]:
                pass
            else:
                return False
    if x < 0 or y < 0:
        return False

    return True


#відсіюю точки які не підходять під обмеження
potential_points_of_the_polygon_shape = x_intersections + y_intersections + line_intersections + [(0,0)]
points_of_polygon_shape = []
for point in potential_points_of_the_polygon_shape:
    if point_in_domain(point):
        points_of_polygon_shape.append(point)

def get_F_value(point):
    x1 = point[0]
    x2 = point[1]
    return x1_coef*x1 + x2_coef*x2

values_in_points = []
for point in points_of_polygon_shape:
    values_in_points.append(get_F_value(point))

if minimize:
    index_of_answer = values_in_points.index(min(values_in_points))
    print(f"Найменше значення = {values_in_points[index_of_answer]}, яке досягається в точці {points_of_polygon_shape[index_of_answer]}")
else:
    index_of_answer = values_in_points.index(max(values_in_points))
    print(f"Найбільше значення = {values_in_points[index_of_answer]}, яке досягається в точці {points_of_polygon_shape[index_of_answer]}")



def plot_line(a,b,c):
    point1 = (0, c/b)
    point2 = (c/a,0)
    xs = [point1[0], point2[0]]
    ys = [point1[1], point2[1]]
    plt.plot(xs, ys)

for i in range(len(left_side_coefs)):
    plot_line(*left_side_coefs[i,:], right_side_coefs[i])

plt.plot(points_of_polygon_shape[index_of_answer][0],points_of_polygon_shape[index_of_answer][1], marker='o', markersize = 12)
plt.show()