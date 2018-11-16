import psycopg2
import datetime
import time
from tabulate import tabulate
import matplotlib.pyplot as plt

conn = psycopg2.connect(host="201.238.213.114", port="54321", database="grupo23", user="grupo23", password="f9kNXT")


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

    opcion = raw_input("ingrese una opcion: ")
    noEncontroE = True
    trutru = False
    if opcion == "1":
        email = raw_input("ingrese su email: ")
        contrasena = raw_input("ingtrese su contrasena: ")

        cur.execute(("SELECT  * FROM clave WHERE {} = email_usuario ORDER BY fecha DESC LIMIT 1;  ").format(
            str("'" + email + "'")))
        rows = cur.fetchall()
        cur.execute("SELECT activo from usuario WHERE email = {};".format(str("'" + email + "'")))
        activo = cur.fetchone()
        usarioE = False
        while True:
            for i in rows:
                if i[0] == email and i[1] == contrasena and activo[0] == True:
                    print("Sesion iniciada")
                    cur.execute(("SELECT id FROM perfil WHERE {} = email;").format(str("'" + email + "'")))
                    id = cur.fetchone()
                    if id == None:
                        id = []
                        id.append(70)
                    usarioE = True
                    break
            if usarioE == False:
                print(" mail o contrasena invalida")
                break
            else:
                main = False
                break


    elif opcion == "2":
        cuenta = str(raw_input("Ingrese el email de la cuenta nueva: "))
        contrasena = raw_input("Ingrese contrasena: ")

        while 1:
            verificacion = raw_input("Ingrese nuevamente la contrasena: ")
            if contrasena != verificacion:
                verificacion = raw_input("Ingrese nuevamente la contrasena dado que no coincide con la inicial:")
            else:
                break

        cur.execute("INSERT INTO usuario(email, activo) VALUES({},{});".format(str("'" + cuenta + "'"), "'t'"))
        conn.commit()
        cur.close()

        fecha = datetime.date.today()

        cur = conn.cursor()
        cur.execute(("INSERT INTO clave(email_usuario,clave,fecha) VALUES(%s,%s,%s);"),
                    (cuenta, verificacion, str(fecha)))
        conn.commit()

    elif opcion=="3":
        #como la fecha es de tipo date hay un detalle cuando se cambia la clave el mismo dia que otrs
        email = raw_input("ingrese su email: ")
        cur.execute("SELECT * FROM clave ORDER BY fecha DESC")
        rows = cur.fetchall()
        for i in rows:
            if i[0] == email:
                print("mail encontrado")
                print("su contrasena es:"+ str(i[1]))
                break 
        claves_antiguas = []
        for i in rows:
            if i[0] == email:
                claves_antiguas.append(i[1])
        clave =raw_input("ingrese nueva clave:")   
        fechaa = datetime.date.today()
        while True:
            if clave not in claves_antiguas:
                cur.execute("INSERT INTO clave(email_usuario,clave,fecha) VALUES(%s,%s,%s);" , (email,clave,str(fechaa)))
                conn.commit()
                print(clave)
                break
            else:
                print("Clave no valida intenetenuevamente!")
                clave =raw_input("Ingrese nueva clave: ")

    elif opcion == "4":
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
    print("(7) INFORMACION")
    opcion = raw_input("ingrese una opcion: ")

    if opcion == "1":
        Bperfil = True
        while Bperfil:
            cur.execute("SELECT * FROM perfil WHERE email = {} ".format(str("'" + email + "'")))
            perfil = cur.fetchone()
            print("--------------------------------------")
            print("ID: " + str(perfil[0]) + "\nemail: " + perfil[1] + "\nnombre completo: " + perfil[2] + " " + perfil[
                3] + "\ngenero: " + perfil[4] +
                  "\nfecha de nacimiento: " + str(perfil[5]) + "\npais: " + perfil[6] + "\ndescripcion: " + perfil[7])
            cur.execute(" SELECT * FROM estudio WHERE id_perfil = {}".format(perfil[0]))
            educacion = cur.fetchone()
            cur.execute(" SELECT * FROM trabaja WHERE id_trabajador = {}".format(perfil[0]))
            experiencia = cur.fetchone()
            cur.execute(" SELECT foto FROM foto_perfil WHERE id_perfil = {}".format(perfil[0]))
            foto_perfil = cur.fetchall()
            print(tabulate(foto_perfil, headers=["Fotos"], tablefmt="fancygrid"))
            cur.execute(" SELECT telefono FROM telefono_perfil WHERE id_perfil = {}".format(perfil[0]))
            telefono_perfil = cur.fetchall()
            print(tabulate(telefono_perfil, headers=["Telefonos"], tablefmt="fancygrid"))
            cur.execute(
                " SELECT  habilidad_perfil, COUNT(*) FROM validar WHERE id_perfil = {} GROUP BY habilidad_perfil".format(
                    perfil[0]))
            habilidad = cur.fetchall()
            cur.execute(("SELECT  * FROM perfil WHERE {} = email ;  ").format(str("'" + email + "'")))
            row = cur.fetchall()
            print(tabulate(habilidad, headers=["habilidades", "validaciones"], tablefmt="fancygrid"))
            print("-----------------------------------")
            print("\t MENU PERFIL ")
            print("(1) EDITAR PERFIL")
            print("(2) SELECCIONAR NUEVA FOTO DE PERFIL")
            print("(3) VER HABILIDADES")
            print("(4) VER EXPERIENCIA LABORAL")
            print("(5) VER EDUCACION")
            print("(6) ELIMINAR CUENTA")
            print("(7) VOLVER")
            opcionperfil = raw_input("ingrese opcion:")
            if opcionperfil == "1":
                while True:
                    print("(1) Cambiar nombre")
                    print("(2) Cambiar apellido")
                    print("(3) Cambiar sexo")
                    print("(4) Cambiar pais")
                    print("(5) Cambiar descripcion")
                    print("(6) VOLVER")
                    cambioperfil = raw_input("ingrese una opcion: ")
                    if cambioperfil == "1":
                        name = raw_input("ingrese nuevo nombre: ")
                        cur.execute("UPDATE perfil SET nombre = {} WHERE id = {};".format(str("'" + name + "'"), id[0]))
                        conn.commit()
                        break
                    elif cambioperfil == "2":
                        lastn = raw_input("ingrese nuevo apellido: ")
                        cur.execute(
                            "UPDATE perfil SET apellido = {} WHERE id = {};".format(str("'" + lastn + "'"), id[0]))
                        conn.commit()
                        break
                    elif cambioperfil == "3":
                        if perfil[4] == "Masculino":
                            sexo = "Femenino"
                        else:
                            sexo = "Masculino"
                        cur.execute("UPDATE perfil SET genero = {} WHERE id = {};".format(str("'" + sexo + "'"), id[0]))
                        conn.commit()
                        break
                    elif cambioperfil == "4":
                        pais = raw_input("ingrese nuevo pais: ")
                        cur.execute("UPDATE perfil SET pais = {} WHERE id = {};".format(str("'" + pais + "'"), id[0]))
                        conn.commit()
                        break
                    elif cambioperfil == "5":
                        desc = raw_input("ingrese nuevo descripcion: ")
                        cur.execute(
                            "UPDATE perfil SET descripcion = {} WHERE id = {};".format(str("'" + desc + "'"), id[0]))
                        conn.commit()
                        break
                    elif cambioperfil == "6":
                        break
                    else:
                        print("opcion incorrecta! Intente nuevamente")

                pass
            elif opcionperfil == "2":
                foto = raw_input("ingrese foto(.png) :")
                cur.execute(
                    "INSERT INTO Foto_perfil(id_perfil, foto)VALUES ({},{});".format(id[0], str("'" + foto + "'")))

            elif opcionperfil == "3":
                while True:
                    cur.execute(
                        " SELECT  habilidad, descripcion  FROM habilidad WHERE id_perfil = {}  ORDER BY habilidad".format(
                            perfil[0]))
                    habilidad = cur.fetchall()
                    cur.execute(
                        "SELECT habilidad_perfil , COUNT(*) FROM validar WHERE id_perfil = {} GROUP BY habilidad_perfil ORDER BY habilidad_perfil".format(
                            perfil[0]))
                    validation = cur.fetchall()
                    count = 1
                    hab = []
                    for hh in habilidad:
                        func = True
                        for val in validation:
                            if hh[0] in val:
                                hab.append([count, val[0], val[1]])
                                count += 1
                                func = False
                                break
                        if func:
                            hab.append([count, hh[0], 0])
                            count += 1
                    print(tabulate(hab, headers=["numero", "habilidades", "validaciones"], tablefmt="fancygrid"))
                    print("(1) VER HABILIDAD")
                    print("(2) AGREGAR HABILIDAD")
                    print("(3) ELIMINAR HABILIDAD")
                    print("(4) VOLVER")
                    opcionhabilidad = raw_input("ingrese una opcion:")
                    if opcionhabilidad == "1":
                        numh = int(raw_input("ingrese numero de habilidad: "))
                        print("NOMBRE habilidad: " + hab[numh - 1][1] + " \ndescricion: " + habilidad[numh - 1][1])
                        cur.execute(
                            " SELECT habilidad_perfil, email_usuario_valida FROM validar  WHERE id_perfil = {} and habilidad_perfil = {}".format(
                                perfil[0], str("'" + hab[numh - 1][1] + "'")))
                        emails = cur.fetchall()
                        if emails == []:
                            print("NO TIENE VALIDACIONES")
                        else:
                            print(tabulate(emails, headers=["habilidad", "usuario que valido"], tablefmt="fancygrid"))
                    elif opcionhabilidad == "2":
                        nuevahab = raw_input("ingrese  nombre de una nueva habilidad: ")
                        deschab = raw_input("ingrse descripcion de esta: ")
                        nuevahab = str("'" + nuevahab + "'")
                        deschab = str("'" + deschab + "'")
                        cur.execute(
                            "INSERT INTO Habilidad(id_perfil,habilidad,descripcion) VALUES ({},{},{})".format(perfil[0],
                                                                                                              nuevahab,
                                                                                                              deschab))
                        conn.commit()
                    elif opcionhabilidad == "3":
                        ophabilidad = int(raw_input("ingrese numero de habilidad: "))
                        for h in hab:
                            if ophabilidad == h[0]:
                                cur.execute(
                                    "DELETE  from  validar WHERE id_perfil = {} and habilidad_perfil = {}".format(id[0],
                                                                                                                  str(
                                                                                                                      "'" +
                                                                                                                      h[
                                                                                                                          1] + "'")))
                                conn.commit()
                                cur.execute(
                                    "DELETE  from habilidad WHERE id_perfil = {} and habilidad = {}".format(id[0], str(
                                        "'" + h[1] + "'")))
                                conn.commit()


                    elif opcionhabilidad == "4":
                        break
                    else:
                        print("Opcion incorrecta!")

                pass
            elif opcionperfil == "4":
                while True:
                    cur.execute(("SELECT  * FROM perfil WHERE {} = email ;  ").format(str("'" + email + "'")))
                    row=cur.fetchall()
                    
                    cur.execute((
                                    "SELECT  e.nombre,t.puesto,t.fecha_de_inicio,t.fecha_fin,e.id FROM trabaja t, perfil p, empresa e WHERE t.id_trabajador=p.id AND e.id=t.id_empresa AND  {} = p.email ;  ").format(
                        str("'" + email + "'")))
                    row1 = cur.fetchall()
                    e = 0
                    for i in row1:
                        e += 1
                        print("(" + str(e) + ") " + row[0][2] + " a trabajado en " + i[0] + " en el puesto " + i[
                            1] + " desde " + i[2].strftime('%d/%m/%Y') + " hasta " + i[3].strftime('%d/%m/%Y'))

                    print("\t MENU EXPERIENCIA LABORAL ")
                    print("(1) VER EXPERIENCIA LABORAL")
                    print("(2) AGREGAR EXPERIENCIA LABORAL")
                    print("(3) ELIMINAR EXPERIENCIA LABORAL")
                    print("(4) VOLVER")
                    opcionexperiencialaboral = raw_input("Ingrese opcion:")
                    if opcionexperiencialaboral == "1":
                        experiencia = int(raw_input("Ingrese numero de experiencia:"))
                        e = 0
                        for i in row1:
                            e += 1
                            if experiencia == e:
                                cur.execute(("SELECT * FROM empresa WHERE nombre={} ;  ").format(str("'" + i[0] + "'")))
                                row10 = cur.fetchall()
                                print("Nombre trabajador :" + row[0][2])
                                print("trabajo en: " + i[0])
                                print("Ubicada en: " + row10[0][2])
                                print("Perteneciente al rubro: " + row10[0][4])
                                print("Creada en: " + row10[0][5] + " el " + row10[0][6].strftime('%d/%m/%Y'))
                                print("En el puesto: " + i[1])
                                print("Desde: " + i[2].strftime('%d/%m/%Y'))
                                print("Hasta: " + i[3].strftime('%d/%m/%Y'))

                    elif opcionexperiencialaboral == "2":
                        cur.execute("SELECT * FROM empresa;")
                        empresas = cur.fetchall()
                        print ("\t EMPRESAS DISPONIBLES ")
                        d = 0
                        for i in empresas:
                            d += 1
                            print("(" + str(d) + ") " + i[1])
                        print("\t MENU AGREGAR EXPERIENCIA LABORAL ")
                        print("(1) EXPERIENCIA LABORAL EN EMPRESA EXISTENTE")
                        print("(2) EXPERIENCIA LABORAL EN EMPRESA NUEVA")
                        crear = raw_input("Ingrese opcion: ")
                        if crear == "1":
                            opcioncrear = int(raw_input("Ingrese numero de empresa: "))
                            puesto = raw_input("Ingrese puesto de trabajo: ")

                            fechai = raw_input("Ingrese fecha de inicio(YY-MM-DD): ")
                            # print("\t FECHA FIN ")
                            # print("(1) TRABAJO ACTUAL")
                            # print("(2) TRABAJO TERMINADO")
                            # opcionfecha=raw_input("Ingrese opcion: ")
                            # if opcionfecha=="1":
                            #    fechaf=""
                            # elif opcionfecha=="2":

                            # fechaf=raw_input("Ingrese fecha de fin(YY-MM-DD): ")
                            fechaf = raw_input("Ingrese fecha de fin(YY-MM-DD): ")
                            d = 0
                            for i in empresas:
                                d += 1
                                if d == opcioncrear:
                                    cur.execute(
                                        "INSERT INTO trabaja(id_trabajador,id_empresa,puesto,fecha_de_inicio,fecha_fin) VALUES('{}','{}','{}','{}','{}');".format(
                                            row[0][0], i[0], puesto, fechai, fechaf))
                                    conn.commit()

                        elif crear == "2":
                            print("\t DATOS EMPRESA ")

                            idempresa = raw_input("Ingrese Id de la empresa(8 digitos): ")
                            nomempresa = raw_input("Ingrese nombre de la empresa: ")
                            dirempresa = raw_input("Ingrese direccion de la empresa: ")
                            desempresa = raw_input("Ingrese descripcion de la empresa: ")
                            rubempresa = raw_input("Ingrese rubro de la empresa: ")
                            paisempresa = raw_input("Ingrese pais de la empresa: ")
                            fecempresa = raw_input("Ingrese fecha de creacion de la empresa(YY-MM-DD): ")
                            cur.execute(
                                "INSERT INTO empresa(id,nombre,direccion,descripcion,pais,rubro,fecha_de_creacion) VALUES('{}','{}','{}','{}','{}','{}','{}');".format(
                                    idempresa, nomempresa, dirempresa, desempresa, rubempresa, paisempresa, fecempresa))
                            conn.commit()

                            puesto = raw_input("Ingrese puesto de trabajo: ")

                            fechai = raw_input("Ingrese fecha de inicio(YY-MM-DD): ")
                            fechaf = raw_input("Ingrese fecha de fin(YY-MM-DD): ")
                            cur.execute(
                                "INSERT INTO trabaja(id_trabajador,id_empresa,puesto,fecha_de_inicio,fecha_fin) VALUES('{}','{}','{}','{}','{}');".format(
                                    row[0][0], idempresa, puesto, fechai, fechaf))
                            conn.commit()

                    elif opcionexperiencialaboral == "3":
                        print("\t ELIMINAR EXPERIENCIA LABORAL ")
                        e = 0
                        for i in row1:
                            e += 1
                            print("(" + str(e) + ") " + row[0][2] + " a trabajado en " + i[0] + " en el puesto " + i[
                                1] + " desde " + i[2].strftime('%d/%m/%Y') + " hasta " + i[3].strftime('%d/%m/%Y'))
                        eliminar = int(raw_input("SELECCIONE EXPERIENCIA A ELIMINAR: "))
                        f = 0
                        for i in row1:
                            f += 1
                            if eliminar == f:
                                cur.execute(
                                    "DELETE FROM trabaja WHERE id_trabajador={} AND id_empresa={} AND puesto={};".format(
                                        row[0][0], i[4], "'" + i[1] + "'"))
                                conn.commit()
                    elif opcionexperiencialaboral == "4":
                        break
                    else:
                        print("Opcion incorrecta!")
            elif opcionperfil == "5":
                while True:
                    cur.execute("SELECT * FROM  estudio  WHERE id_perfil = {}".format(perfil[0]))
                    estudio = cur.fetchall()
                    c = 1
                    estu = []
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
                            if numero_estudio == es[0]:
                                print("nombre institucion: " + es[2] + "\ngrado academico: " + es[3] + "\nestudio: " +
                                      es[4] +
                                      "\nfecha de inicio: " + str(es[5]) + "\nfecha de fin: " + str(es[6]))

                    elif opcionestudio == "2":
                        cur.execute("SELECT  * from institucion")
                        instituciones = cur.fetchall()
                        institucion = []
                        c = 1
                        for ins in instituciones:
                            institucion.append([c, ins[0], ins[1], ins[2], ins[3]])
                            print("(" + str(c) + ") " + ins[0])
                            c += 1
                        numinst = int(raw_input("Ingrese un numero de una institucion: "))
                        for insti in institucion:
                            if numinst == insti[0]:
                                grado = raw_input("Ingrese grado academico: ")
                                descripcion = raw_input("Ingrese estudio: ")
                                fecha_inicio = raw_input("ingrese fecha de inicio(YY-MM-DD): ")
                                fecha_termino = raw_input("ingrese fecha de fin(YY-MM-DD): ")
                                cur.execute(
                                    "INSERT INTO Estudio(id_perfil,nombre_institucion,grado_academico,descripcion,fecha_inicio,fecha_fin) VALUES ({},'{}','{}','{}','{}','{}');".format(
                                        perfil[0], insti[1], grado, descripcion, fecha_inicio, fecha_termino))
                                conn.commit()

                    elif opcionestudio == "3":
                        opcionestudio = raw_input("Ingrese numero de estudio")
                        for est in estu:
                            if opcionestudio == str(est[0]):
                                cur.execute(
                                    "DELETE  FROM  estudio WHERE id_perfil = {} and nombre_institucion = {} and grado_academico = {}".format(
                                        perfil[0], str("'" + est[2] + "'"), str("'" + est[3] + "'")))
                                conn.commit()

                    elif opcionestudio == "4":
                        break
                    else:
                        print("Opcion incorrecta! Intente nuevamente!")

            elif opcionperfil == "6":
                print("seguro desea borrar la cuenta (1)SI (2)NO :")
                borrar = raw_input()
                if borrar == "1":
                    cur.execute(
                        "UPDATE usuario SET activo = false  WHERE email = {};".format(str("'" + perfil[1] + "'")))
                    conn.commit()
                    TRUUEEE = False
                    break
                else:
                    break


            elif opcionperfil == "7":
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
                cont = "'" + cont + "'"
                fechapubli = "'" + str(datetime.date.today()) + "'"
                cur.execute("SELECT id_publicacion  from publicacion;")
                idp = cur.fetchall()
                ids = []
                for ij in idp:
                    ids.append(ij[0])
                id_publicacion = 1
                while id_publicacion in ids:
                    id_publicacion += 1
                cur.execute(
                    "INSERT INTO Publicacion(id_publicacion,id_usuario,privacidad,contenido,fecha,estado) VALUES ({},{},{},{},{},{});".format(
                        id_publicacion, id[0], privada, cont, fechapubli, estado))
                conn.commit()
            elif opcionpublicacion == "2":
                while True:
                    cur.execute(
                        "SELECT id_publicacion, contenido from publicacion WHERE id_usuario = {} and estado = 'Activo'".format(
                            id[0]))
                    publicaciones = cur.fetchall()
                    print(tabulate(publicaciones, headers=["id_publicacion", "publicacion"], tablefmt="fancygrid"))
                    npubli = int(raw_input("Ingrese id de publicacion: "))
                    cur.execute(
                        "SELECT id_comentario, texto from comentario WHERE  estado = 'Vigente' and id_publicacion = {};".format(
                            npubli))
                    coment = cur.fetchall()
                    print(tabulate(coment, headers=["id_comentario", "comentario"], tablefmt="fancygrid"))
                    print("(0) COMENTAR COMENTARIO")
                    print("(1) COMENTAR PUBLICACION")
                    print("(2) ELIMINAR COMENTARIO")
                    print("(3) EDITAR PUBLICACION")
                    print("(4) ELIMINAR PUBLICACION")
                    print("(5) VOLVER")
                    opmispubli = raw_input("Ingrese una opcion: ")
                    if opmispubli == "0":
                        numcomen = int(raw_input("ingrese id de comentario: "))
                        for nc in coment:
                            if numcomen == nc[0]:
                                break
                        copucha = raw_input("COMENTE(300 max): ")
                        copucha = str("'" + copucha + "'")
                        fehcahd = "'" + str(datetime.date.today()) + "'"
                        cur.execute("SELECT id_sub_comentario  from sub_comentario;")
                        idc = cur.fetchall()
                        ids = []
                        for ij in idc:
                            ids.append(ij[0])
                        id_sub_comentario = 1
                        vigente = "'Vigente'"
                        while id_sub_comentario in ids:
                            id_sub_comentario += 1
                        cur.execute("SELECT id_notificacion  from notificacion;")
                        idn = cur.fetchall()
                        ids = []
                        for ij in idn:
                            ids.append(ij[0])
                        id_notificacion = 1
                        vigente = "'Vigente'"
                        while id_notificacion in ids:
                            id_notificacion += 1
                        cur.execute(
                            "INSERT INTO Sub_Comentario(id_sub_comentario,id_comentario,id_usuario,texto,fecha,estado) VALUES ({},{},{},{},{},{})".format(
                                id_sub_comentario, numcomen, id[0], copucha, fehcahd, vigente))
                        cur.execute(
                            "INSERT INTO notificacion(id_notificacion, estado, tipo_notificacion, id_perfil)VALUES ({}, 'no leido', 'comentario', {});".format(
                                id_notificacion, id[0]))
                        conn.commit()
                        break
                    elif opmispubli == "1":
                        copucha = raw_input("COMENTE(300 max): ")
                        copucha = str("'" + copucha + "'")
                        fehcahd = "'" + str(datetime.date.today()) + "'"
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
                        idn = cur.fetchall()
                        ids = []
                        for ij in idn:
                            ids.append(ij[0])
                        id_notificacion = 1
                        vigente = "'Vigente'"
                        while id_notificacion in ids:
                            id_notificacion += 1
                        cur.execute(
                            "INSERT INTO Comentario(id_comentario,id_usuario,id_publicacion,texto,fecha,estado) VALUES ({},{},{},{},{},{});".format(
                                id_comentario, id[0], npubli, copucha, fehcahd, vigente))
                        cur.execute(
                            "INSERT INTO notificacion(id_notificacion, estado, tipo_notificacion, id_perfil)VALUES ({}, 'no leido', 'publicacion', {});".format(
                                id_notificacion, id[0]))
                        conn.commit()
                        break
                    elif opmispubli == "2":
                        elincom = int(raw_input("ingrese id de comentario que desea eliminar: "))
                        for cc in coment:
                            if elincom == cc[0]:
                                break
                        cur.execute(
                            "UPDATE sub_comentario SET estado = 'Borrado' WHERE id_comentario = {}".format(elincom))
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
                            cur.execute("UPDATE publicacion SET privacidad = {} WHERE id_publicacion = {}".format(priva,
                                                                                                                  npubli))
                            conn.commit()

                        elif edipubli == "2":
                            copu = raw_input("Ingrese nuevo texto: ")
                            copu = "'" + copu + "'"
                            cur.execute(
                                "UPDATE publicacion SET contenido = {} WHERE id_publicacion = {}".format(copu, npubli))
                            conn.commit()

                    elif opmispubli == "4":
                        cur.execute(
                            "UPDATE publicacion SET estado = 'Borrado' WHERE id_publicacion = {}".format(npubli))
                        conn.commit()
                    elif opmispubli == "5":
                        break
                    else:
                        print("Opcion incorrecta! Intente nuevamente!")
            elif opcionpublicacion == "3":
                while True:
                    cur.execute(
                        "SELECT DISTINCT p.id_publicacion, p.contenido  FROM publicacion p, (SELECT DISTINCT id_empresa as i  FROM postulacion WHERE id_perfil = {} )t1 WHERE i = p.id_usuario".format(
                            id[0]))
                    idsd = []
                    idempre = cur.fetchall()
                    for ii in idempre:
                        idsd.append(ii[0], ii[1])
                    cur.execute(
                        "SELECT  DISTINCT p.id_publicacion, p.contenido  FROM publicacion p, (SELECT id_empresa as i FROM trabaja WHERE id_trabajador = {})t1 WHERE i = p.id_usuario".format(
                            id[0]))
                    idmpre = cur.fetchall()
                    for ii in idmpre:
                        idsd.append(ii[0], ii[1])
                    cur.execute(
                        "SELECT  DISTINCT p.id_publicacion, p.contenido FROM publicacion p ,(SELECT e.id as id FROM perfil e, (SELECT email_usuario_amistad as i FROM solicitud WHERE email_usuario = {})t1  WHERE i = e.email)t2 WHERE id = p.id_usuario ".format(
                            str("'" + email + "'")))
                    idams = cur.fetchall()
                    for ii in idams:
                        idsd.append(ii[0], ii[1])
                    print(tabulate(idsd, headers=["id publicacion", "contenido"], tablefmt="fancygrid"))
                    print("(1) COMENTAR PUBLICACION")
                    print("(2) COMENTAR COMENTARIO")
                    print("(3) ELIMINAR COMENTARIO")
                    print("(4) VOLVER")
                    opccc = raw_input("Ingrese una opcion")
                    if opccc == "1":
                        npubli = int(raw_input("Ingrese id de publicacion: "))
                        copucha = raw_input("COMENTE(300 max): ")
                        copucha = str("'" + copucha + "'")
                        fehcahd = "'" + str(datetime.date.today()) + "'"
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
                        idn = cur.fetchall()
                        ids = []
                        for ij in idn:
                            ids.append(ij[0])
                        id_notificacion = 1
                        vigente = "'Vigente'"
                        while id_notificacion in ids:
                            id_notificacion += 1
                        cur.execute(
                            "INSERT INTO Comentario(id_comentario,id_usuario,id_publicacion,texto,fecha,estado) VALUES ({},{},{},{},{},{});".format(
                                id_comentario, id[0], npubli, copucha, fehcahd, vigente))
                        cur.execute(
                            "INSERT INTO notificacion(id_notificacion, estado, tipo_notificacion, id_perfil)VALUES ({}, 'no leido', 'publicacion', {});".format(
                                id_notificacion, id[0]))
                        conn.commit()
                        break
                    elif opccc == "2":
                        npubli = int(raw_input("Ingrese id de publicacion: "))
                        cur.execute(
                            "SELECT id_comentario, texto from comentario WHERE  estado = 'Vigente' and id_publicacion = {};".format(
                                npubli))
                        coment = cur.fetchall()
                        print(tabulate(coment, headers=["id_comentario", "comentario"], tablefmt="fancygrid"))
                        numcomen = int(raw_input("ingrese id de comentario: "))
                        for nc in coment:
                            if numcomen == nc[0]:
                                break
                        copucha = raw_input("COMENTE(300 max): ")
                        copucha = str("'" + copucha + "'")
                        fehcahd = "'" + str(datetime.date.today()) + "'"
                        cur.execute("SELECT id_sub_comentario  from sub_comentario;")
                        idc = cur.fetchall()
                        ids = []
                        for ij in idc:
                            ids.append(ij[0])
                        id_sub_comentario = 1
                        vigente = "'Vigente'"
                        while id_sub_comentario in ids:
                            id_sub_comentario += 1
                        cur.execute("SELECT id_notificacion  from notificacion;")
                        idn = cur.fetchall()
                        ids = []
                        for ij in idn:
                            ids.append(ij[0])
                        id_notificacion = 1
                        vigente = "'Vigente'"
                        while id_notificacion in ids:
                            id_notificacion += 1
                        cur.execute(
                            "INSERT INTO Sub_Comentario(id_sub_comentario,id_comentario,id_usuario,texto,fecha,estado) VALUES ({},{},{},{},{},{})".format(
                                id_sub_comentario, numcomen, id[0], copucha, fehcahd, vigente))
                        cur.execute(
                            "INSERT INTO notificacion(id_notificacion, estado, tipo_notificacion, id_perfil)VALUES ({}, 'no leido', 'comentario', {});".format(
                                id_notificacion, id[0]))
                        conn.commit()
                        break
                    elif opccc == "3":
                        npubli = int(raw_input("Ingrese id de publicacion: "))
                        cur.execute(
                            "SELECT id_comentario, texto from comentario WHERE  estado = 'Vigente' and id_publicacion = {};".format(
                                npubli))
                        coment = cur.fetchall()
                        print(tabulate(coment, headers=["id_comentario", "comentario"], tablefmt="fancygrid"))
                        elincom = int(raw_input("ingrese id de comentario que desea eliminar: "))
                        for cc in coment:
                            if elincom == cc[0]:
                                break
                        cur.execute(
                            "UPDATE sub_comentario SET estado = 'Borrado' WHERE id_comentario = {}".format(elincom))
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
                c += 1
                print("(" + str(c) + ") " + " IDN: " + str(i[0]) + "\t  " + str(i[2]))
            print("--------------------------------------------")
            print("(1) VER NOTIFICACION")
            print("(2) SELECIONAR TODAS COMO LEIDAS")
            print("(3) VER NOTIFICACIONES LEIDAS")
            print("(4) VOLVER")
            opcionnotificaciones = raw_input("ingrese opcion: ")
            if opcionnotificaciones == "1":
                numero = int(raw_input("ingrese numero de notificacion:"))
                c = 0
                for i in rows:
                    c += 1
                    if (numero == c):
                        if i[2] == "solicitud":

                            cur.execute("SELECT * FROM solicitud;")
                            tsolicitud = cur.fetchall()
                            for s in tsolicitud:
                                if s[3] == i[0]:
                                    print("\t NOTIFICACION")
                                    print("--------------------------------------------")
                                    print("La solicitud: " + str(s[3]) + "\nUsuario de amistad:" + s[
                                        1] + "\nfecha: " + str(s[4]) + "\n" + s[2])
                                    print("--------------------------------------------")
                                    cur.execute(
                                        ("UPDATE notificacion SET  estado = 'leido' where id_notificacion = {}").format(
                                            i[0]))
                                    conn.commit()
                        elif i[2] == "publicacion":  # son los de comentario
                            cur.execute(
                                "SELECT * FROM comentario WHERE id_comentario = {}  and estado ='Vigente'".format(i[0]))
                            ncom = cur.fetchone()
                            print("\t NOTIFICACION")
                            print("--------------------------------------------")
                            print("La publicacion: " + str(ncom[2]) + "\nUsuario de comentario:" + str(
                                ncom[1]) + "\ntexto: " + str(ncom[3]) + "\nfecha: " + str(ncom[5]) + "\n" + str(ncom[4]))
                            print("--------------------------------------------")
                            cur.execute(
                                ("UPDATE notificacion SET  estado = 'leido' where id_notificacion = {}").format(i[0]))
                            conn.commit()
                        elif i[2] == "comentario":
                            cur.execute(
                                "SELECT * FROM sub_comentario WHERE id_comentario = {}  and estado ='Vigente'".format(
                                i[0]))
                            nsubcom = cur.fetchone()
                            print("\t NOTIFICACION")
                            print("--------------------------------------------")
                            print("La publicacion: " + str(nsubcom[1]) + "\nUsuario de comentario:" + str(
                                nsubcom[2]) + "\ntexto: " + nsubcom[3] + "\nfecha: " + str(nsubcom[5]) + "\n" + nsubcom[
                                      4])
                            print("--------------------------------------------")
                            cur.execute(
                                ("UPDATE notificacion SET  estado = 'leido' where id_notificacion = {}").format(i[0]))
                            conn.commit()



            elif opcionnotificaciones == "2":
                cur.execute(("UPDATE notificacion SET estado =  'leido' WHERE id_perfil =  {} ").format(str(id[0])))
                conn.commit()
            elif opcionnotificaciones == "3":
                cur.execute(
                    ("SELECT * from notificacion WHERE estado = 'leido' and  id_perfil =  {} ").format(str(id[0])))
                rowss = cur.fetchall()
                cc = 0
                print("NOTIFICIONES LEIDAS")
                print("--------------------------------------------")

                for i in rowss:
                    cc += 1
                    print("(" + str(cc) + ") " + " IDN: " + str(i[0]) + "\t  " + str(i[2]))
                print("---------------------------------------")
                numero = int(raw_input("ingrese numero de notificacion:"))
                cc = 0
                for i in rowss:
                    cc += 1
                    if (numero == cc):
                        if i[2] == "solicitud":

                            cur.execute("SELECT * FROM solicitud;")
                            tsolicitud = cur.fetchall()
                            for s in tsolicitud:
                                if s[3] == i[0]:
                                    print("\t NOTIFICACION")
                                    print("--------------------------------------------")
                                    print("La solicitud: " + str(s[3]) + "\nUsuario de amistad:" + s[
                                        1] + "\nfecha: " + str(s[4]) + "\n" + s[2])
                                    print("--------------------------------------------")

                        elif i[2] == "publicacion":  # son los de comentario
                            cur.execute(
                                "SELECT * FROM comentario WHERE id_comentario = {}  and estado ='Vigente'".format(i[0]))
                            ncom = cur.fetchone()
                            print("\t NOTIFICACION")
                            print("--------------------------------------------")
                            print("La publicacion: " + str(ncom[2]) + "\nUsuario de comentario:" + str(
                                ncom[1]) + "\ntexto: " + ncom[3] + "\nfecha: " + str(ncom[5]) + "\n" + ncom[4])
                            print("--------------------------------------------")

                        elif i[2] == "comentario":
                            cur.execute(
                                "SELECT * FROM sub_comentario WHERE id_comentario = {}  and estado ='Vigente'".format(
                                i[0]))
                            nsubcom = cur.fetchone()
                            print("\t NOTIFICACION")
                            print("--------------------------------------------")
                            print("La publicacion: " + str(nsubcom[1]) + "\nUsuario de comentario:" + str(
                                nsubcom[2]) + "\ntexto: " + nsubcom[3] + "\nfecha: " + str(nsubcom[5]) + "\n" + nsubcom[
                                      4])
                            print("--------------------------------------------")
            elif opcionnotificaciones == "4":
                Boolnotiifcaciones = False
            else:
                print("")
                    
    elif opcion == "4":
        while True:
            print "######### CONTACTOS #########"
            print "-----------------------------"
            cur.execute("SELECT * from solicitud WHERE aceptada = 'Aceptada'")
            rows = cur.fetchall()
            all_contacts=[]
            for i in rows:
                all_contacts.append(i)
            contactos=[]
            contactosReal=[]
            cont=0
            for i in rows:
                if i[0]==email:
                    contactos.append([i[1],i[3],i[4],cont])
                    contactosReal.append(i)
                    cont+=1
                elif i[1]==email:
                    contactos.append([i[0],i[3],i[4],cont])
                    contactosReal.append(i)
                    cont+=1
            while True:
                print "(1) Ver Contactos"
                print "(2) Agregar Contactos"
                print "(3) Solicitudes Pendientes"
                print "(4) Volver"
                opcion2=raw_input("ingrese una opcion valida: ")
                if opcion2=='1' or opcion2=='2' or opcion2=='3' or opcion2=="4":
                    break

            if opcion2=='4':
                break
            if opcion2=='1':

                print "### Ver Contactos ###"
                print "------------------"
                print "Su lista de contactos: "

                print(tabulate(contactos, headers=["email", "id solicitud", "fecha_solicitud", "indice"],
                               tablefmt="fancygrid"))

                print "(1) Ver Perfil"
                print "(2) Dejar de ser Contactos"
                print "(3) Volver"
                op=raw_input("cual opcion desea: ")
                while op!="1" and op!='2' and op!="3":
                    op = raw_input("ingrese una opcion valida :")

                if op=="1":
                    print "para volver al menu anterior ingrese 'atras'"
                    contact = int(raw_input("ingrese el indece de un contacto para ver la informacion del perfil:"))
                    if contact > len(contactos) or contact < 0:
                        print "ingrese una opcion valida"
                        continue
                    if contact == 'atras':
                        continue
                    info_contacto=[]
                    #sacando la informacion del perfil del contacto
                    exe = "SELECT * FROM perfil WHERE email='" + str(contactos[contact][0]) + "'"
                    cur.execute(exe)
                    perfil_contacto = cur.fetchall()
                    for i in perfil_contacto:
                        info_contacto.append(i)
                        print(tabulate(perfil_contacto, headers=["id", "email", "nombre", "apellido", "genero", "fecha nacimiento", "nacionalidad", "descripcion"], tablefmt="fancygrid"))
                    #sacando el telefono del contacto

                    exe="SELECT telefono FROM telefono_perfil WHERE id_perfil=" + str(perfil_contacto[0][0]) +" LIMIT 1"
                    cur.execute(exe)
                    telefono_contacto=cur.fetchall()
                    print(tabulate(telefono_contacto,
                                   headers=["telefono"], tablefmt="fancygrid"))
                    # sacando el telefono del contacto1



                    #sacando las fotos de perfil del contacto
                    exe="SELECT foto FROM foto_perfil WHERE id_perfil=" + str(perfil_contacto[0][0])
                    cur.execute(exe)
                    fotos_contact=cur.fetchall()
                    info_contacto.append(fotos_contact)
                    print(tabulate(fotos_contact,
                                   headers=["fotos"], tablefmt="fancygrid"))
                    #sacando el estudio del contacto
                    exe="SELECT nombre_institucion, grado_academico, descripcion FROM estudio WHERE id_perfil=" + str(perfil_contacto[0][0])
                    cur.execute(exe)
                    estudio_contact=cur.fetchall()
                    info_contacto.append(estudio_contact)
                    print(tabulate(estudio_contact,
                                   headers=["Institucion", "grado", "descripcion"], tablefmt="fancygrid"))
                    #sacando la experiencia laboral
                    exe="SELECT id_empresa, puesto FROM trabaja WHERE id_trabajador=" + str(perfil_contacto[0][0])
                    cur.execute(exe)
                    experiencia_contacto=cur.fetchall()
                    info_contacto.append(experiencia_contacto)
                    print(tabulate(experiencia_contacto,
                                   headers=["id empresa","puesto"], tablefmt="fancygrid"))
                    #sacando la =s habilidades
                    exe="SELECT habilidad FROM habilidad WHERE id_perfil=" + str(perfil_contacto[0][0])
                    cur.execute(exe)
                    habilidades=cur.fetchall()

                    #validaciones habilidades
                    exe="SELECT * FROM validar WHERE id_perfil=" + str(perfil_contacto[0][0])
                    cur.execute(exe)
                    validaciones=cur.fetchall()

                    habilidades_contacto=[]
                    for i in habilidades:
                        count=0
                        for j in validaciones:
                            if i[0]==j[1]:
                                count+=1
                        habilidades_contacto.append([i,count])

                    print(tabulate(habilidades_contacto,
                                   headers=["habilidad","validaciones"], tablefmt="fancygrid"))
                    #sacando todos los contactos en comun
                    contactos_contacto = []
                    for i in rows:
                        if i[0] == perfil_contacto[0][1]:
                            contactos_contacto.append([i[1], i[3], i[4]])
                        if i[1] == perfil_contacto[0][1]:
                            contactos_contacto.append([i[0], i[3], i[4]])
                    cant_comun=0
                    for i in contactos_contacto:
                        for j in contactos:
                            if i==j:
                                cant_comun+=1

                    x=raw_input("ingrese una habilidad para validar o 'salir' para volver al menu anterior")
                    n=0
                    while n!=1:
                        for i in habilidades_contacto:
                            print i
                            print i[0][0]
                            if i[0][0]==x:
                                i[1]+=1
                                n=1
                                break
                            if x=="salir":
                                n=1
                                break
                        if n==1:
                            break
                        x=raw_input("la habilidad que ingreso no se encuentra en las habilidades, intente denuevo , para salir escriba salir:")

                    if x=="salir":
                        break
                    print perfil_contacto[0]
                    print x
                    print email
                    exe="INSERT INTO validar(id_perfil,habilidad_perfil,email_usuario_valida) VALUES ("+str(perfil_contacto[0][0])+",'"+x+"','"+email+"')"
                    cur.execute(exe)
                    conn.commit()


                if op=='2':
                    print "### Dejar de ser contacto"
                    print "-------------------------"
                    print(tabulate(contactos, headers=["email", "id solicitud", "fecha_solicitud", "indice"],
                                   tablefmt="fancygrid"))
                    print "para volver al menu anterior ingrese 'atras'"
                    contact = int(raw_input("ingrese el indece de un contacto para eliniminarlo de sus contactos:"))
                    if contact > len(contactos) or contact < 0:
                        print "ingrese una opcion valida"
                        continue
                    if contact == 'atras':
                        continue
                    exe = "SELECT * FROM perfil WHERE email='" + str(contactos[contact][0]) + "'"
                    cur.execute(exe)
                    perfil_contacto = cur.fetchone()
                    exe="UPDATE solicitud SET  aceptada = 'Rechazada' WHERE  id_solicitud="+str(contactos[contact][2])
                    cur.execute(exe)
                    conn.commit()
                    contactos.remove(contactos[contact])

                if op=='3':
                    continue

            if opcion2=="2":
                print"### Agregar Contactos ###"
                print"-------------------------"
                exe="SELECT * FROM perfil"
                cur.execute(exe)
                perfiles=cur.fetchall()
                not_contactos=[]
                for i in perfiles:
                    for j in contactosReal:
                        if i[1]==j[1]:
                            continue
                        else:
                            not_contactos.append(i)

                print"Lista de usuarios que puede agregar:"
                print(tabulate(not_contactos, headers=["id", "email", "nombre","apellido","genero","fecha nacimiento", "pais","descripcion"], tablefmt="fancygrid"))
                id_Agregar=int(raw_input("ingrese el id del usuario que quiera agregar :"))
                for i in not_contactos:
                    if id_Agregar==i[0]:
                        persAgregar=i
                exe="SELECT id_solicitud FROM solicitud GROUP BY id_solicitud ORDER BY id_solicitud DESC LIMIT 1"
                cur.execute(exe)
                numID2=cur.fetchone()
                numID=numID2[0]
                numID+=1
                print numID
                exe = "INSERT INTO solicitud (email_usuario, email_usuario_amistad, aceptada, id_solicitud) VALUES ('"+email+"','"+str(persAgregar[1])+"', 'Ignored',"+str(numID)+")"
                cur.execute(exe)
                conn.commit()


            if opcion2=="3":
                exe="SELECT * FROM solicitud WHERE aceptada= 'Ignored' AND  email_usuario_amistad="+"'"+email+"'"
                cur.execute(exe)
                sol_pend=cur.fetchall()

                print sol_pend
                print(tabulate(sol_pend, headers=["email", "tu email","condicion", "id solicitud","fecha"], tablefmt="fancygrid"))
                mant=True
                sol=int(raw_input("elija una solicitud con su id"))
                for i in sol_pend:
                    if i[3]==sol:
                        mant=False
                while mant:
                    sol = raw_input("Error, elija una solicitud con su id o escriba atras para volver")
                    for i in sol_pend:
                        if i[3] == sol:
                            mant = False
                    if sol=='atras':
                        break
                if sol=='atras':
                    continue
                print "(1) Aceptar"
                print "(2) Rechazar"
                print "(3) Ignorar"
                op1=raw_input("ingrese una opcion: ")
                while op1!="1" and op1!="2" and op1!="3":
                    op1 = raw_input("ingrese una opcion valida: ")

                if op1=="1":
                    exe = "UPDATE solicitud SET  aceptada = 'Aceptada' WHERE  id_solicitud=" + str(sol)
                    cur.execute(exe)
                    conn.commit()

                if op1 == "2":
                    exe = "UPDATE solicitud SET  aceptada = 'Rechazada' WHERE  id_solicitud=" + str(sol)
                    cur.execute(exe)
                    conn.commit()

                if op1 == "3":
                    continue



    elif opcion == "5":
        print "### Empresas ###"
        print "----------------"

        exe="SELECT * FROM admin WHERE mail_admin='"+ email + "'"
        cur.execute(exe)
        admins=cur.fetchall()
        print "(1) Empresesas que soy administrador"
        print "(2) Ver Trabajps"
        print "(3) Volver"
        op3=raw_input("ingrese una opcion")
        while op3!='1' and op3!='2' and op3!='salir':
            op3=raw_input("Error, ingrese una opcion valida")

        if op3=="1":
            print "Lista de empresas que es admin"
            print(tabulate(admins,headers=["id_empresa","fecha ini", 'fecha fin', "mail admin"], tablefmt="fancygrid"))
            a=0
            while a!=1:
                id_emp=int(raw_input("ingrese el id de la empresa que quiere selecionar: "))
                for i in admins:
                    if i[0]==id_emp:
                        a=1
            print "(1) Ver trabajos"
            print "(2) Crear Publicacion"
            print "(3) Mis Publicaciones"
            print "(4) Agregar admin"
            print "(5) Dejar de ser admin"
            print "(6) Crear Empresa"
            print "(7) Eliminar empresa"
            op4=int(raw_input("ingrese una opcion: "))
            while op4 not in [1,2,3,4,5,6,7]:
                op4=int(raw_input("Error, ingrese una opcion valida"))

            if op4==1:
                exe="SELECT * FROM cargos_disponibles WHERE id_empresa= "+ str(id_emp)
                cur.execute(exe)
                trabajosos=cur.fetchall()
                trabajos=[]
                for i in trabajosos:
                    l=[]
                    for j in i:
                        l.append(j)
                    trabajos.append(l)
                print trabajos
                exe = "SELECT nombre_cargo, id_empresa ,COUNT(*) FROM postulacion GROUP BY nombre_cargo, id_empresa HAVING id_empresa=" + str(id_emp)
                #exe = "SELECT nombre_cargo, id_empresa FROM postulacion WHERE id_empresa=" + str(id_emp)
                cur.execute(exe)
                trabajos1=cur.fetchall()
                print trabajos1
                for i in trabajos:
                    i.append(0)
                    for j in trabajos1:
                        if i[0]==j[0]:
                            i[-1]+=1

                print(tabulate(trabajos, headers=["nombre", "id empresa", "Cant de postulaciones"],tablefmt="fancygrid"))

                print "(1) Ver trabajo"
                print "(2) Cerar postulacion"
                print "(3) Agregar trabajo"
                print "(4) Eliminar trabajo"
                op5=int(raw_input("ingrese una opcion valida: "))
                while op5 not in [1,2,3,4]:
                    op5=int(raw_input("ingrese una opcion valida: "))

                if op5==1:
                    count=0
                    tra=raw_input("ingrese el nombre del trabajo")
                    l_tra=[count]
                    for i in trabajos1:
                        count+=1
                        if i[0]==tra:
                            l_tra.append(i)
                    print(tabulate(l_tra, headers= ["index", "nombre cargo", "id empresa", "id perfil ","fecha postulacion", "Estado"], tablefmt="fancygrid"))
                    post=int(raw_input("ingrese el index de una postulacion: "))
                    while post<0 and post>len(l_tra):
                        post=int(raw_input("ingrese el index de una postulacion: "))
                    print "(1) Ver perfil del postulante"
                    print "(2) Aceptar postulacion"
                    print "(3) Rechazar potulacion"

                    op6=int(raw_input("ingrese una opcion valida: "))
                    while op6 not in [1,2,3]:
                        op6=int(raw_input("ingrese una opcion valida"))

                    if op6==1:
                        exe="SELECT * FROM perfil WHERE id= "+str(l_tra[post][3])
                        cur.execute(exe)
                        per=cur.fetchone()
                        print(tabulate(per, headers=["id", "email", "nombre", "apellido","genero","fecha nacimiento", "pais", "descripcion"], tablefmt="fancygrid"))
                    if op6==2:
                        exe="UPDATE solicitud SET  aceptada = TRUE WHERE  nombre_cargo='"+l_tra[post][1]+"' AND id_perfil="+str(l_tra[post][3])
                        cur.execute(exe)
                        conn.commit()
                    if op6==3:
                        continue
                if op5==2:
                    tra=raw_input("ingrese el nombre del trabajo")
                    exe="DELETE FROM cargos_disponibles WHERE id_empresa="+str(id_emp)+"AND nombre='"+tra+"'"
                    cur.execute(exe)
                    conn.commit()
                if op5==3:
                    nombre_c=raw_input("ingrese el nombre del cargo: ")
                    vacantes=int(raw_input("ingrese las vacantes del cargo:"))
                    sueldo=int("ingrese el sueldo:")
                    descripcion=raw_input("ingrese una descripcion del cargo:")
                    exe = "INSERT INTO cargos_disponibles(nombre,id_empresa,vacantes, sueldo, mail_admin, fecha_disponible, descripcion) VALUES ('"+nombre_c+"',"+str(id_emp)+","+str(sueldo)+",'"+email+"','"+str(fecha)+"','"+descripcion+"')"
                    cur(exe)
                    conn.commit()
                if op5==4:
                    tra = raw_input("ingrese el nombre del trabajo")
                    exe = "DELETE FROM cargos_disponibles WHERE id_empresa=" + str(id_emp) + "AND nombre='" + tra + "'"
                    cur.execute(exe)
                    conn.commit()
                    exe = "DELETE FROM postulacion WHERE id_empresa=" + str(id_emp) + "AND nombre_cargo='" + tra + "'"
                    cur.execute(exe)
                    conn.commit()

            if op4==2:
                exe="SELECT id_publicacion FROM publicacion GROUP BY id_publicacion ORDER BY DESC LIMIT 1"
                cur.execute(exe)
                id=cur.fetchone()
                id=id+1
                id_usuario=id_emp
                privacidad=raw_input("ingrese la privacidad:")
                contenido=raw_input("ingrese el contenido de la postulacion:")
                fecha = datetime.date.today()
                estado=raw_input("ingrese el estado: ")
                exe="INSER INTO publicacion (id_publicacion, id_usurario, privacidad, contenido, fecha, estado) VALUES ("+str(id)+","+str(id_usuario)+",'"+privacidad+"', '"+contenido+"',"+str(fecha)+",'"+estado+"')"
                cur.execute(exe)
                conn.commit()
            if op4==3:
                exe="SELECT * FROM publicacion WHERE id_usario="+str(id_emp)
                cur.execute(exe)
                postulaciones=cur.fetchall()
                print(tabulate(postulaciones, headers=["id publicacion", "id usuario", "privacidad", "contenido", "fecha", "estado",], tablefmt="fancygrid"))
                id_post=int(raw_input("ingrese el id de la publicacion:"))
                print "(1) Ver publiccacion"
                print "(2) Eliminar publicacion"
                print "(3( Comentar"
                op7=int(raw_input("ingrese la ocion que quiere: "))
                while op7 not in [1,2,3]:
                    op7 = int(raw_input("Error, ingrese la ocion que quiere: "))

                if op7==1:
                    for i in postulaciones:
                        if i[0]==id_post:
                            print(tabulate(i,headers=["id publicacion", "id usuario", "privacidad", "contenido", "fecha", "estado", ], tablefmt="fancygrid"))

                    exe="SELECT * FROM comentario WHERE id_publicacion=" +id_post
                    cur.execute(exe)
                    coments=cur.fetchall()
                    print "y estos son los comentarios a esta publicacion"
                    print(tabulate(coments,headers=["id comentario", "id usuario", "id_post", "texto", "estado","fecha", ], tablefmt="fancygrid"))
                if op7==2:
                    seguro=int(raw_input("esta seguro? (1) si, (2) no"))
                    while seguro not in [1,2]:
                        seguro = int(raw_input("Error, esta seguro? (1) si, (2) no"))

                    if seguro==1:
                        exe="DELETE FROM comentario WHERE id_publicacion=" +str(id_post)
                        cur.execute(exe)
                        conn.commit()
                        exe = "DELETE FROM publicacion WHERE id_publicacion=" + str(id_post)
                        cur.execute(exe)
                        conn.commit()
                    else: continue

                if op7==3:
                    exe = "SELECT id_comentario FROM comentario GROUP BY id_comentario ORDER BY DESC LIMIT 1"
                    cur.execute(exe)
                    id_c = cur.fetchone()
                    id_C = id + 1
                    id_usuario=id_emp
                    id_publicacion=id_post
                    texto=raw_input("ingrese el comentario")
                    exe="INSERT INTO cometario (id_cometario, id_usuario, id_publicacion, texto, fecha) VALUES("+str(id_C)+", "+str(id_usuario)+", "+str(id_publicacion)+",'"+texto+"',"+str(fecha)+")"

            if op4==4:
                exe="SELECT * FROM trabaja WHERE id_empresa="+str(id_emp)
                cur.execute(exe)
                trabajadores=cur.fetchall()
                print(tabulate(trabajadores, headers=["id trabajador", "id empresa", "puesto", "contenido", "fecha ini", "fecha fin" ],tablefmt="fancygrid"))
                idNuevoAdmin=int(raw_input("ingrese el id del nuevo admin:"))
                a=0
                while a!=1:
                    for i in trabajadores:
                        if i[0]==idNuevoAdmin:
                            a=1
                            break
                    if a!=1:
                        idNuevoAdmin = int(raw_input("Error, ingrese el id del nuevo admin:"))
                exe="SELECT email FROM perfil WHERE id="+str(idNuevoAdmin)
                cur.execute(exe)
                emailNuevoAdmin=cur.fetchone()
                exe="INSERT INTO admin (id_empresa, fecha de inicio, fecha fin, mail admin) VALUES("+str(id_emp)+", "+str(fecha)+", NULL, '"+emailNuevoAdmin+"')"
                cur.execute(exe)
                conn.commit()

            if op4==5:
                exe="UPDATE admin SET fecha_fin="+str(fecha)+"WHERE mail_admin='"+email+"'"
                cur.execute(exe)
                conn.commit()
            if op4==6:
                exe = "SELECT id FROM empresa GROUP BY id ORDER BY DESC LIMIT 1"
                cur.execute(exe)
                id_e = cur.fetchone()
                id_e = id + 1
                nombre=raw_input("ingrese el nombre de su empresa:")
                dirrecion=raw_input("ingrese la direcion de su empresa:")
                descripcion=raw_input("ingrese una descripcion de empresa:")
                pais=raw_input("ingrese el pais en que esta la empresa:")
                rubro=raw_input("ingrese le ribro de su empresa:")

                exe="INSERT INTO empresa (id, nombre, direccion, descripcion, pais, rubro, fecha de creacion) VALUES("+str(id_e)+", '"+nombre+"', '"+dirrecion+"', '"+descripcion+"', '"+pais+"', '"+rubro+"', "+str(fecha)+")"
                cur.execute(exe)
                conn.commit()
                exe="INSERT INTO admin (id_empresa, fecha_de_inicio, fecha_fin, mail_admin) VALUES("+str(id_e)+", "+ str(fecha)+", NULL, '"+email+"')"
                cur.execute(exe)
                conn.commit()
            if op4==7:
                exe="SELECT id FROM empresa"
                cur.execute(exe)
                empresas=cur.fetchall()
                id_e=int(raw_input("ingrese el id de la empresa que quiere eliminar:"))
                a=1
                while a!=1:
                    for i in empresas:
                        if i==id_e:
                            a=1
                            break
                    if a!=1:
                        id_e = int(raw_input("ingrese el id de la empresa que quiere eliminar:"))
                exe="DELETE FROM empresa WHERE id="+str(id_e)

        elif op3 == "2":
            print("\t EMPRESAS CON TRABAJOS OFRECIENDOSE")
            cur.execute(
                "SELECT e.nombre,e.id FROM empresa e, cargos_disponibles cd WHERE cd.id_empresa=e.id GROUP BY e.nombre,e.id;")
            trabempresas = cur.fetchall()
            print trabempresas
            j = 0
            for i in trabempresas:
                j += 1
                print("(" + str(j) + ") " + i[0])

            print("\t MENU TRABAJOS ")
            print("(1) VER EMPRESA")
            opciontrabajos = raw_input("Ingrese opcion: ")
            if opciontrabajos == "1":
                nempresa = int(raw_input("Seleccione numero de empresa: "))
                j = 0
                for i in trabempresas:
                    j += 1
                    if nempresa == j:
                        cur.execute(
                            "SELECT p.contenido, p.fecha FROM publicacion p WHERE p.id_usuario={} ORDER BY p.fecha DESC LIMIT 5;".format(
                                i[1]))
                        pubempresa = cur.fetchall()
                        print("\t ULTIMAS PUBLICACIONES ")
                        for k in pubempresa:
                            print(i[0] + " Publico un/una: " + j[0] + " el: " + j[1].strftime('%d/%m/%Y'))

                        cur.execute(
                            "SELECT c.texto, c.fecha FROM comentario c WHERE c.id_usuario={}  ORDER BY c.fecha DESC LIMIT 2;".format(
                                i[1]))

                        comempresa = cur.fetchall()
                        print("\t ULTIMOS COMENTARIOS ")
                        for g in comempresa:
                            print(i[0] + " Comento: " + g[0] + " el: " + g[1].strftime('%d/%m/%Y'))

                        cur.execute("SELECT * FROM cargos_disponibles cd WHERE cd.id_empresa={};".format(i[1]))
                        trabajosofrecidos = cur.fetchall()

                        print("\t TRABAJOS QUE OFRECE LA EMPRESA ")
                        h = 0
                        for l in trabajosofrecidos:
                            h += 1
                            print("(" + str(h) + ") " + l[0])
                print("\t MENU VER EMPRESA ")
                print("(1) VER TRABAJOS")
                print("(2) POSTULAR A TRABAJO")
                opcionverempresa = raw_input("Ingrese opcion: ")
                if opcionverempresa == "1":
                    trabajon = int(raw_input("Ingrese trabajo a ver: "))
                    h = 0
                    for l in trabajosofrecidos:
                        h += 1

                        if trabajon == h:
                            print("\t INFORMACION DE TRABAJO ")
                            print("Cargo disponible: " + l[0])
                            print("Sueldo ofrecido: $" + str(l[2]))
                            print("Vacantes disponibles: " + str(l[3]))
                            print("Descripcion del cargo: " + str(l[6]))
                            cur.execute(
                                "SELECT COUNT(*) FROM postulacion WHERE id_empresa={} AND nombre_cargo={};".format(l[1],
                                                                                                                   "'" +
                                                                                                                   l[
                                                                                                                       0] + "'"))
                            cantidadpostulacion = cur.fetchall()
                            print("Cantidad de postulaciones al trabajo: " + str(cantidadpostulacion[0][0]))

                elif opcionverempresa == "2":
                    posttrabajo = int(raw_input("Ingrese trabajo a postular: "))
                    h = 0
                    for l in trabajosofrecidos:
                        h += 1

                        if trabajon == h:
                            fech = datetime.date.today()
                            cur.execute(
                                "INSERT INTO postulacion(nombre_cargo,id_empresa,id_perfil,fecha_de_postulacion,aceptado) VALUES('{}','{}','{}','{}','{}');".format(
                                    l[0], l[1], row[0][0], str(fech), 'FALSE'))
                            conn.commit()
                            
                    print("Su postulacion ya ah sido realizada")
                elif opcionverempresa == "3":
                    break
                else:
                    print("Opcion invalida!")

        if op3=="3":
            break


    elif opcion == "6":
        TRUUEEE = False

    elif opcion == "7":

        fechast = []
        fechasr = []
        cur.execute(
            "SELECT id_publicacion FROM  publicacion WHERE id_usuario = {} and 	estado = 'Activo'".format(id))
        publicaciones = cur.fetchall()
        for i in publicaciones:
            cur.execute(
                "SELECT EXTRACT(MONTH FROM fecha)m , COUNT(*)  FROM comentario WHERE id_publicacion = {} GROUP BY m ".format(
                    i[0]))
            ff = cur.fetchall()
            for f in ff:
                fechast.append(f)

        cur.execute(
            "SELECT EXTRACT(MONTH FROM fecha)m , COUNT(*)  FROM comentario WHERE id_usuario = {} GROUP BY m ".format(
                id))
        fe = cur.fetchall()
        for f in fe:
            fechasr.append(f)
        cur.execute(
            "SELECT EXTRACT(MONTH FROM fecha)m , COUNT(*)  FROM sub_comentario WHERE id_usuario = {} GROUP BY m ".format(
                id))
        fe = cur.fetchall()
        for f in fe:
            fechasr.append(f)

        cur.execute("SELECT id_comentario FROM comentario WHERE id_usuario = {} ".format(id))
        coments = cur.fetchall()
        for j in coments:
            cur.execute(
                "SELECT  EXTRACT(MONTH FROM fecha)m , COUNT(*) FROM sub_comentario  WHERE id_comentario = {} GROUP BY m".format(
                    j[0]))
            cc = cur.fetchall()
            for c in cc:
                fechast.append(c)
        mesest = []
        c1 = 0
        c2 = 0
        c3 = 0
        c4 = 0
        c5 = 0
        c6 = 0
        c7 = 0
        c8 = 0
        c9 = 0
        c10 = 0
        c11 = 0
        c12 = 0

        for k in fechast:
            if k[0] == 1:
                c1 += k[1]
            elif k[0] == 2:
                c2 += k[1]
            elif k[0] == 3:
                c3 += k[1]
            elif k[0] == 4:
                c4 += k[1]
            elif k[0] == 5:
                c5 += k[1]
            elif k[0] == 6:
                c6 += k[1]
            elif k[0] == 7:
                c7 += k[1]
            elif k[0] == 8:
                c8 += k[1]
            elif k[0] == 9:
                c9 += k[1]
            elif k[0] == 10:
                c10 += k[1]
            elif k[0] == 11:
                c11 += k[1]
            elif k[0] == 12:
                c12 += k[1]

        mesest.append(c1)
        mesest.append(c2)
        mesest.append(c3)
        mesest.append(c4)
        mesest.append(c5)
        mesest.append(c6)
        mesest.append(c7)
        mesest.append(c8)
        mesest.append(c9)
        mesest.append(c10)
        mesest.append(c11)
        mesest.append(c12)

        mesesr = []
        c1 = 0
        c2 = 0
        c3 = 0
        c4 = 0
        c5 = 0
        c6 = 0
        c7 = 0
        c8 = 0
        c9 = 0
        c10 = 0
        c11 = 0
        c12 = 0

        for k in fechasr:
            if k[0] == 1:
                c1 += k[1]
            elif k[0] == 2:
                c2 += k[1]
            elif k[0] == 3:
                c3 += k[1]
            elif k[0] == 4:
                c4 += k[1]
            elif k[0] == 5:
                c5 += k[1]
            elif k[0] == 6:
                c6 += k[1]
            elif k[0] == 7:
                c7 += k[1]
            elif k[0] == 8:
                c8 += k[1]
            elif k[0] == 9:
                c9 += k[1]
            elif k[0] == 10:
                c10 += k[1]
            elif k[0] == 11:
                c11 += k[1]
            elif k[0] == 12:
                c12 += k[1]

        mesesr.append(c1)
        mesesr.append(c2)
        mesesr.append(c3)
        mesesr.append(c4)
        mesesr.append(c5)
        mesesr.append(c6)
        mesesr.append(c7)
        mesesr.append(c8)
        mesesr.append(c9)
        mesesr.append(c10)
        mesesr.append(c11)
        mesesr.append(c12)

        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        plt.plot(x, mesesr, "r", x, mesest, "b")
        plt.legend(["Comentario creados", "Comentario que ha tenido"])
        plt.show()

    else :
        print("Opcion no valida! Intente nuevamente")
        continue







cur.close()




conn.close()