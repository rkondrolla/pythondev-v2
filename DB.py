from sqlalchemy import create_engine
import os

# Define the correct database connection string

db_connection_string = os.environ[" DB_CONNECTION_STRI"]


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

