#!/usr/bin/env python3
import math
from xarm import version
from xarm.wrapper import XArmAPI
import time
#from MesObjets import Objet
#from commandes1 import MesCommandes

class UfactoryRobot:

    def __init__(self, ip_address, use_sdk=False):
        """
        Initialisation du robot
        :param ip_address: l'adresse IP du robot
        :param use_sdk: si True, utilise l'API du SDK Ufactory
        """
        self.ip_address = ip_address
        self.use_sdk = use_sdk
        if self.use_sdk:
            self.robot = XArmAPI(ip_address, is_radian=True)

    def connect(self):
        """
        Se connecter au robot
        """
        if self.use_sdk:
            self.robot.motion_enable(enable=True)
            self.robot.set_mode(0)
            self.robot.set_state(state=0)
        else:
            self.client.connect()
            

    def disconnect(self):
        """
        Se déconnecter du robot
        """
        if self.use_sdk:
            pass  # Je ne vois pas de fonction de déconnexion dans le SDK
        else:
            self.client.disconnect()

    def move_forward(self):
        """
        Commande pour faire avancer le robot
        :return: la commande à envoyer ou la fonction du SDK à appeler
        """
        if self.use_sdk:
            # Obtenir la position actuelle
            current_position = self.robot.get_position()

            # Définir la nouvelle position
            new_position_x = current_position[1][0]+10

            # Déplacer le robot vers la nouvelle position
            self.robot.set_position(x = new_position_x)
        else:
            command = 'MOVE_FORWARD'  # Remplacer par la vraie commande
            self.client.send_command(command)
            return command
        
    def EnregistrePosition(self,L_position):
        """
        L_position est la liste des points parcourus par le bras.
        Le programme ajoute à la liste la position actuelle du robot
        """
        # Obtenir la position actuelle
        current_position = self.robot.get_servo_angle()  
        del current_position[1][-1]
        #current_position_radians = [math.radians(angle) for angle in current_position[1]]
        L_position.append(current_position[1])
        print (L_position)
    
    def DeplaceRobot(self,L_position2,index):
        """
        L_position2 est la liste des coordonnées des points parcourus.
        Le programme deplace le robot à la coordonnée d'un des points de la liste.
        L_position2 est de la forme [[...],[...],...,[...]]
        """
        try:
            # Obtenir la position actuelle
            #current_position = self.robot.get_servo_angle()

            # Déplacer le robot vers la nouvelle position
            self.robot.set_servo_angle(angle=L_position2[index])
            print(True)
        except ValueError:
            # En cas d'erreur, afficher un message et ne rien faire
            print("Erreur : impossible de déplacer le robot")

    def NextPosition(self,L_position3,i):
        """
        Le programme deplace le bras à la prochaine position lu dans la liste.
        L_position3 est de la forme [[...],[...],...,[...]]
        """
        try:
            # Obtenir la position actuelle
            current_position = L_position3[i]
            if len(L_position3)==i+1:
                self.robot.set_servo_angle(angle=L_position3[0],wait = True)
            else:
                # Déplacer le robot vers la nouvelle position
                self.robot.set_servo_angle(angle=L_position3[i+1],wait = True)
            print(True)
        except IndexError :
            return "Le robot n'a pas bougé"
        
    def PreviousPosition(self,L_position4,index):          # inutile
        """
        Le programme deplace le bras à la precedente position lu dans la liste.
        L_position4 est de la forme [[...],[...],...,[...]]
        """
        try:
            # Obtenir la position actuelle
            current_position = L_position4[index]
            if index==0:
                precedente_position_x = L_position4[-1][0]
                precedente_position_y = L_position4[-1][1]
                precedente_position_z = L_position4[-1][2]
            else:
                precedente_position_x = L_position4[index-1][0]
                precedente_position_y = L_position4[index-1][1]
                precedente_position_z = L_position4[index-1][2]
                
            # Déplacer le robot vers la nouvelle position
            self.robot.set_position(x=precedente_position_x,y=precedente_position_y,z=precedente_position_z)
            print(True)
        except TypeError :
            return "Le robot n'a pas bougé"
    
    def CloseGripper(self):
        """
        Le programme ferme la pince du robot
        """
        try:
            self.robot.set_gripper_position(0, wait=True)
            return True
        except xarm.core.exception.XArmError as e:
            print("Error: ", e)
            return False
        
    def OpenGripper(self):
        """
        Le programme ouvre la pince du robot
        """
        try :
            self.robot.set_gripper_position(850,wait=True,speed = 1500)
            return True
        except ValueError : 
            return "Probleme"
        
    def CloseGripper_moitie(self):
        """
        Le programme ferme à moitié la pince du robot
        """
        try :
            self.robot.set_gripper_position(400,wait=True)
            return True
        except ValueError : 
            return "Probleme"
            
    def MouvementComplet(self,L_position):
        try : 
            if self.CloseGripper()==True:
                position = self.DeplaceRobot(L_position,0)
                for i in range(0,len(L_position)-1):
                    position = self.NextPosition(L_position,i)
                position_gripper = self.OpenGripper()
            else:
                position = self.DeplaceRobot(L_position,0)
                for i in range(0,len(L_position)-1):
                    position = self.NextPosition(L_position,i)
                position_gripper = self.CloseGripper()
            return True
        except ValueError :
            return "Probleme"
        
    def MouvementComplet_bis(self,L_position):
        try :
            position = self.DeplaceRobot(L_position,0)
            for i in range(0,len(L_position)-1):
                position = self.NextPosition(L_position,i)
            return True
        except ValueError :
            return "Probleme"   
    
