import os
import moviepy.video.io.ImageSequenceClip

videocase = "2D"

images_forward = []
images_backward = []
for root, dirs, paths in os.walk(f'.\\!images{videocase}'):
    for path in paths:
        if path[-4:] == ".png":
            number = path[:-4]
            if number[0] =='B':
                images_backward.append(float(number[1:]))
            else:
                images_forward.append(float(number))

images_backward.sort(reverse=True)
images_forward.sort()

order = []

for image in images_forward:
    image = str(image)
    if image[-2:] == ".0":
        image = image[:-2]
    order.append(f".\\!images{videocase}\\" + image + ".png")

for image in images_backward:
    image = str(image)
    if image[-2:] == ".0":
        image = image[:-2]
    order.append(f".\\!images{videocase}\\" + "B" + image + ".png")

print(order)

clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(order, fps=5)
clip.write_videofile(f'!{videocase}.mp4')
