'''
CREATE OR REPLACE FUNCTION search_phonebook(pattern TEXT)
RETURNS TABLE (id INT, name VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT t.id, t.name, t.phone
    FROM phonebook t
    WHERE t.name ILIKE '%' || pattern || '%'
       OR t.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;
'''

import psycopg2
from config import load_config
def search_by_pattern(pattern):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM search_phonebook(%s);", (pattern,))
                results = cur.fetchall()
                for row in results:
                    print(row)
    except Exception as error:
        print("Error:", error)
if __name__ == '__main__':
    pattern=input("pattern: ")
    search_by_pattern(pattern)