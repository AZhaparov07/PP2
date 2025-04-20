'''
CREATE OR REPLACE FUNCTION get_phonebook_paginated(limit_count INT, offset_count INT)
RETURNS TABLE(id INT, name TEXT, phone TEXT)
AS $$
BEGIN
    RETURN QUERY
    SELECT phonebook.id, phonebook.name::TEXT, phonebook.phone::TEXT
    FROM phonebook
    LIMIT limit_count OFFSET offset_count;
END;
$$ LANGUAGE plpgsql;
'''


import psycopg2
from config import load_config

def get_phonebook_paginated(limit, offset):
    conn = None
    try:
        params = load_config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT * FROM get_phonebook_paginated(%s, %s)", (limit, offset))
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
    except Exception as e:
        print("Error:", e)
    finally:
        if conn is not None:
            conn.close()

limit = 7
offset = 2
get_phonebook_paginated(limit, offset)