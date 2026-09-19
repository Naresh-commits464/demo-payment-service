# Synthetic values for security-scanner testing only.
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"


def get_aws_client():
    return {"access_key": AWS_ACCESS_KEY_ID, "secret_key": AWS_SECRET_ACCESS_KEY}
