import speech_recognition as sr
import openai
import re
import pyttsx3
from xArm6_Ufactory import UfactoryRobot
from Cocktails import MesCocktails
import reconnaissance_bouton
from Alertes import Alertes

class RobotBarman:
    def __init__(self):
        cocktail = MesCocktails()


    #fonction pour lire a haute voix les textes
    def lire_texte(self,texte):
        engine = pyttsx3.init()
        engine.say(texte)
        engine.runAndWait()


    # Fonction pour effectuer la reconnaissance vocale
    def recognize_speech(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Dites quelque chose...")
            audio = r.listen(source)

        try:
            print("En cours de reconnaissance vocale...")
            text = r.recognize_google(audio, language='fr-FR')
            print("Reconnaissance vocale terminée.")
            return text
        except sr.UnknownValueError:
            print("Impossible de reconnaître la parole.")
        except sr.RequestError as e:
            print(f"Erreur lors de la demande à l'API de reconnaissance vocale : {e}")



    # Fonction pour interagir avec OpenAI et obtenir une réponse
    def ask_openai(self,question):
        openai.api_key = "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"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Assistant is a robot bairman, he knows only two coktails [punch] and [ricard]. If you're not sure of an answer, you have to guess and give the closest coktail from [punch] and [ricard]. GIVE ME ONLY [punch] or [ricard] as an answer!. Always answer with two lines, first line is the coktail name from the known list, second line is a quick fun fact about it"},
                {"role": "user", "content": question}
            ],
        )

        return response['choices'][0]['message']['content']

    # fonction qui ajoute le prompt de début pour openAI
    def modify_openAI_prompt(self,phraseHumain):

        promptDebut = "D'après la question suivante : quel coktail dois-tu préparer:"
        promptFin = ""

        print ("=======")
        print (promptDebut+phraseHumain+promptFin)
        print ("============")

        return promptDebut+phraseHumain

    # Fonction pour extraire le texte après --->
    def extract_text_after_arrow(self,text):
        arrow_index = text.find("--->")
        if arrow_index != -1:
            extracted_text = text[arrow_index + len("--->"):].strip()
            return extracted_text
        else:
            return None

    def enlever_caracteres(self,texte):
        if isinstance(texte, list) and len(texte) > 0:
            texte = texte[0]
        else:
            return texte
        if texte:
            texte = texte.replace("'", "")
            texte = texte.replace("[", "")
            texte = texte.replace("]", "")
        return texte.lower()

    #pour enlever les caracteres genant et trouver les mots sans les corchets
    def extract_text_within_brackets(self,text):
        pattern = r"\[(.*?)\]"
        matches = re.findall(pattern, text)
        
        if len(matches) == 0:
            if "ricard" in text:
                return ["ricard"]
            elif "punch" in text:
                return ["punch"]
            else:
                return []
        
        unique_matches = list(set(matches))
        return unique_matches


    #retrouver juste le fun fact
    def getFunFact(self,texte):

        # Diviser le texte en lignes
        lignes = texte.splitlines()

        # Récupérer la deuxième ligne
        deuxieme_ligne = lignes[1]

        return deuxieme_ligne


    #appel de function ricard
    def callRicard(self):

        self.cocktail.ricard()

    #appel de function punch
    def callPunch(self):

        self.cocktail.ti_punch()

    def appeler_fonction(self,mot):
        if mot == "ricard":
            self.callRicard()
        elif mot == "punch":
            self.callPunch()
        else:
            print("Mot non reconnu.")
    
    def reconnaissance_vocale(self):
        ip = '192.168.1.209'
        use_sdk = True
        # Créer une instance du robot
        robot = UfactoryRobot(ip, use_sdk=use_sdk)
        robotbarman = RobotBarman()
        question = robotbarman.recognize_speech()
        answer = robotbarman.ask_openai(robotbarman.modify_openAI_prompt(question))
        #print (answer)

        extracted_text = robotbarman.enlever_caracteres(robotbarman.extract_text_within_brackets(answer))

        print (extracted_text)
        robot.connect()
        robotbarman.appeler_fonction(extracted_text)
        robotbarman.lire_texte(robotbarman.getFunFact(answer))

        robot.disconnect()

