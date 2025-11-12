import pytest
import psycopg2

def test_sql_schema():
    conn = psycopg2.connect(
        host="localhost",
        database="sonarqube",
        user="sonar",
        password="sonar_secure_password"
    )
    cur = conn.cursor()
    cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'users'")
    columns = [row[0] for row in cur.fetchall()]
    assert 'id' in columns
    assert 'name' in columns
    cur.close()
    conn.close()