import os
import cv2
from detecteur import DetecteurRouge, DetecteurVert
from dessinateur import DessinCroix, DessinRond

couleur = "rouge"
forme = "croix"

detecteurs = {"rouge": DetecteurRouge(), "vert": DetecteurVert()}
dessinateurs = {"croix": DessinCroix(), "rond": DessinRond()}


dossier = os.path.dirname(os.path.abspath(__file__))
image = cv2.imread(os.path.join(dossier, "ballons.png"))
if image is None or couleur not in detecteurs or forme not in dessinateurs:
    print("Problème : image introuvable ou choix invalide")
    exit()

coordonnees = detecteurs[couleur].detecter(image)              # Bloc 1 : détection
if coordonnees is None:
    print("Aucun ballon", couleur, "trouvé")
else:
    x, y = coordonnees
    image = dessinateurs[forme].dessiner(image, x, y)          # Bloc 2 : dessin
    cv2.imwrite(os.path.join(dossier, "image_traitee.png"), image)
    print("Coordonnées :", x, y, "- image enregistrée : image_traitee.png")