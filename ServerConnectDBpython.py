#Programm zum Schreiben von Datenbankeinträgen
#von Nicolas Csaba Bohocki
#08.06.2020
#---------------------------------------------------------------------------------------------------
import mysql.connector                                                      #Importieren des Moduls für eine Datenbank mithilfe von MySQL

Username = input("Username: ")                                              #Angabe des Benutzernames für den Zugriff auf die Datenbank
Password = input("Password: ")                                              #Angabe des Passwortes für den Benutzer zum Zugriff auf die Datenbank
Database = input("Connect to Database: ")
connection=mysql.connector.connect(host="DESKTOP-OGGKVHD",                  
                                   database=Database,                       #Verbindungsaufnahme zur Datenbank
                                   user=Username,                           #Verbinden mit der Datenbank
                                   password=Password)                       #Einloggen mit dem Userprofil und Passwort                                                
#---------------------------------------------------------------------------------------------------
db_Info=connection.get_server_info                                          #Informationen vom Server abrufen
print("Informationen des Servers ", db_Info)




