from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://klsxor2lnsp2ensqqw4b:pscale_pw_MdPYk3MbSir6H3kvrHkv8EwQdNAYR958RMOGd6SEcfk@aws.connect.psdb.cloud/r9?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._mapping)
    return jobs

