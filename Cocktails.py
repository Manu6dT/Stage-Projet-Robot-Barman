import xarm
from xarm.wrapper import XArmAPI
from xArm6_Ufactory import UfactoryRobot
import time
from Trajectoires1 import MesTrajectoires

class MesCocktails:

    def __init__ (self):
        self.traj = MesTrajectoires()
        self.robot = UfactoryRobot(ip, use_sdk=True)

    def ti_punch(self):
        #Commandes à réaliser
        self.traj.PrendreVerre_1()
        self.traj.RemplirDosette2()
        self.traj.TransitionDosette_Jare()
        self.traj.TransitionJare_Versement()
        self.traj.VerserDiluantJare()
        self.traj.TransitionVersement_RecuperationVerre()
        self.traj.RecuperationVerre()
        self.traj.ServirVerre_1()
        self.traj.RetournePositionBase_1()

    def ricard(self):
        #commandes à réaliser
        self.traj.PrendreVerre_2()
        self.traj.RemplirDosette3()
        self.traj.RemplirDosette4()
        time.sleep(4)
        self.traj.RemplirDosette4()
        time.sleep(4)
        self.traj.RemplirDosette4()
        time.sleep(4)
        self.traj.RemplirDosette4()
        self.traj.ServirVerre_bis()
        self.traj.RetournePositionBase_2()
        


