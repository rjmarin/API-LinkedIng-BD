1)SELECT p.id , COUNT(*) FROM perfil p LEFT JOIN comentario c ON p.id = c.id_usuario GROUP BY p.id ORDER BY p.id;

2)SELECT p.id_publicacion, COUNT(*) FROM publicacion p LEFT JOIN comentario c ON p.id_publicacion = c.id_publicacion GROUP BY p.id_publicacion ORDER BY p.id_publicacion;

3)SELECT u.email, COUNT(*) FROM usuario u LEFT JOIN validar v ON u.email = v.email_usuario_valida  GROUP BY u.email ORDER BY COUNT(*);
## no tenemos datos en la tabla validar todavia (se arregla para la entrga 3##

4)SELECT p.id , COUNT(*) FROM perfil p LEFT JOIN notificacion n ON p.id = n.id_perfil GROUP BY p.id ORDER BY p.id; 
