import psycopg2
import datetime  
import time 
from tabulate import tabulate

conn = psycopg2.connect(host = "201.238.213.114", port= "54321", database="grupo23", user="grupo23", password="f9kNXT")

cur = conn.cursor()
print("\t BIENVENIDO A LINKEDING ")
main = True
while main:

    print("(1) Iniciar sesion")
    print("(2) Crear cuenta")
    print("(3) Recuperar contrasena")
    print("(4) Salir")
    opcion=raw_input("ingrese una opcion: ")
    noEncontroE = True
    trutru = False
    if opcion=="1":
            email=raw_input("ingrese su email: ")
            contrasena=raw_input("ingtrese su contrasena: ")

            cur.execute(("SELECT  * FROM clave WHERE {} = email_usuario ORDER BY fecha DESC LIMIT 1;  ").format(str("'" + email + "'")))
            rows = cur.fetchall()
            usarioE = False
            while True:
                for i in rows:
                    if i[0]==email and i[1] == contrasena:                 
                        print("Sesion iniciada")
                        cur.execute(("SELECT id FROM perfil WHERE {} = email;").format(str("'" + email + "'")))
                        id = cur.fetchone()
                        print(id)
                        if id == None:
                            id = 70
                        usarioE=True
                        break
                if usarioE == False:
                        print(" mail o contrasena invalida")
                        break
                else:
                    main = False
                    break
                



    elif opcion=="3":
        email = raw_input("ingrese su email: ")
        cur.execute("SELECT * FROM clave ORDER BY fecha DESC")
        rows = cur.fetchall()
        cur.close()
        for i in rows:
            if i[0] == email:
                print("mail encontrado")
                print("su contrasena es:"+ str(i[1]))
                break 
        cur = conn.cursor()
        clave =raw_input("ingrese nueva clave")   
        fechaa = datetime.date.today()
        cur.execute("INSERT INTO clave(email_usuario,clave,fecha) VALUES(%s,%s,%s);" , (email,clave,str(fechaa)))
        conn.commit()

    elif opcion=="2":
        cuenta=str(raw_input("Ingrese el email de la cuenta nueva: "))
        contrasena= raw_input("Ingrese contrasena: ")

        while 1:
            verificacion=raw_input("Ingrese nuevamente la contrasena: ")
            if contrasena!=verificacion:
                verificacion=raw_input("Ingrese nuevamente la contrasena dado que no coincide con la inicial:")
            else:
                break

        cur.execute("INSERT INTO usuario(email) VALUES({});".format(str("'" + cuenta +"'")))    
        conn.commit()    
        cur.close()
        
        fecha=datetime.date.today()
        
        cur=conn.cursor()
        cur.execute(("INSERT INTO clave(email_usuario,clave,fecha) VALUES(%s,%s,%s);"), (cuenta,verificacion,str(fecha)))
        conn.commit() 
    elif opcion== "4":
        trutru = True
        break 
    else:
        print("Opcion invalida! Intente nuevamente")  
        

TRUUEEE = True
if trutru:
    TRUUEEE = False
