-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` compute la cantidad de registros por letra de la 
-- columna 2 y clave de al columna 3; esto es, por ejemplo, la cantidad de 
-- registros en tienen la letra `b` en la columna 2 y la clave `jjj` en la 
-- columna 3 es:
-- 
--   ((b,jjj), 216)
-- 
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
data = LOAD 'data.tsv'
    AS (f1:CHARARRAY, f2:bag{}, f3:MAP[]);
DUMP data;
a = FOREACH data GENERATE FLATTEN(f2), FLATTEN(KEYSET(f3));
DUMP a;
b = FOREACH a GENERATE ($0, $1) AS c;
DUMP b;
d = GROUP b BY c;
DUMP d;
e = FOREACH d GENERATE group, COUNT(b);
DUMP e;
STORE e INTO 'output';
