-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` compute Calcule la cantidad de registros en que 
-- aparece cada letra minúscula en la columna 2.
-- 
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--

data = LOAD 'data.tsv'
    AS (f1:CHARARRAY, f2:BAG{}, f3:MAP[]);

quitar = FOREACH data GENERATE FLATTEN (f2) AS minus, f1;
agrupa = GROUP quitar by minus;
cuenta = FOREACH agrupa GENERATE group, COUNT(quitar.f1);
STORE cuenta INTO 'output';
