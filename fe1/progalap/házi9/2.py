def beszivargas(dic):
    if "takarító" not in dic.values():
        return ""
    else:
        for name, job in dic.items():
            if job == "takarító":
                return name
