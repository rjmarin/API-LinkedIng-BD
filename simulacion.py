# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import random
import datetime

##############################################################
#Usuarios y Perfiles
Usuarios=[]
Perfiles=[]
Nacimiento=[]
IDPerfil=[]
Nombresh=["'Mario","'Pedro","'Andres","'Julio","'Carmelo","'Alexis"]
Nombresm=["'Maria","'Pascale","'Gabriela","'BeckyG","'Natynatasha","'Shakira"]
Apellidos=["perez","gutierrez","lopez","garcia","messi","james","curry","harden",
           "jordan","cortes","reymond"]
termino= ["gmail.com'", "outlook.com'", "hotmail.com'", "live.cl'", "miuandes.cl'"]
nacionalidad= ["'Chilena'","'Argentina'","'Brasilera'","'Japonesa'","'Mexicana'","'Uruguaya'"]
descripcionh= ["'moreno joven bajo.'","'colorin adulto joven alto.'",
               "'moreno adulto alto.'","'rubio tercera edad.'","'rubio alto.'"]
               
descripcionm=["'morena joven baja.'","'colorina adulta joven alta.'",
               "'morena adulta alta.'","'rubia tercera edad.'","'rubia alta.'"]        
h=1  
mails= [] 
IDP = 0    
for i in Nombresh:
    
    for j in Apellidos:
        email= i+j+"@"+termino[random.randint(0,len(termino)-1)]
        mails.append(email)
        Usuarios.append(email) 
        nac= nacionalidad[random.randint(0,len(nacionalidad)-1)]
        
        des=descripcionh[random.randint(0,len(descripcionh)-1)]
        ano = random.randint(1960, 2000)
        Nacimiento.append(ano)
        mes = random.randint(1, 12)
        if mes < 10:
            mess = "0" + str(mes)
        dia = str(random.randint(1, 28))
        if len(dia)==1:
            dia = "0" + str(dia)
        fecha = "'" + str(ano) + "-" + str(mes) + "-" + str(dia) + "'"
        #telep= random.randint(56960000000, 56999999999)
        IDP +=1
        IDPerfil.append(IDP)
        
        perl= "(" + str(IDP) + "," + email+  "," + i + "'" + "," + "'" + j + "'," + "'Masculino'" + "," + fecha + "," + nac + "," + des +")"
        Perfiles.append(perl)
        h+=1
for i in Nombresm:
    
    for j in Apellidos:
        email= i+j+"@"+termino[random.randint(0,len(termino)-1)]
        mails.append(email)
        Usuarios.append(email) 
        nac= nacionalidad[random.randint(0,len(nacionalidad)-1)]
        
        des=descripcionm[random.randint(0,len(descripcionm)-1)]
        ano = random.randint(1960, 2000)
        
        Nacimiento.append(ano)
        mes = str(random.randint(1, 12))
        if len(mes)==1:
            mes = "0" + mes
        dia = random.randint(1, 28)
        if dia < 10:
            dia = "0" + str(dia)

        fecha = "'" + str(ano) + "-" + str(mes) + "-" + str(dia) + "'"
        #telep= random.randint(56960000000, 56999999999)
        IDP += 1
        
        IDPerfil.append(IDP)
        
        perl=  "(" + str(IDP) + ","  + email+  "," + i + "'" + "," + "'" + j + "'," + "'Femenino'" + "," + fecha + "," + nac + "," + des +")" 
        Perfiles.append(perl)
        h+=1
  
print("INSERT INTO Usuario(email)\n VALUES ")
for j in Usuarios:
    print("(" + j +"),")
print(";\n\n") 
print("INSERT INTO Perfil(id,email, nombre, apellido, genero,fecha_nacimiento,pais,descripcion)\n VALUES     ")
for j in Perfiles:
    print(j +",")
print(";\n\n")  

####################################################
#Telefono     ID,Telefono
Telefonos=[]
for i in IDPerfil:
    j=0
    n=random.randint(1,3)
    while j <n:
        telep=random.randint(569600000, 569999999)
        agreg=str(i)+","+str(telep)
        Telefonos.append(agreg)
        j+=1
