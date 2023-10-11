from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://7cohmii5g9gu96c9j1hv:pscale_pw_HhFJIhNeRpPlY5nN0bMCBN5EJvldFoZaxiQM4wO7KwB@aws.connect.psdb.cloud/r9?charset=utf8mb4"

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

