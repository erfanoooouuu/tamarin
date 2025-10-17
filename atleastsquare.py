main_points = [(1, 6), (2, 4), (4, 3), (6, 2), (8, 3.2), (9, 5), (10, 7.5)]
prediceted_points = [(1, 1), (2, 1.5), (4, 2.5), (6, 3.5), (8, 4.5), (9, 5), (10, 6)]

def alsq(mmain,prd_point):
    minimoum_least_square_fault = 0

    for i in mmain:
        j = prd_point[mmain.index(i)]
        z = (i[1]-j[1])**2
        minimoum_least_square_fault += z
    return minimoum_least_square_fault

print(alsq(main_points, prediceted_points))