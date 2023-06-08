from Cocktails import MesCocktails
from Trajectoires1 import MesTrajectoires

class Alertes:
    def __init__(self) :
        self.compteur_alcool_1 = 0
        self.compteur_alcool_2 = 0
        self.compteur_alcool_3 = 0
        self.compteur_alcool_4 = 0
        self.compteur_diluant_1 = 0
        self.compteur_diluant_2 = 0
        self.compteur_diluant_3 = 0
        self.cocktail = MesCocktails()
        self.traj = MesTrajectoires
        
    def compteurs(self,commande):
        if commande == self.traj.RemplirDosette_alcool_1():
            self.compteur_alcool_1 += 1
        elif commande == self.traj.RemplirDosette_alcool_2():
            self.compteur_alcool_2 += 1
        elif commande == self.traj.RemplirDosette_alcool_3():
            self.compteur_alcool_3 += 1
        elif commande == self.traj.RemplirDosette_alcool_4():
            self.compteur_alcool_4 += 1
        elif commande == self.traj.Verser_diluant_1():
            self.compteur_diluant_1 += 1
        elif commande == self.traj.Verser_diluant_2():
            self.compteur_diluant_2 += 1
        elif commande == self.traj.Verser_diluant_3():
            self.compteur_diluant_3 += 1

    def choix_bouteilles(self):
        alcool_1 = str(input("Qu'avez-vous mis en premier alcool :" ))
        alcool_2 = str(input("Qu'avez-vous mis en deuxième alcool :" ))
        alcool_3 = str(input("Qu'avez-vous mis en troisième alcool :" ))
        alcool_4 = str(input("Qu'avez-vous mis en quatrième alcool :" ))
        diluant_1 = str(input("Qu'avez-vous mis en premier diluant :" ))
        diluant_2 = str(input("Qu'avez-vous mis en deuxième diluant :" ))
        diluant_3 = str(input("Qu'avez-vous mis en troisième diluant :" ))

    def contenance_bouteille(self):
        contenance_alcool_1 = str(input("Quelle est le volume d'alcool 1 mis (en cl):"))
        contenance_alcool_2 = str(input("Quelle est le volume d'alcool 2 mis (en cl):"))
        contenance_alcool_3 = str(input("Quelle est le volume d'alcool 3 mis (en cl):"))
        contenance_alcool_4 = str(input("Quelle est le volume d'alcool 4 mis (en cl):"))
        contenance_diluant_1 = str(input("Quelle est le volume de diluant 1 versé (en cl):"))
        contenance_diluant_2 = str(input("Quelle est le volume de diluant 2 versé (en cl):"))
        contenance_diluant_3 = str(input("Quelle est le volume de diluant 3 versé (en cl):"))

    def contenance_verre(self):
        contenance_verre_small = 10 
        contenance_verre_medium = 15
        contenance_verre_large = 20
        
    def seuil_compteurs(self):
        """
        Une dosette d'alcool fait 4 cl
        On suppose que une dose de diluant représente 12 cl
        """()
        bouteille = self.choix_bouteilles()
        seuil = self.contenance_bouteille()
        seuil_compteur_alcool_1 = seuil.contenance_alcool_1 // 4
        seuil_compteur_alcool_2 = seuil.contenance_alcool_2 // 4
        seuil_compteur_alcool_3 = seuil.contenance_alcool_3 // 4
        seuil_compteur_alcool_4 = seuil.contenance_alcool_4 // 4
        seuil_compteur_diluant_1 = seuil.contenance_diluant_1 // 12
        seuil_compteur_diluant_2 = seuil.contenance_diluant_2 // 12
        seuil_compteur_diluant_3 = seuil.contenance_diluant_3 // 12

        #exemple pour 1 alcool et 1 diluant
        if self.compteur_alcool_1 > seuil_compteur_alcool_1 :                   
            print(f"Il manque de l'{bouteille.alcool_1}")
            
        elif self.compteur_diluant_1 > seuil_compteur_diluant_1 :
            print(f'Il manque du {bouteille.diluant_1}')

def main():
    alertes = Alertes()
    commandes = MesTrajectoires()
    alertes.choix_bouteilles()
    alertes.contenance_bouteille()
    alertes.contenance_verre()
    alertes.compteurs(commandes)
    alertes.seuil_compteurs()

if __name__ == '__main__':
    main()

            





        


