import json,os,platform,hashlib,stat
# on récupère les dossiers seulement, avec leur chemin complet (windows)
def hash_file(file_path):
    import hashlib
    sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            for block in iter(lambda: f.read(4096), b""):
                sha256.update(block)
        return sha256.hexdigest()
    except PermissionError:
        print(f" Permission denied: {file_path}")
        return None
    except FileNotFoundError:
        print(f" File not found: {file_path}")
        return None
    except Exception as e:
        print(f" Error reading {file_path}: {e}")
        return None


with open("file's_path.json", "r") as f:
    path = json.load(f)
template_paths = path["windows"]["important_files"]+path["windows"]["critical_directories"]+path["windows"]["optional_targets"]



user_base = "C:\\Users"
user_dirs = [
    user for user in os.listdir(user_base)
    if os.path.isdir(os.path.join(user_base, user))]


resolved_paths = []
for user in user_dirs:
    for template in template_paths:
        resolved_paths.append(template.replace("${user}", user))
if (platform.system().lower() == "windows"):
    final_dirs= [
        directory for directory in resolved_paths
        if os.path.isdir(os.path.join(directory)) and  os.access(os.path.join(directory), os.R_OK)]
    #print(final_dirs)

directories_linux = path["linux"]["important_files"]+path["linux"]["critical_directories"]+path["linux"]["optional_targets"]
if (platform.system().lower() == "linux"):
    final_dirs = [
        directory for directory in resolved_paths
        if os.path.isdir(os.path.join(directory)) and  os.access(os.path.join(directory), os.R_OK)]
    #print(final_dirs)

#calcul du Hash 
full_paths=[]
roots =[]
for directory in final_dirs:
    for root, dirs, files in os.walk(directory):
        for file in files:
            if os.access(os.path.join(root, file), os.R_OK):
                full_paths.append(os.path.join(root, file))


with open("hashes.txt", "w") as fichier_hashc:
    for file in full_paths:
        h = hash_file(file)
        if h is not None:
            fichier_hashc.write(f"{file} {h}\n")
        else:
            print(f"Skipped hashing for {file} due to error.")

with open("final_hash.txt", "w") as final_hash:
    h = hash_file("hashes.txt")
    final_hash.write(h)
