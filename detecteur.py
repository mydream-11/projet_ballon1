import cv2
from abc import ABC, abstractmethod

def centre_du_masque(masque):                                  # Trouve le milieu des pixels blancs
    m = cv2.moments(masque)
    if m["m00"] == 0:                                          # Aucun pixel blanc : rien trouvé
        return None
    x = int(m["m10"] / m["m00"])
    y = int(m["m01"] / m["m00"])
    return x, y

class Detecteur(ABC):                                          # Cahier de règles : "sache trouver un ballon"
    @abstractmethod
    def detecter(self, image):                                 # Règle obligatoire : rendre (x, y) ou None
        pass

class DetecteurRouge(Detecteur):                               # Cherche le ballon rouge
    def detecter(self, image):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        masque = cv2.inRange(hsv, (0, 120, 70), (10, 255, 255))
        return centre_du_masque(masque)

class DetecteurVert(Detecteur):                                # Cherche le ballon vert
    def detecter(self, image):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        masque = cv2.inRange(hsv, (40, 80, 70), (80, 255, 255))
        return centre_du_masque(masque)
