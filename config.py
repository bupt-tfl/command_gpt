import os

profile_path = os.path.expanduser("~/.bash_profile")
env_vars = {}

with open(profile_path, "r") as f:
    for line in f:
        if line.startswith("export "):
            line = line.strip("export ")
            key, value = line.split("=")
            env_vars[key] = value.strip()

print(env_vars)



