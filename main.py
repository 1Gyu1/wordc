from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt #to display our wordcloud
from PIL import Image #to load our image
import numpy as np #to get the color of our image

#Content-related
text = open('test.txt', 'r').read()
stopwords = set(STOPWORDS)

#Appearance-related
custom_mask = np.array(Image.open('cloud.png'))
wc = WordCloud(background_color = 'white',
               stopwords = stopwords,
               mask = custom_mask,
               contour_width = 3,
               contour_color = 'black',
               font_path='nanum.ttf')

wc.generate(text)
image_colors = ImageColorGenerator(custom_mask)
wc.recolor(color_func = image_colors)

#Plotting
##plt.imshow(wc, interpolation = 'bilinear')
##plt.axis('off')
##plt.show()

wc.to_file('Batman_wordcloud.png')
