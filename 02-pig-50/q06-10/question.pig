-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` Calcule la cantidad de registros por clave de la 
-- columna 3. En otras palabras, cuántos registros hay que tengan la clave 
-- `aaa`?
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

a = FOREACH data GENERATE FLATTEN(f3) AS f32;
DUMP a;

b = GROUP a BY f32;
DUMP b;

c = FOREACH b GENERATE group, COUNT(a);
DUMP c;

STORE c INTO 'output' USING PigStorage(',');