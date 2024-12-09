#!/usr/bin/python

import jwt
from datetime import datetime, timezone, timedelta
import json

# used timezone.utc instead of datetime.utcnow() because it is deprecated
# used json for printing JWT in a human readable format

payload = {
	"username":"abdelhamid",
	"role":"admin",
	# expire in one hour for example
	"exp": 	datetime.now(timezone.utc) + timedelta(hours=1)
}

secret = "secret_key"

token = jwt.encode(payload,secret,algorithm='HS256')

print(f'Encoded JWT :\n\n{token}\n\n')
decoded = jwt.decode(token,secret,algorithms=["HS256"])

print(f'Decoded JWT : \n\n')
pretty_print = json.dumps(decoded,indent=4)
print(pretty_print)
