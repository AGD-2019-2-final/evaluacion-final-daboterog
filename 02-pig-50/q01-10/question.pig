-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` compute la cantidad de registros por letra. 
-- Escriba el resultado a la carpeta `output` del directorio actual.
--
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--

data = LOAD 'data.tsv'
    AS (letra:CHARARRAY, fecha:CHARARRAY, num:INT);

campos = FOREACH data GENERATE letra, num;
agrupa = GROUP campos BY letra;
cuenta = FOREACH agrupa GENERATE group, COUNT(campos.num);
STORE cuenta INTO 'output';