import sqlalchemy
from sqlalchemy import create_engine, text

engine = create_engine("mysql://root:DmVUZFeMESZcbunysgpfZDxIYCLDrXHb@shinkansen.proxy.rlwy.net:49234/railway")
with engine.connect() as conn:
    projects = conn.execute(text("select * from Projects"))
    print(projects)