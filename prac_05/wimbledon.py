def read_wimbledon_data(filename):
    """Read the Wimbledon champions data from a CSV file."""
    champions = []
    countries = set()

    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            if line.startswith('Year'):
                continue
            parts = line.strip().split(",")
            if len(parts) > 1:
                champion = parts[2].strip()
                country = parts[1].strip()
                champions.append((champion, country))
                countries.add(country)
    return champions, countries
def count_champions_wins(champions):
    """Count how many times each champion has won Wimbledon."""
    champion_counts = {}
    for champion, country in champions:
        if champion in champion_counts:
            champion_counts[champion] += 1
        else:
            champion_counts[champion] = 1
    return champion_counts


def display_champions(champion_counts):
    """Display the champions and the number of times they have won."""
    print("Wimbledon Champions:")
    for champion, wins in sorted(champion_counts.items()):
        print(f"{champion} {wins}")


def display_countries(countries):
    """Display the list of countries in alphabetical order."""
    print("\nThese countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def main():
    """Main function to read, process, and display the data."""
    champions, countries = read_wimbledon_data("wimbledon.csv")
    champion_counts = count_champions_wins(champions)

    display_champions(champion_counts)
    display_countries(countries)

    main()
