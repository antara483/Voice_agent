# generate_env_example.py

with open(".env", "r") as infile, open(".env.example", "w") as outfile:
    for line in infile:
        if "=" in line and not line.strip().startswith("#"):
            key = line.split("=")[0]
            outfile.write(f"{key}=your-{key.lower().replace('_', '-')}-here\n")