print("INSERT INTO Telefono_perfil(id_perfil, telefono)\n VALUES ")
for j in Telefonos:
    print("(" + j + "),")
print(";\n\n")           
######################################
    #FOTOSSS    ID, Fotos
Fotos=[]
for i in IDPerfil:
    j=0
    n=random.randint(1,10)
    while j <n:
        
        agreg=str(i)+","+"'Foto "+str(j)+"'"
        Fotos.append(agreg)
        j+=1
print("INSERT INTO Foto_perfil(id_perfil, foto)\n VALUES ")
for j in Fotos:
    print("(" + j +"),")
print(";\n\n") 
################################################################
#Claves
#ID,Clave,Activo,Fecha
Claves=[]    
PosClaves=["la","le","li","lo","lu","ca","ce","co","cu","na","ne","ni","no","nu",
           "pa","pe","pi","po","pu","ra","re","ro","ru","a","b","c","d","e","f",
           "j","g","k","l","m","n","o","p","q","h","i","j","r","s","t","W","V","Z"]
           
for i in range(len(IDPerfil)):
    j=0
    n=random.randint(1,6)
    while j <n:
        k=0
        z=random.randint(1,8)
        clav=""
        while k <z:
            clav+=PosClaves[random.randint(0,len(PosClaves)-1)]
            k+=1
        
        ano=random.randint(2000,2018)
        
        mes = random.randint(1, 12)
        if mes < 10:
            mes = "0" + str(mes)

        dia = random.randint(1, 28)
        if dia < 10:
            dia = "0" + str(dia)

        fecha = "'" + str(ano) + "-" + str(mes) + "-" + str(dia) + "'"        
        
        veri=random.randint(0,99)
        agreg=str(mails[i])+","+"'"+clav+str(veri)+"'"+","+fecha
        Claves.append(agreg)
        j+=1           
print("INSERT INTO Clave(email_usuario,clave,fecha)\n VALUES ")
for j in Claves:
    print("(" + j +"),")
print(";\n\n")
      
##########################################################################
 #PErfiles
#ID,email,nombre,apellido,genero,fechanacimiento,pais,descripcion,telefono,fotoperfil
        
        


#######################################################################3
#Empresas
#ID,nombre,direccion, descripcion,pais, rubro, fecha_creacion,foto perfil, telefono
Emp=[]
IDEmpresa=[]

Empresas = ["'Bayer'","'Roche'","'Novartis Farmacéutica'","'Volkswagen'","'Honda'",
           "'Kelloggs'","'DHL'","'Fedex'","'Citibank'","'HSBC'","'Siemens'","'Nestle'",
           "'Pepsi cola'","'Bimbo'","'Ford'","'Chevrolet'","'General Electric'","'Sony'",
           "'Nextel'","'Movistar'","'HP'","'Walmart'" ]

Fotos = ["'Foto Bayer'","'Foto Roche'","'Foto Novartis Farmacéutica'","'Foto Volkswagen'","'Foto Honda'",
           "'Foto Kelloggs'","'Foto DHL'","'Foto Fedex'","'Foto Citibank'","'Foto HSBC'","'Foto Siemens'","'Foto Nestle'",
           "'Foto Pepsi cola'","'Foto Bimbo'","'Foto Ford'","'Foto Chevrolet'","'Foto General Electric'","'Foto Sony'",
           "'Foto Nextel'","'Foto Movistar'","'Foto HP'","'Foto Walmart'" ]           


#ext = [" LTDA.'", " SPA.'", " SA.'", " Inc.'"]
direcciones= ["'Colon","'Vespucio","'San Carlos","'Apoquindo","'Vitacura","'Grecia",
            "'Matucana","'Los Trapenses","'La Gloria","'Holanda","'Vaticano",
            "'Concepcion","'Camino Agricola","'Flandes","'Padre Hurtado","'Lota",
            "'Estoril","'Malaga","'Camino el alba","'Carlos Antunes","'Francisco Bilbao",
            "'Pocuro","'Los Leones"]
