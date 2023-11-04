import os

class StanFileHandler:
    def __init__(self, storage_directory: str):
        self.storage_directory = storage_directory
        if not os.path.exists(storage_directory):
            os.makedirs(storage_directory)

    def save_stan_file(self, model_code, model_name: str):
        # Save the Stan model code to a .stan file
        file_path = os.path.join(self.storage_directory, f"{model_name}.stan")
        with open(file_path, 'w') as file:
            file.write(model_code)
        return file_path

    def load_stan_file(self, model_name: str):
        # Load the Stan model code from a .stan file
        file_path = os.path.join(self.storage_directory, f"{model_name}.stan")
        with open(file_path, 'r') as file:
            model_code = file.read()
        return model_code

    # You might add additional utility methods if needed
