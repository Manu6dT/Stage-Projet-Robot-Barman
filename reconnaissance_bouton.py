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

    def move_forward(self):
        if self.connected:
            print("Moving forward")
        else:
            print("Robot not connected")
    
    def EnregistrePosition(self):
        if self.connected:
            print("Position enregistrée")
        else:
            print("Robot not connected")

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

class RobotController:
    def __init__(self, robot, boisson):
        self.robot = robot
        self.boisson = boisson

    def connect(self):
        self.robot.connect()

    def disconnect(self):
        self.robot.disconnect()

    def move_forward(self):
        self.robot.move_forward()

    def EnregistrePosition(self,L):
        L = []
        self.robot.EnregistrePosition(L)

    def OpenGripper(self):
        self.robot.OpenGripper()

    def ricard(self):
        self.boisson.ricard()

    def ti_punch(self):
        self.boisson.ti_punch()

class Interface:
    def __init__(self, controller):
        self.controller = controller

        self.window = tk.Tk()
        self.window.geometry("400x200")

        self.btn_connect = tk.Button(self.window, text="Connect", command=self.controller.connect)
        self.btn_connect.pack()

        self.btn_disconnect = tk.Button(self.window, text="Disconnect", command=self.controller.disconnect)
        self.btn_disconnect.pack()

        self.btn_move_forward = tk.Button(self.window, text="Move Forward", command=self.controller.move_forward)
        self.btn_move_forward.pack()

        self.btn_EnregistrePosition = tk.Button(self.window, text="Enregistre une position", command=self.controller.EnregistrePosition)
        self.btn_EnregistrePosition.pack()

        self.btn_OpenGripper = tk.Button(self.window, text="Gripper Open", command=self.controller.OpenGripper)
        self.btn_OpenGripper.pack()

        self.btn_ricard = tk.Button(self.window, text="Ricard", command=self.controller.ricard)
        self.btn_ricard.pack()

        self.btn_ti_punch = tk.Button(self.window, text="Ti_punch", command=self.controller.ti_punch)
        self.btn_ti_punch.pack()

        self.window.mainloop()
""""
class VoiceRecognition:
    def __init__(self, controller):
        self.controller = controller
        self.recognizer = sr.Recognizer()

    def recognize_speech(self):
        with sr.Microphone() as source:
            audio_data = self.recognizer.listen(source)
        try:
            recognized_text = self.recognizer.recognize_google(audio_data, language="en-US")
            self.process_request(recognized_text)
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

    def process_request(self, text):
        if "connect" in text:
            self.controller.connect()
        elif "disconnect" in text:
            self.controller.disconnect()
        elif "move forward" in text:
            self.controller.move_forward()
        else:
            print("Unknown command")
"""
def main():
    # Demander à l'utilisateur les paramètres de connexion au robot
    ip = '192.168.1.209'
    use_sdk = True

    # Créer une instance du robot
    robot = UfactoryRobot(ip, use_sdk=use_sdk)
    boisson = MesCocktails()

    # Créer une instance du contrôleur du robot
    robot_controller = RobotController(robot,boisson)

    # Se connecter au robot
    robot_controller.connect()

    # Créer une instance de l'interface avec le robot
    interface = Interface(robot_controller)

    # Effectuer d'autres opérations nécessaires
    # ...

    # Se déconnecter du robot à la fin
    robot_controller.disconnect()

if __name__ == "__main__":
    main()
    
