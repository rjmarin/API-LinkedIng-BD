1)SELECT u.email, COUNT(*) c FROM solicitud s, usuario u,  Estudio e WHERE e.grado_academico ='Doctorado' AND e.fecha_fin > '2018-09-11' AND s.email_usuario =u.email GROUP BY u.email  ORDER BY COUNT(*) DESC LIMIT 2;


2)SELECT EXTRACT(MONTH FROM cd.fecha_disponilbe) m, COUNT(*) c FROM cargos_disponilbes cd GROUP BY m;  


3)SELECT EXTRACT(MONTH FROM p.fecha_de _postulacion) m,AVG(COUNT(*)) FROM postulaciones p WHERE p.aceptada = 'false' GROUP BY m DESC; 


4)SELECT t.id_empresa, COUNT(*) c FROM trabaja t GROUP BY t.id_empresa ORDER BY  COUNT(* )DESC LIMIT 1;





