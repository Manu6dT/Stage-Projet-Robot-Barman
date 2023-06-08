from xArm6_Ufactory import UfactoryRobot
from Cocktails import MesCocktails
from Alertes import Alertes
from reconnaissance_vocale import RobotBarman
import Interfaces



def main():
    # Demander à l'utilisateur les paramètres de connexion au robot
    ip = '192.168.1.209'
    use_sdk = True

    # Créer les instances pour le robot
    robot = UfactoryRobot(ip, use_sdk=use_sdk)
    boisson = MesCocktails()

    # Lancer le programme d'alertes
    Alertes()

    # Créer une instance du contrôleur du robot
    robot_controller = Interfaces.RobotController(robot,boisson)

    # Se connecter au robot
    robot_controller.connect()

    # Créer une instance de l'interface avec le robot pour la reconnaissance vocale et bouton
    interface = Interfaces.Interface(robot_controller)

    # Se déconnecter du robot à la fin
    robot_controller.disconnect()

if __name__ == "__main__":
    main()
    