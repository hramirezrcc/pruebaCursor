import datetime


def main() -> None:
    print("Hola, Gurú!")
    hoy = datetime.date.today().strftime("%Y-%m-%d")
    with open("evidencia2.txt", "w", encoding="utf-8") as f:
        f.write(f"Fecha de ejecución: {hoy}\n")


if __name__ == "__main__":
    main()
