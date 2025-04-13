import wikipedia

def main():
    print("Wikipedia Search\n")

    while True:
        title = input("Enter page title: ").strip()
        if not title:
            print("Thank you.")
            break

        try:
            # Try to get the page
            page = wikipedia.page(title, auto_suggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipedia.exceptions.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()

