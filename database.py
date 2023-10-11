from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://4919448ioqjnfe3jjfey:pscale_pw_Ff5gGb2wg8oDDg3T69xFrAvzT7kMh6SJ2jLwEjKJaCC@aws.connect.psdb.cloud/r9?charset=utf8mb4"

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