rubros = [ "'TECNOLOGIA'", "'AGRICOLA'","'BIENESTAR Y SALUD'", "'MODA'", "'RECREACION'"]

paises = ["'Alemania'","'Chile'", "'Brasil'","'Estados Unidos'", "'Mexico'"]

descripciones = ["'Empresa dedicada a celulares.'", "'Empresa dedicada a computadores.'", 
				"'Cultivo de tomates.'", "'Cultivo de papas'",
				"'Masajista especializada en espalda.'", "'Fabricante de remedios.'", 
				 "'Fabricante de ropa.'","'Distribuidor de ropa.'",
				"'Distribuidor de juegos de mesa.'","'Coleccion de antiguedades.'"]

NacimientoEmpresa=[]
for i in range(len(Empresas)):
    ID = random.randint(90000000, 99999999)
    
    IDEmpresa.append(ID)
    
    direc= direcciones[random.randint(0,len(direcciones)-1)] + " "+ str(random.randint(0,10000))+ "'" 
    pais= paises[random.randint(0,len(paises)-1)]
    rubro= rubros[random.randint(0,len(rubros)-1)]
    
    descripcion = ""
    if (rubro == "'TECNOLOGIA'"):
        descripcion=descripciones[random.randint(0, 1)]
    elif (rubro == "'AGRICOLA'"):
        descripcion = descripciones[random.randint(2, 3)]
    elif (rubro == "'BIENESTAR Y SALUD'"):
        descripcion = descripciones[random.randint(4, 5)]
    elif (rubro == "'MODA'"):
        descripcion = descripciones[random.randint(6, 7)]
    elif (rubro == "'RECREACION'"):
        descripcion = descripciones[random.randint(8, 9)]

    year = random.randint(1900, 2018)
    NacimientoEmpresa.append(year)    
    
    month = random.randint(1, 12)
    if month < 10:
        month = "0" + str(month)

    day = random.randint(1, 28)
    if day < 10:
        day = "0" + str(day)

    date = "'" + str(year) + "-" + str(month) + "-" + str(day) + "'"
    #telefono = random.randint(2200000000, 2299999999)
#ID,nombre,direccion, descripcion,pais, rubro, fecha_creacion,foto perfil, telefono
    full_str = str(ID) + ","+ Empresas[i]+","+direc+","+descripcion+","+pais+","+rubro+","+date#+","+ Fotos[i]+","+str(telefono)
    Emp.append(full_str)

print("INSERT INTO Empresa(id,nombre,direccion,descripcion,rubro,pais,fecha_de_creacion)\n VALUES")
for j in Emp:
    print("(" + j +"),")
print(";\n\n")

################################################################################
#Telefonos Empresas
TelefonosEmpresas=[]
for i in IDEmpresa:
    j=0
    n=random.randint(1,2)
    while j <n:
        telep=random.randint(220000000, 229999999)
        agreg=str(i)+","+str(telep)
        TelefonosEmpresas.append(agreg)
        j+=1

print("INSERT INTO Telefono_Empresa(ID_Empresa,Telefono) \n VALUES") 
for j in TelefonosEmpresas:
    print("(" + j +"),")
print(";\n\n")         
######################################
    #FOTOSSS    ID, Fotos
FotosEmpresa=[]
for i in IDEmpresa:
    j=0
    n=random.randint(1,4)
    while j <n:
        
        agreg=str(i)+","+"'Foto "+str(j)+"'"
        FotosEmpresa.append(agreg)
        j+=1   



print("INSERT INTO Foto_Empresa(ID_Empresa,foto) \nVALUES")
for j in FotosEmpresa:
    print("(" + j +"),")
print(";\n\n")


    
    
    
    
#######################################################    
#Institucion
#ID nombre, direccion, descripcion, grado
    
