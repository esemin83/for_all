CREATE TABLE public.clients  (
	id        	int4 NOT NULL,
	client_id 	varchar(1024) NOT NULL,
	address   	varchar(1024) NOT NULL,
	through_id	varchar(1024) NOT NULL,
	PRIMARY KEY(id)
);
-----
CREATE SEQUENCE clients_id;
-----
CREATE OR REPLACE FUNCTION public.insert_to_clients (in client_id varchar, in address varchar, in through_id varchar) RETURNS void AS
'
    BEGIN
      INSERT INTO clients VALUES (nextval("clients_id"), client_id, address, through_id);
    END;
    '
LANGUAGE 'plpgsql';
----
truncate clients;
----

