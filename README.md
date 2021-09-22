# USRC Python Open CV Tutorial 
This series of workshops should help you familiarise yourself with the basics of using OpenCV in the Python environment. Try your best to follow along and ask questions from the execs whenever you get lost. 

OpenCV is a toolkit for processing computer imagery. This tutorial covers some common jobs you can do using openCV. But first, a bit of context. OpenCV is NOT machine learning; instead, it is a series of algorithms made by humans that do certain tasks. They are not perfect, and you, as another human, have to make the most of them. Additionally, since OpenCV is a toolkit, it is not applicable in every scenario. 

What does this repository help you do? It assumes you have a windows/linux/macbook and know nothing except how to click stuff and type stuff. It will help you understand how to solve certain problems. Let's get started!

# Credit 
The content in this tutorial series is credited to Jason Dsouza for the original tutorial from freeCodeCamp.org
- Youtube: https://www.youtube.com/jasmcaus
- Medium: https://jasmcaus.medium.com
- Twitter: https://twitter.com/jasmcaus
- LinkedIn: https://www.linkedin.com/in/jasmcaus

The images in the Photos and Videos folders were downloaded from Unsplash and Pixabay, unless otherwise mentioned.

The images in the Faces folder were procurred from a repo on Kaggle.

## Additional Links:
- Original Github link: https://github.com/jasmcaus/opencv-co...
- 🔗The Caer Vision library: https://github.com/jasmcaus/caer
- FreeCodeCamp:https://www.freecodecamp.org/


## Installing OpenCV
1. Install python. If you need step by step instructions doing this, check out our python tutorial: https://github.com/usydroboticsclub/python
2. Learn python. If you need step by step instructions doing this, check out our python tutorial: https://github.com/usydroboticsclub/python; and our other python tutorial: https://github.com/usydroboticsclub/py_harder
3. Open a command shell. All platforms have a command shell. If you're on windows, click the start menu and type CMD, then press enter. If you're on mac, go to launcher and type in Terminal. If you're on linux, press your equivalent of a start button and type in terminal.
4. Type in `pip3 install opencv-python` and press enter. You many have to wait a bit. 
5. Hooray! You now have opencv on your computer.
6. While you're at it, as install numpy and caer using `pip3 install numpy` and `pip3 install caer`. They will be useful to us in the future

Download this repository by clicking the big green 'Code' button towards the top of the page, followed by 'Download Zip'. In each of the python files are instructions and explainations for each of the lessons. Also in the folder is some suplementary material that will be usefull for the challenges!

## Lesson 1
In lesson 1, we'll be going over how to include OpenCV in your Python projects and some of the basics functions you can use with it.


## Lesson 1 - Challenge
Be able to open and read both an image and a video of your choosing (can be taken off the Internet)

## Lesson 1.1 - Challenge
Take an image of your choice (could be from the Internet or your own) and perform the following operations in separate instances (so don't do everything at once to the poor image).

- Rescale it to be half the original size
- Draw a shape (circle, line or rectangle) at the center of the image
- Pass it through a greyscale, blur and then canny layer
- Rotate it by 45 degrees

## Lesson 2 -Challenge
Choose an option:
- Challenge: Instead of filtering for the heart, instead filter for a pentagon, look in the file folder!
- Challenge: Draw the grid lines of the sudoku image by detecting the lines using a Hough transform. Use image sudoku.png from the Github.
- Challenge: Determine the road lane lines from a given image an drawing line onto them.  Use the provided image lane_img.jpg from the Github as your testing image. 
## Lesson 3 - Challenge
- Consider `Faces/usrc_all.png` and `Faces/usrc_cropped.png`. Using the face detection in part 1, tune the face detection so that all the faces in the cropped version are accounted for and there are no extra faces in the uncropped version. (Except for the clock. Apparently the clock looks like a face.)
- For each detected face (including the clock, I guess) use the imageFrame in `Faces/imageframe.png` to enframe the face, putting the resultant images into an output folder.


## Lesson 4 - Challenge
- Easy: Take a screenshot of yourself holding up 3 fingers in the hand tracking.
- Medium: Develop a module that shows the pose points for a person on screen but ignores the points on their head.
- Hard: Create a paint program that allows you to draw on screen based on how many fingers you're holding up.