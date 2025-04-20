'''
CREATE OR REPLACE PROCEDURE delete_user_by_name_or_phone(username TEXT, userphone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE name = username OR phone = userphone;
END;
$$;
'''

import psycopg2
from config import load_config

def delete_user(username, userphone):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("CALL delete_user_by_name_or_phone(%s, %s)", (username, userphone))
                print("User deleted")
    except Exception as e:
        print("Error:", e)

delete_user('arystan', '87026142282')