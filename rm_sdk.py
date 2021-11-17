# -*- encoding: utf-8 -*-
# Test environment: Python 3.6
#importation de mode python qui ajoute des nouvelles fonctionalites
import socket
import sys

# En mode de connexion directe, l'adresse IP par défaut du robot est 192.168.2.1 et le port de commande de contrôle est le port 40923.
host = "192.168.2.1"
port = 40923
#defenir la fonction main
def main():
        address = (host, int(port))
        # Établissez une connexion TCP avec le port de commande de contrôle du robot.
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(address)

        print("Connected!")
        msg = "command;"
        s.send(msg.encode('utf-8'))

        while True:
                # Attendre que l'utilisateur entre les commandes de contrôle.
                msg = input(">>> please input SDK cmd: ")

                # Lorsque l'utilisateur entre Q ou q, quitte le programme en cours.
                if msg.upper() == 'Q':
                        break
                # Ajoutez le caractère de fin.
                msg += ';'
                # Envoyez des commandes de contrôle au robot.
                s.send(msg.encode('utf-8'))

                try:
                        # Attendez que le robot renvoie le résultat de l'exécution.
                        buf = s.recv(1024)

                        print(buf.decode('utf-8'))
                except socket.error as e:
                        print("Error receiving :", e)
                        sys.exit(1)
                if not len(buf):
                        break
        # Déconnectez la connexion du port.
        s.shutdown(socket.SHUT_WR)
        s.close()

main()




