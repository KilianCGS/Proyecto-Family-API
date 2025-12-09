class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        self._members.append({
        "id": self._generate_id(),
        "first_name": member['first_name'],
        "last_name": self.last_name,
        "age": member['age'],
        "lucky_numbers": member['lucky_numbers']
    })
        return self._members[-1]


    def delete_member(self, id):
        for m in self._members:
            if m["id"] == id:
                self._members.remove(m)
                return True
        return False

    def get_member(self, id):
         for value in self._members:
            if value["id"] == id:
                return {
                "id": value["id"],
                "first_name": value["first_name"],
                "age": value["age"],
                "lucky_numbers": value["lucky_numbers"]
            }
         return None

    def get_all_members(self):
        return self._members
