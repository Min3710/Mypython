names=[
        ["김유신","계백","관창"],
        ["홍길동","이순신","강감찬","권율"],
        ["김구","윤봉길","안창호","안중근"]
      ]
for name in names:
    for warrior in name:
        print(warrior)

print()
print()
for name in names[0]:
    print(name)
names.append(["강감찬","왕건","이성계"])
print()
print()

for name in names:
    for warrior in name:
        print(warrior)
