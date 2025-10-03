# trim.py

def remove_empty_lines(filename):
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # filter hanya yang tidak kosong
    cleaned_lines = [line.strip() for line in lines if line.strip()]

    # print hasil ke console
    for line in cleaned_lines:
        print(line)

if __name__ == "__main__":
    # ganti "translate.txt" dengan nama file kamu
    remove_empty_lines("translate.txt")