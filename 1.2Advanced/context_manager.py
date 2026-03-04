class MyContext:
    def __enter__(self):
        print("Entering the context")
        return "Resource Ready"
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context")
        # You can handle exceptions here if needed
        return False  # If True, suppresses the exception

with MyContext() as res:
    print(res)
