import sqlalchemy
from sqlalchemy import create_engine, text

engine = create_engine("mysql://root:DmVUZFeMESZcbunysgpfZDxIYCLDrXHb@shinkansen.proxy.rlwy.net:49234/railway")
def projects_from_database():
    with engine.connect() as conn:
        results = conn.execute(text("select * from Projects"))
        results_all = results.all()
        result_row = results_all[0]

        projects = []
        for result in results_all:
            print(result._mapping)
            projects.append(result._mapping)
        return projects
    
def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM Projects WHERE id = :val"), {"val":id})
        #print(type(result.mappings().all()))
        result_list = result.mappings().all()
        if len(result_list) == 0:
            return None
        return dict(result_list[0])
    
#load_job_from_db(1)