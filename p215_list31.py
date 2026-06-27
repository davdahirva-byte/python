heros=['spider man','thor','hulk','iron man','captain america']

print(len(heros))

heros.append("black panther")
print(heros)

heros.remove("black panther")

print(heros)
i=heros.index("hulk")

heros.insert(i + 1, "black panther")

print(heros)
heros[1:3] = ["doctor strange"]

print(heros)