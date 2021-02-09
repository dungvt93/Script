import imageio
import os
images = []
root_dir = "C:/Users/tiend/Desktop/photoshop/gif/"
for filename in os.listdir(root_dir):
    images.append(imageio.imread(root_dir + filename))

kargs = { 'duration': 1 }
imageio.mimsave('C:/Users/tiend/Desktop/photoshop/movie.gif', images, ** kargs)