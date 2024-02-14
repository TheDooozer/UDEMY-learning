import webbrowser

user_input = input("Enter: ").replace(" ", "+")
webbrowser.open("https://google.com/search?q=" + user_input)

