import psycopg2
import datetime  
import time 
from tabulate import tabulate

conn = psycopg2.connect(host = "201.238.213.114", port= "54321", database="grupo23", user="grupo23", password="f9kNXT")

def pasastring(stg):
    st = str("'" + stg + "'") 
    return st
 
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
            cur.execute("SELECT activo from usuario WHERE email = {};".format(str("'" + email + "'")))
            activo = cur.fetchone()
            usarioE = False
            while True:
                for i in rows:  
                    if i[0]==email and i[1] == contrasena and (activo[0] == True or activo[0] == None):                 
                        print("Sesion iniciada")
                        cur.execute(("SELECT id FROM perfil WHERE {} = email;").format(str("'" + email + "'")))
                        id = cur.fetchone()
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
                

    elif opcion=="2":
        cuenta=str(raw_input("Ingrese el email de la cuenta nueva: "))
        contrasena= raw_input("Ingrese contrasena: ")

        while 1:
            verificacion=raw_input("Ingrese nuevamente la contrasena: ")
            if contrasena!=verificacion:
                verificacion=raw_input("Ingrese nuevamente la contrasena dado que no coincide con la inicial:")
            else:
                break

        cur.execute("INSERT INTO usuario(email,activo) VALUES({}, 'true');".format(str("'" + cuenta +"'")))    
        conn.commit()    
        cur.close()
        
        fecha=datetime.date.today()
        
        cur=conn.cursor()
        cur.execute(("INSERT INTO clave(email_usuario,clave,fecha) VALUES(%s,%s,%s);"), (cuenta,verificacion,str(fecha)))
        conn.commit()


    elif opcion=="3":
        #como la fecha es de tipo date hay un detalle cuando se cambia la clave el mismo dia que otrs
        email = raw_input("ingrese su email: ")
        cur.execute("SELECT * FROM clave ORDER BY fecha DESC")
        rows = cur.fetchall()
        row = cur.execute("SELECT clave from clave WHERE email_usuario = {}".format(str("'" +email+"'")))
        print(email)
        print(row)
        for i in rows:
            if i[0] == email:
                print("mail encontrado")
                print("su contrasena es:"+ str(i[1]))
                break 
        clave =raw_input("ingrese nueva clave:")   
        fechaa = datetime.date.today()
        while True:
            rows = cur.execute("SELECT clave from clave WHERE email_usuario = {}".format(str("'" +email+"'")))
            print(rows)
            if clave not in rows:
                cur.execute("INSERT INTO clave(email_usuario,clave,fecha) VALUES(%s,%s,%s);" , (email,clave,str(fechaa)))
                conn.commit()
                print(clave)
                break
            else:
                print("Clave no valida intenetenuevamente!")
                clave =raw_input("Ingrese nueva clave: ")
 
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
                while True:
                    print("(1) Cambiar nombre")
                    print("(2) Cambiar apellido")
                    print("(3) Cambiar sexo")
                    print("(4) Cambiar pais")
                    print("(5) Cambiar descripcion")
                    print("(6) VOLVER")
                    cambioperfil =raw_input("ingrese una opcion: ")
                    if cambioperfil == "1":
                        name = raw_input("ingrese nuevo nombre: ")
                        cur.execute("UPDATE perfil SET nombre = {} WHERE id = {};".format(str("'" + name +"'" ) , id[0]))
                        conn.commit()
                        break
                    elif cambioperfil == "2":
                        lastn = raw_input("ingrese nuevo apellido: ")
                        cur.execute("UPDATE perfil SET apellido = {} WHERE id = {};".format(str("'" + lastn +"'" ) , id[0]))
                        conn.commit()
                        break
                    elif cambioperfil == "3":
                        if perfil[4] == "Masculino":
                            sexo = "Femenino"
                        else:
                            sexo = "Masculino"
                        cur.execute("UPDATE perfil SET genero = {} WHERE id = {};".format(str("'" + sexo +"'" ) , id[0]))
                        conn.commit()
                        break
                    elif cambioperfil == "4":
                        pais = raw_input("ingrese nuevo pais: ")
                        cur.execute("UPDATE perfil SET pais = {} WHERE id = {};".format(str("'" + pais +"'" ) , id[0]))
                        conn.commit()
                        break
                    elif cambioperfil == "5":
                        desc = raw_input("ingrese nuevo descripcion: ")
                        cur.execute("UPDATE perfil SET descripcion = {} WHERE id = {};".format(str("'" + desc +"'" ) , id[0]))
                        conn.commit()
                        break
                    elif cambioperfil == "6":
                        break
                    else:
                        print("opcion incorrecta! Intente nuevamente")
                
                pass
            elif opcionperfil=="2":
                foto = raw_input("ingrese foto(.png) :")
                cur.execute("INSERT INTO Foto_perfil(id_perfil, foto)VALUES ({},{});".format(id[0], str("'" +foto + "'" )))
                
            elif opcionperfil=="3":
                while True:
                    cur.execute(" SELECT  habilidad, descripcion  FROM habilidad WHERE id_perfil = {}  ORDER BY habilidad".format(perfil[0]))
                    habilidad = cur.fetchall()
                    cur.execute("SELECT habilidad_perfil , COUNT(*) FROM validar WHERE id_perfil = {} GROUP BY habilidad_perfil ORDER BY habilidad_perfil".format(perfil[0]))
                    validation = cur.fetchall()
                    count = 1
                    hab =[]
                    for hh in habilidad:
                        func = True
                        for val in validation:
                            if hh[0] in val:
                                hab.append([count, val[0], val[1]])
                                count +=1
                                func = False
                                break
                        if func:
                            hab.append([count,hh[0], 0])
                            count += 1
                    print(tabulate(hab, headers=["numero", "habilidades", "validaciones"], tablefmt= "fancygrid"))
                    print("(1) VER HABILIDAD")
                    print("(2) AGREGAR HABILIDAD")
                    print("(3) ELIMINAR HABILIDAD")
                    print("(4) VOLVER")
                    opcionhabilidad = raw_input("ingrese una opcion:")
                    if opcionhabilidad == "1":
                        numh = int(raw_input("ingrese numero de habilidad: "))
                        print("NOMBRE habilidad: " + hab[numh-1][1] +" \ndescricion: " + habilidad[numh-1][1] )
                        cur.execute(" SELECT habilidad_perfil, email_usuario_valida FROM validar  WHERE id_perfil = {} and habilidad_perfil = {}".format(perfil[0], str("'" +  hab[numh-1][1] + "'")))
                        emails = cur.fetchall()
                        if emails == []:
                            print("NO TIENE VALIDACIONES")
                        else:
                            print(tabulate(emails, headers=[ "habilidad", "usuario que valido"], tablefmt= "fancygrid"))
                    elif opcionhabilidad == "2":
                        nuevahab = raw_input("ingrese  nombre de una nueva habilidad: ")
                        deschab = raw_input("ingrse descripcion de esta: ")
                        nuevahab = str("'" + nuevahab + "'")
                        deschab = str("'" + deschab + "'" ) 
                        cur.execute("INSERT INTO Habilidad(id_perfil,habilidad,descripcion) VALUES ({},{},{})".format(perfil[0],nuevahab, deschab ))
                        conn.commit()
                    elif opcionhabilidad == "3":
                        ophabilidad = int(raw_input("ingrese numero de habilidad: "))
                        for h in hab:
                            if ophabilidad == h[0]:
                                cur.execute("DELETE  from  validar WHERE id_perfil = {} and habilidad_perfil = {}".format(id[0], str("'"+h[1]+"'")))
                                conn.commit()
                                cur.execute("DELETE  from habilidad WHERE id_perfil = {} and habilidad = {}".format(id[0], str("'"+h[1]+"'")))
                                conn.commit()
                                

                    elif opcionhabilidad == "4":
                        break              
                    else:
                        print("Opcion incorrecta!") 

                
                pass
            elif opcionperfil=="4":


                #aquii
                pass
            elif opcionperfil=="5":
                while True:
                    cur.execute("SELECT * FROM  estudio  WHERE id_perfil = {}".format(perfil[0]))
                    estudio = cur.fetchall()
                    c = 1
                    estu =[]
                    print("\tESTUDIOS")
                    for e in estudio:
                        estu.append([c, e[0], e[1], e[2], e[3], e[4], e[5]])
                        print("(" + str(c) + ")  " + e[3] + " en " + e[1])
                        c += 1
                    print("------------------------")
                    print("(1) VER EDUCACION")
                    print("(2) AGREGAR EDUCACION")
                    print("(3) ELIMINAR EDUCACION")
                    print("(4) VOLVER")
                    print("------------------")
                    opcionestudio = raw_input("Ingrese una opcion: ")
                    if opcionestudio == "1":
                        numero_estudio = int(raw_input("ingrese un numero de la educacion: "))
                        for es in estu:
                            if numero_estudio ==  es[0]:
                                print("nombre institucion: " + es[2] + "\ngrado academico: " + es[3] + "\nestudio: " + es[4] +
                                 "\nfecha de inicio: " + str(es[5]) + "\nfecha de fin: " + str(es[6]))

                    elif opcionestudio == "2":
                        cur.execute("SELECT  * from institucion")
                        instituciones = cur.fetchall()
                        institucion = []
                        c=1
                        for ins in instituciones:
                            institucion.append([c, ins[0], ins[1], ins[2] , ins[3]])
                            print("(" + str(c) + ") " + ins[0])
                            c += 1
                        numinst= int(raw_input("Ingrese un numero de una institucion: "))
                        for insti in institucion:
                            if numinst == insti[0]:
                                grado = raw_input("Ingrese grado academico: ")
                                descripcion = raw_input("Ingrese estudio: ")
                                fecha_inicio = raw_input("ingrese fecha de inicio(YY-MM-DD): ")
                                fecha_termino = raw_input("ingrese fecha de fin(YY-MM-DD): ") 
                                cur.execute("INSERT INTO Estudio(id_perfil,nombre_institucion,grado_academico,descripcion,fecha_inicio,fecha_fin) VALUES ({},'{}','{}','{}','{}','{}');".format(perfil[0], insti[1], grado, descripcion,fecha_inicio,fecha_termino))
                                conn.commit()

                    elif opcionestudio == "3":
                        opcionestudio = raw_input("Ingrese numero de estudio")
                        for est in estu:
                            if opcionestudio == str(est[0]):
                                cur.execute("DELETE  FROM  estudio WHERE id_perfil = {} and nombre_institucion = {} and grado_academico = {}". format(perfil[0],str("'"+est[2]+"'"),str("'"+est[3]+"'") ))
                                conn.commit()
                        
                    elif opcionestudio == "4":
                        break
                    else:
                        print("Opcion incorrecta! Intente nuevamente!")

            elif opcionperfil=="6":
                print("seguro desea borrar la cuenta (1)SI (2)NO :")
                borrar = raw_input()
                if borrar == "1":
                    cur.execute("UPDATE usuario SET activo = false  WHERE email = {};".format(str("'"+perfil[1]+"'")))
                    conn.commit()
                    TRUUEEE = False
                    break
                else:
                    break

                
            elif opcionperfil== "7":
                Bperfil = False
            else:
                 print("Opcion invalida")

    elif opcion == "2":
        Bpublicacion = True
        while Bpublicacion:
            print("(1) CREAR PUBLICACION")
            print("(2) MIS PUBLICACIONES")
            print("(3) OTRAS PUBLICACIONES")
            print("(4) VOLVER")
            opcionpublicacion = raw_input("Ingrese una opcion: ")
            if opcionpublicacion == "1":
                priv = raw_input("quiere que la publicacion sea privada? (1)SI (2)NO ")
                if priv == "1":
                    privada = "'Privado'"
                else:
                    privada = "'Publico'"
                cont = raw_input("Ingrese contenido de la publicacion(MAX 100 chr): ")
                estado = "'Activo'"
                cont = "'" +cont + "'"
                fechapubli = "'" + str(datetime.date.today()) + "'"
                cur.execute("SELECT id_publicacion  from publicacion;")
                idp = cur.fetchall()
                ids = []
                for ij in idp:
                    ids.append(ij[0])
                id_publicacion = 1
                while id_publicacion in ids:
                    id_publicacion +=1 
                cur.execute("INSERT INTO Publicacion(id_publicacion,id_usuario,privacidad,contenido,fecha,estado) VALUES ({},{},{},{},{},{});".format(id_publicacion,id[0],privada,cont,fechapubli,estado))
                conn.commit()
            elif opcionpublicacion == "2":
                while True:
                    cur.execute("SELECT id_publicacion, contenido from publicacion WHERE id_usuario = {} and estado = 'Activo'".format(id[0]))
                    publicaciones = cur.fetchall()
                    print(tabulate(publicaciones, headers=["id_publicacion", "publicacion"], tablefmt= "fancygrid"))
                    npubli = int(raw_input("Ingrese id de publicacion: "))
                    cur.execute("SELECT id_comentario, texto from comentario WHERE  estado = 'Vigente' and id_publicacion = {};".format(npubli))
                    coment = cur.fetchall()
                    print(tabulate(coment, headers=["id_comentario", "comentario"], tablefmt= "fancygrid"))
                    print("(0) COMENTAR COMENTARIO")
                    print("(1) COMENTAR PUBLICACION")
                    print("(2) ELIMINAR COMENTARIO")
                    print("(3) EDITAR PUBLICACION")
                    print("(4) ELIMINAR PUBLICACION")
                    print("(5) VOLVER")
                    opmispubli = raw_input("Ingrese una opcion: ")
                    if opmispubli =="0":
                        numcomen = int(raw_input("ingrese id de comentario: "))
                        for nc in coment:
                            if numcomen == nc[0]:
                                break
                        copucha = raw_input("COMENTE(300 max): ")
                        copucha = str("'" +copucha + "'")
                        fehcahd = "'" +str(datetime.date.today()) +"'"
                        cur.execute("SELECT id_sub_comentario  from sub_comentario;")
                        idc = cur.fetchall()
                        ids = []
                        for ij in idc:
                            ids.append(ij[0])
                        id_sub_comentario = 1
                        vigente = "'Vigente'"
                        while id_sub_comentario in ids:
                            id_sub_comentario += 1
                        cur.execute("INSERT INTO Sub_Comentario(id_sub_comentario,id_comentario,id_usuario,texto,fecha,estado) VALUES ({},{},{},{},{},{})".format(id_sub_comentario,numcomen,id[0],copucha,fehcahd,vigente))
                        conn.commit()
                        break
                    elif opmispubli == "1":
                        copucha = raw_input("COMENTE(300 max): ")
                        copucha = str("'" +copucha + "'")
                        fehcahd = "'" +str(datetime.date.today()) +"'"
                        cur.execute("SELECT id_comentario  from comentario;")

                        idc = cur.fetchall()
                        ids = []
                        for ij in idc:
                            ids.append(ij[0])
                        id_comentario = 1
                        vigente = "'Vigente'"
                        while id_comentario in ids:
                            id_comentario += 1
                        cur.execute("SELECT id_notificacion  from notificacion;")
                        idn= cur.fetchall()
                        ids = []
                        for ij in idn:
                            ids.append(ij[0])
                        id_notificacion = 1
                        vigente = "'Vigente'"
                        while id_notificacion in ids:
                            id_notificacion += 1
                        cur.execute("INSERT INTO Comentario(id_comentario,id_usuario,id_publicacion,texto,fecha,estado) VALUES ({},{},{},{},{},{});".format(id_comentario, id[0],npubli, copucha,fehcahd ,vigente))
                        cur.execute("INSERT INTO notificacion(id_notificacion, estado, tipo_notificacion, id_perfil)VALUES ({}, 'no leido', 'publicacion', {});".format(id_notificacion,id[0]))
                        conn.commit()
                        break
                    elif opmispubli == "2":
                        elincom = int(raw_input("ingrese id de comentario que desea eliminar: "))
                        for cc in coment:
                            if elincom == cc[0]:
                                break
                        cur.execute("UPDATE sub_comentario SET estado = 'Borrado' WHERE id_comentario = {}".format(elincom))
                        cur.execute("UPDATE comentario SET estado = 'Borrado' WHERE id_comentario = {}".format(elincom))
                        conn.commit()

                    elif opmispubli == "3":
                        cur.execute("SELECT *  FROM publicacion WHERE id_publicacion = {}".format(npubli))
                        cambio = cur.fetchone()
                        print("(1) CAMBIAR PRIVACIDAD")
                        print("(2) CAMBIAR CONTENIDO")
                        edipubli = raw_input("Ingrese una opcion: ")
                        if edipubli == "1":
                            if cambio[2] == "Privado":
                                priva = "'Publico'"
                            else:
                                priva = "'Privado'"
                            cur.execute("UPDATE publicacion SET privacidad = {} WHERE id_publicacion = {}".format(priva,npubli))
                            conn.commit()

                        elif edipubli == "2":
                            copu= raw_input("Ingrese nuevo texto: ")
                            copu = "'" + copu + "'"
                            cur.execute("UPDATE publicacion SET contenido = {} WHERE id_publicacion = {}".format(copu,npubli))
                            conn.commit()

                    elif opmispubli == "4":
                        cur.execute("UPDATE publicacion SET estado = 'Borrado' WHERE id_publicacion = {}".format(npubli))
                        conn.commit()
                    elif opmispubli == "5":
                        break
                    else:
                        print("Opcion incorrecta! Intente nuevamente!")
            elif opcionpublicacion == "3":
                while True:
                    cur.execute("SELECT DISTINCT p.id_publicacion, p.contenido  FROM publicacion p, (SELECT DISTINCT id_empresa as i  FROM postulacion WHERE id_perfil = {} )t1 WHERE i = p.id_usuario".format(id[0]))
                    idsd= []
                    idempre = cur.fetchall()
                    for ii in idempre:
                        idsd.append(ii[0], ii[1])
                    cur.execute("SELECT  DISTINCT p.id_publicacion, p.contenido  FROM publicacion p, (SELECT id_empresa as i FROM trabaja WHERE id_trabajador = {})t1 WHERE i = p.id_usuario".format(id[0]))
                    idmpre= cur.fetchall()
                    for ii in idmpre:
                        idsd.append(ii[0],ii[1])
                    cur.execute("SELECT  DISTINCT p.id_publicacion, p.contenido FROM publicacion p ,(SELECT e.id as id FROM perfil e, (SELECT email_usuario_amistad as i FROM solicitud WHERE email_usuario = {})t1  WHERE i = e.email)t2 WHERE id = p.id_usuario ".format(str("'"+email+"'")))
                    idams = cur.fetchall()
                    for ii in idams:
                        idsd.append(ii[0],ii[1])
                    print(tabulate(idsd, headers=["id publicacion", "contenido"], tablefmt= "fancygrid"))
                    print("(1) COMENTAR PUBLICACION")
                    print("(2) COMENTAR COMENTARIO")
                    print("(3) ELIMINAR COMENTARIO")
                    print("(4) VOLVER")
                    opccc = raw_input("Ingrese una opcion")
                    if opccc== "1":
                        npubli = int(raw_input("Ingrese id de publicacion: "))
                        copucha = raw_input("COMENTE(300 max): ")
                        copucha = str("'" +copucha + "'")
                        fehcahd = "'" +str(datetime.date.today()) +"'"
                        cur.execute("SELECT id_comentario  from comentario;")
                        idc = cur.fetchall()
                        ids = []
                        for ij in idc:
                            ids.append(ij[0])
                        id_comentario = 1
                        vigente = "'Vigente'"
                        while id_comentario in ids:
                            id_comentario += 1
                        cur.execute("SELECT id_notificacion  from notificacion;")
                        idn= cur.fetchall()
                        ids = []
                        for ij in idn:
                            ids.append(ij[0])
                        id_notificacion = 1
                        vigente = "'Vigente'"
                        while id_notificacion in ids:
                            id_notificacion += 1
                        cur.execute("INSERT INTO Comentario(id_comentario,id_usuario,id_publicacion,texto,fecha,estado) VALUES ({},{},{},{},{},{});".format(id_comentario, id[0],npubli, copucha,fehcahd ,vigente))
                        cur.execute("INSERT INTO notificacion(id_notificacion, estado, tipo_notificacion, id_perfil)VALUES ({}, 'no leido', 'publicacion', {});".format(id_notificacion,id[0]))
                        conn.commit()
                    
                    elif opccc == "2":
                        npubli = int(raw_input("Ingrese id de publicacion: "))
                        cur.execute("SELECT id_comentario, texto from comentario WHERE  estado = 'Vigente' and id_publicacion = {};".format(npubli))
                        coment = cur.fetchall()
                        print(tabulate(coment, headers=["id_comentario", "comentario"], tablefmt= "fancygrid"))
                        numcomen = int(raw_input("ingrese id de comentario: "))
                        for nc in coment:
                            if numcomen == nc[0]:
                                break
                        copucha = raw_input("COMENTE(300 max): ")
                        copucha = str("'" +copucha + "'")
                        fehcahd = "'" +str(datetime.date.today()) +"'"
                        cur.execute("SELECT id_sub_comentario  from sub_comentario;")
                        idc = cur.fetchall()
                        ids = []
                        for ij in idc:
                            ids.append(ij[0])
                        id_sub_comentario = 1
                        vigente = "'Vigente'"
                        while id_sub_comentario in ids:
                            id_sub_comentario += 1
                        cur.execute("INSERT INTO Sub_Comentario(id_sub_comentario,id_comentario,id_usuario,texto,fecha,estado) VALUES ({},{},{},{},{},{})".format(id_sub_comentario,numcomen,id[0],copucha,fehcahd,vigente))
                        conn.commit()
                    elif opccc == "3":
                        npubli = int(raw_input("Ingrese id de publicacion: "))
                        cur.execute("SELECT id_comentario, texto from comentario WHERE  estado = 'Vigente' and id_publicacion = {};".format(npubli))
                        coment = cur.fetchall()
                        print(tabulate(coment, headers=["id_comentario", "comentario"], tablefmt= "fancygrid"))
                        elincom = int(raw_input("ingrese id de comentario que desea eliminar: "))
                        for cc in coment:
                            if elincom == cc[0]:
                                break
                        cur.execute("UPDATE sub_comentario SET estado = 'Borrado' WHERE id_comentario = {}".format(elincom))
                        cur.execute("UPDATE comentario SET estado = 'Borrado' WHERE id_comentario = {}".format(elincom))
                        conn.commit()

                    elif opccc == "4":
                        break
                    else:
                        print("Opcion incorrecta! Intente nuevamente")  
 
            elif opcionpublicacion == "4":
                break
            else:
                print("opcion incorrecta!")

        
    elif opcion == "3":
        Boolnotiifcaciones = True
        while Boolnotiifcaciones:
            cur.execute("SELECT * from notificacion WHERE estado = 'no leido' and  id_perfil =  {} ".format(id[0]))
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
                        elif i[2]== "publicacion":# son los de comentario
                            cur.execute("SELECT * FROM comentario WHERE id_comentario = {}  and estado ='Vigente'").format(i[0])
                            ncom = cur.fetchone()
                            print("\t NOTIFICACION")
                            print("--------------------------------------------")
                            print("La publicacion: " + str(ncom[2]) + "\nUsuario de comentario:" + str(ncom[1])   + "\ntexto: " + ncom[2] + "\nfecha: "  + str(ncom[5]) + "\n" + ncom[4]) 
                            print("--------------------------------------------")
                            cur.execute(("UPDATE notificacion SET  estado = 'leido' where id_notificacion = {}").format(i[0])) 
                            conn.commit()
                        elif i[2] == "comentario":
                            cur.execute("SELECT * FROM sub_comentario WHERE id_comentario = {}  and estado ='Vigente'").format(i[0])
                            nsubcom = cur.fetchone()
                            print("\t NOTIFICACION")
                            print("--------------------------------------------")
                            print("La publicacion: " + str(nsubcom[1]) + "\nUsuario de comentario:" + str(nsubcom[2])   + "\ntexto: " + nsubcom[3] + "\nfecha: "  + str(nsubcom[5]) + "\n" + nsubcom[4]) 
                            print("--------------------------------------------")
                            cur.execute(("UPDATE notificacion SET  estado = 'leido' where id_notificacion = {}").format(i[0])) 
                            conn.commit()          
            elif opcionnotificaciones == "2":
                            cur.execute(("UPDATE notificacion SET estado =  'leido' WHERE id_perfil =  {} ").format(str(id[0])))
                            conn.commit()
            elif opcionnotificaciones == "3":
                cur.execute(("SELECT * from notificacion WHERE estado = 'leido' and  id_perfil =  {} ").format(str(id[0])))
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