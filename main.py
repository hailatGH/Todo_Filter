from controllers import TodoTitleFilter
from constants import APIConstants

class Application:
    """
    The main application class to be excuted
    """

    def __init__(self):
        """
        initilizes the class by create instance of APIConstants class
        """
        self.constants = APIConstants()

    def get_filter_string(self):
        """
        Propmt users to enter the filter string and return the value
        """
        return input("Please enter the desired filter string:  ")
    
    def create_filter(self):
        """
        creates a filter instance form TodoTitleFilter class and returns the instance
        """
        filter_string = self.get_filter_string()
        return TodoTitleFilter(self.constants.todo_url, filter_string)

    def run_filters(self):
        """
        executes the functions sequentailly to achive the desired result
        """
        filter = self.create_filter() 
        filter.fetch_data()
        filter.process_data()
        filter.display_results()
        filter.check_title_type()

if __name__ == "__main__":
    app = Application()
    app.run_filters()