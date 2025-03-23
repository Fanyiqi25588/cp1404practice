import datetime
from project import Project


def load_projects(filename="projects.txt"):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    try:
        with open(filename, "r") as file:
            next(file)
            for line in file:
                parts = line.strip().split("\t")
                if len(parts) == 5:
                    project = Project(*parts)
                    projects.append(project)
        print(f"Loaded {len(projects)} projects from {filename}")
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    return projects


def save_projects(filename, projects):
    """Save the list of projects to a file."""
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")
    print(f"Projects saved to {filename}")


def display_projects(projects):
    """Display incomplete and completed projects separately, sorted by priority."""
    incomplete = sorted([p for p in projects if not p.is_complete()])
    completed = sorted([p for p in projects if p.is_complete()])

    print("\nIncomplete projects:")
    for project in incomplete:
        print(f"  {project}")

    print("\nCompleted projects:")
    for project in completed:
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Filter projects by user-specified start date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        filtered_projects = sorted([p for p in projects if p.start_date > filter_date], key=lambda p: p.start_date)
        for project in filtered_projects:
            print(project)
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")


def add_project(projects):
    """Prompt user for project details and add a new project."""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))

    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)
    print("Project added.")


def update_project(projects):
    """Allow user to update an existing project's completion and priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    try:
        choice = int(input("Project choice: "))
        project = projects[choice]
        print(project)

        new_completion = input("New Percentage (leave blank to keep current): ")
        if new_completion:
            project.completion_percentage = int(new_completion)

        new_priority = input("New Priority (leave blank to keep current): ")
        if new_priority:
            project.priority = int(new_priority)

        print("Project updated.")
    except (ValueError, IndexError):
        print("Invalid selection.")


def main():
    """Main menu-driven program for project management."""
    projects = load_projects()

    MENU = """
- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
"""
    print("Welcome to Pythonic Project Management")

    while True:
        print(MENU)
        choice = input(">>> ").lower()

        if choice == "l":
            filename = input("Enter filename to load: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Enter filename to save: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            save = input("Would you like to save to projects.txt? (yes/no): ").lower()
            if save == "yes":
                save_projects("projects.txt", projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please select again.")


if __name__ == "__main__":
    main()
