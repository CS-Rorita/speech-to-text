
# Program To Read video
# and Extract Frames
import cv2
import os
# Python code to convert video to audio
import moviepy.editor as mp
import speech_recognition as sr

# Function to extract frames
def FrameCapture(path):
    # =========================================================================================================
    # Path to audio file
    # Insert Local Video File Path
    clip = mp.VideoFileClip(path)

    # Insert Local Audio File Path
    sound = clip.audio.write_audiofile(r'./data/audio.wav')

    # ==================================================================================================
    # Path to video file
    vidcap = cv2.VideoCapture(path)
    try:
        if not os.path.exists('data'):
            os.makedirs('data')  # extract frames from this video. Following it, create a folder where you want to save the images
    except OSError:
        print('Error: Creating directory of data')

    def getFrame(sec):
        vidcap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
        hasFrames, image = vidcap.read()
        if hasFrames:
            # Saves image of the current frame in jpg file
            name = './data/frame' + str(count) + '.jpg'
            cv2.imwrite(name, image)  # save frame as JPG file

        return hasFrames

    sec = 0
    frameRate = 30  # //it will capture image in each 30 second
    count = 1
    success = getFrame(sec)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec)

#========================================================================

    r = sr.Recognizer()
    sound = sr.AudioFile("./stanford.wav")
    with sound as source:
        r.adjust_for_ambient_noise(source)


        print("Converting Audio To Text ..... ")


        audio = r.listen(source)

    type(audio)

    try:
        text=r.recognize_google(audio)
        print("Converted Audio Is : \n"+text)


    except Exception as e:
        print("Error can't recognize the voice {} : ".format(e))

# Driver Code
if __name__ == '__main__':
    # Calling the function
    FrameCapture('Java Programming Tutorial 1 - Introduction to Java.mp4')
