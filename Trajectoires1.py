import math
from xarm import version
from xarm.wrapper import XArmAPI
import time
from xArm6_Ufactory import UfactoryRobot

class MesTrajectoires:

    def __init__(self):
        ip = '192.168.1.209' 
        self.robot = UfactoryRobot(ip, use_sdk=True)

    def RemplirDosette1(self):      
        # Pour remplir le verre de la dosette en première position en partant de la gauche         
        Liste_points_1 = [[-1.194864, -0.060339, -0.185359, 2.391231, 1.396551, 0.118926],
                        [-1.184469, -0.241964, -0.161536, 2.365437, 1.281438, 0.230848]]
        Liste_points_2 =  [[-1.275356, 0.070838, -0.21609, 2.287863, 1.479084, 0.061321]]
        self.robot.connect()
        code = self.robot.MouvementComplet_bis(Liste_points_1)
        time.sleep(4)
        code = self.robot.DeplaceRobot(Liste_points_2,0)
        self.robot.disconnect()

    def RemplirDosette2(self):      
        # Pour remplir le verre de la dosette en deuxieme position en partant de la gauche         
        Liste_points_1 = [[-1.551959, 0.294227, -0.635584, 1.751244, 1.518277, 0.286874],
                          [-1.548718, 0.189236, -0.607923, 1.749694, 1.503267, 0.362881]]
        Liste_points_2 = [[-1.554997, 0.404252, -0.672283, 1.751621, 1.532353, 0.21483]]
        self.robot.connect()
        code = self.robot.MouvementComplet_bis(Liste_points_1)
        time.sleep(4)
        code = self.robot.DeplaceRobot(Liste_points_2,0)
        self.robot.disconnect()

    
    def RemplirDosette3(self):      
        # Pour remplir le verre de la dosette en troisième position en partant de la gauche         
        Liste_points_1 = [[-1.57828, 0.234128, -0.61002, 2.135434, 1.353385, 0.289665],
                          [-1.568995, 0.127646, -0.589947, 2.12641, 1.3026, 0.362358]]
        Liste_points_2 = [[-1.577619, 0.220545, -0.604218, 2.136461, 1.288077, 0.295263]]
        self.robot.connect()
        code = self.robot.MouvementComplet_bis(Liste_points_1)
        time.sleep(4)
        code = self.robot.DeplaceRobot(Liste_points_2,0)
        self.robot.disconnect()
    
    def RemplirDosette4(self):      
        # Pour remplir le verre de la dosette en quatrième position en partant de la gauche         
        Liste_points_1 = [[-1.709934, 0.443877, -0.940409, 1.954048, 1.373089, 0.410137],
                          [-1.703728, 0.366974, -0.914442, 1.950425, 1.350428, 0.457626]]
        Liste_points_2 = [[-1.704095, 0.479472, -0.927073, 1.97084, 1.386761, 0.364169]]
        self.robot.connect()
        code = self.robot.MouvementComplet_bis(Liste_points_1)
        time.sleep(4)
        code = self.robot.DeplaceRobot(Liste_points_2,0)
        self.robot.disconnect()

    def VerserDiluantJare(self):
        # Pour remplir le verre du diluant, adapter le temps de versement
        Liste_points_1 = [[-2.84698, -0.453181, -0.78142, 6.162742, 1.278786, -2.131552],
                        [-2.845214, -0.415645, -0.653683, 6.151718, 1.118707, -2.110899]]
        Liste_points_2 = [[-2.832827, -0.463818, -0.81127, 6.15916, 1.327726, -2.129894]]
        self.robot.connect()
        code = self.robot.MouvementComplet_bis(Liste_points_1)
        time.sleep(4)
        code = self.robot.DeplaceRobot(Liste_points_2,0)
        self.robot.disconnect()

    def SortirPaille1(self):
        # Pour sortir la paille de droite ( côté jare )
        Liste_points = [[-2.447127, 0.63199, -0.937003, 4.415445, 1.519757, -0.317053],
                        [-2.460801, 0.260361, -0.819557, 4.4242, 1.442914, -0.560729]]
        self.robot.connect()
        code = self.robot.DeplaceRobot(Liste_points,0)
        #self.robot.CloseGripper()
        #self.robot.DeplaceRobot(Liste_points,1)
        self.robot.disconnect()

    def SortirPaille2(self):
        # Pour sortir la paille du milieu
        Liste_points = [[-2.41537, 0.714783, -1.151065, 4.460028, 1.425588, -0.430354],
                        [-2.426686, 0.402373, -1.026074, 4.47929, 1.382376, -0.615124]]
        code = self.robot.MouvementComplet_bis(Liste_points)

    def SortirPaille3(self):
        # Pour sortir la paille de gauche
        Liste_points_1 = [[-2.116858, 0.545574, -0.5617, 3.093955, 1.5283, 0.032163],
                        [-2.127781, 0.423294, -0.233317, 3.09694, 1.681249, 0.032152],
                        [-2.127752, -0.783364, -0.567157, 3.095429, 0.179788, 0.032152],
                        [-2.260045, -0.195172, -1.24459, 2.35668, -0.236333, 0.032118],
                        [-2.257249, -0.343736, -1.603982, 6.248291, 2.030239, 0.932219],
                        [-2.584654, 0.135815, -1.603136, 6.248291, 1.447911, 0.932352],
                        [-2.606398, 0.39304, -1.595706, 6.248274, 1.184914, 1.000529],
                        [-2.592681, 0.512706, -1.528393, 6.229021, 0.993264, 1.075171]]
        Liste_points_2 = [[-2.592681, 0.512706, -1.528393, 6.229021, 0.993264, 1.075171],
                          [-2.584019, 0.551297, -1.597156, 6.229021, 1.003484, 1.075069]]
        Liste_points_3 = [[-2.592681, 0.512706, -1.528393, 6.229021, 0.993264, 1.075171],
                          [-2.592531, 0.455985, -1.598194, 6.233621, 1.116475, 1.070436],
                          [-2.592138, 0.516946, -2.244731, 6.241302, 1.690182, 1.054694],
                          [-2.085374, 0.254999, -2.141759, 6.241246, 1.911979, 1.054742],
                          [-2.072287, 0.015175, -1.250743, 6.24064, 1.135134, 1.05493],
                          [-2.115227, 0.060691, -1.137977, 6.23848, 0.981128, 1.057158],
                          [-2.08046, 0.027349, -1.187351, 6.238477, 1.050518, 1.054922],
                          [-2.088071, 0.085811, -1.076161, 6.233507, 0.882358, 1.062485],
                          [-2.093516, 0.147037, -1.020182, 6.228306, 0.76619, 1.069008]]
        self.robot.connect()
        #code = self.robot.MouvementComplet_bis(Liste_points_1)  
        #self.robot.CloseGripper_moitie()
        #code = self.robot.MouvementComplet_bis(Liste_points_2) 
        self.robot.CloseGripper()
        code = self.robot.MouvementComplet_bis(Liste_points_3)  
        self.robot.OpenGripper()
        self.robot.disconnect()

    def TransitionDosette_Jare(self):
        Liste_points = [[-1.674467, 0.404269, -0.687383, 1.945515, 1.486732, 0.302559],
                        [-1.960565, 0.274214, -0.056288, 3.114336, 1.851283, -0.037178],
                        [-1.971311, 0.331859, -0.356116, 4.806769, 1.566666, 0.015301],
                        [-2.238068, 0.456277, -0.469212, 4.658255, 1.559874, 0.014337],
                        [-2.241476, 0.516177, -0.503656, 4.658243, 1.559888, 0.014341],
                        [-2.244528, 0.524679, -0.516165, 4.672628, 1.559755, 0.014024],
                        [-2.244301, 0.548538, -0.527638, 4.672636, 1.560245, 0.026367]]
        code = self.robot.MouvementComplet(Liste_points)

    def TransitionJare_Versement(self):
        Liste_points = [[-2.244301, 0.548538, -0.527638, 4.672636, 1.560245, 0.026367],
                        [-2.078285, 0.350171, -0.384498, 4.767183, 1.483637, -0.049475],
                        [-2.318261, -0.480792, -0.832871, 6.248295, 1.31368, -2.231643],
                        [-2.762711, -0.618455, -0.868206, 6.111905, 1.375037, -2.095604],
                        [-2.907494, -0.518313, -0.802558, 6.16626, 1.284095, -2.222153]]
        self.robot.connect()
        code = self.robot.MouvementComplet_bis(Liste_points)
        self.robot.CloseGripper()
        self.robot.disconnect()

    def TransitionVersement_RecuperationVerre(self):
        Liste_points = [[-2.832827, -0.463818, -0.81127, 6.15916, 1.327726, -2.129894],
                        [-2.513659, -0.631107, -0.722662, 6.159161, 1.368838, -2.129902],
                        [-1.733487, -0.524786, -0.238367, 4.970527, 1.808659, -0.697708],
                        [-1.825602, 0.311525, -0.367005, 4.972805, 1.539658, -0.052897],
                        [-1.958723, 0.548122, -0.442983, 4.834311, 1.573101, 0.105471]]
        self.robot.connect()
        code = self.robot.MouvementComplet_bis(Liste_points)
        self.robot.OpenGripper()
        self.robot.disconnect()

    def RecuperationVerre(self):
        Liste_points = [[-1.958723, 0.548122, -0.442983, 4.834311, 1.573101, 0.105471],
                        [-2.103495, 0.548954, -0.447978, 4.690266, 1.588304, 0.101575],
                        [-2.242099, 0.549619, -0.452504, 4.552216, 1.601592, 0.096491]]
        self.robot.connect()
        code = self.robot.MouvementComplet_bis(Liste_points)
        self.robot.CloseGripper()
        self.robot.disconnect()

    def ServirVerre_1(self):
        Liste_points = [[-2.242099, 0.549619, -0.452504, 4.552216, 1.601592, 0.096491],
                        [-2.245365, 0.43148, -0.397724, 4.547342, 1.591542, 0.033913],
                        [-1.816176, 0.222218, -0.154754, 4.547337, 1.591296, 0.077696],
                        [-1.760425, 0.223116, -0.166262, 3.016495, 1.623466, -0.041097],
                        [-1.196795, 0.399945, -0.501527, 4.075149, 1.5406, -0.098307],
                        [-1.414743, 0.560641, -0.791864, 3.954873, 1.411078, -0.156911],
                        [-1.444199, 0.588061, -0.78796, 3.867871, 1.410447, -0.129742],
                        [-1.445821, 0.613312, -0.798703, 3.868104, 1.417127, -0.120535]]
        self.robot.connect()
        code = self.robot.MouvementComplet_bis(Liste_points)
        self.robot.OpenGripper()
        self.robot.disconnect()

    def ServirVerre_2(self):
        Liste_points = [[-2.242099, 0.549619, -0.452504, 4.552216, 1.601592, 0.096491],
                        [-2.245479, 0.427676, -0.396067, 4.547185, 1.591193, 0.031794],
                        [-1.9568, 0.272537, -0.084277, 3.325569, 1.803852, 0.033044],
                        [-1.589476, 0.38632, -0.350492, 3.673127, 1.660137, 0.033065],
                        [-1.681556, 0.486795, -0.612917, 3.64214, 1.444763, -0.086424],
                        [-1.688186, 0.522926, -0.61346, 3.616601, 1.492538, -0.083485],
                        [-1.68621, 0.549539, -0.62337, 3.618869, 1.507331, -0.075835],
                        [-1.684895, 0.567538, -0.630346, 3.62045, 1.517069, -0.070748]]
        self.robot.connect()
        code = self.robot.MouvementComplet_bis(Liste_points)
        self.robot.OpenGripper()
        self.robot.disconnect()

    def ServirVerre_3(self):
        Liste_points = [[-2.242099, 0.549619, -0.452504, 4.552216, 1.601592, 0.096491],
                        [-2.245414, 0.42985, -0.397014, 4.547275, 1.591393, 0.033006],
                        [-2.035048, 0.429676, -0.364556, 3.80311, 1.633433, 0.033184],
                        [-2.045373, 0.424067, -0.398887, 3.236408, 1.630367, 0.00772],
                        [-2.050116, 0.46926, -0.530807, 3.236109, 1.500032, 0.007737],
                        [-2.032638, 0.539286, -0.552561, 3.270757, 1.554983, 0.012866]]
        self.robot.connect()
        code = self.robot.MouvementComplet_bis(Liste_points)
        self.robot.OpenGripper()
        self.robot.disconnect()

    def PrendreVerre_1(self):
        Liste_points_1 = [[-1.30937, 0.091003, -0.309026, 3.866533, 1.374017, -0.208566],
                          [-1.396153, 0.482544, -0.632351, 3.863935, 1.374017, -0.084973],
                          [-1.45993, 0.630023, -0.781552, 3.804583, 1.452655, -0.091655]]
        Liste_points_2 = [[-1.45993, 0.630023, -0.781552, 3.804583, 1.452655, -0.091655],
                          [-1.472184, 0.447562, -0.713056, 3.803849, 1.36121, -0.160664],
                          [-1.642368, 0.226665, -0.375756, 2.871376, 1.361118, 0.042541],
                          [-1.623337, 0.276648, -0.30904, 2.23776, 1.578372, 0.041906]]
        self.robot.connect()
        self.robot.OpenGripper()
        code = self.robot.MouvementComplet_bis(Liste_points_1)
        self.robot.CloseGripper()
        code = self.robot.MouvementComplet_bis(Liste_points_2)
        self.robot.disconnect()

    def PrendreVerre_2(self):
        Liste_points_1 = [[-1.904704, -0.00465, 0.047718, 3.082116, 1.685507, -0.128387],
                          [-1.497984, 0.168462, -0.178481, 3.723464, 1.486677, -0.004314],
                          [-1.687647, 0.476537, -0.454781, 3.541783, 1.557115, -0.005492],
                          [-1.726775, 0.578207, -0.621864, 3.520097, 1.537264, -0.007513]]
        Liste_points_2 = [[-1.726775, 0.578207, -0.621864, 3.520097, 1.537264, -0.007513],
                          [-1.743071, 0.305826, -0.537738, 3.512067, 1.361175, -0.074698],
                          [-1.697524, -0.149567, -0.011942, 3.512055, 1.361661, -0.074667],
                          [-1.691756, 0.028312, 0.025359, 2.905634, 1.579962, 0.046888],
                          [-1.692746, 0.162456, -0.172281, 2.346943, 1.578961, 0.046955],
                          [-1.528219, 0.289453, -0.370851, 2.278949, 1.503729, 0.04707]]
        self.robot.connect()
        self.robot.OpenGripper()
        code = self.robot.MouvementComplet_bis(Liste_points_1)
        self.robot.CloseGripper()
        code = self.robot.MouvementComplet_bis(Liste_points_2)
        self.robot.disconnect()
    
    def PrendreVerre_3(self):
        Liste_points_1 = [[-2.332926, 0.111133, -0.096292, 2.656715, 1.623678, 0.022074],
                          [-2.069977, 0.354043, -0.267225, 3.175388, 1.607445, 0.021796],
                          [-2.075992, 0.434607, -0.449464, 3.175388, 1.468018, 0.021539],
                          [-2.077936, 0.513617, -0.561356, 3.17539, 1.47196, 0.021246]]
        Liste_points_2 = [[-2.077936, 0.513617, -0.561356, 3.17539, 1.47196, 0.021246],
                          [-2.079253, 0.309596, -0.504883, 3.174915, 1.32449, 0.016387],
                          [-2.494741, 0.115694, -0.113124, 2.758512, 1.522055, 0.021899],
                          [-2.494741, 0.115694, -0.113124, 1.787879, 1.522055, 0.021899],
                          [-1.961762, 0.306403, -0.370782, 2.449441, 1.504528, 0.02137],
                          [-1.519619, 0.375827, -0.441944, 2.250467, 1.505867, 0.016906]]
        self.robot.connect()
        self.robot.OpenGripper()
        code = self.robot.MouvementComplet_bis(Liste_points_1)
        self.robot.CloseGripper()
        code = self.robot.MouvementComplet_bis(Liste_points_2)
        self.robot.disconnect()

    def RetournePositionBase_3(self):
        Liste_points = [[-2.122408, 0.498254, -0.552703, 3.080295, 1.451765, 0.000533],
                        [-2.121804, 0.192984, -0.269549, 3.080289, 1.451804, 0.000635],
                        [-2.121783, 0.217789, -0.045178, 3.080299, 1.72926, 0.000635]]
        self.robot.connect()
        code = self.robot.MouvementComplet_bis(Liste_points)
        self.robot.CloseGripper()
        self.robot.disconnect()

    def RetournePositionBase_1(self):
        Liste_points = [[-1.450701, 0.619087, -0.799739, 3.847322, 1.397866, -0.096865],
                        [-1.365337, 0.547995, -0.631805, 3.875179, 1.537944, -0.094014],
                        [-1.29626, 0.32859, -0.253709, 3.945199, 1.537977, 0.011969]]
        self.robot.connect()
        code = self.robot.MouvementComplet_bis(Liste_points)
        self.robot.CloseGripper()
        self.robot.disconnect()

    def RetournePositionBase_2(self):
        Liste_points = [[-1.741327, 0.506292, -0.604379, 3.508534, 1.43134, -0.04755],
                        [-1.662456, 0.454361, -0.442429, 3.582449, 1.601982, 0.021399],
                        [-1.591003, 0.392471, -0.139491, 3.641158, 1.76992, 0.14086]]
        self.robot.connect()
        code = self.robot.MouvementComplet_bis(Liste_points)
        self.robot.CloseGripper()
        self.robot.disconnect()

    def ServirVerre_bis(self):
        Liste_points = [[-1.704095, 0.479472, -0.927073, 1.97084, 1.386761, 0.364169],
                        [-1.704153, 0.371427, -0.520508, 1.970715, 1.462854, 0.121955],
                        [-1.706826, 0.215852, -0.119135, 3.2509, 1.600837, 0.12022],
                        [-1.568392, 0.374769, -0.327923, 3.685632, 1.598164, 0.084885],
                        [-1.674948, 0.491083, -0.610655, 3.68565, 1.473586, 0.007051],
                        [-1.676798, 0.524332, -0.630056, 3.649106, 1.468681, -0.070695],
                        [-1.682283, 0.564559, -0.640912, 3.63648, 1.494289, -0.05551]]
        self.robot.connect()
        code = self.robot.MouvementComplet_bis(Liste_points)
        self.robot.OpenGripper()
        self.robot.disconnect()
    

    