Institucion=[]
NombreInt=[]
Nuniversidad=["de los Andes'","del desarrollo'","Mayor'","del Pacifico'",
              "de Chile'","Catolica'","Federico Santa Maria'","Autonoma'","Adolfo Ibanez'",
              "de Santiago'","Diego Portales'"] 
              
DescUni=["'Universidad dedicada a formar alumnos comprometidos'",
         "'Universidad con enfasis en generar conciencia'",
         "'Universidad formadora de buenos profecionales'",
         "'Universidad formando el futuro de Chile'"]
Grado=["'Pre-grado'","'Doctorado'","'Bajo'","'Medio'","'Alto'","'Bajito'","'Universitario'"]
 
for i in Nuniversidad:
    nom= "'Universidad "+i
    NombreInt.append(nom)
    direcc=direcciones[random.randint(0,len(direcciones)-1)]+" "+str(random.randint(5000,99999999))+"'"
    des=DescUni[random.randint(0,len(DescUni)-1)]
    grad=Grado[random.randint(0,len(Grado)-1)]
    inti=nom+","+direcc+","+des+","+grad
    Institucion.append(inti)
    
print("INSERT INTO Institucion(nombre,direccion,descripcion,grado) \nVALUES")
for j in Institucion:
    print("(" + j +"),")
print(";\n\n")
###################################################3
#Estudio
#Id perfil,nombre instirucion,grado academico,descripcion,fecha inicio, fecha termino

Estudio=[]
DesEst=["'Ingeniero Civil en Computacion.'","'Contador Auditor.'","'Ingeniero Comercial.'",
        "'Doctorado en sotfware.'","'Ingeniero Civil.'","'Abogado.'","'Medico.'",
        "'Tecnico en computacion.'","'Ingeniero en minas.'","'Periodista.'",
        "'Kinesiologo.'","'Terapeuta.'","'Analista.'"]
 
for i in range(len(IDPerfil)):
    
    IPer=IDPerfil[i]
    nint=NombreInt[random.randint(0,len(NombreInt)-1)]
    grad=Grado[random.randint(0,len(Grado)-1)]
    descp=DesEst[random.randint(0,len(DesEst)-1)]
    Ainicio=Nacimiento[i]+random.randint(20,45)  
    
    mes = random.randint(1, 12)
    if mes < 10:
        mes = "0" + str(mes)
    dia = random.randint(1, 28)
    if dia < 10:
        dia = "0" + str(dia)
    fechai = "'" + str(Ainicio) + "-" + str(mes) + "-" + str(dia) + "'"  
    
    Atermino=Ainicio+random.randint(2,8)
    mes1 = random.randint(1, 12)
    if mes1 < 10:
        mes1 = "0" + str(mes1)
    dia1 = random.randint(1, 28)
    if dia1 < 10:
        dia1 = "0" + str(dia1)
    fechat = "'" + str(Atermino) + "-" + str(mes1) + "-" + str(dia1) + "'" 
    est= str(IPer)+","+nint+","+grad+","+descp+","+fechai+","+fechat
    Estudio.append(est)
   
print("INSERT INTO Estudio(id_perfil,nombre_institucion,grado_academico,descripcion,fecha_inicio,fecha_fin)\n VALUES") 
for j in Estudio:
    print("(" + j +"),")
print(";\n\n")
#################################################
    #Habilidad
    #ID,Habilidad,descripcion
Habilidades=[]
Habilidad=["'en Excel'","'en Python'","'C++'","'en Presentaciones'",
           "'en Docencia'","'en Manejo de Grupos'", "'en R'","'En Stata'",
           "'en Manejo de Datos'","'En Big Data'"] 
           
DesHab=["'Descripcion 1.'","'Descripcion 2.'","'Descripcion 3.'",
        "'Descripcion 4.'","'Descripcion 5.'"]
NEW_Habilidad=[]

