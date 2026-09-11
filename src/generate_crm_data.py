import os
import psycopg
from dotenv import load_dotenv
from faker import Faker

load_dotenv()

fake = Faker("pt_BR")

# Conexão com o PostgreSQL
conn = psycopg.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
)

# Gera 100 clientes
for _ in range(100):
    conn.execute(
        """
        INSERT INTO crm.customers (name, email, state)
        VALUES (%s, %s, %s)
        """,
        (fake.name(), fake.email(), fake.estado_sigla()),
    )

conn.commit()
conn.close()

print("100 clientes gerados com sucesso!")