while TRUUEEE:
    print("\t MENU PRINCIPAL ")
    print("(1) USARIO")
    print("(2) VER PUBLICACIONES")
    print("(3) VER NOTIFICACIONES")
    print("(4) CONTACTO")
    print("(5) EMPRESA")
    print("(6) SALIR ")
    opcion = raw_input("ingrese una opcion: ")

    if opcion == "1":
        Bperfil = True
        while Bperfil:
            cur.execute("SELECT * FROM perfil WHERE email = {} ".format(str("'"+email+ "'")))
            perfil = cur.fetchone()
            print("--------------------------------------")
            print("ID: " + str(perfil[0]) + "\nemail: " + perfil[1]  + "\nnombre completo: " + perfil[2] + " " + perfil[3] + "\ngenero: " + perfil[4] + 
            "\nfecha de nacimiento: " + str(perfil[5]) + "\npais: " + perfil[6] + "\ndescripcion: " + perfil[7] )
            cur.execute(" SELECT * FROM estudio WHERE id_perfil = {}".format(perfil[0]))
            educacion = cur.fetchone()
            cur.execute(" SELECT * FROM trabaja WHERE id_trabajador = {}".format(perfil[0]))
            experiencia = cur.fetchone()
            cur.execute(" SELECT foto FROM foto_perfil WHERE id_perfil = {}".format(perfil[0]))
            foto_perfil = cur.fetchall()
            print(tabulate(foto_perfil, headers=["Fotos"] , tablefmt= "fancygrid"))
            cur.execute(" SELECT telefono FROM telefono_perfil WHERE id_perfil = {}".format(perfil[0]))
            telefono_perfil = cur.fetchall()
            print(tabulate(telefono_perfil, headers=["Telefonos"], tablefmt= "fancygrid"))
            cur.execute(" SELECT  habilidad_perfil, COUNT(*) FROM validar WHERE id_perfil = {} GROUP BY habilidad_perfil".format(perfil[0]))
            habilidad = cur.fetchall()
            print(tabulate(habilidad, headers=["habilidades", "validaciones"], tablefmt= "fancygrid"))

            print("-----------------------------------")
            print("\t MENU PERFIL ")
            print("(1) EDITAR PERFIL")
            print("(2) SELECCIONAR NUEVA FOTO DE PERFIL")
            print("(3) VER HABILIDADES")
            print("(4) VER EXPERIENCIA LABORAL")
            print("(5) VER EDUCACION")
            print("(6) ELIMINAR CUENTA")
            print("(7) VOLVER")
            opcionperfil=raw_input("ingrese opcion:")
            if opcionperfil=="1":

                
                pass
            elif opcionperfil=="2":
                pass
            elif opcionperfil=="3":
                pass
            elif opcionperfil=="4":
                pass
            elif opcionperfil=="5":
                pass
            elif opcionperfil=="6":
                pass
            elif opcionperfil== "7":
                Bperfil = False
            else:
                 print("Opcion invalida")
                 


    elif opcion == "2": 
        pass
    elif opcion == "3":
        Boolnotiifcaciones = True
        while Boolnotiifcaciones:
            cur.execute("SELECT * from notificacion WHERE estado = 'no leido' and  id_perfil =  {} ".format(id))
            rows = cur.fetchall()
            c = 0
            print("NOTIFICIONES SIN LEER")
            print("--------------------------------------------")

            for i in rows:
                    c+= 1
                    print("(" + str(c)  + ") " +" IDN: " + str(i[0]) + "\t  " + str(i[2]) )
            print("--------------------------------------------")
            print("(1) VER NOTIFICACION")
            print("(2) SELECIONAR TODAS COMO LEIDAS")
            print("(3) VER NOTIFICACIONES LEIDAS")
            print("(4) VOLVER")
            opcionnotificaciones = raw_input("ingrese opcion: ")
            if opcionnotificaciones =="1":
                numero =int(raw_input("ingrese numero de notificacion:"))
                c = 0
                for i in rows:
                    c += 1
                    if (numero ==  c):
                        if i[2] == "solicitud":
                            
                            cur.execute("SELECT * FROM solicitud;")
                            tsolicitud = cur.fetchall()
                            for s in tsolicitud:
                                if s[3] == i[0]:
                                    print("\t NOTIFICACION")
                                    print("--------------------------------------------")
                                    print("La solicitud: " + str(s[3]) + "\nUsuario de amistad:" + s[1]   + "\nfecha: "  + str(s[4]) + "\n" + s[2]) 
                                    print("--------------------------------------------")
                                    cur.execute(("UPDATE notificacion SET  estado = 'leido' where id_notificacion = {}").format(i[0])) 
                                    conn.commit()        
                        elif i[2]== "'publicacion'":# son los de comentario
                            cur.execute("SELECT * FROM comentario WHERE id_comentario = {}  and estado ='Vigente'").format(i[0])
                            ncom = cur.fetchone()
                            print("\t NOTIFICACION")
                            print("--------------------------------------------")
                            print("La publicacion: " + str(ncom[2]) + "\nUsuario de comentario:" + str(ncom[1])   + "\ntexto: " + ncom[2] + "\nfecha: "  + str(ncom[5]) + "\n" + ncom[4]) 
                            print("--------------------------------------------")
                            cur.execute(("UPDATE notificacion SET  estado = 'leido' where id_notificacion = {}").format(i[0])) 
                            conn.commit()
                        elif i[2] == "'comentario'":
                            cur.execute("SELECT * FROM sub_comentario WHERE id_comentario = {}  and estado ='Vigente'").format(i[0])
                            nsubcom = cur.fetchone()
                            print("\t NOTIFICACION")
                            print("--------------------------------------------")
                            print("La publicacion: " + str(nsubcom[1]) + "\nUsuario de comentario:" + str(nsubcom[2])   + "\ntexto: " + nsubcom[3] + "\nfecha: "  + str(nsubcom[5]) + "\n" + nsubcom[4]) 
                            print("--------------------------------------------")
                            cur.execute(("UPDATE notificacion SET  estado = 'leido' where id_notificacion = {}").format(i[0])) 
                            conn.commit()

            elif opcionnotificaciones == "2":
                            cur.execute(("UPDATE notificacion SET estado =  'leido' WHERE id_perfil =  {} ").format(str(id)))
                            conn.commit()
            elif opcionnotificaciones == "3":
                cur.execute(("SELECT * from notificacion WHERE estado = 'leido' and  id_perfil =  {} ").format(str(id)))
                rowss = cur.fetchall()
                cc = 0
                print("NOTIFICIONES LEIDAS")
                print("--------------------------------------------")

                for i in rowss:
                        cc+= 1
                        print("(" + str(cc)  + ") " +" IDN: " + str(i[0]) + "\t  " + str(i[2]) )
                        print("---------------------------------------")
                numero =int(raw_input("ingrese numero de notificacion:"))
                cc = 0
                for i in rowss:
                    cc += 1
                    if (numero ==  cc):
                        if i[2] == "solicitud":
                            
                            cur.execute("SELECT * FROM solicitud;")
                            tsolicitud = cur.fetchall()
                            for s in tsolicitud:
                                if s[3] == i[0]:
                                    print("\t NOTIFICACION")
                                    print("--------------------------------------------")
                                    print("La solicitud: " + str(s[3]) + "\nUsuario de amistad:" + s[1]   + "\nfecha: "  + str(s[4]) + "\n" + s[2]) 
                                    print("--------------------------------------------")
                                        
                        elif i[2]== "'publicacion'":# son los de comentario
                            cur.execute("SELECT * FROM comentario WHERE id_comentario = {}  and estado ='Vigente'").format(i[0])
                            ncom = cur.fetchone()
                            print("\t NOTIFICACION")
                            print("--------------------------------------------")
                            print("La publicacion: " + str(ncom[2]) + "\nUsuario de comentario:" + str(ncom[1])   + "\ntexto: " + ncom[2] + "\nfecha: "  + str(ncom[5]) + "\n" + ncom[4]) 
                            print("--------------------------------------------")
                    
                        elif i[2] == "'comentario'":
                            cur.execute("SELECT * FROM sub_comentario WHERE id_comentario = {}  and estado ='Vigente'").format(i[0])
                            nsubcom = cur.fetchone()
                            print("\t NOTIFICACION")
                            print("--------------------------------------------")
                            print("La publicacion: " + str(nsubcom[1]) + "\nUsuario de comentario:" + str(nsubcom[2])   + "\ntexto: " + nsubcom[3] + "\nfecha: "  + str(nsubcom[5]) + "\n" + nsubcom[4]) 
                            print("--------------------------------------------")
            elif opcionnotificaciones == "4":
                Boolnotiifcaciones = False
            else:
                print("")
                    
    elif opcion == "4":
        pass
    elif opcion == "5":
        pass
    elif opcion == "6":
        TRUUEEE = False
    else :
        print("Opcion no valida! Intente nuevamente")
        continue






cur.close()




conn.close()