for i in range(len(IDPerfil)):
    
    hab1=Habilidad[random.randint(0,len(Habilidad)-1)]
    des1=DesHab[random.randint(0,len(DesHab)-1)]
    hab2=Habilidad[random.randint(0,len(Habilidad)-1)] 
    des2=DesHab[random.randint(0,len(DesHab)-1)]
    
    while 0!=1:
        if hab1==hab2:
            hab2= Habilidad[random.randint(0,len(Habilidad)-1)]
        else:
            break
    habilidad1= str(IDPerfil[i])+","+hab1+","+ des1
    habilidad2= str(IDPerfil[i])+","+hab2+","+ des2
    
    Habilidades.append(habilidad1)
    Habilidades.append(habilidad2)
    NEW_Habilidad.append([hab1, IDPerfil[i]])

print("INSERT INTO Habilidad(id_perfil,habilidad,descripcion)\n VALUES ") 
for j in Habilidades:
    print("(" + j +"),")
print(";\n\n") 
###############################################
 #PUESTO   
#ID trabajador,ID Empresa, Puesto,Fecha Inicio,Fecha fin
    
Puestos=[]
Puesto=["'Gerente General.'","'Asistente.'","'Ejecutivo.'","'Administrador.'",
         "'Gerente Comercial.'","'Analista.'","'Analista Senior.'","'Ejecutivo Avanzado'"]
    
for i in range(len(IDPerfil)):
    
    idem=IDEmpresa[random.randint(0,len(IDEmpresa)-1)]
    pue=Puesto[random.randint(0,len(Puesto)-1)]    
    Ainicio=Nacimiento[i]+random.randint(25,45)  
    if Ainicio > 2018:
            Ainicio = 2018
        
    mes = random.randint(1, 12)
    if mes < 10:
                mes = "0" + str(mes)
    dia = random.randint(1, 28)
    if dia < 10:
        dia = "0" + str(dia)
    fechai = "'" + str(Ainicio) + "-" + str(mes) + "-" + str(dia) + "'"  
    
    Atermino=Ainicio+random.randint(1,10)
    mes1 = random.randint(1, 12)
    if mes1 < 10:
        mes1 = "0" + str(mes1)
    dia1 = random.randint(1, 28)
    if dia1 < 10:
        dia1 = "0" + str(dia1)
    
    if Ainicio==2018:
        fechat="NULL"
    else:
        
        fechafin=["'" + str(Atermino) + "-" + str(mes1) + "-" + str(dia1) + "'","NULL","NULL"]
  
        fechat = fechafin[random.randint(0,len(fechafin)-1)] 
    
    datos= str(IDPerfil[i])+","+str(idem)+","+pue+","+fechai+","+fechat
    
    Puestos.append(datos)


print("INSERT INTO Trabaja(id_trabajador,id_empresa,puesto,fecha_de_inicio,fecha_fin)\n VALUES")
for j in Puestos:
    print("(" + j +"),")
print(";\n\n")


####################################3
#Publicacion 
#ID Publicacion,Id usuario, privacidad, contenido, fecha, estado 
Publicacion=[]
Privacidad=["'Publico'","'Publico'","'Privado'","'Privado'","'Privado'"]
Contenido=["'Foto'","'Link'","'Texto'"]
Estado=["'Activo'","'Borrado'"]
IDPublicacion=[]
IDPublica=[]
for i in range(len(IDEmpresa)):
    j=0
    k=random.randint(1,3) 
    while j < k:
    
                IDP= random.randint(10000,40000)
                priv=Privacidad[random.randint(0,len(Privacidad)-1)]
                cont=Contenido[random.randint(0,len(Contenido)-1)]
                est=Estado[random.randint(0,len(Estado)-1)]
                
                if priv=="'Publico'":
                    IDPublica.append(IDP)
                
                Ainicio=NacimientoEmpresa[i]+random.randint(9,30)  
                if Ainicio > 2018:
                        Ainicio = 2018        
                mes = random.randint(1, 12)
                if mes < 10:
                    mes = "0" + str(mes)
                dia = random.randint(1, 28)
                if dia < 10:
                    dia = "0" + str(dia)
                fechap = "'" + str(Ainicio) + "-" + str(mes) + "-" + str(dia) + "'" 
                
                pub= str(IDP)+","+str(IDEmpresa[i])+","+priv+","+cont+","+fechap+","+est
                Publicacion.append(pub)
                j+=1

