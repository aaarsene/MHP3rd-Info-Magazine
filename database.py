import sqlite3



class MHP3DB :
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.c = self.conn.cursor()

    def get_monsters(self):
        """
        Return the list of the monsters
        """
        monsters = []
        for row in self.c.execute("SELECT `ID`, `Name` FROM `Monster` ORDER BY `ID`") :
            monsters.append(row)
        return monsters

    def get_parts(self, monster_id):
        parts = []
        for row in self.c.execute("SELECT PartID, Name \
                                   FROM Monster_Part \
                                   LEFT JOIN Body_Part \
                                   ON Body_Part.ID = Monster_Part.PartID \
                                   WHERE MonsterID = {} \
                                   ORDER BY PartID \
                                   ".format(monster_id)) :
            parts.append(row)
        return parts

    def get_damages(self, monster_id):
        damages = []
        parts = self.get_parts(monster_id)
        for part in parts :
            damages.append([])
            damages[-1].append(part[1])
            for row in self.c.execute("SELECT `Damages` \
                                  FROM `Damage_Resistance` \
                                  WHERE MonsterID = {0} \
                                  AND BodyPart = {1} \
                                  ".format(monster_id, part[0])) :
                damages[-1].append(row[0])
        return damages

    def get_damage_type(self):
        types = []
        for row in self.c.execute("SELECT Name FROM Damage_Type") :
            types.append(row)
        return types

if __name__ == '__main__':
    db = MHP3DB('mhp3rd.db')
    print(db.get_damages(1))
