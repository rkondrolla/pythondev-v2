from sqlalchemy import create_engine
import os

# Define the correct database connection string

db_connection_string = "mysql+pymysql://admin:Mustang123@database-1.cdqw6m6qe49l.us-east-2.rds.amazonaws.com/UNMSHUTTLE?charset=utf8mb4"


# Create an engine with SSL connection
engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "us-east-2-bundle.pem"  # Adjust this path to your SSL certificate
        }
    }
)

# Connect and execute a query

