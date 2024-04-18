class APIConstants:
    """
    class that stores contants
    """

    BASE_URL = "https://jsonplaceholder.typicode.com"
    TODOS_ENDPOINT = "todos"

    @property
    def todo_url(self):
        """
        constructs the complete url by combining base_url and todos_endpoint
        """
        return f"{self.BASE_URL}/{self.TODOS_ENDPOINT}"