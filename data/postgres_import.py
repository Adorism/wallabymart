from sqlalchemy import create_engine
import pandas as pd
df = pd.read_csv('wallabymart_customer_data.csv')
# postgres doesn't like capitals or spaces
# that's probably my answer
df.columns = [c.lower() for c in df.columns]

engine = create_engine(
    'postgresql://audreymaldonado:tr33fr0g@localhost:5432/wallabymart')

df.to_sql("wallaby_customers", engine)
