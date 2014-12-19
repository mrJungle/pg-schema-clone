pg-schema-clone
===============

Script per clonare uno schema da un DB ad un'altro

Obbiettivo:
Creare uno script python che riesca a fare download di uno schema o di una collezione di tabelle di uno schema postgres e lo spari sun un altro database.

Operazioni e TODO:
Effettuare controllo che sia installato il software Expect
Controllo che credenziali, db, schema e tabelle siano presenti nella sorgente dei dati
Controllo che credenziali, db, schema e tabelle siano presenti nella destinazione dei dati
Esecuzione dei file di script Expect con python in base ai parametri di un file di configurazione

documentazione presa da:

http://www.postgresql.org/docs/9.3/static/app-pgdump.html
http://www.thegeekstuff.com/2009/01/how-to-backup-and-restore-postgres-database-using-pg_dump-and-psql/

http://www.thegeekstuff.com/2010/10/expect-examples/

Per installare Expect:
sudo apt-get install expect
(controllare che i file abbiano i permessi di esecuzione, altrimenti non potranno essere eseguiti.)

-------------------------------------------------------------------------------------

USO:

1 - settare i parametri dei db in cartella Config

2 - eseguire: python dumpStart.py

