from app.handlers.pdf_handler import upload_pdf
from app.handlers.video_handler import upload_video
from app.handlers.qa_handler import ask_question
from app.handlers.load_data_handler import load_data


def show_menu():
    print("\n=== MAIN MENU ===")
    print("1) Upload PDF")
    print("2) Upload Video")
    print("3) Ask Question")
    print("4) Load Data")
    print("0) Exit")

    choice = input("Choose option: ").strip()

    if choice == "1":
        upload_pdf()
    elif choice == "2":
        upload_video()
    elif choice == "3":
        ask_question()
    elif choice == "4":
        load_data()
    elif choice == "0":
        print("Goodbye")
        exit()
    else:
        print("Invalid choice")