for i in range(len(IDPerfil)):
    
    j=0
    k=random.randint(1,2) 
    while j < k:
                    IDP= random.randint(10000,40000)
                    IDPublicacion.append(IDP)
                    priv=Privacidad[random.randint(0,len(Privacidad)-1)]
                    cont=Contenido[random.randint(0,len(Contenido)-1)]
                    est=Estado[random.randint(0,len(Estado)-1)]
                    Ainicio=Nacimiento[i]+random.randint(9,25)
                    print 
                    if priv=="'Publico'":
                                    IDPublica.append(IDP)
                    if Ainicio > 2018:
                            Ainicio = 2018        
                    mes = random.randint(1, 12)
                    if mes < 10:
                        mes = "0" + str(mes)
                    dia = random.randint(1, 28)
                    if dia < 10:
                        dia = "0" + str(dia)
                    fechap = "'" + str(Ainicio) + "-" + str(mes) + "-" + str(dia) + "'" 
                    
                    pub= str(IDP)+","+str(IDPerfil[i])+","+priv+","+cont+","+fechap+","+est
                    Publicacion.append(pub) 
                    j+=1

print("INSERT INTO Publicacion(id_publicacion,id_usuario,privacidad,contenido,fecha,estado) \n VALUES ")
for j in Publicacion:
    print("(" + j +"),")
print(";\n\n")
#################################################
#Comentario
    #IDpublicacion,IDComentario,IDUsuario,texto,fecha,estado
Comentario=[]    
IDComentario=[]
Texto=["la","le","li","lo","lu","ca","ce","co","cu","na","ne","ni","no","nu",
           "pa","pe","pi","po","pu","ra","re","ro","ru","a","b","c","d","e","f",
           "j","g","k","l","m","n","o","p","q","h","i","j","r","s","t","W","V","Z"," ","foto","casa",
           "calle","hogar"]
EstadoComentario=["'Vigente'","'Vigente'","'Borrado'","'Borrado'"]

f=0
w=1
    
for i in range(len(IDPublica)):
    
    IDC=random.randint(40000,60000)
    IDComentario.append(IDC)
    est1=EstadoComentario[random.randint(0,len(EstadoComentario)-1)]
    tex1=""
    j=0
    k=random.randint(1,20) 
    while j < k:
        tex1+=Texto[random.randint(0,len(Texto)-1)]
        j+=1
    Ainicio=random.randint(2000,2016)

    if Ainicio > 2018:
               Ainicio = 2018        
    mes = random.randint(1, 12)
    if mes < 10:
            mes = "0" + str(mes)
    dia = random.randint(1, 28)
    if dia < 10:
                		dia = "0" + str(dia)
    fechap = "'" + str(Ainicio) + "-" + str(mes) + "-" + str(dia) + "'"     
    
    com1=str(IDPublica[i])+","+str(IDC)+","+str(IDPerfil[f])+","+"'"+tex1+"'"+","+fechap+","+est1
    est2=EstadoComentario[random.randint(0,len(EstadoComentario)-1)]
    tex2=""
    l=0
    IDC=random.randint(40000,60000)
    IDComentario.append(IDC)
    m=random.randint(1,20) 
    while l < m:
        tex2+=Texto[random.randint(0,len(Texto)-1)]
        l+=1
    Ainicio1=random.randint(2000,2016)

    if Ainicio > 2018:
               Ainicio = 2018        
    mes1 = random.randint(1, 12)
    if mes1 < 10:
            mes1 = "0" + str(mes1)
    dia1 = random.randint(1, 28)
    if dia1 < 10:
                		dia1 = "0" + str(dia1)
    fechap1 = "'" + str(Ainicio1) + "-" + str(mes1) + "-" + str(dia1) + "'"     
    
    com2=str(IDPublica[i])+","+str(IDC)+","+str(IDPerfil[w])+","+"'"+tex2+"'"+","+fechap1+","+est2
    Comentario.append(com1)
    Comentario.append(com2)
    f+=1
    w+=1

