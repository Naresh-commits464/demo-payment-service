# Synthetic values for security-scanner testing only.
MONGO_URI = "mongodb+srv://admin:Sup3rSecretDbPass@cluster0.abcde.mongodb.net/prod"


def get_db_connection():
    return connect(MONGO_URI)
