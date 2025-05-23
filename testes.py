from time import sleep

print("Início em:")
for i in range(5, 0, -1):
    print(f"Segundos: {i}", end="\r")
    sleep(1.0)

print("Fim        ")
