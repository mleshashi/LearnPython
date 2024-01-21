import colorgram

rgb_colors = []

# Using double backslashes
path = "D:\\GitHub\\LearnPython\\12. Hirst_Painting\\"
colors = colorgram.extract(path + "image.jpg", 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
