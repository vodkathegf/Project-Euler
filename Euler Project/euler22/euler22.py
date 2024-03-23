class Name_Value():
    def __init__(self) -> None:
        pass

    def calculate_alphabetical_value(self, name):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        value = sum(alphabet.index(char.upper()) + 1 for char in name if char.isalpha())
        return value

    def calculate_name_score(self, names):
        total_score = 0
        for i, name in enumerate(names, start=1):
            alphabetical_value = self.calculate_alphabetical_value(name)
            name_score = alphabetical_value * i
            total_score += name_score
        return total_score


def main():
    name_value = Name_Value()
    with open(r"C:\Users\ÖMER\OneDrive\Masaüstü\Euler Project\euler22\names.txt", "r") as file:
        names = file.read().replace('"', " ").split(",")
        names.sort()

    result = name_value.calculate_name_score(names)
    print(f"name score of the file is {result}")

if __name__ == "__main__":
    main()