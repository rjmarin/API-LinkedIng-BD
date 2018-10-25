import psycopg2
import numpy as np
import matplotlib.pyplot as plt
from numpy import random
from tabulate import tabulate

def print_table(ranking):
    for i in ranking:
        for x in range(len(i)):
            if i[x] == None:
                i[x] = ""
            if isinstance(i[x], unicode) == False:
                info = str(i[x]).decode("utf-8")
                i[x] = info.encode("ascii", "ignore")


    print tabulate(ranking, headers="firstrow", tablefmt="fancy_grid")

def get_name (id):
    curr = conn.cursor()
    curr.execute("select i.nombre_insti,i.comu_cas_cen from institucion i where i.numero_institucion = " + str(id))
    list = []
    for r in curr:
        list.append(r)
    try:
        return  list[0][0]
    except IndexError:
        return "SIN NOMBRE"

print"Bienvenido al Manejador de datos"
conn = psycopg2.connect(database="grupo1", user="grupo1", password="uDVh6Z",host="201.238.213.114",port = "54321")
cur = conn.cursor()
cur.execute("select i.nombre_insti,i.numero_institucion,i.tipo,i.comu_cas_cen,i.ano_creacion,i.propiedad from institucion i")
instituciones = []
instituciones_a_mostrar = []
contador = 1
for a in cur:
    try :
        instituciones_a_mostrar.append(str(contador)+"                 " + a[0])
        instituciones.append(a)
        contador += 1
    except TypeError:
        pass
