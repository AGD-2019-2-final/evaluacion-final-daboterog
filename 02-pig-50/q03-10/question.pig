-- Pregunta
-- ===========================================================================
-- 
-- Obtenga los cinco (5) valores más pequeños de la 3ra columna.
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
data = LOAD 'data.tsv'
    AS (letra:CHARARRAY, fecha:CHARARRAY, num:INT);

campos = FOREACH data GENERATE num;
ordena = ORDER campos BY num;
top = LIMIT ordena 5;
STORE top INTO 'output';