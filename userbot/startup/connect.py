import os
REDIS_KEY = os.environ.get("REDIS_KEY", None)
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", None)
if REDIS_KEY and REDIS_PASSWORD:
    import redis
    redis_info = REDIS_KEY.split(":")
    dB = redis.StrictRedis(
        host=redis_info[0],
        port=redis_info[1],
        password=REDIS_PASSWORD,
        charset="utf-8",
        decode_responses=True,
    )
    print("Connected To Redis")
else:
    print("Could Not Connnect To Redis Check Your Redis Key And Pass if facing issue come to support group @Legend_userbot Quitting!")
    sys.exit(1)