loopMenu = True
cur.close()
while (loopMenu):
    print "Ingrese opcion deseada \n [1] = Administrar Instituciones \n [2] = Administrar programas \n [3] = Reportes Generales \n [4] = Ranking institucional \n [5] = Salir"
    opcion = raw_input("Ingrese opcion aca :")
    if opcion == "1":
        print "numero institucion      nombre institucion"
        for i in instituciones_a_mostrar:
            print i
        loopinstitucion = True
        while loopinstitucion:
            print "Elegir una opcion \n [1] = Ficha Informacion General \n [2] = Actualizar Datos Actuales \n [3] = Volver al Menu \n [4] = Salir del Programa"
            opcion_institucion = raw_input("ingrese opcion aca :")
            if opcion_institucion == "1":
                elegida = int(raw_input("Ingrese numero de institucion a revisar :"))
                try:
                    insti = (instituciones[elegida - 1])
                    try:
                        print "Ficha se la institucion numero :" + str(elegida)
                        print "Nombre                         :" + str(insti[0])
                        print "Tipo                           :" + str(insti[2])
                        print "Direccion casa central         :" + str((insti)[3])
                        print "Ano Fundacion                  :" + str(insti[4])
                        print "Propiedad                      :" + str(insti[5])
                        cur2 = conn.cursor()
                        cur2.execute("select numero_institucion7,gratuidad,ano_dato,cruch from datosinstitucion where numero_institucion7 ="+ str(insti[1])+" order by ano_dato asc")
                        procesos_gratuidad = []
                        duracion = []
                        gratuidad_lista = []
                        gratuidad_not_lista =[]
                        ano_inicio_gratuidad = 0
                        ano_termino_gratuidad = 0
                        contaodr_gratuidad = 0
                        for i in cur2:
                            if i[1] =='(b) No Adscritas/No Aplica' :
                                gratuidad_not_lista.append(i[2])
                            if i[1] =='(a)Adscritas a Gratuidad'  :
                                gratuidad_lista.append(i[2])
                            cruch = i[3]
                        if ano_inicio_gratuidad == 0:
                            ano_inicio_gratuidad = 2005
                        cur2.close()
                        print "NO Adscritas a la Gratuidad en ano " +str(gratuidad_not_lista)
                        print "Adscritas a la Gratuidad en ano " + str(gratuidad_lista)
                        cur2 = conn.cursor()
                        cur2.execute("select numero_institucion7,sua,ano_dato from datosinstitucion where numero_institucion7 =" + str(insti[1]) + " order by ano_dato asc")
                        procesos_gratuidad = []
                        anoss=[]
                        notanoss = []
                        contaodr_gratuidad = 0
                        ano_inicio_sua = 0
                        for i in cur2:
                            if (i[1] =='(a) Universidades Estatales CRUCH' or i[1] == '(d) Universidades Privadas' or i[1] == '(b) Universidades Privadas CRUCH' or i[1] == '(e) Institutos Profesionales' or i[1] == '(f) Centros de Formacion Tecnica'):
                                notanoss.append(i[2])
                            if i[0] =='(c) Univ. Privadas Adscritas SUA'  :
                                anoss.append(i[2])

                        print "NO Adscritas al Sua en ano " +str(notanoss)
                        print "Adscritas al Sua en ano " + str(anoss)
                        cur2.close()


                        cur4 = conn.cursor()
                        cur4.execute("select * from acreditacion_institucion where numero_institucion5 ="+ str(insti[1]))
                        acre = cur4.fetchone()
                        if acre == None:
                            print "No se tiene info de su proceso de acreditacion"
                        else:
                            if acre[7] == 0:
                                acre[7] = 2005
                                printacre = "Acreditada desde :" +str(acre[7]) + " y por "+ str(acre[8]) + " anos"
                                print printacre
                            else:
                                printacre = "Acreditada desde :" + str(acre[7]) + " y por " + str(acre[8]) + " anos"
                                print printacre
                        cur4.close()
                        cur = conn.cursor()
                        cur.execute("select s.id_sede ,s.ubicacion ,i.numero_institucion from institucion i , sede s where s.id_institucion1 = i.numero_institucion and i.numero_institucion ="+str(insti[1]))
                        sedess = []
                        suma_matriculados = 0
                        suma_programas = 0
                        for i in cur:
                            sedess.append(i)
                        if len(sedess) >0:
                            for i in sedess:
                                print "Sede :" + str(i[0]) + " Ubicada en :" + str(i[1])
                                sedes_programas = []
                                cur6 = conn.cursor()
                                cur6.execute("select  m.id_sede9,count(m.id_programa1)  from matriculados m  where m.ano_matricula = 2017 and m.id_Sede9 = " + str(i[0]) +" group by m.id_sede9")
                                for t in cur6:
                                    sedes_programas.append(t)
                                if len(sedes_programas)>0:
                                    for h in sedes_programas:
                                        print "La cantidad de programas que ofrece esta sede en el 2017 son :"+ str(h[1])
                                        suma_programas += h[1]
                                        cur7 = conn.cursor()
                                        cant_programas =[]
                                        cur7.execute("select  m.id_sede9,sum(m.matriculados_otra_via + m.ingreso_psu)  from matriculados m  where m.ano_matricula = 2017 and m.id_sede9 =" +str(i[0])+"group by m.id_sede9")
                                        for rr in cur7:
                                            cant_programas.append(rr)
                                        if len(cant_programas)> 0:
                                            print "La cantidad de matriculados para esta sede son :" + str((cant_programas[0])[1])
                                            suma_matriculados += (cant_programas[0])[1]
                                        else:
                                            print "La sede no tiene matriculados para el 2017"
                                        cur7.close()

                                else:
                                    print "La sede " + str(i[0]) + " no tiene programas en el 2017"
                                cur6.close()


                        else:
                            print "No se han encontrado sedes"
                        cur.close()
                        print "La cantidad total de matriculados = " + str(suma_matriculados)
                        print "La cantidad total de programas = " + str(suma_programas)
                    except TypeError:
                        pass
                except IndexError:
                    print "OOPS... No se encontro una la institucion deseada \nretornando..."
            if opcion_institucion == "2":
                loodatosinstitucion = True
                while loodatosinstitucion:
                    print "Menu Actualizar Datos: \n\t [1] = Actualizar Sua \n\t [2] = Actualizar Gratuidad \n\t [3] = Agregar proceso acreditacion \n\t [4] = Volver al Menu Institucion \n\t [5] = Volver al Menu Inicial \n\t [6] = Salir del Programa"
                    opcion_institucion_datos = raw_input("Ingrese opcion :")
                    if opcion_institucion_datos == "1":
                        try:
                            print "Ingrese numero de institucion "
                            numero = raw_input()
                            int(numero)
                            try:
                                instituu = instituciones[int(numero) - 1]
                            except IndexError:
                                print "Institucion ingresada no valida \n Retornando"
                                break
                            loopSua = True
                            while loopSua:
                                print "Que desea hacer  \n[1] Ingresarla  \n[2] Sacarla \n[3] Volver"
                                opcion_sua = raw_input()
                                if opcion_sua == "1":
                                    suaa = '(c) Univ. Privadas Adscritas SUA'
                                    ano_sua = raw_input("Ingrese ano aqui:")
                                    int(ano_sua)
                                    cu = conn.cursor()
                                    cu.execute(
                                        "select ano_dato from datosinstitucion where sua is not null and numero_institucion7 = " + str(
                                            instituu[1]))
                                    anossss = []
                                    for i in cu:
                                        anossss.append(i[0])
                                    if int(ano_sua) in anossss:
                                        print "Ya se tiene dato sua para ese ano elegido, desea sobreescribirlo?"
                                        opcio = raw_input("[1] YES \n[2] NO")
                                        if opcio == "1":
                                            ro = conn.cursor()
                                            ro.execute("update datosinstitucion set sua = '(c) Univ. Privadas Adscritas SUA' where numero_institucion7 =" + str(instituu[1]) + " and ano_dato = " + str(ano_sua))
                                            conn.commit()
                                            print instituu[1]
                                            ro.close()
                                            print "Dato ingresado a la base de datos!"
                                            break
                                        if opcio == "2":
                                            print "Volviendo..."
                                            break
                                    else:
                                        cur = conn.cursor()
                                        cur.execute("insert into datosinstitucion(numero_institucion7,sua,ano_dato) values (" +str(instituu[1])+","+"'"+suaa+"'"+","+ano_sua+");")
                                        conn.commit()
                                        cur.close()
                                        print"Dato ingresado con exito"
                                        break
                                if opcion_sua == "2":
                                    suaa = "(b) Universidades Privadas CRUCH"
                                    print "ingrese ano de salida o ano de dato"
                                    ano_sua = raw_input()
                                    int(ano_sua)
                                    cu = conn.cursor()
                                    cu.execute("select ano_dato from datosinstitucion where sua is not null and numero_institucion7 = " +str(instituu[1]))
                                    anossss = []
                                    for i in cu:
                                        anossss.append(i[0])
                                    if int(ano_sua) in anossss:
                                        print "Ya se tiene dato sua para ese ano elegido, desea sobreescribirlo?"
                                        opcio = raw_input("[1] YES \n[2] NO")
                                        if opcio == "1":
                                            ro = conn.cursor()
                                            ro.execute("update datosinstitucion set sua = '(b) Universidades Privadas CRUCH' where numero_institucion7 ="+str(instituu[1])+" and ano_dato = "+ str(ano_sua))
                                            conn.commit()
                                            ro.close()
                                            print "Dato ingresado a la base de datos!"
                                            break
                                        if opcio == "2":
                                            print "Volviendo..."
                                            break
                                    else:
                                        rr = conn.cursor()
                                        rr.execute("insert into datosinstitucion(numero_institucion7,sua,ano_dato) values (" + str( instituu[1]) + "," + "'" + suaa + "'" + "," + ano_sua+");")
                                        conn.commit()
                                        rr.close()
                                        print "Dato ingresado con exito!"
                                        break

                                if opcion_sua == "3":
                                    loopSua = False

                                if opcion_sua != "1" and opcion_sua != "2" and opcion_sua != "3":
                                    print "opcion no valida"
                        except ValueError:
                            print "OOOPs algo salio mal... \nRetornando"

                    if opcion_institucion_datos == "2":
                        try:
                            print "Ingrese numero de institucion "
                            numero = raw_input()
                            ano_sua = raw_input("Ingrese ano aqui:")
                            int(numero)
                            instituu = instituciones[int(numero) - 1]
                            loopSua = True
                            while loopSua:
                                print "Desea\n [1] Introducir \n [2] Sacar \n [3] Volver"
                                op = raw_input("Ingrese opcion:")
                                if op == "1":
                                    cu = conn.cursor()
                                    cu.execute("select ano_dato from datosinstitucion where gratuidad is not null and numero_institucion7 = " + str(instituu[1]))
                                    anossss = []
                                    for i in cu:
                                        anossss.append(i[0])
                                    cu.close()
                                    if int(ano_sua) in anossss:
                                        print "Ya se tiene dato sua para ese ano elegido, desea sobreescribirlo?"
                                        opcio = raw_input("[1] YES \n[2] NO")
                                        if opcio == "1":
                                            ro = conn.cursor()
                                            ro.execute("update datosinstitucion set gratuidad = '(a)Adscritas a Gratuidad' where numero_institucion7 =" + str(instituu[1]) + " and ano_dato = " + str(ano_sua))
                                            conn.commit()
                                            ro.close()
                                            print "Dato ingresado a la base de datos!"
                                            break
                                        if opcio == "2":
                                            print "Volviendo..."
                                            break
                                    else:
                                        rr = conn.cursor()
                                        suaa= "(a)Adscritas a Gratuidad"
                                        rr.execute("insert into datosinstitucion(numero_institucion7,gratuidad,ano_dato) values (" + str(instituu[1]) + "," + "'" + suaa + "'" + "," + ano_sua + ");")
                                        conn.commit()
                                        rr.close()
                                        print "Dato ingresado con exito!"
                                        break
                                    if opcion_sua == "3":
                                        break
                                    if opcion_sua != "1" and opcion_sua != "2" and opcion_sua !="3":
                                        print "opcion no valida"
                                if op == "2":
                                    cu = conn.cursor()
                                    cu.execute(
                                        "select ano_dato from datosinstitucion where gratuidad is not null and numero_institucion7 = " + str(
                                            instituu[1]))
                                    anossss = []
                                    for i in cu:
                                        anossss.append(i[0])
                                    cu.close()
                                    if int(ano_sua) in anossss:
                                        print "Ya se tiene dato sua para ese ano elegido, desea sobreescribirlo?"
                                        opcio = raw_input("[1] YES \n[2] NO")
                                        if opcio == "1":
                                            ro = conn.cursor()
                                            ro.execute(
                                                "update datosinstitucion set gratuidad = '(b) No Adscritas/No Aplica' where numero_institucion7 =" + str(
                                                    instituu[1]) + " and ano_dato = " + str(ano_sua))
                                            conn.commit()
                                            ro.close()
                                            print "Dato ingresado a la base de datos!"
                                            break
                                        if opcio == "2":
                                            print "Volviendo..."
                                            break
                                    else:
                                        rr = conn.cursor()
                                        suaa = '(b) No Adscritas/No Aplica'
                                        rr.execute("insert into datosinstitucion(numero_institucion7,gratuidad,ano_dato) values (" + str(instituu[1]) + "," + "'" + suaa + "'" + "," + ano_sua + ");")
                                        conn.commit()
                                        rr.close()
                                        print "Dato ingresado con exito!"
                                        break
                                    if op == "3":
                                        break
                                    if op != "1" and op != "2" and op != "3":
                                        print "opcion no valida"
                        except ValueError:
                            print "OOOPs algo salio mal... \nRetornando"
                        pass
                    if opcion_institucion_datos == "3":
                        print "Selecciona la institucion deseada"
                        loopAcre = True
                        while loopAcre:
                            deseada = raw_input("Ingrese numero de institucion aqui :")
                            try:
                                try:
                                    try:
                                        print "Desea acreditrla en gestion institucional(REQUISITO OBLIGATORIO)"
                                        gii = raw_input(" [1] Yes \n [2] No \n [3] Salir al menu institucion:")
                                        if gii =="3":
                                            break
                                        elif gii == "1":
                                            print "Desea acreditarla en docencia pre grado(REQUISITO OBLIGATORIO)"
                                            dpp = raw_input("[1] Yes \n [2] No  :")
                                            if dpp == "1":
                                                instii = instituciones[int(deseada)-1]
                                                print"Desea acreditarla en Investigacion \n1 Yes/ 2 No"
                                                inve = raw_input()
                                                if inve == "1":
                                                    investigacion = True
                                                elif inve == "2":
                                                    investigacion = False
                                                else:
                                                    print "OOPS algo salio mal \nretornando..."
                                                    continue
                                                print"Desea acreditarla en Vinculacion con el medio "
                                                medio = raw_input("1 Yes/ 2 No")
                                                if medio == "1":
                                                    medi = True
                                                elif medio == "2":
                                                    medi = False
                                                else:
                                                    print "OOPS algo salio mal \nretornando..."
                                                    continue
                                                print"Desea acreditarla en docencia post grado "
                                                docencia_post_grado = raw_input("1 Yes/ 2 No:")
                                                if docencia_post_grado == "1":
                                                    dp = True
                                                elif docencia_post_grado == "2":
                                                    dp = False
                                                else:
                                                    print "OOPS algo salio mal \nretornando..."
                                                    continue
                                                docencia_pre_grado = True
                                                gestion_institucional = True
                                                max=conn.cursor()
                                                max.execute("select a.ano_inicio ,a.duracion ,a.numero_institucion5 from acreditacion_institucion a where a.numero_institucion5 = " +str(instii[1])+";")
                                                maxo = max.fetchone()
                                                max.close()
                                                duracion = raw_input("Ingrese duracion:")
                                                int(duracion)
                                                ano_inicio_acreditacion =[]
                                                ano_inicio_acreditacionn = raw_input("ingrese ano acreditacion :")
                                                try:
                                                    for p in range(int(maxo[1])):
                                                            ano_inicio_acreditacion.append(int(maxo[0]+p))
                                                except TypeError:
                                                    print "no tiene proceso previo de acreditacion"
                                                if int(ano_inicio_acreditacionn) in ano_inicio_acreditacion:
                                                    lop =True
                                                    while lop :
                                                        print "Ya hay un dato entre esos lapsos de tiempo(" + str(ano_inicio_acreditacionn) + "," + str(int(ano_inicio_acreditacionn) + int(duracion)) + "), desea sobre escribirlo?"
                                                        print "desea sobreescribirla "
                                                        opcion_sobre = raw_input("[1] SI\n[2] NO \n[3] Salir\nIngrese opcio:")
                                                        if opcion_sobre == "1":
                                                            cur = conn.cursor()
                                                            cur.execute("insert into acreditacion_institucion (numero_institucion5,gestio_institucional,docencia_pregrado,investigacion,vinculacion_con_el_medio,docencia_postgrado,ano_inicio,duracion) values (%s,%s,%s,%s,%s,%s,%s,%s);",(int(instii[1]),gestion_institucional,docencia_pre_grado,investigacion,medi,dp,int(ano_inicio_acreditacionn),int(duracion)))
                                                            print "Se ha anadido el proceso de acreditacion a la base de datos \nretornando al menu de actualizacion info..."
                                                            cur.close()
                                                            loopAcre = False
                                                            break
                                                        if opcion_sobre =="2":
                                                            print "Saliendo..."
                                                            break
                                                            loopAcre = False
                                                        if opcion_sobre=="3":
                                                            break
                                                else:
                                                    cur = conn.cursor()
                                                    cur.execute("insert into acreditacion_institucion (numero_institucion5,gestio_institucional,docencia_pregrado,investigacion,vinculacion_con_el_medio,docencia_postgrado,ano_inicio,duracion) values (%s,%s,%s,%s,%s,%s,%s,%s);",(int(instii[1]), gestion_institucional, docencia_pre_grado, investigacion,medi, dp, int(ano_inicio_acreditacionn), int(duracion)))
                                                    print "Se ha anadido el proceso de acreditacion a la base de datos \nretornando al menu de actualizacion info..."
                                                    break
                                            else:
                                                print "No se acredito, regresando al menu de acreditacion \nDocencia pregrado es obligatoria!"
                                        else:
                                            print "No se acredito , regresando al menu de acreditacion\nGestion institucional es obligatorio!"
                                    except TypeError:
                                        print "OOPS... algo salio mal \nretornando..."
                                        continue
                                except IndexError:
                                    print "OOPS... algo salio mal \nretornando..."
                                    continue
                            except ValueError:
                                print "OOPS... algo salio mal \nretornando..."
                                continue
                        pass
                    if opcion_institucion_datos == "4":
                        loodatosinstitucion = False
                    if opcion_institucion_datos == "5":
                        loodatosinstitucion = False
                        loopinstitucion = False
                    if opcion_institucion_datos == "6":
                        loodatosinstitucion = False
                        loopinstitucion = False
                        loopMenu = False
                    if opcion_institucion_datos != "1" and opcion_institucion_datos != "2" and opcion_institucion_datos != "3" and opcion_institucion_datos != "4" and opcion_institucion_datos != "5" and opcion_institucion_datos != "6":
                        print "OOPPS.. opcion ingresada no valida \nretornando..."

            if opcion_institucion == "3":
                 loopinstitucion = False
            if opcion_institucion == "4":
                loopinstitucion = False
                loopMenu = False
            if opcion_institucion != "1" and opcion_institucion != "2" and opcion_institucion != "3" and opcion_institucion != "4" :
                print "OOPS opcion ingresada no valida"

    if opcion == "2":
        #inicio clase
        loopclase9 = True
        while loopclase9:
            opcionnnnn = "1"
            if opcionnnnn == "1":
                print "Ingrese texto a continuacion recomendado : 2 letras \n Cuidado con las mayusculas!"
                cur = conn.cursor()
                eleccccion = raw_input()
                cur.execute("select count(m.id_sede9) ,p.nombre,i.nombre_insti from programa p, institucion i , matriculados m where i.numero_institucion = m.numero_institucion9 and m.id_programa1 = p.id_programa  and  m.ano_matricula = 2017  and p.nombre like '%" +eleccccion+ "%' group by p.nombre, i.nombre_insti")
                cleanlist = []
                programas_a_mostrar = []
                listt = []
                programas_a_mostrar_nuevo = []
                contador_mostrar = 1
                for i in cur:
                    listt.append(i)
                    programas_a_mostrar_nuevo.append(i)
                es = [["Numero Programa","Nombre Programa","Nombre Institucion","Nombre Carrera"]]
                for i in programas_a_mostrar_nuevo:
                    frase = str(contador_mostrar)
                    if len(i[1])<90:
                        frase +=  " "+i[1]+((90 - len(i[1])) * " ")
                    else:
                        frase +=  " " + i[1]
                    if len(i[2]) <90:
                        frase += " "+i[2]+((90-len(i[2])) *  " ")
                    else:
                        frase += " "+ i[2]
                    cur5 = conn.cursor()
                    cur5.execute("select m.id_programa1 , c.nombre , c.area_estudio ,i.nombre_insti,p.nombre from carrera c , institucion i , matriculados m , programa p where p.id_carrera2 = c.id_carrera and m.id_programa1 = p.id_programa and m.ano_matricula = 2017 and i.numero_institucion = m.numero_institucion9 and i.nombre_insti ='" +i[2] + "' and p.nombre ='" + i[1] + "'")
                    carrerrrr = ""
                    carrerrrr = cur5.fetchone()
                    cur5.close()
                    frase += carrerrrr[1]
                    tuplille = [contador_mostrar,i[1],i[2],carrerrrr[1]]
                    contador_mostrar +=1
                    es.append(tuplille)

                cur.close()
                print_table(es)
                loopprograma = True
                if len(programas_a_mostrar_nuevo) != 0:
                    while loopprograma:
                        print "Ingrese opcion \n\t [1] = Ver info \n\t [2] = Volver al menu \n\t [3] = Salir del Programa \n\t [4] = Evolucion anual \n\t [5] = Titulados historicos \n\t [6] = Participacion de mercado"
                        opcionnnn = raw_input()
                        if opcionnnn == "1":
                            print "Ingrese numero de programa a ver info"
                            opcion_programa = raw_input()
                            try:

                                #aca obtengo el id del programa
                                programa_elegido = (programas_a_mostrar_nuevo[int(opcion_programa)-1])
                                print "Nombre      : " + programa_elegido[1]
                                print "Institucion :" + programa_elegido[2]
                                nombre_carrera = ""
                                cur5 = conn.cursor()
                                cur5.execute("select m.id_programa1 , c.nombre , c.area_estudio ,i.nombre_insti,p.nombre from carrera c , institucion i , matriculados m , programa p where p.id_carrera2 = c.id_carrera and m.id_programa1 = p.id_programa and m.ano_matricula = 2017 and i.numero_institucion = m.numero_institucion9 and i.nombre_insti ='" +programa_elegido[2] +"' and p.nombre ='"+ programa_elegido[1]+"'")
                                datos_elegidos_programa = []
                                nombre_carrera = cur5.fetchone()
                                cur5.close()
                                rorro = conn.cursor()
                                rorro.execute("select ap.ano_inicio_ap,ap.duracion_ap from acreditacion_programa ap, matriculados m where m.id_programa1 = ap.id_programa8 and m.id_programa1 = "+ str(nombre_carrera[0]))
                                rerre = rorro.fetchone()
                                rorro.close()
                                nato = conn.cursor()
                                nato.execute("select t.titulados_hombres + t.titulados_mujeres from titulados t, matriculados m where m.id_programa1 = t.id_programa7 and m.id_programa1 = "+ str(nombre_carrera[0]))
                                nate = nato.fetchone()

                                try:
                                    try:
                                        carlo = nate[0]
                                        print "Total titulados ultimo ano :" + str(carlo)

                                    except TypeError:
                                        pass
                                except IndexError:
                                    pass
                                nato.close()
                                pelo = conn.cursor()
                                pelo.execute("Select m.ingreso_psu +m.matriculados_otra_via from matriculados m where m.id_programa1 = "+ str(nombre_carrera[0]))
                                contadores = 1
                                razonnn = 0
                                razon_m = []
                                for i in pelo:
                                    if contadores <= 2:
                                        razon_m.append(i[0])
                                    contadores +=1
                                razonnn = razon_m[0] - razon_m[1]
                                razonnn = abs(razonnn)
                                print "Tasa de retencion ultimo ano " + str(razonnn)
                                pelo.close()
                                nato = conn.cursor()
                                nato.execute("select m.matriculados_otra_via  + m.ingreso_psu from matriculados m where m.ano_matricula = 2017 and m.id_programa1 = "+ str(nombre_carrera[0]))
                                el_popo = nato.fetchone()
                                el_pepe = el_popo[0]
                                print "Total de matriculados para el ultimo ano es " + str(el_pepe)
                                nato.close()
                                try:
                                    print "Acreditado desde el " + str(rerre[0]) + " hasta el " + str(rerre[0]+rerre[1])
                                except TypeError:
                                    pass
                                print "Carrera     : " + nombre_carrera[1]
                                cur = conn.cursor()
                                cur.execute("select m.id_sede9  from programa p, institucion i , matriculados m where i.numero_institucion = m.numero_institucion9 and m.id_programa1 = p.id_programa  and  m.ano_matricula = 2017 and p.nombre = '"+ programa_elegido[1] +"' and i.nombre_insti = '"+programa_elegido[2] +"'")
                                for i in cur:
                                    datos_elegidos_programa.append(i)

                                contador_sedess = 1
                                for i in datos_elegidos_programa:
                                    print "sede  " + str(contador_sedess) + "de id :" + str(i[0])
                                    contador_sedess +=1


                                cur.close()
                            except TypeError:
                                print " OPPS algo salio mal \nRetornando..."
                                continue
                        if opcionnnn == "4":
                            try:
                                try:
                                    lista_a_trabajar = []
                                    cur4 = conn.cursor()
                                    numeroo = raw_input("Ingrese numero aqui :")
                                    progama_elegidoo = (programas_a_mostrar_nuevo)[int(numeroo)-1]
                                    cur4.execute("select distinct on(m.ano_matricula) m.id_programa1,m.cnt_muj,m.cnt_homb,m.ano_matricula from matriculados m , institucion i, programa p where p.id_programa = m.id_programa1 and i.numero_institucion = m.numero_institucion9 and i.nombre_insti = '"+ str(progama_elegidoo[2])   +"' and p.nombre = '"+ str(progama_elegidoo[1])  +"'")
                                    for p in cur4:
                                        lista_a_trabajar.append(p)
                                    cnt_barras = len(lista_a_trabajar)
                                    etiquetas = []
                                    valores_hombres = []
                                    valores_mujeres = []
                                    anono = []
                                    for i in lista_a_trabajar:
                                        etiquetas.append(i[3])
                                    for p in lista_a_trabajar:
                                        valores_hombres.append(p[2])
                                        valores_mujeres.append(p[1])
                                        anono.append(p[3])
                                    x_pos = range(len(lista_a_trabajar))

                                    plt.bar(x_pos, valores_hombres, align='center', alpha=0.5)
                                    plt.xticks(x_pos, anono)
                                    plt.ylabel('anos')
                                    plt.title('Evolucion hombres')
                                    plt.show()
                                    plt.bar(x_pos, valores_mujeres, align='center', alpha=0.5)
                                    plt.xticks(x_pos, anono)
                                    plt.ylabel('anos')
                                    plt.title('Evolucion mujeres')
                                    plt.show()
                                except IndexError:
                                    print "no se encontro ese elemento \nRetornando"
                            except ValueError:
                                print"Ooops Algo Salio mal \nRetornando..."
                        if opcionnnn == "5":
                            try:
                                try:
                                    print "Ingrese numero de programa a ver info"
                                    opcion_programa = raw_input()
                                    programa_elegido = (programas_a_mostrar_nuevo[int(opcion_programa) - 1])
                                    cor = conn.cursor()
                                    cor.execute("select m.id_programa1 , c.nombre , c.area_estudio ,i.nombre_insti,p.nombre from carrera c , institucion i , matriculados m , programa p where p.id_carrera2 = c.id_carrera and m.id_programa1 = p.id_programa and m.ano_matricula = 2017 and i.numero_institucion = m.numero_institucion9 and i.nombre_insti ='" +programa_elegido[2] +"' and p.nombre ='"+ programa_elegido[1]+"'")
                                    nombre_carrera = cor.fetchone()
                                    cor.close()
                                    altura = []
                                    anos_altura = []
                                    cur = conn.cursor()
                                    cur.execute("select titulados_hombres+titulados_mujeres,ano_titulo from titulados where id_programa7 ="+str(nombre_carrera[0]))
                                    for i in cur:
                                        altura.append(i[0])
                                        anos_altura.append(i[1])
                                    if len(anos_altura) >=1:
                                        plt.bar(anos_altura,altura)
                                        plt.title("Titulados Historicos para el programa" + str(nombre_carrera[1]))
                                        plt.show()
                                    else:
                                        print"No se encontraron datos para ese programa \n Retornando...\n Probar escribiendo 'Ing' y usando el numero 481.."
                                except IndexError:
                                    print "No se encontro programa...\nRetornando\n Probar escribiendo 'Ing' y usando el numero 481.."
                            except TypeError:
                                print "no hay datos para es programa... \n retornando\n Probar escribiendo 'Ing' y usando el numero 481.."
                        if opcionnnn == "2":
                           loopprograma = False
                           loopclase9 = False
                        if opcionnnn== "6":
                            try :
                                print "Grafico que contiene el total de carreras y sus jornadas  para la carrera del programa elegido"
                                lista_a_trabajar = []
                                cur4 = conn.cursor()
                                numeroo = raw_input("Ingrese numero de programa aqui aqui :")
                                progama_elegidoo = (programas_a_mostrar_nuevo)[int(numeroo) - 1]
                                cur4.execute("select c.nombre from carrera c, programa p where p.id_carrera2 = c.id_carrera and p.nombre = '" + str(progama_elegidoo[1]) + "'")
                                nom = cur4.fetchone()
                                cur = conn.cursor()
                                anos = []
                                ekis = []
                                cur.execute("select sum(m.matriculados_otra_via + m.ingreso_psu) , m.ano_matricula from programa p , matriculados m , carrera c where c.nombre = '"+ nom[0]  +"'and c.id_carrera = p.id_carrera2 and m.id_programa1 = p.id_programa group by m.ano_matricula order by m.ano_matricula")
                                for i in cur:
                                    anos.append(i[1])
                                    ekis.append(i[0])
                                plt.plot(anos, ekis, label=nom[0])
                                cur.close()
                                cur = conn.cursor()
                                cur.execute("select m.min_pon_psulm from matriculados m , programa p, carrera c where p.id_programa = m.id_programa1 and c.id_carrera = p.id_carrera2 and c.nombre = '"+ nom[0]   +"'")
                                min_min = cur.fetchone()
                                cur.close()
                                cur = conn.cursor()
                                cur.execute("select sum(m.ingreso_psu + m.matriculados_otra_via),m.ano_matricula from matriculados m , programa p, carrera c where c.id_carrera = p.id_carrera2 and c.nombre = '"+ nom[0]  +"' and p.id_programa = m.id_programa1 and  m.min_pon_psulm >= "+ str(int(min_min[0])) +" group by m.ano_matricula order by m.ano_matricula")
                                anoss = []
                                ekiss = []
                                for y in cur:
                                    anoss.append(y[1])
                                    ekiss.append(y[0])
                                plt.plot(anoss,ekiss ,  label = "Evolucion carreras con ese nombre ,  y ptje min superior")
                                plt.ylabel("Cantidad de matriculados")
                                plt.title("Evolucion matriculados por carrera elegida")
                                plt.legend()
                                plt.show()
                                cur.close()
                            except TypeError:
                                print "OOps algo salio mal retornando..."

                        if opcionnnn == "3":
                            loopclase9 = False
                            loopMenu = False
                            loopprograma = False
                        if opcionnnn != "1" and opcionnnn != "2" and opcionnnn != "3" and opcionnnn != "4" and opcionnnn != "5" and opcionnnn != "6":
                            print "OOPS opcion ingresada no valida \nRetornando..."
            if opcionnnnn == "2":
                pass

            if opcionnnnn == "3":
                loopMenu = False
                loopclase9 = False

            if opcionnnnn != "1" and opcionnnnn != "2" and opcionnnnn != 3:
                print " OPPPS ALGO SALIO MAL \nretornando..."
                continue

    if opcion == "3":
        loopreportes = True
        while(loopreportes):
            print "Inregese opcion a contninuacion \n\t [1] = Area de conocimiento que mas a aumentado su arancel \n\t [2] = Top 10 ratio alumnos /profesor docente medico o doctores jornada completa \n\t [3] = Grafico acreditacion, gratuidad \n\t [4] = Grafico evolucion docentes doctores y docentes medicos \n\t [5] = Ver Evolucion Matriculas Por Tipo Institucion \n\t [6] = Volver al menu \n\t [7] = Salir del Programa \n\t [8] = Ver evolucion matriculas segun area del conocimiento \n\t [9] = Order mayor porcentaje sobre eleccion usuario"
            opcionreporte = raw_input()
            if opcionreporte == "1":
                curr = conn.cursor()
                curr.execute("select distinct c.area_estudio from carrera c ")
                cont = 1
                areas = []
                for i in curr:
                    print str(cont)+ " " +str(i[0])
                    cont += 1
                    areas.append(i[0])
                curr.close()
                opcion_area = raw_input("Ingrese numero de area que desea ver :")
                try:
                    int(opcion_area)
                    area_elegida = areas[int(opcion_area)- 1]
                    print "Area elegida : " + area_elegida
                    curr = conn.cursor()
                    diferencias = []
                    diferencias_a_mostrar = []
                    la_real = []
                    print "Imprimiendo los 10 programas con mayor variacion porcentual de valor arancel"
                    curr.execute("  select cast((cast(m.v_arancel as real) - cast( y.v_arancel as real))/(cast (y.v_arancel as real)) as real)  as diferencia,y.v_arancel ,y.id_programa1,c.area_estudio,p.nombre from (select m.v_arancel,m.id_programa1  from matriculados m where m.ano_matricula = 2012 and m.v_arancel != 0) y , carrera c,programa p ,matriculados m where m.id_programa1 = y.id_programa1 and m.ano_matricula = 2017 and m.v_arancel != 0 and p.id_programa = m.id_programa1 and p.id_programa = y.id_programa1 and p.id_carrera2 = c.id_carrera  and c.area_estudio = "+ "'"+area_elegida+"'" +" order by diferencia desc limit 10" )
                    for i in curr:
                        print str(i[2]) + " " + i[4]
                    curr.close()
                except ValueError:
                    print "opcion ingresada no valida"
            if opcionreporte =="2":
                loopratio = True
                while loopratio:
                    print"Eliga un tipo \n\t 1 = C.F.T \n\t 2 = Univ \n\t 3 = I.P \n\t 4 = Volver al menu reportes"
                    tipoo = raw_input("ingrese aca :")

                    if tipoo == "1":
                        curt = conn.cursor()
                        list = [["Lugar","Nombre","Ratio","Tipo"]]
                        contadorr = 1
                        curt.execute("select t.sim/p.sum as ratio,p.numero_institucion,p.tipo,i.nombre_insti from  (select sum(m.matriculados_otra_via + m.ingreso_psu)as sim,m.numero_institucion9,i.tipo from institucion i ,matriculados m where m.numero_institucion9  = i.numero_institucion and m.ano_matricula =2017 group by m.numero_institucion9,i.tipo) t ,  (select sum(ds.n_dd_j_c + ds.n_dm_j_c) as sum , i.tipo, i.numero_institucion from institucion i , datos_profesor_sede ds,sede s where ds.ano_profe = 2017 and ds.id_sede8 = s.id_sede and s.id_institucion1 = i.numero_institucion group by i.tipo,i.numero_institucion) p, institucion i where p.sum != 0 and i.numero_institucion = p.numero_institucion and t.numero_institucion9 = p.numero_institucion and p.tipo = '" +"(c) C.F.T." +"' order by ratio desc limit 10")
                        for i in curt:
                            list.append([contadorr,i[3],(i[0]),i[2]])
                            contadorr +=1
                        print_table(list)
                        curt.close()
                    if tipoo == "2":
                        curt = conn.cursor()
                        contadorr = 1
                        list = [["Lugar","Nombre","Ratio","Tipo"]]
                        curt.execute("select t.sim/p.sum as ratio,p.numero_institucion,p.tipo,i.nombre_insti from  (select sum(m.matriculados_otra_via + m.ingreso_psu)as sim,m.numero_institucion9,i.tipo from institucion i ,matriculados m where m.numero_institucion9  = i.numero_institucion and m.ano_matricula =2017 group by m.numero_institucion9,i.tipo) t ,  (select sum(ds.n_dd_j_c + ds.n_dm_j_c) as sum , i.tipo, i.numero_institucion from institucion i , datos_profesor_sede ds,sede s where ds.ano_profe = 2017 and ds.id_sede8 = s.id_sede and s.id_institucion1 = i.numero_institucion group by i.tipo,i.numero_institucion) p, institucion i where p.sum != 0 and i.numero_institucion = p.numero_institucion and t.numero_institucion9 = p.numero_institucion and p.tipo = '" + "(a) Univ."+"' order by ratio desc limit 10")
                        for i in curt:
                            list.append([contadorr,i[3],(i[0]),i[2]])
                            contadorr +=1
                        print_table(list)
                        curt.close()
                    if tipoo == "3":
                        curt = conn.cursor()
                        contadorr = 1
                        list = [["Lugar","Nombre","Ratio","Tipo"]]
                        curt.execute("select t.sim/p.sum as ratio,p.numero_institucion,p.tipo,i.nombre_insti from  (select sum(m.matriculados_otra_via + m.ingreso_psu)as sim,m.numero_institucion9,i.tipo from institucion i ,matriculados m where m.numero_institucion9  = i.numero_institucion and m.ano_matricula =2017 group by m.numero_institucion9,i.tipo) t ,  (select sum(ds.n_dd_j_c + ds.n_dm_j_c) as sum , i.tipo, i.numero_institucion from institucion i , datos_profesor_sede ds,sede s where ds.ano_profe = 2017 and ds.id_sede8 = s.id_sede and s.id_institucion1 = i.numero_institucion group by i.tipo,i.numero_institucion) p, institucion i where p.sum != 0 and i.numero_institucion = p.numero_institucion and t.numero_institucion9 = p.numero_institucion and p.tipo = '" + "(b) I.P."+"' order by ratio desc limit 10")
                        for i in curt:
                            list.append([contadorr,i[3],(i[0]),i[2]])
                            contadorr +=1
                        print_table(list)
                        curt.close()
                    if tipoo == "4":
                        loopratio = False

            if opcionreporte == "3":
                con = conn.cursor()
                xe = []
                xe_ano = []
                con.execute("select count(di.numero_institucion7),di.ano_dato,i.tipo from institucion i , datosinstitucion di where di.numero_institucion7 = i.numero_institucion and di.gratuidad = '(a)Adscritas a Gratuidad'  and i.tipo ='"+    "(c) C.F.T."    +"' group by di.ano_dato,i.tipo")
                for i in con:
                    xe.append(i[0])
                    xe_ano.append(i[1])
                plt.plot(xe_ano,xe,label = " gratuitad (c) C.F.T.")
                con.close()
                con = conn.cursor()
                xe = []
                xe_ano = []
                con.execute(
                    "select count(di.numero_institucion7),di.ano_dato,i.tipo from institucion i , datosinstitucion di where di.numero_institucion7 = i.numero_institucion and di.gratuidad = '(a)Adscritas a Gratuidad'  and i.tipo ='" + "(a) Univ." + "' group by di.ano_dato,i.tipo")
                for i in con:
                    xe.append(i[0])
                    xe_ano.append(i[1])
                plt.plot(xe_ano, xe, label=" gratuitad (c) (a) Univ.")
                con.close()
                con = conn.cursor()
                xe = []
                xe_ano = []
                con.execute(
                    "select count(di.numero_institucion7),di.ano_dato,i.tipo from institucion i , datosinstitucion di where di.numero_institucion7 = i.numero_institucion and di.gratuidad = '(a)Adscritas a Gratuidad'  and i.tipo ='" + "(b) I.P." + "' group by di.ano_dato,i.tipo")
                for i in con:
                    xe.append(i[0])
                    xe_ano.append(i[1])
                plt.plot(xe_ano, xe, label=" gratuitad (c) (b) I.P.")

                con.close()
                rin = []
                con = conn.cursor()
                con.execute("select count(ai.numero_institucion5),i.tipo  from acreditacion_institucion ai , institucion i where i.numero_institucion = ai.numero_institucion5 and ai.ano_inicio =2011 and i.tipo = '(a) Univ.' group by i.tipo")
                trer = con.fetchone()
                rin.append(trer[0])
                con.close()
                con = conn.cursor()

                con.execute(
                    "select count(ai.numero_institucion5),i.tipo  from acreditacion_institucion ai , institucion i where i.numero_institucion = ai.numero_institucion5 and ai.ano_inicio =2012 and i.tipo = '(a) Univ.' group by i.tipo")
                trer = con.fetchone()
                rin.append(trer[0])
                con.close()
                con = conn.cursor()

                con.execute(
                    "select count(ai.numero_institucion5),i.tipo  from acreditacion_institucion ai , institucion i where i.numero_institucion = ai.numero_institucion5 and ai.ano_inicio =2013 and i.tipo = '(a) Univ.' group by i.tipo")
                trer = con.fetchone()
                rin.append(trer[0])
                con.close()
                con = conn.cursor()

                con.execute(
                    "select count(ai.numero_institucion5),i.tipo  from acreditacion_institucion ai , institucion i where i.numero_institucion = ai.numero_institucion5 and ai.ano_inicio =2014 and i.tipo = '(a) Univ.' group by i.tipo")
                trer = con.fetchone()
                rin.append(trer[0])
                con.close()
                con = conn.cursor()

                con.execute(
                    "select count(ai.numero_institucion5),i.tipo  from acreditacion_institucion ai , institucion i where i.numero_institucion = ai.numero_institucion5 and ai.ano_inicio =2015 and i.tipo = '(a) Univ.' group by i.tipo")
                rtrer = con.fetchone()
                rin.append(trer[0])
                con.close()
                con = conn.cursor()

                con.execute(
                    "select count(ai.numero_institucion5),i.tipo  from acreditacion_institucion ai , institucion i where i.numero_institucion = ai.numero_institucion5 and ai.ano_inicio =2016 and i.tipo = '(a) Univ.' group by i.tipo")
                trer = con.fetchone()
                rin.append(trer[0])
                con.close()
                con = conn.cursor()

                con.execute(
                    "select count(ai.numero_institucion5),i.tipo  from acreditacion_institucion ai , institucion i where i.numero_institucion = ai.numero_institucion5 and ai.ano_inicio =2017  and i.tipo = '(a) Univ.'group by i.tipo")
                trer = con.fetchone()
                rin.append(trer[0])
                con.close()
                con = conn.cursor()

                con.execute(
                    "select count(ai.numero_institucion5),i.tipo  from acreditacion_institucion ai , institucion i where i.numero_institucion = ai.numero_institucion5 and ai.ano_inicio =2018 and i.tipo = '(a) Univ.' group by i.tipo")
                trer = con.fetchone()
                rin.append(trer[0])
                con.close()
                ron = [2011,2012,2013,2014,2015,2016,2017,2018]
                plt.plot(ron,rin,label = "Introduccion a la acreditacion  (a) Univ.")

                rin = []

                con.close()
                con = conn.cursor()

                con.execute(
                    "select count(ai.numero_institucion5),i.tipo  from acreditacion_institucion ai , institucion i where i.numero_institucion = ai.numero_institucion5 and ai.ano_inicio =2012 and i.tipo = '(c) C.F.T.' group by i.tipo")
                trer = con.fetchone()
                rin.append(trer[0])
                con.close()
                con = conn.cursor()

                con.execute(
                    "select count(ai.numero_institucion5),i.tipo  from acreditacion_institucion ai , institucion i where i.numero_institucion = ai.numero_institucion5 and ai.ano_inicio =2013 and i.tipo = '(c) C.F.T.' group by i.tipo")
                trer = con.fetchone()
                rin.append(trer[0])
                con.close()

                con = conn.cursor()

                con.execute(
                    "select count(ai.numero_institucion5),i.tipo  from acreditacion_institucion ai , institucion i where i.numero_institucion = ai.numero_institucion5 and ai.ano_inicio =2015 and i.tipo = '(c) C.F.T.' group by i.tipo")
                rtrer = con.fetchone()
                rin.append(trer[0])
                con.close()
                con = conn.cursor()

                con.execute(
                    "select count(ai.numero_institucion5),i.tipo  from acreditacion_institucion ai , institucion i where i.numero_institucion = ai.numero_institucion5 and ai.ano_inicio =2016 and i.tipo = '(c) C.F.T.' group by i.tipo")
                trer = con.fetchone()
                rin.append(trer[0])
                con.close()
                con = conn.cursor()

                con.execute(
                    "select count(ai.numero_institucion5),i.tipo  from acreditacion_institucion ai , institucion i where i.numero_institucion = ai.numero_institucion5 and ai.ano_inicio =2017  and i.tipo = '(c) C.F.T.'group by i.tipo")
                trer = con.fetchone()
                rin.append(trer[0])
                con.close()
                con = conn.cursor()

                con.execute(
                    "select count(ai.numero_institucion5),i.tipo  from acreditacion_institucion ai , institucion i where i.numero_institucion = ai.numero_institucion5 and ai.ano_inicio =2018 and i.tipo = '(c) C.F.T.' group by i.tipo")
                trer = con.fetchone()
                rin.append(trer[0])
                con.close()
                ron = [ 2012, 2013, 2015, 2016, 2017, 2018]
                plt.plot(ron, rin, label="Introduccion a la acreditacion  (c) C.F.T.")
                ##

                rin = []

                con.close()
                con = conn.cursor()

                con.execute(
                    "select count(ai.numero_institucion5),i.tipo  from acreditacion_institucion ai , institucion i where i.numero_institucion = ai.numero_institucion5 and ai.ano_inicio =2013 and i.tipo = '(b) I.P.' group by i.tipo")
                trer = con.fetchone()
                rin.append(trer[0])
                con.close()
                con = conn.cursor()

                con.execute(
                    "select count(ai.numero_institucion5),i.tipo  from acreditacion_institucion ai , institucion i where i.numero_institucion = ai.numero_institucion5 and ai.ano_inicio =2014 and i.tipo = '(b) I.P.' group by i.tipo")
                trer = con.fetchone()
                rin.append(trer[0])
                con.close()

                con = conn.cursor()

                con.execute(
                    "select count(ai.numero_institucion5),i.tipo  from acreditacion_institucion ai , institucion i where i.numero_institucion = ai.numero_institucion5 and ai.ano_inicio =2015 and i.tipo = '(b) I.P.' group by i.tipo")
                rtrer = con.fetchone()
                rin.append(trer[0])
                con.close()
                con = conn.cursor()

                con.execute(
                    "select count(ai.numero_institucion5),i.tipo  from acreditacion_institucion ai , institucion i where i.numero_institucion = ai.numero_institucion5 and ai.ano_inicio =2016 and i.tipo = '(b) I.P.' group by i.tipo")
                trer = con.fetchone()
                rin.append(trer[0])
                con.close()
                con = conn.cursor()

                con.execute(
                    "select count(ai.numero_institucion5),i.tipo  from acreditacion_institucion ai , institucion i where i.numero_institucion = ai.numero_institucion5 and ai.ano_inicio =2017  and i.tipo = '(b) I.P.'group by i.tipo")
                trer = con.fetchone()
                rin.append(trer[0])
                con.close()

                ron = [ 2013, 2014, 2015, 2016, 2017]
                plt.plot(ron, rin, label="Introduccion a la acreditacion  (b) I.P.")
                ##
                plt.ylabel("Cantidad")
                plt.legend()
                plt.show()
            if opcionreporte == "5":
                curr = conn.cursor()
                curr.execute("select avg(m.v_matricula),i.tipo,m.ano_matricula from institucion i , matriculados m where m.numero_institucion9 = i.numero_institucion and m.v_matricula != 0 group by i.tipo , m.ano_matricula order by m.ano_matricula")
                univ = []
                cft = []
                tp = []
                for i in curr:
                    if i[1] == "(a) Univ.":
                        univ.append(i)
                    if i[1] == "(b) I.P.":
                        tp.append(i)
                    if i[1] == "(c) C.F.T.":
                        cft.append(i)
                curr.close()
                ano_cft = []
                valores_uni = []
                valores_tp = []
                ano_tp = []
                for i in tp:
                    ano_tp.append(i[2])
                    valores_tp.append((i[0]))
                ano_univ = []
                for i in univ:
                    valores_uni.append(i[0])
                    ano_univ.append(i[2])
                valores_cft = []
                for i in cft:
                    ano_cft.append(i[2])
                    valores_cft.append((i[0]))
                plt.plot(ano_univ,valores_uni,label="Univeridad")
                plt.ylabel("cantidad")
                plt.plot(ano_cft, valores_cft,label = "C.F.T")
                plt.plot(ano_tp, valores_tp,label = "I.P")
                plt.title('Evolucion ')
                plt.legend()
                plt.show()
            if opcionreporte == "6":
                loopreportes = False
                print "Retornando..."
            if opcionreporte == "9":
                puntaje_usuario = raw_input("Ingrese puntaje ")
                try :
                    yy = int(puntaje_usuario)
                    cur = conn.cursor()
                    cur.execute("select i.nombre_insti, t.numero_institucion9,cast(t.chico as real)/cast(h.total as real) as ratio from  (select count(m.id_programa1)as chico,m.numero_institucion9 from matriculados m where m.ano_matricula = 2017 and m.min_pon_psulm >= "+str(yy) +" group by m.numero_institucion9)t, (select count(m.id_programa1) as total,m.numero_institucion9  from matriculados m where  m.ano_matricula =2017 group by m.numero_institucion9) h, institucion i where t.numero_institucion9 = h.numero_institucion9 and i.numero_institucion = t.numero_institucion9 order by ratio desc limit 5")
                    for i in cur:
                        print i[0] + "   " + "Ratio : "+str(i[2])
                    cur.close()
                except ValueError:
                    print "OOps algo salio mal.. \n Retornando...."
            if opcionreporte == "4":
                cur = conn.cursor()
                xi = []
                ano_xi = []
                cur.execute("select cast ((cast(sum(ds.n_dd_j_c+ds.n_dd_j_m+ds.n_dd_j_h+ds.n_dm_j_c+ds.n_dm_j_h+ds.n_dm_j_m) as real)/(sum(ds.n_d_j_c))) as real) ,ds.ano_profe , i.tipo from datos_profesor_sede ds,sede s , institucion i where i.numero_institucion = s.id_institucion1 and i.tipo = '" +"(c) C.F.T." +"' and ds.n_d_j_c != 0 and ds.id_sede8 = s.id_sede  group by ds.ano_profe,i.tipo order by ds.ano_profe")
                for a in cur:
                    xi.append(a[0])
                    ano_xi.append(a[1])
                plt.plot(ano_xi,xi,label = '(c) C.F.T.')
                cur.close()
                cur = conn.cursor()
                xi = []
                ano_xi = []
                cur.execute(
                    "select cast ((cast(sum(ds.n_dd_j_c+ds.n_dd_j_m+ds.n_dd_j_h+ds.n_dm_j_c+ds.n_dm_j_h+ds.n_dm_j_m) as real)/(sum(ds.n_d_j_c))) as real) ,ds.ano_profe , i.tipo from datos_profesor_sede ds,sede s , institucion i where i.numero_institucion = s.id_institucion1 and i.tipo = '" + "(a) Univ." + "' and ds.n_d_j_c != 0 and ds.id_sede8 = s.id_sede  group by ds.ano_profe,i.tipo order by ds.ano_profe")
                for a in cur:
                    xi.append(a[0])
                    ano_xi.append(a[1])
                plt.plot(ano_xi, xi, label='(a) Univ.')
                cur.close()
                cur = conn.cursor()
                xi = []
                ano_xi = []
                cur.execute(
                    "select cast ((cast(sum(ds.n_dd_j_c+ds.n_dd_j_m+ds.n_dd_j_h+ds.n_dm_j_c+ds.n_dm_j_h+ds.n_dm_j_m) as real)/(sum(ds.n_d_j_c))) as real) ,ds.ano_profe , i.tipo from datos_profesor_sede ds,sede s , institucion i where i.numero_institucion = s.id_institucion1 and i.tipo = '" + "(b) I.P." + "' and ds.n_d_j_c != 0 and ds.id_sede8 = s.id_sede  group by ds.ano_profe,i.tipo order by ds.ano_profe")
                for a in cur:
                    xi.append(a[0])
                    ano_xi.append(a[1])
                plt.plot(ano_xi, xi, label='(b) I.P.')
                cur.close()
                cur = conn.cursor()
                xi = []
                ano_xi = []
                cur.execute(
                    "select cast ((cast(sum(ds.n_dd_j_c+ds.n_dd_j_m+ds.n_dd_j_h+ds.n_dm_j_c+ds.n_dm_j_h+ds.n_dm_j_m) as real)/(sum(ds.n_d_j_c))) as real) ,ds.ano_profe , i.tipo from datos_profesor_sede ds,sede s , institucion i where i.numero_institucion = s.id_institucion1 and i.tipo = '" + "FFAA" + "' and ds.n_d_j_c != 0 and ds.id_sede8 = s.id_sede  group by ds.ano_profe,i.tipo order by ds.ano_profe")
                for a in cur:
                    xi.append(a[0])
                    ano_xi.append(a[1])
                plt.plot(ano_xi, xi, label='FFAA')
                cur.close()

                plt.ylabel("Ratio")
                plt.legend()
                plt.title("Evolucion")
                plt.show()



            if opcionreporte == "7":
                loopreportes = False
                loopMenu = False
            if opcionreporte == "8":
                curr = conn.cursor()
                are = []
                curr.execute("select distinct c.area_estudio from carrera c ")
                for i in curr:
                    are.append(i[0])
                curr.close()
                for i in are:
                    curo3 = conn.cursor()
                    curo3.execute("select avg(m.v_matricula),m.ano_matricula,c.area_estudio from carrera c,programa p , matriculados m where m.id_programa1 = p.id_programa and c.id_Carrera = p.id_carrera2 and c.area_estudio ="+ "'"+  i  +"'"+ "and m.v_matricula != 0 group by c.area_estudio , m.ano_matricula  order by m.ano_matricula ")
                    listaa = []
                    ano_area = []
                    curosama = []
                    namee = curo3.fetchone()
                    label_names = []
                    for yo in curo3:
                        curosama.append(yo)
                        listaa.append(int(yo[0]))
                        ano_area.append(yo[1])
                        label_names.append(yo[2])
                    curo3.close()
                    try:
                        plt.plot(ano_area,listaa,label =namee[2])
                    except TypeError:
                        pass

                plt.ylabel("Cantidad matriculados")
                plt.title("Evolucion Areas")
                plt.legend()
                plt.show()

    if opcion == "4":
        loopranking = True
        while loopranking:
            print "Bienvenido al Ranking de instituciones"
            print " [1] = Universidades \n [2] = Centros de formacion tecnica \n [3] = Institutos Profecionales \n [4] = FFAA \n [5] = Volver al menu \n [6] = Salir"
            ranking = []
            try:
                        # Parte 1 , puntaje ranking e igualdad de generos
                        # el de igualdad de generos = 10%
                        # clasificacion puntajes  = 10# total  = 20%
                        opcionranking = raw_input("Ingrse opcion aqui :")
                        ano_ranking = raw_input("Ingrese Ano :")
                        int(ano_ranking)
                        if opcionranking == "1" or opcionranking == "2" or opcionranking == "3":
                            totales = []
                            if opcionranking== "1":
                                tipo ='(a) Univ.'
                            if opcionranking == "2":
                                tipo = '(c) C.F.T.'
                            if opcionranking =="3":
                                tipo = '(b) I.P.'
                            totales = []
                            print "Ranking de "+ str(tipo)
                            cur2 = conn.cursor()
                            cur2.execute("Select distinct m.numero_institucion9 from institucion i,matriculados m where i.numero_institucion = m.numero_institucion9 and i.tipo = '" + tipo + "'")
                            for i in cur2:
                                totales.append((i[0]))
                            cur2.close()
                            for t in totales:
                                sub = [t, 0]
                                ranking.append(sub)
                            cur2.close()
                            looprnk = True
                            while looprnk:
                                print"[1]  Calidad alumnos \n[2]  Calidad Doscentes \n[3]  Retencion \n[4]  Acreditacion \n[5]  Complejidad institucional \n[6]  Ranking Global acumulado \n[7]  Volver al menu  \n[8]  Salir"

                                opcionrnk = raw_input("Ingrese Opcion aqui :")
                                if opcionrnk == "1":
                                    cur = conn.cursor()
                                    print "\nRanking puntajes PSU\n"
                                    listaa = []
                                    ptje_comparar = 0
                                    r_puntaje = [["Lugar ranking","Nombre","Puntaje obtenido","total"]]
                                    cur.execute(" select o.numero_institucion9 , (o.mini + o.promedioRNK) as loco  from (select m.numero_institucion9, avg(m.min_pon_psulm) as mini, avg((m.max_ranking + m.min_ranking)/2)  as promedioRNK from institucion i , matriculados m  where m.numero_institucion9 =i.numero_institucion and i.tipo = '"+tipo+"'  and m.max_ranking >0 and m.min_ranking>0 and m.ano_matricula = "+ str(ano_ranking) +" group by m.numero_institucion9 )o order by loco desc")
                                    for i in cur:
                                        listaa.append(i)
                                    conta = 1

                                    try:
                                        ptje_comparar = (listaa[0])[1]
                                        totall = len(listaa)+1
                                    except IndexError:
                                        pass
                                    for p in listaa:
                                        for t in ranking:
                                            if p[0] == t[0]:
                                                puntaje_a_dar = 100*p[1]/ptje_comparar
                                                name = get_name(p[0])
                                                tuplilla = [conta,name,puntaje_a_dar,p[1]/2]
                                                r_puntaje.append(tuplilla)
                                        conta +=1
                                    print_table(r_puntaje)

                                    cur = conn.cursor()
                                    print "\nRanking puntajes ranking\n"
                                    listaa = []
                                    ptje_comparar = 0
                                    r_puntaje = [["Lugar ranking", "Nombre", "Puntaje obtenido", "total"]]
                                    cur.execute(
                                        " select o.numero_institucion9 , (o.mini + o.promedioRNK) as loco  from (select m.numero_institucion9, avg(m.min_pon_psulm) as mini, avg((m.max_pon_psulm + m.min_pon_psulm)/2)  as promedioRNK from institucion i , matriculados m  where m.numero_institucion9 =i.numero_institucion and i.tipo = '"+tipo+"' and m.min_pon_psulm >0 and m.max_pon_psulm >0  and m.ano_matricula = " + str(ano_ranking) + " group by m.numero_institucion9 )o order by loco desc")
                                    for i in cur:
                                        listaa.append(i)
                                    conta = 1

                                    try:
                                        ptje_comparar = (listaa[0])[1]
                                        totall = len(listaa) + 1
                                    except IndexError:
                                        pass
                                    for p in listaa:
                                        for t in ranking:
                                            if p[0] == t[0]:
                                                puntaje_a_dar = 100 * p[1] / ptje_comparar
                                                name = get_name(p[0])

                                                tuplilla = [conta, name, puntaje_a_dar, p[1] / 2]
                                                r_puntaje.append(tuplilla)
                                        conta += 1
                                    print_table(r_puntaje)

                                    ptje_comparar =  0
                                    cur.close()
                                    cur = conn.cursor()
                                    cur.execute("select abs(avg(m.cnt_homb - m.cnt_muj))  as hola, m.numero_institucion9 from matriculados m, institucion i where (m.cnt_homb != 0 or m.cnt_muj != 0) and i.numero_institucion = m.numero_institucion9 and i.tipo = '"+str(tipo)+"' and m.ano_matricula = "+ str(ano_ranking) +" group by m.numero_institucion9 order by hola desc")
                                    listaa = []
                                    conta = 0
                                    print "\nRanking Diferencia de generos\n"
                                    r_difgeneros =[["Lugar ranking","Nombre","Puntaje obtenido","Diferencia Generos"]]
                                    for i in cur:
                                        listaa.append(i)
                                    ptje_comparar = 1
                                    for i in listaa:
                                        for t in ranking:
                                            if i[1] == t[0]:
                                                puntaje_a_dar = 100 *conta / len(listaa)
                                                name = get_name(i[1])
                                                tuplango = [len(listaa)-conta,name,puntaje_a_dar,i[0]]
                                                r_difgeneros.append(tuplango)
                                        conta += 1
                                    print_table(r_difgeneros)
                                    cur.close()
                                if opcionrnk == "2":
                                    print "Ranking Docencentes estudiantes"
                                    r_matriDoce = [["Lugar ranking","Nombre","Puntaje obtenido","Ratio"]]
                                    # el ratio alumnos matriculados por docente jornada completa vale un 12.5 %
                                    # el ratio alumnos matriculados por docente de especialidad medicao con doctorado vale un 12.5%
                                    cur = conn.cursor()
                                    ptje_comparar =0
                                    cur.execute("select (o.matri/o.doce) as ratio, o.numero_institucion9 from (select sum(cast((m.ingreso_psu + m.matriculados_otra_via) as real))  as matri, sum(cast(d.n_d_j_c as real)) as doce, m.numero_institucion9 from matriculados m , datos_profesor_sede d, institucion i where i.tipo = '"+str(tipo)+"' and i.numero_institucion = m.numero_institucion9 and d.id_sede8 = m.id_sede9 and m.ano_matricula = "+  str(ano_ranking)+" group by m.numero_institucion9) o where o.doce != 0 order by ratio asc")
                                    listaa = []
                                    for i in cur:
                                        listaa.append(i)
                                    ptje_comparar = (listaa[len(listaa)- 1])[0]
                                    cur.close()
                                    conta = 0
                                    for t in listaa:
                                        for p in ranking:
                                            if t[1] == p[0]:
                                                puntaje_a_dar = 100 * t[0] / ptje_comparar
                                                name = get_name(t[1])
                                                tuplilla = [len(listaa)-conta,name, puntaje_a_dar,t[0]]
                                                r_matriDoce.append(tuplilla)
                                        conta += 1
                                    print_table(r_matriDoce)
                                    print "\nRanking Ratio Docentes medicos/magister Estudiante\n"
                                    r_matriDocemedi = [["Lugar ranking","Nombre","Puntaje obtenido","Ratio"]]
                                    cur = conn.cursor()
                                    cur.execute("select (o.matri/o.doce) as ratio, o.numero_institucion9 from (select sum(cast((m.ingreso_psu + m.matriculados_otra_via) as real))  as matri, sum(cast(d.n_dm_j_c+d.n_dm_j_c as real)) as doce, m.numero_institucion9 from matriculados m , datos_profesor_sede d, institucion i where i.tipo = '"+str(tipo)+"' and i.numero_institucion = m.numero_institucion9 and d.id_sede8 = m.id_sede9 and m.ano_matricula = "+str(ano_ranking)+"   group by m.numero_institucion9) o where o.doce != 0 order by ratio asc")
                                    listaa = []
                                    for i in cur:
                                        listaa.append(i)
                                    ptje_comparar = (listaa[len(listaa)-1])[0]
                                    cur.close()
                                    conta = 0
                                    for t in listaa:
                                        for p in ranking:
                                            if t[1] == p[0]:
                                                puntaje_a_dar = 100 * t[0] / ptje_comparar
                                                name = get_name(t[1])
                                                tuplilla = [len(listaa) - conta, name, puntaje_a_dar, t[0]]
                                                r_matriDocemedi.append(tuplilla)
                                        conta += 1
                                    cur.close()
                                    print print_table(r_matriDocemedi)
                                if opcionrnk == "3":
                                    cur = conn.cursor()
                                    print"\nRanking Retencion\n"
                                    ano_proximo = int(ano_ranking) + 1
                                    cur.execute("select ht.numero_institucion , sum(ht.orden) from (select h.id_programa1 ,h.orden , i.numero_institucion from (select n.nuevo - v.viejo as orden, v.id_programa1 from  (select sum(m.ingreso_psu + m.matriculados_otra_via) as nuevo, m.id_programa1 from matriculados m where m.ano_matricula = "+ str(ano_proximo) +" group by m.id_programa1) n ,(select sum(m.ingreso_psu + m.matriculados_otra_via) as viejo, m.id_programa1 from matriculados m where m.ano_matricula = "+ str(ano_ranking) +" group by m.id_programa1) v where v.id_programa1 = n.id_programa1 and v.viejo != 0 and n.nuevo != 0 order by orden asc)h , institucion i , sede s , programa_sede ps where h.id_programa1 = ps.id_programa2 and ps.id_sede2 = s.id_sede and s.id_institucion1 = i.numero_institucion and i.tipo = '"+tipo+"')ht group by ht.numero_institucion order by sum asc")
                                    listaa = []
                                    r_retencion = [["Lugar ranking","Nombre","Puntaje obtenido","Retencion"]]
                                    for i in cur:
                                        listaa.append(i)
                                    if len(listaa) !=0:
                                        ptje_comparar = (listaa[len(listaa)-1])[1]
                                        cur.close()
                                        conta = 1
                                        for t in listaa:
                                            for p in ranking:
                                                if t[0] == p[0]:
                                                    puntaje_a_dar = 100 * t[1] / ptje_comparar
                                                    name = get_name(t[1])
                                                    tuplilla = [len(listaa) - conta, name, puntaje_a_dar, t[1]]
                                                    r_retencion.append(tuplilla)
                                            conta += 1
                                    cur.close()
                                    print_table(r_retencion)
                                if opcionrnk == "5":
                                    cur=conn.cursor()
                                    print"\nRanking Cantidad de carreras para ano dado\n"
                                    listaa = []
                                    conta = 1
                                    r_carreras = []
                                    cur.execute("select count(c.id_carrera),m.numero_institucion9 from matriculados m , carrera c,programa p , institucion i where i.tipo = '"+tipo+"' and i.numero_institucion = m.numero_institucion9 and c.id_carrera = p.id_carrera2 and m.id_programa1 = p.id_programa and m.ano_matricula = "+ str(ano_ranking)+" group by m.numero_institucion9 order by count asc")
                                    for i in cur:
                                        listaa.append(i)
                                    ptje_comparar = (listaa[len(listaa)-1])[0]
                                    for t in listaa:
                                        for y in ranking:
                                            if t[1] == y[0]:
                                                name = get_name(t[1])
                                                puntaje_a_dar = 100 * t[0] / ptje_comparar
                                                tuplilla = [conta,name,int(puntaje_a_dar),t[0]]
                                                r_carreras.append(tuplilla)
                                        conta +=1
                                    cur.close()
                                    print_table(r_carreras)
                                    r_areas = [["Lugar","Nombre","Puntaje Obtenido","Cantidad areas cubiertas"]]
                                    cur = conn.cursor()
                                    listaa = []
                                    print "\nRanking Cantidad de areas cubiertas\n"
                                    cur.execute("select count(y.area_estudio) ,y.numero_institucion9 from (select distinct c.area_estudio,m.numero_institucion9 from matriculados m , carrera c,programa p , institucion i where i.tipo = '"+tipo+"' and i.numero_institucion = m.numero_institucion9 and c.id_carrera = p.id_carrera2 and m.id_programa1 = p.id_programa and m.ano_matricula = "+ str(ano_ranking)+")y group by y.numero_institucion9 order by count asc ")
                                    for t in cur:
                                        listaa.append(t)
                                    ptje_max = (listaa[len(listaa) -1])[0]
                                    for y in listaa:
                                        for u in ranking:
                                            if u[0] == y[1]:
                                                puntaje_a_dar = 100*y[0] /ptje_max
                                                name = get_name(u[0])
                                                tuplilla = [conta,name,y[0], int(puntaje_a_dar)]
                                                r_areas.append(tuplilla)
                                        conta +=1
                                    print_table(r_areas)
                                    cur.close()
                                if opcionrnk == "4":
                                    cur = conn.cursor()
                                    print "\nRanking Cantidad de anos acreditacion\n"
                                    cur.execute("select a.numero_institucion5,sum(a.duracion)summ  from acreditacion_institucion a, institucion i  where a.numero_institucion5 = i.numero_institucion and i.tipo = '"+tipo+"' group by a.numero_institucion5 order by summ desc")
                                    r_anos = [["Lugar","Nombre","Puntaje","Cantidad Anos"]]
                                    listaa = []
                                    conta =1
                                    for i in cur:
                                        listaa.append(i)
                                    puntaje_max = listaa[0][1]
                                    for i in listaa:
                                        for t in ranking:
                                            if i[0] == t[0]:
                                                puntaje_a_dar = 100*i[1]/puntaje_max
                                                name = get_name(i[0])
                                                tuplilla = [conta,name,int(puntaje_a_dar),i[1]]
                                                r_anos.append(tuplilla)
                                        conta +=1
                                    cur.close()
                                    print_table(r_anos)
                                    cur = conn.cursor()
                                    print "Ranking Numero de areas acreditadas \n Imprimeindo..."
                                    cur.execute("select a.numero_institucion5, sum(u.inv+i.vin+o.post)as summm from (select a.numero_institucion5,count(a.investigacion) as inv from acreditacion_institucion a left join institucion i  on a.numero_institucion5 = i.numero_institucion and i.tipo = '"+tipo+"' and a.investigacion = True group by a.numero_institucion5)u, (select a.numero_institucion5,count(a.vinculacion_con_el_medio)as vin from acreditacion_institucion a left join institucion i  on a.numero_institucion5 = i.numero_institucion and i.tipo = '"+tipo+"' and a.vinculacion_con_el_medio = True group by a.numero_institucion5 )i,(select a.numero_institucion5,count(a.docencia_postgrado)as post from acreditacion_institucion a left join institucion i on a.numero_institucion5 = i.numero_institucion and i.tipo = '"+tipo+"' and a.docencia_postgrado = True group by a.numero_institucion5 )o, acreditacion_institucion a where a.numero_institucion5 = u.numero_institucion5 and i.numero_institucion5 = u.numero_institucion5 and o.numero_institucion5 = u.numero_institucion5 group by a.numero_institucion5 order by summm asc")
                                    r_areas = [["Lugar","Nombre","Puntaje","Cantidad Areas"]]
                                    listaa = []
                                    conta= 1
                                    for p in cur:
                                        listaa.append(p)
                                    puntaje_a_dar = listaa[len(listaa) - 1][1]
                                    for i in listaa:
                                        for p in ranking:
                                            if p[0] == i[0]:
                                                puntaje_obt = 100 * i[1]/puntaje_a_dar
                                                name = get_name(p[0])
                                                tuplilla =[p[0],name,int(puntaje_obt),i[1]]
                                                r_areas.append(tuplilla)
                                        conta +=1
                                    cur.close()
                                    print_table(r_areas)
                                if opcionrnk =="6":
                                    ranking = []
                                    totales = []
                                    cur2 = conn.cursor()
                                    cur2.execute(
                                        "Select distinct m.numero_institucion9 from institucion i,matriculados m where i.numero_institucion = m.numero_institucion9 and i.tipo = '" + tipo + "'")
                                    for i in cur2:
                                        totales.append((i[0]))
                                    cur2.close()
                                    for t in totales:
                                        sub = [t, 0]
                                        ranking.append(sub)
                                    cur2.close()
                                    cur = conn.cursor()
                                    listaa = []
                                    ptje_comparar = 0
                                    r_puntaje = [["Lugar ranking", "Nombre", "Puntaje obtenido", "total"]]
                                    cur.execute(
                                        " select o.numero_institucion9 , (o.mini + o.promedioRNK) as loco  from (select m.numero_institucion9, avg(m.min_pon_psulm) as mini, avg((m.max_ranking + m.min_ranking)/2)  as promedioRNK from institucion i , matriculados m  where m.numero_institucion9 =i.numero_institucion and i.tipo = '" + tipo + "'  and m.max_ranking >0 and m.min_ranking>0 and m.ano_matricula = " + str(
                                            ano_ranking) + " group by m.numero_institucion9 )o order by loco desc")
                                    for i in cur:
                                        listaa.append(i)
                                    conta = 1

                                    try:
                                        ptje_comparar = (listaa[0])[1]
                                        totall = len(listaa) + 1
                                    except IndexError:
                                        pass
                                    for p in listaa:
                                        for t in ranking:
                                            if p[0] == t[0]:
                                                puntaje_a_dar = 100 * p[1] / ptje_comparar
                                                name = get_name(p[0])
                                                t[1] += (int(
                                                    puntaje_a_dar) * 0.1)  # vale 10% el ranking del puntaje y rnking
                                                tuplilla = [conta, name, puntaje_a_dar, p[1] / 2]
                                                r_puntaje.append(tuplilla)
                                        conta += 1
                                    cur = conn.cursor()
                                    listaa = []
                                    ptje_comparar = 0
                                    r_puntaje = [["Lugar ranking", "Nombre", "Puntaje obtenido", "total"]]
                                    cur.execute(
                                        " select o.numero_institucion9 , (o.mini + o.promedioRNK) as loco  from (select m.numero_institucion9, avg(m.min_pon_psulm) as mini, avg((m.max_pon_psulm + m.min_pon_psulm)/2)  as promedioRNK from institucion i , matriculados m  where m.numero_institucion9 =i.numero_institucion and i.tipo = '" + tipo + "' and m.min_pon_psulm >0 and m.max_pon_psulm >0  and m.ano_matricula = " + str(
                                            ano_ranking) + " group by m.numero_institucion9 )o order by loco desc")
                                    for i in cur:
                                        listaa.append(i)
                                    conta = 1

                                    try:
                                        ptje_comparar = (listaa[0])[1]
                                        totall = len(listaa) + 1
                                    except IndexError:
                                        pass
                                    for p in listaa:
                                        for t in ranking:
                                            if p[0] == t[0]:
                                                puntaje_a_dar = 100 * p[1] / ptje_comparar
                                                name = get_name(p[0])
                                                t[1] += (int(
                                                    puntaje_a_dar) * 0.1)  # vale 10% el ranking del puntaje y rnking
                                                tuplilla = [conta, name, puntaje_a_dar, p[1] / 2]
                                                r_puntaje.append(tuplilla)
                                        conta += 1
                                    ptje_comparar = 0
                                    cur.close()
                                    cur = conn.cursor()
                                    cur.execute(
                                        "select abs(avg(m.cnt_homb - m.cnt_muj))  as hola, m.numero_institucion9 from matriculados m, institucion i where (m.cnt_homb != 0 or m.cnt_muj != 0) and i.numero_institucion = m.numero_institucion9 and i.tipo = '" + str(
                                            tipo) + "' and m.ano_matricula = " + str(
                                            ano_ranking) + " group by m.numero_institucion9 order by hola desc")
                                    listaa = []
                                    conta = 0
                                    r_difgeneros = [
                                        ["Lugar ranking", "Nombre", "Puntaje obtenido", "Diferencia Generos"]]
                                    for i in cur:
                                        listaa.append(i)
                                    ptje_comparar = 1
                                    for i in listaa:
                                        for t in ranking:
                                            if i[1] == t[0]:
                                                puntaje_a_dar = 100 * conta / len(listaa)
                                                name = get_name(i[1])
                                                t[1] += (int(puntaje_a_dar) * 0.1)  # vale 10%
                                                tuplango = [len(listaa) - conta, name, puntaje_a_dar, i[0]]
                                                r_difgeneros.append(tuplango)
                                        conta += 1
                                    cur.close()
                                    r_matriDoce = [["Lugar ranking", "Nombre", "Puntaje obtenido", "Ratio"]]
                                    # el ratio alumnos matriculados por docente jornada completa vale un 12.5 %
                                    # el ratio alumnos matriculados por docente de especialidad medicao con doctorado vale un 12.5%
                                    cur = conn.cursor()
                                    ptje_comparar = 0
                                    cur.execute(
                                        "select (o.matri/o.doce) as ratio, o.numero_institucion9 from (select sum(cast((m.ingreso_psu + m.matriculados_otra_via) as real))  as matri, sum(cast(d.n_d_j_c as real)) as doce, m.numero_institucion9 from matriculados m , datos_profesor_sede d, institucion i where i.tipo = '" + str(
                                            tipo) + "' and i.numero_institucion = m.numero_institucion9 and d.id_sede8 = m.id_sede9 and m.ano_matricula = " + str(
                                            ano_ranking) + " group by m.numero_institucion9) o where o.doce != 0 order by ratio asc")
                                    listaa = []
                                    for i in cur:
                                        listaa.append(i)
                                    ptje_comparar = (listaa[len(listaa) - 1])[0]
                                    cur.close()
                                    conta = 0
                                    for t in listaa:
                                        for p in ranking:
                                            if t[1] == p[0]:
                                                puntaje_a_dar = 100 * t[0] / ptje_comparar
                                                p[1] += (int(puntaje_a_dar) * 0.125)
                                                name = get_name(t[1])
                                                tuplilla = [len(listaa) - conta, name, puntaje_a_dar, t[0]]
                                                r_matriDoce.append(tuplilla)
                                        conta += 1
                                    r_matriDocemedi = [["Lugar ranking", "Nombre", "Puntaje obtenido", "Ratio"]]
                                    cur = conn.cursor()
                                    cur.execute(
                                        "select (o.matri/o.doce) as ratio, o.numero_institucion9 from (select sum(cast((m.ingreso_psu + m.matriculados_otra_via) as real))  as matri, sum(cast(d.n_dm_j_c+d.n_dm_j_c as real)) as doce, m.numero_institucion9 from matriculados m , datos_profesor_sede d, institucion i where i.tipo = '" + str(
                                            tipo) + "' and i.numero_institucion = m.numero_institucion9 and d.id_sede8 = m.id_sede9 and m.ano_matricula = " + str(
                                            ano_ranking) + "   group by m.numero_institucion9) o where o.doce != 0 order by ratio asc")
                                    listaa = []
                                    for i in cur:
                                        listaa.append(i)
                                    ptje_comparar = (listaa[len(listaa) - 1])[0]
                                    cur.close()
                                    conta = 0
                                    for t in listaa:
                                        for p in ranking:
                                            if t[1] == p[0]:
                                                puntaje_a_dar = 100 * t[0] / ptje_comparar
                                                name = get_name(t[1])
                                                tuplilla = [len(listaa) - conta, name, puntaje_a_dar, t[0]]
                                                p[1] += (int(
                                                    puntaje_a_dar) * 0.125)  # vale 12.5% el ratio docente medico o doctorado
                                                r_matriDocemedi.append(tuplilla)
                                        conta += 1
                                    cur.close()

                                    cur = conn.cursor()
                                    ano_proximo = int(ano_ranking) + 1
                                    cur.execute(
                                        "select ht.numero_institucion , sum(ht.orden) from (select h.id_programa1 ,h.orden , i.numero_institucion from (select n.nuevo - v.viejo as orden, v.id_programa1 from  (select sum(m.ingreso_psu + m.matriculados_otra_via) as nuevo, m.id_programa1 from matriculados m where m.ano_matricula = " + str(
                                            ano_proximo) + " group by m.id_programa1) n ,(select sum(m.ingreso_psu + m.matriculados_otra_via) as viejo, m.id_programa1 from matriculados m where m.ano_matricula = " + str(
                                            ano_ranking) + " group by m.id_programa1) v where v.id_programa1 = n.id_programa1 and v.viejo != 0 and n.nuevo != 0 order by orden asc)h , institucion i , sede s , programa_sede ps where h.id_programa1 = ps.id_programa2 and ps.id_sede2 = s.id_sede and s.id_institucion1 = i.numero_institucion and i.tipo = '" + tipo + "')ht group by ht.numero_institucion order by sum asc")
                                    listaa = []
                                    r_retencion = [["Lugar ranking", "Nombre", "Puntaje obtenido", "Retencion"]]
                                    for i in cur:
                                        listaa.append(i)
                                    if len(listaa) != 0:
                                        ptje_comparar = (listaa[len(listaa) - 1])[1]
                                        cur.close()
                                        conta = 1
                                        for t in listaa:
                                            for p in ranking:
                                                if t[0] == p[0]:
                                                    puntaje_a_dar = 100 * t[1] / ptje_comparar
                                                    p[1] += (int(puntaje_a_dar) * 0.1)  # vale 10% la tasa de retencion
                                                    name = get_name(t[1])
                                                    tuplilla = [len(listaa) - conta, name, puntaje_a_dar, t[1]]
                                                    r_retencion.append(tuplilla)
                                            conta += 1
                                    cur.close()
                                    cur = conn.cursor()
                                    listaa = []
                                    conta = 1
                                    r_carreras = []
                                    cur.execute(
                                        "select count(c.id_carrera),m.numero_institucion9 from matriculados m , carrera c,programa p , institucion i where i.tipo = '" + tipo + "' and i.numero_institucion = m.numero_institucion9 and c.id_carrera = p.id_carrera2 and m.id_programa1 = p.id_programa and m.ano_matricula = " + str(
                                            ano_ranking) + " group by m.numero_institucion9 order by count asc")
                                    for i in cur:
                                        listaa.append(i)
                                    ptje_comparar = (listaa[len(listaa) - 1])[0]
                                    for t in listaa:
                                        for y in ranking:
                                            if t[1] == y[0]:
                                                name = get_name(t[1])
                                                puntaje_a_dar = 100 * t[0] / ptje_comparar
                                                y[1] += (int(
                                                    puntaje_a_dar) * 0.1)  # vale 10% la cantidad de carreras para ese ano
                                                tuplilla = [conta, name, int(puntaje_a_dar), t[0]]
                                                r_carreras.append(tuplilla)
                                        conta += 1
                                    cur.close()
                                    r_areas = [["Lugar", "Nombre", "Puntaje Obtenido", "Cantidad areas cubiertas"]]
                                    cur = conn.cursor()
                                    listaa = []
                                    cur.execute(
                                        "select count(y.area_estudio) ,y.numero_institucion9 from (select distinct c.area_estudio,m.numero_institucion9 from matriculados m , carrera c,programa p , institucion i where i.tipo = '" + tipo + "' and i.numero_institucion = m.numero_institucion9 and c.id_carrera = p.id_carrera2 and m.id_programa1 = p.id_programa and m.ano_matricula = " + str(
                                            ano_ranking) + ")y group by y.numero_institucion9 order by count asc ")
                                    for t in cur:
                                        listaa.append(t)
                                    ptje_max = (listaa[len(listaa) - 1])[0]
                                    for y in listaa:
                                        for u in ranking:
                                            if u[0] == y[1]:
                                                puntaje_a_dar = 100 * y[0] / ptje_max
                                                name = get_name(u[0])
                                                u[1] += (int(
                                                    puntaje_a_dar) * 0.1)  # vale 10% la cantidad de carreras para ese ano
                                                tuplilla = [conta, name, y[0], int(puntaje_a_dar)]
                                                r_areas.append(tuplilla)
                                        conta += 1
                                    cur.close()
                                    cur = conn.cursor()
                                    cur.execute(
                                        "select a.numero_institucion5,sum(a.duracion)summ  from acreditacion_institucion a, institucion i  where a.numero_institucion5 = i.numero_institucion and i.tipo = '" + tipo + "' group by a.numero_institucion5 order by summ desc")
                                    r_anos = [["Lugar", "Nombre", "Puntaje", "Cantidad Anos"]]
                                    listaa = []
                                    conta = 1
                                    for i in cur:
                                        listaa.append(i)
                                    puntaje_max = listaa[0][1]
                                    for i in listaa:
                                        for t in ranking:
                                            if i[0] == t[0]:
                                                puntaje_a_dar = 100 * i[1] / puntaje_max
                                                name = get_name(i[0])
                                                t[1] += puntaje_a_dar * 0.1  # vale 10% la cantidad de anos matriculados
                                                tuplilla = [conta, name, int(puntaje_a_dar), i[1]]
                                                r_anos.append(tuplilla)
                                        conta += 1
                                    cur.close()
                                    cur = conn.cursor()
                                    cur.execute(
                                        "select a.numero_institucion5, sum(u.inv+i.vin+o.post)as summm from (select a.numero_institucion5,count(a.investigacion) as inv from acreditacion_institucion a left join institucion i  on a.numero_institucion5 = i.numero_institucion and i.tipo = '" + tipo + "' and a.investigacion = True group by a.numero_institucion5)u, (select a.numero_institucion5,count(a.vinculacion_con_el_medio)as vin from acreditacion_institucion a left join institucion i  on a.numero_institucion5 = i.numero_institucion and i.tipo = '" + tipo + "' and a.vinculacion_con_el_medio = True group by a.numero_institucion5 )i,(select a.numero_institucion5,count(a.docencia_postgrado)as post from acreditacion_institucion a left join institucion i on a.numero_institucion5 = i.numero_institucion and i.tipo = '" + tipo + "' and a.docencia_postgrado = True group by a.numero_institucion5 )o, acreditacion_institucion a where a.numero_institucion5 = u.numero_institucion5 and i.numero_institucion5 = u.numero_institucion5 and o.numero_institucion5 = u.numero_institucion5 group by a.numero_institucion5 order by summm asc")
                                    r_areas = [["Lugar", "Nombre", "Puntaje", "Cantidad Areas"]]
                                    listaa = []
                                    conta = 1
                                    for p in cur:
                                        listaa.append(p)
                                    puntaje_a_dar = listaa[len(listaa) - 1][1]
                                    for i in listaa:
                                        for p in ranking:
                                            if p[0] == i[0]:
                                                puntaje_obt = 100 * i[1] / puntaje_a_dar
                                                p[1] += int(puntaje_obt) * 0.1
                                                name = get_name(p[0])
                                                tuplilla = [p[0], name, int(puntaje_obt), i[1]]
                                                r_areas.append(tuplilla)
                                        conta += 1
                                    cur.close()
                                    print "Ranking Alumno :\n\tpuntaje y ranking = 10% \n\tdiferencia de generos = 10% \nRanking Docente :\n\tdocentes jornada completa vs alumnos = 12.5% \n\tratio docentes medicos y doctores vs alumnos = 12.5% \nRanking retencion :\n\tretencion = 10% \nRanking acreditacion :\n\tranking anos de acreditacion = 12.5% \n\tranking cantidad de areas = 12.5% \nRanking Complejidad institucional :\n\tranking cantidad carreras genericas diferentes = 10% \n\tranking cantidad areas cubiertas = 10%"
                                    print "Resutado final :"
                                    ranking_nuevo = [["Lugar", "Nombre", "Comuna", "Punataje"]]

                                    conta = 0
                                    ran = []
                                    ran = sorted(ranking, key=lambda student: student[1])

                                    for i in ran:
                                        id = i[0]
                                        curr = conn.cursor()
                                        curr.execute("select i.nombre_insti,i.comu_cas_cen from institucion i where i.numero_institucion = " + str(id))
                                        list = []
                                        for r in curr:
                                            list.append(r)
                                        nombre = list[0][0]
                                        comu = list[0][1]
                                        tuplo = []
                                        tupplo = [len(ran)-conta, nombre, comu, i[1]]
                                        conta += 1
                                        curr.close()
                                        ranking_nuevo.append(tupplo)
                                    if 3044 in ranking_nuevo:
                                        print "hola"
                                    print_table(ranking_nuevo)
                                if opcionrnk == "7":
                                    looprnk = False
                                    loopranking = False
                                    print "Retornando"
                                if opcionrnk == "8":
                                    looprnk = False
                                    loopranking = False
                                    loopMenu = False



                        if opcionranking == "4":
                            print "no hay data sobre F.F.A.A"
                        if opcionranking == "5":
                            loopranking = False
                            print "Retornando..."
                        if opcionranking == "6":
                            loopranking = False
                            loopMenu = False
                        if opcionranking != "1" and opcionranking != "2" and opcionranking != "3" and opcionranking != "4" and opcionranking != "5" and opcionranking != "6" :
                            print "OOps Opcion ingresada no valida \nRetornando..."


            except ValueError :
                print"Ooops algo salio mal... \nRetornando..."
    if opcion == "5":
        loopMenu = False
    if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5":
        print "OOPS ! opcion ingresada no valida \nretornando...."
conn.close()