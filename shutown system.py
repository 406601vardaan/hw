def shutdown():
    answer = input("Do you want to shut down? ")

    if answer == "Yes":
        print("shutting down")
    elif answer == "No":
        print("abort shut down")
    else:
        print("sorry")

shutdown()
