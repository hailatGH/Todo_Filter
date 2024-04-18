import requests

class TodoTitleFilter:
    """
    Fetches todo data fro a URL, filters tiltles based on the filter string provide, perform type checking and display result.
    """
    
    def __init__(self, url, filter_string):
        """
        Initializes the class with url, and filter string

        Args:
            url (str): The URL to fetch data from
            filter_string (str): The string to filter titles by
        """

        self.url = url
        self.todos = []
        self.filtered_title = []
        self.filter_string = filter_string

    def fetch_data(self):
        """
        Fetches todo data from the URL and stores it in the todos list

        Raises: 
            requests.exceptions.RequestException: If thers is an error during the request.
        """
        
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            self.todos = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error getting data: {e}")

    def process_data(self):
        """
        Filters titles from the fetched data based on the filter string and stores them in the filtered_title list.
        """
        self.filtered_title = [todo['title'] for todo in self.todos if self.filter_string in todo['title']]

    def display_results(self):
        """
        Displays the filtered titles with type checking if any titles were found
        """
        if self.filtered_title:
            print(f"\nTitles containg '{self.filter_string}':")
            for title in self.filtered_title:
                if isinstance(title, str):
                    print(f"- {title}")
                else:
                    print(f"\n** Unexpected data type: '{type(title)}' **")
        else:
            print(f"\nNot title found matching '{self.filter_string}'")

    def check_title_type(self):
        """
        Checks if any titles in the filtered list are of type integer and prints them.
        """
        if self.filtered_title:
            found_int_titles = False
            for title in self.filtered_title:
                if isinstance(title, int):
                    found_int_titles = True
                    print(f"Title '{title}' is part of type integer.")
            
            if not found_int_titles:
                print("\nNot title found of type integer.")