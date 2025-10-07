import time
import datetime

# Temps actuel en secondes depuis l'époque Unix
seconds = time.time()

# Affichage
print("Seconds since January 1, 1970: {:.4f} or {:.2e} in scientific notation".format(seconds, seconds))

# Date + heure formatée : ex "Jul 20 2025 15:43:07"
print(datetime.datetime.now().strftime("%b %d %Y"))
