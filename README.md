**Relstorage**

https://relstorage.readthedocs.io/en/latest/index.html

RelStorage is a storage implementation for ZODB that stores pickles in a relational database. It is intended to be as 
transparent as possible, so that you can use it as a drop-in replacement for FileStorage.

Permet guardar els objectes de ZODB dins d'una base de dades relacional d'igual forma a com els guardem a un fitxer. 
Això permet tenir integrada la base de dades relacional, Oracle en el nostre cas, en ZODB.

Per a fer-ho, s'ha de crear el fitxer de configuració de ZODB per a que utilitzi RelStorage com a backend. Teniu 
l'exemple al projecte al fitxer zodb_config.zcml.

A més s'ha de crear un usuari a l'Oracle en els permisos necessaris per a que ZODB pugue accedir a la base de dades.

El podeu crear en les següents instruccions a l'Oracle des del compte _sys as sysdba_:

_CREATE USER zodb IDENTIFIED BY zodb 
DEFAULT TABLESPACE USERS
TEMPORARY TABLESPACE TEMP;
ALTER USER zodb QUOTA UNLIMITED ON USERS;
GRANT EXECUTE ON DBMS_LOCK TO zodb;
GRANT CONNECT, RESOURCE, CREATE TABLE, CREATE SEQUENCE, CREATE VIEW TO zodb;_

Evidentment podeu canviar el nom d'usuari i contrasenya, que ara són _zodb_, pels que vulgueu.