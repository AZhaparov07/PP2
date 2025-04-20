'''
CREATE OR REPLACE PROCEDURE insert_many_users(names TEXT[], phones TEXT[])
AS $$
DECLARE
    i INT;
    invalid_name TEXT;
    invalid_phone TEXT;
BEGIN
    FOR i IN 1..array_length(names, 1) LOOP
        IF phones[i] ~ '^\d+$' THEN
            BEGIN
                INSERT INTO phonebook(name, phone)
                VALUES (names[i], phones[i]);
            EXCEPTION WHEN unique_violation THEN
                UPDATE phonebook
                SET phone = phones[i]
                WHERE name = names[i];
            END;
        ELSE
            invalid_name := names[i];
            invalid_phone := phones[i];
            RAISE NOTICE 'Invalid data: % %', invalid_name, invalid_phone;
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;
'''


import psycopg2
import config

def insert_many_users(names, phones):
    conn = psycopg2.connect(**config.load_config())
    cur = conn.cursor()
    cur.execute("CALL insert_many_users(%s, %s)", (names, phones))
    
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    names = ['alina', 'amilai'] 
    phones = ['87025145447', '22222222222']  
    
    insert_many_users(names, phones)
    print("Data inserted ")