print("INSERT INTO Comentario(id_publicacion,id_comentario,id_usuario,texto,fecha,estado)\n VALUES")
for j in Comentario:
    print("(" + j +"),")
print(";\n\n")
#######################################################################################
    #Sub Comentario
# IDcomentario,IdSubcomentario,ID Usuario,texto,fecha,estado    
IDSComentario=[]    
SubComentario=[]    
for i in range(len(IDComentario)):
    
    IDSC=random.randint(60000,80000)
    IDSComentario.append(IDSC)
    est1=EstadoComentario[random.randint(0,len(EstadoComentario)-1)]
    IDper=IDPerfil[random.randint(0,len(IDPerfil)-1)]
    tex1=""
    j=0
    k=random.randint(1,20) 
    while j < k:
        tex1+=Texto[random.randint(0,len(Texto)-1)]
        j+=1
    Ainicio=random.randint(2015,2018)

    if Ainicio > 2018:
               Ainicio = 2018        
    mes2 = random.randint(1, 12)
    if mes2 < 10:
            mes2 = "0" + str(mes2)
    dia = random.randint(1, 28)
    if dia < 10:
        dia = "0" + str(dia)
    fechapp = "'" + str(Ainicio) + "-" + str(mes2) + "-" + str(dia) + "'"   
    
    scom1=str(IDSC)+","+str(IDComentario[i])+","+str(IDper)+","+"'"+tex1+"'"+","+fechapp+","+est1
    
    SubComentario.append(scom1)

print("INSERT INTO Sub_Comentario(id_sub_comentario,id_comentario,id_usuario,texto,fecha,estado) \n VALUES")
for j in SubComentario:
    print("(" + j +"),")
print(";\n\n")

#####################################################
#Solicitud(email_usuario,email_usuario_amistad, aceptada, id_solicitud,fecha_solicitud)
Solicitud=[]
contSolicitudRechazada=0
numSolicitud=101
solicitudIgnored=0
acept="lol"
for i in Usuarios:
    contAceptada=0
    for j in Usuarios:
        mes = random.randint(1, 12)
        if mes < 10:
                mes = "0" + str(mes)
        dia = random.randint(1, 28)
        if dia < 10:
            dia = "0" + str(dia)
        ano = 2010
        fecha="'"+str(dia)+'-'+str(mes)+'-'+ str(ano)+"'"
        if i!=j:
            if contAceptada<3:
                acept="'Aceptada'"
                contAceptada+=1
            elif contSolicitudRechazada<50:
                acept="'Rechazada'"
                contSolicitudRechazada+=1
            else:
                acept="'Ignored'"
                solicitudIgnored+=1
            Solicitud.append([i, j, acept, numSolicitud, fecha])
            numSolicitud+=1
        if solicitudIgnored>100:
            break

##########################################################################
#Validar(id_perfil, habilidad_perfil,email_usuario_valida)
Validar=[]
for i in Solicitud:
    if i[2]=="'Aceptada'":
        for j in NEW_Habilidad:
            if Usuarios[NEW_Habilidad.index(j)]==i[0] and  NEW_Habilidad.index(j)%2==0:

                Validar.append([Usuarios.index(i[0])+1,j[0],i[1]])
############################################################################
#Admin(id_empresa,fecha_de_inicio, fecha_fin, mail_admin)
Admin=[]
for i in IDEmpresa:
    mes = random.randint(1, 12)
    if mes < 10:
            mes = "0" + str(mes)
    dia = random.randint(1, 28)
    if dia < 10:
            dia = "0" + str(dia)
    ano = 2010
    fecha = "'"+str(dia) + '-' + str(mes) + '-' + str(ano)+"'"

    mes = random.randint(1, 12)
    if mes < 10:
            mes = "0" + str(mes)
    dia = random.randint(1, 28)
    if dia < 10:
        dia = "0" + str(dia)
    ano = 2012
    fecha2 = "'"+str(dia) + '-' + str(mes) + '-' + str(ano)+"'"

    j=IDEmpresa.index(i)+1
    Admin.append([i,fecha,fecha2,Usuarios[j]])
    Admin.append([i, fecha2, 'NULL', Usuarios[-j]])


