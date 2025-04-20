'''
CREATE OR REPLACE PROCEDURE insert_or_update_user(p_name TEXT, p_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN

	IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
		UPDATE phonebook
		SET phone = p_phone
		WHERE name = p_name;
	ELSE 
		INSERT INTO phonebook(name,phone)
		VALUES (p_name,p_phone);
	END IF;
END;
$$;
'''


import psycopg2
from config import load_config
def insert_or_update_user(name,phone):
    command ="""CALL insert_or_update_user(%s, %s); """
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(command, (name,phone))
                conn.commit()
                print(f"User {name} inserted or updated succesfully.")
    except Exception as e:
        print(f"Error: {e}")
if __name__=='__main__':
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    insert_or_update_user(name,phone)