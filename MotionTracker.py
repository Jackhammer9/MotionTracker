import tkinter
from utils import GetVideoCaptureSources
import cv2
from main import Launcher

class App():

    def __init__(self , WindowName , WindowSize):
        self.window = tkinter.Tk()
        self.window.title(WindowName)
        self.window.geometry(WindowSize)
        self.window.resizable(0,0)

    def labels(self):
        self.DeviceLabel = tkinter.Label(self.window , text = 'Select Camera: ' , fg='dark green')
        self.DeviceLabel.place(x=0 , y = 20)
        self.DeviceLabel.config(font=("Courier", 12))

        self.WindowLess = tkinter.Label(self.window , text = 'Windowless Detection: ' , fg='dark green')
        self.WindowLess.place(x=0 , y = 70)
        self.WindowLess.config(font=("Courier", 12))

        self.icon = tkinter.PhotoImage(file = 'icon.png')
        self.window.iconphoto(False , self.icon)

        self.sources = GetVideoCaptureSources()
        if len(self.sources) == 0:
            tkinter.Label(self.window , text = 'No Video Capture Devices Found \n Please Exit!' , fg="red" ).place(x=200 , y = 20)
            return
        self.Clicked = tkinter.StringVar()
        self.Clicked.set(self.sources[0])
        SourcesMenu = tkinter.OptionMenu(self.window , self.Clicked , *self.sources)
        SourcesMenu.place(x=200 , y = 15)

        self.WindowLessClicked = tkinter.IntVar()
        self.WindowLessClicked.set(0)
        WindowLessMenu = tkinter.Checkbutton(self.window , text = '' , variable = self.WindowLessClicked)
        WindowLessMenu.place(x=250 , y = 70)

        self.TestCam = tkinter.Button(self.window , text = 'Test Camera' , command = self.TestCam , bg='red' , fg='white' , borderwidth=0)
        self.TestCam.place(x=0 , y = 280 , width=175)

        self.Launcher = tkinter.Button(self.window , text = 'Launch Tracker' , command = self.Launch , bg='dark green' , fg='white' , borderwidth=0)
        self.Launcher.place(x=175 , y = 280 , width=175)

        self.Text= tkinter.Text(self.window , wrap="word" , font=("Courier", 12))
        self.Text.insert(tkinter.INSERT , '''Click on Test Camera Button to ensure camera is working, if satisfied with the results click 'q' key to stop testing then click on launch tracker button to begin''')
        self.Text.place(x=0 , y = 100 , width=350 , height=100)
        self.Text.config(state='disabled')

    def TestCam(self):
        self.cap = cv2.VideoCapture(self.sources.index(self.Clicked.get()))

        while (self.cap.isOpened()):
            _ , img = self.cap.read()
            img = cv2.flip(img , 1)
            cv2.imshow('Camera Testing' , img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def Launch(self):
        self.window.destroy()
        Launcher(self.sources.index(self.Clicked.get()) , self.WindowLessClicked.get())

if __name__ == '__main__':
    app = App('Motion Tracker' , '350x300')
    app.labels()
    app.window.mainloop()