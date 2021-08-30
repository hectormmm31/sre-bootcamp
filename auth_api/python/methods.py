import jwt
import hashlib
from flask import jsonify, make_response, abort
import mysql.connector
from mysql.connector import Error


class Token:

    def generate_token(self, username, password):
       
        secretKey   = 'my2w7wjd7yXF64FIADfJxNs1oupTGAuW'

        #DB connection 
        myDataBase = mysql.connector.connect(
            host="bootcamp-tht.sre.wize.mx",
            user="secret",
            password="noPow3r",
            database="bootcamp_tht"
        )
            
        cursor = myDataBase.cursor()

        rows_count = cursor.execute("SELECT password,salt,role FROM users WHERE username=%s", (username,))
        
        dbresult = cursor.fetchall()

        if dbresult:
            for row in dbresult:
              password_db = row[0]
              salt_db = row[1]
              role_db = row[2]

            #Convert password received to check if it matches 
            #saltedpassword = password+salt_db
            hashed_password = hashlib.sha512(password.encode("utf-8") + salt_db.encode("utf-8")).hexdigest()

            if hashed_password == password_db:
                #Contraseña correcta
                #response = "Contrasena correcta"
                try:
                    payload = {
                        "role": role_db
                    }
                    response = jwt.encode(
                        payload,
                        secretKey,
                        algorithm='HS256'
                    )
                except Exception as e:
                    return e

            else:
               #response = "Contraseña incorrecta"
                abort(401) 


        else:
            #response = "No hay resultados"
            abort(401)
            #make_response('Could not verify login', 401)

        # Closing database connection
        myDataBase.close()
        
        return response


class Restricted:

    def access_data(self, authorization):
        return 'test'
