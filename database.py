import sqlite3

conn = sqlite3.connect('mhp3rd.db')

c = conn.cursor()

for row in c.execute("SELECT `ID`, `Name` FROM `Monster` ORDER BY `ID`") :
    print("{}  {}".format(row[0], row[1]))

print()

parts = []
for row in c.execute("SELECT PartID, Name \
                      FROM Monster_Part \
                      LEFT JOIN Body_Part \
                      ON Body_Part.ID = Monster_Part.PartID \
                      WHERE MonsterID = 1 \
                      ORDER BY PartID") :
    parts.append(row)

line = "Body Part"
for row in c.execute("SELECT Name FROM Damage_Type") :
    line = line + " | " + row[0]

print(line)

for part in parts:
    line = part[1]
    for row in c.execute("SELECT `Damages` FROM `Damage_Resistance` WHERE MonsterID = 1 AND BodyPart = {}".format(part[0])) :
        line = line + " | {}".format(row[0])
    print(line)
