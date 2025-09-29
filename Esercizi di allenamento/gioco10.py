def deep_get(d: dict | list, path: list, default=None):
    for p in path:
        if isinstance(d,dict):
            if p in d:
                d = d[p]
            else:
                return default
        elif isinstance(d, list):
            if isinstance(p, int) and 0 <= p < len(d):
                d = d[p]
            else:return default
        else:
            return default
    return d
            

d = {
    "regno": {
        "foresta": [
            {"albero": "quercia"},
            {"albero": "pino"}
        ]
    }
}

path = ["regno", "foresta", 1, "albero"]
default = "ignoto"


print(deep_get(d,path,default))