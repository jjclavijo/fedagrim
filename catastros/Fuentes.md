
# San Juan

http://geoserver.sgis.com.ar/geoserver/

# chubut

http://catastro.chubut.gov.ar/geoserver/

# Neuquen

http://catastro.neuquen.gov.ar/nqn_ide/services/IDE/Catastro/MapServer/WFSServer?request=GetCapabilities&service=WFS

http://catastro.neuquen.gov.ar/nqn_ide/services/IDE/Catastro/MapServer/WFSServer?service=WFS&request=GetCapabilities

Bounding completo: -71.81 -41.05 -69.9 -32.5
http://catastro.neuquen.gov.ar/nqn_ide/services/IDE/Catastro/MapServer/WFSServer?service=WFS&request=GetFeature&typeName=IDE_Catastro:Parcelas&bbox=-71.81,-41.05,-69.9,-32.5,urn:ogc:def:crs:EPSG:4326

maxFeatures es 40000 asi que hay que consultar por boxes.

# San Luis

http://visualcatsl.dyndns.info/geoserver/

# Buenos Aires

http://www.urbasig.gob.gba.gob.ar/geoserver/arba/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=arba:parcelas

# Cordoba

https://idecor-ws.mapascordoba.gob.ar/geoserver/

# Corrientes
https://geoportal.corrientes.gob.ar/geoserver/opengeo/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=opengeo:Parcelario_Catastral

Informacion incompleta, solo tiene parcelas de la capital.

# Formosa
https://sit.formosa.gob.ar/WMSServer?request=GetCapabilities

No hay WFS

# Entre Rios

Hay unos pdf para bajar pero no hay información completa.

http://www.entrerios.gov.ar/catastro/v2/pdfs/pdfs.php

# Jujuy 

IDERA Dice que hay, y hay!

http://190.52.39.247:9881/geoserver/Provincia/ows?service=WFS&version=2.0.0&request=GetCapabilities


# La Pampa

Crear usuario

Hay PDFS

curl "https://catastro.lapampa.gob.ar/images/stories/Archivos/Cartografia/Planos/074.pdf" -o 075.pdf

y KML

https://catastro.lapampa.gob.ar/images/stories/Archivos/Cartografia/LOTERO_PROVINCIAL.rar

Se los podria combinar y con un poco de esfuerzo unir los bordes, para tener un lotero completo. Dificil pero posible.

# Mendoza

http://idemza2.mendoza.gov.ar/geoserver/

# Misiones

http://www.ide.misiones.gov.ar/cgi-bin/mapserv?MAP=/var/www/ide/htdocs/00_INFO_PORTAL_IDE/WMSMinEcologia.map&service=WFS&version=1.1.0&request=GetFeature&typeName=parcelario_mnes

# Rio Negro

http://ide.extranet.rionegro.gov.ar/geoserver/ows?service=wfs&version=2.0.0&request=GetCapabilities

No tiene parcelas

http://catastro.rionegro.gov.ar/arcgis/rest/services/IDE/PARCELAS/MapServer/0/query?where=1+%3D+1&geometry=geometryType%3DesriGeometryEnvelope%26geometry%3D-70%2C-40%2C-69.9%2C-39.9&geometryType=esriGeometryEnvelope&spatialRel=esriSpatialRelContains&returnGeometry=true&returnTrueCurves=false&geometryPrecision=3&returnIdsOnly=false&returnZ=false&returnM=false&returnDistinctValues=false&f=pjson

Ahi tiene etiquetas de parcelas, me sirve.

## COUNT

http://catastro.rionegro.gov.ar/arcgis/rest/services/IDE/PARCELAS/MapServer/0/query?where=1+%3D+1&geometry=geometryType%3DesriGeometryEnvelope%26geometry%3D-70%2C-40%2C-69.9%2C-39.9&geometryType=esriGeometryEnvelope&spatialRel=esriSpatialRelContains&f=pjson&returnCountOnly=true

# Salta

http://geoportal.idesa.gob.ar/geoserver/ows?service=wfs&version=2.0.0&request=GetFeature&typeName=geonode:fc_parcelas_v11

# Santa Fe

https://www.santafe.gov.ar/idesf/catalogo/srv/spa/metadata.show?uuid=32cf0fa0-eb2d-11de-ac11-00145e46faf9

Muy buen catalogo 

WMS WMTS CWS, WFS??? son unos capos.

# Tucuman

http://131.161.237.108:8080/geoserver/

# Santiago a duras penas tiene catastro.

# La Rioja

http://catastroweb.com.ar:8091/geoserver/ows?service=wfs&version=2.0.0&request=GetCapabilities

# Chaco tiene WMS

http://www.catastrochaco.gov.ar/cgi-bin/mapserv.exe?map=C:%5Cms4w%5CApache%5Chtdocs%5Cmapa%5Cassets%5Cmapfiles%5Ccatastro-mapa-chaco.map&service=wms&request=GetCapabilities

IDERA Dice que hay, pero no hay. Parece que el DNS no anda.

# Santa Cruz

Hay un wms sin parcelario completo 

http://spm.sitsantacruz.gob.ar/geoserver/
