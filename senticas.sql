

psql -h 201.238.213.114 -p 54321 -d grupo23 -U grupo23

create function validar_clave()
RETURNS TRIGGER 
AS $$
r = plpy.execute("SELECT COUNT(*) c FROM clave c WHERE  c.email_usuario  = {} and c.clave = {}  GROUP BY p.id;".format(TD['new']['email_usuario'], TD['new']['clave']))
if r[0]['c']  > 1: return 'SKIP'
else: return 'OK'
$$ LANGUAGE plpythonu;
CREATE TRIGGER clave BEFORE INSERT OR UPDATE ON clave FOR EACH ROW  EXECUTE PROCEDURE validar_clave();
   







