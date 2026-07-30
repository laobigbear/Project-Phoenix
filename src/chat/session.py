class Session:
    def __init__(self):
        self.history = []

    def add_to_history(self, user_input, ai_response):
        self.history.append((user_input, ai_response))

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history = []

    def save_history(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            for user_input, ai_response in self.history:
                f.write(f"User: {user_input}\n")
                f.write(f"AI: {ai_response}\n")
                f.write("\n")  # Add a newline between interactions

    def exit(self):
        print("Exiting the session.")
        exit()