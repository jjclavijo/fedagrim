# Archivos

El archivo [informacion-web.csv](./informacion-web.csv)
Tiene información por provincia acerca de la dirección de catastro, recopilada a partir de las
páginas web oficiales.

El archivo [delegaciones.csv](./delegaciones.csv)
Tiene una lista --incompleta-- de las delegaciones de catastro provinciales.

El archivo [delegaciones.gpkg](../gpkg/delegaciones.gpkg) 
Tiene una capa vectorial con las delegaciones que se pudieron ubicar en forma automática utilizando nominatim. No es la lista completa, pero sirve por ahora de ejemplo.

# Geocoding de delegaciones.

para obtener las direcciones se uso nominatium.

```
while read prov loc dir
do
curl "https://nominatim.openstreetmap.org/search?country=Argentina&state=$prov&city=$loc&street=$dir&limit=1&format=geojson" >> Direcciones.geojson
done <<< $( cut -d, -f 1,2,4 delegaciones.csv | tr ',' '\t' | sed 's/\([a-z]\)\([A-Z]\)/\1 \2/;s/[Nn][rR]*[oO]*°//g;s/[Nn][rR][oO]//g' | tr 'A-Z' 'a-z' | sed 's/ /%20/g')
```
Luego se utilizó sed para separar la lineas coorrespondeintes

```
sed 's/}{\(\"type\":\ *\"FeatureColl\)/}\n{\1/g' Direcciones.geojson > Direcciones_linea.geojson
```

Finalmente se generó un fid para cada línea, tanto en el geojson como en el csv


```
nl -w1 Direcciones_linea.geojson | sed -n 's/\([0-9]*\)\t{.*\"features":\[/\1:\t/g;s/]}$//;s/\([0-9]*\):\t\(.*properties\":{\)/\2\"fid\":\1,/p' > Delegaciones.geojson

seq 1 216 | paste - delegaciones.csv
```
