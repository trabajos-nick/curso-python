#2 lsitas, una con nombres otra con appellidos
nombres = ["Nick", "Matias", "Camila", "Pedro", "Roberto"]
apellidos = ["Duran","Zing","Dalto","Robetix","tarado"]

#Registrar esta informacion en un txt de forma optima

with open("archivos_problemas_resueltos\\nombres_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son:\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n------------\n") for n,a in zip(nombres,apellidos)]