#############################################################################
#Cargos Disponibles(nombre, id_empresa,vacantes,sueldo, mail admin, fecha disponible)

CargosDisponibles=[]
beef=0
for i in IDEmpresa:
    for j in Puesto: 
        mes = random.randint(1, 12)
        if mes < 10:
                mes = "0" + str(mes)
        dia = random.randint(1, 28)
        if dia < 10:
                        dia = "0" + str(dia)
        ano = 2013
        fecha = "'"+str(dia) + '-' + str(mes) + '-' + str(ano)+"'"
        sueldo=random.randint(100000,100000000)
        vacantes=random.randint(5,30)
        for k in Admin:
            if k[0]==i and beef==0:
                beef=1
                CargosDisponibles.append([j,i,sueldo, vacantes,k[3],fecha,'NULL'])
            else:
                beef=0
###############################################################################
#Postulacion(nombre_cargo, id_empresa, id_perfil, fecha_postulacion, aceptado)

Postulacion=[]

for i in CargosDisponibles:
    cont=0
    for j in IDPerfil:
        mes = random.randint(1, 12)
        if mes < 10:
                mes = "0" + str(mes)
        dia = random.randint(1, 28)
        if dia < 10:
                        dia = "0" + str(dia)
        ano = 2014
        fecha = "'"+str(dia) + '-' + str(mes) + '-' + str(ano)+"'"
        if cont<1:
            Postulacion.append([i[0],i[1],j,fecha,'TRUE'])
        elif cont<10:
            Postulacion.append([i[0], i[1], j, fecha, 'FALSE'])
        cont+=1


###############################################################################
#notificacion(id_notificacion, enail_usuario, estado, tipo_notificacion)
notificacion=[]
for i in Solicitud:
    if i[2]=="'Aceptada'" or i[2]=="'Rechazada'":
        notificacion.append([i[3],"'leido'","'solicitud'",Usuarios.index(i[1])+2])
    else:
        notificacion.append([i[3],"'no leido'","'solicitud'",Usuarios.index(i[1])+2])
c =0

for i in Comentario:
    for j in Publicacion:
        if i[2] == j[0]
        notificacion.append(i[0], "'no leido'" , "'publicacion'",  j[1])

for i in SubComentario:
    for j in Comentario:
        if i[1] == j[2]
        notificacion.append(i[0], "'no leido'" , "'comentario'",  i[2])








def CambiarABD(lista ,nombre):
    lista2=[]
    for i in lista:
        cosa1=''
        for j in i:
            if j==i[-1]:
                cosa1 += str(j)
            else:
                cosa1+=str(j)+', '
        lista2.append(cosa1)
    linea1='INSERT INTO '+nombre+ '\n VALUES '
    print(linea1)

    for i in lista2:
        if i==lista2[-1]:
            print('(' + i + ')')
        else:
            print('('+i+'),')
    print(';')
    print('\n')
    print('')
    print('')


CambiarABD(Solicitud ,'solicitud(email_usuario,email_usuario_amistad, aceptada, id_solicitud,fecha_solicitud)')

CambiarABD(Validar,'validar(id_perfil, habilidad_perfil,email_usuario_valida)')

CambiarABD(Admin,'admin(id_empresa,fecha_de_inicio, fecha_fin, mail_admin)')

CambiarABD(Postulacion,'postulacion(nombre_cargo, id_empresa, id_perfil, fecha_de_postulacion, aceptado)')

CambiarABD(CargosDisponibles,'cargos_disponibles(nombre, id_empresa,vacantes,sueldo, mail_admin, fecha_disponible, descripcion)')

CambiarABD(notificacion,'notificacion(id_notificacion, estado, tipo_notificacion, id_perfil)')

