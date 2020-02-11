"""."""
from skimage import io
from skimage.color import rgb2gray

number = 'uno'
for i in range(1, 6):
    image = io.imread('{a}s/{a}{b}.jpg'.format(a=number, b=i,))
    gray = rgb2gray(image)
    [rows, columns] = gray.shape

    for row in range(rows):
        for column in range(columns):
            if gray[row, column] > 100:
                gray[row, column] = 255
            else:
                gray[row, column] = 0

    M00 = 0
    M10 = 0
    M01 = 0

    for row in range(1, rows + 1):
        M10_add = 0
        for column in range(1, columns + 1):
            if gray[row - 1, column - 1] != 0:
                M00 += 1
                M10_add += 1
                M01 += column
        M10_add *= row
        M10 += M10_add

    centroid_x = M10 / M00
    centroid_y = M01 / M00

    is_js = [
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 0),
        (1, 1),
        (1, 2),
        (1, 3),
        (2, 0),
        (2, 1),
        (2, 2),
        (2, 3),
        (3, 0),
        (3, 1),
        (3, 2),
        (3, 3),
    ]

    central_moments = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    counter = 0
    for i in range(4):
        for j in range(4):
            for row in range(1, rows + 1):
                for column in range(1, columns + 1):
                    if gray[row - 1, column - 1] != 0:
                        central_moments[counter] += (
                            ((row - centroid_x)**i) * ((column - centroid_y)**j)
                        )
            counter += 1

    normalized_central_moments = []
    for i_j, central_moment in zip(is_js, central_moments):
        nij = central_moment / (central_moments[0]**((i_j[0] + i_j[1]) / 2) + 1)
        normalized_central_moments.append(nij)

    n02 = normalized_central_moments[2]
    n03 = normalized_central_moments[3]
    n11 = normalized_central_moments[5]
    n12 = normalized_central_moments[6]
    n20 = normalized_central_moments[8]
    n21 = normalized_central_moments[9]
    n30 = normalized_central_moments[12]

    h0 = n20 - n02
    h1 = (n20 - n02)**2 + 4 * (n11**2)
    h2 = (n30 - (3 * n12))**2 + ((3 * n21) - n03)**2
    h3 = (n30 + n12)**2 + (n21 + n03)**2
    h4 = ((n30 - (3 * n12)) * (n30 + n12) * ((n30 + n12)**2 - (3 * (n21 + n03))**2)) + ((3 * (n30 + n12)) * ((3 * (n30 + n12)**2) - (n21 + n03)**2))
    h5 = (n20 - n02) * ((n30 + n12)**2 - (n21 + n03)**2 + (4 * n11 * ((n30 + n12) * (n21 + n03))))
    h6 = (((3 * n21) - n03) * (n30 + n12) * ((n30 + n12)**2 - 3*((n21 + n03)**2))) + ((n30 - 3*n12)*(n21 + n03)*((3*((n30 + n12)**2)) - (n21 + n03)**2))

    print([h0, h1, h2, h3, h4, h5, h6])
