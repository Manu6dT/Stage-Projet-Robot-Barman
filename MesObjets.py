import xarm
import math
from xarm.wrapper import XArmAPI
import pickle
from xArm6_Ufactory import UfactoryRobot

class Objet:
    def __init__(self):
        #self.commandes1 = MesCommandes()
        self.robot = UfactoryRobot(ip, use_sdk=True)

    def CreationListePoints(self):
        """
        Le programme génère une liste de coordonnées à partir de positions décidées 
        manuellement par l'utilisateur
        et enregistre la liste dans un fichier spécifié par le chemin_fichier.
        """
        try:
            L_position = []
            #L_radians = []
            self.robot.EnregistrePosition(L_position)#On enregistre la première position (actuelle)
            # On demande à l'utilisateur s'il a bougé le robot
            mouvement = str(input("Avez-vous bougé le robot : "))
            while mouvement == 'oui':
                self.robot.EnregistrePosition(L_position)
                mouvement = str(input("Avez-vous bougé le robot : "))
            #L_radians = [math.radians(angle) for angle in L_position]
            return L_position
            
        except ValueError:
            return False

# Pour utiliser cette classe, on peut faire comme suit:
ip = '192.168.1.209'  # Remplacer par l'adresse IP du robot
robot = UfactoryRobot(ip, use_sdk=True)
robot.connect()
objet = Objet()
L_position = objet.CreationListePoints()  # Remplacez [...] par votre liste de coordonnées

# Enregistrement de la liste dans un fichier texte
chemin_fichier = r'C:\connexion via bouton\Liste trajectoires.txt'
with open(chemin_fichier, 'w') as fichier:
    for coordonnee in L_position:
        fichier.write(f"{coordonnee}\n")

print("Liste de coordonnées enregistrée dans le fichier :", chemin_fichier)

robot.disconnect()
