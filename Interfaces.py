import tkinter as tk
import speech_recognition as sr
from xArm6_Ufactory import UfactoryRobot
from Cocktails import MesCocktails

class Robot:
    def __init__(self):
        self.connected = False

    def connect(self):
        self.connected = True
        print("Robot connected")

    def disconnect(self):
        self.connected = False
        print("Robot disconnected")

    def ricard(self):
        if self.connected:
            print("ricard en préparation")
        else:
            print("Robot not connected")

    def ti_punch(self):
        if self.connected:
            print("ti_punch en préparation")
        else:
            print("Robot not connected")

    def reconnaissance_vocale(self):
        if self.connected:
            print("Reconnaissance vocale en cours")
        else:
            print("Robot not connected")

class RobotController:
    def __init__(self, robot, boisson,robotbarman):
        self.robot = robot
        self.boisson = boisson
        self.robotbarman = robotbarman

    def connect(self):
        self.robot.connect()

    def disconnect(self):
        self.robot.disconnect()

    def OpenGripper(self):
        self.robot.OpenGripper()

    def ricard(self):
        self.boisson.ricard()

    def ti_punch(self):
        self.boisson.ti_punch()

    def reconnaissance_vocale(self):
        self.robotbarman.reconnaissance_vocale()

class Interface:
    def __init__(self, controller):
        self.controller = controller

        self.window = tk.Tk()
        self.window.geometry("400x200")

        self.btn_connect = tk.Button(self.window, text="Connect", command=self.controller.connect)
        self.btn_connect.pack()

        self.btn_disconnect = tk.Button(self.window, text="Disconnect", command=self.controller.disconnect)
        self.btn_disconnect.pack()

        self.btn_OpenGripper = tk.Button(self.window, text="Gripper Open", command=self.controller.OpenGripper)
        self.btn_OpenGripper.pack()

        self.btn_ricard = tk.Button(self.window, text="Ricard", command=self.controller.ricard)
        self.btn_ricard.pack()

        self.btn_ti_punch = tk.Button(self.window, text="Ti_punch", command=self.controller.ti_punch)
        self.btn_ti_punch.pack()

        self.btn_reconnaisance_vocale = tk.Button(self.window, text="Reconnaissance vocale", command=self.controller.reconnaissance_vocale)
        self.btn_reconnaisance_vocale.pack()

        self.window.mainloop()


