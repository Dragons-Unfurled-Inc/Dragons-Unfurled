# import dotenv
# from vue.start_vue import StartVue

# dotenv.load_dotenv(override=True)

# if __name__ == "__main__":
#     # run the StartVue
#     current_vue = StartVue()

#     # while current_vue is not none, the application is still running
#     while current_vue:
#         # a border between vue
#         with open('app/client/dessins_ascii/border.txt', 'r', encoding="utf-8") as asset:
#             print(asset.read())
#         # Display the info of the vue
#         current_vue.display_info()
#         # ask user for a choice
#         current_vue = current_vue.make_choice()

#     with open('app/client/dessins_ascii/fin.txt', 'r', encoding="utf-8") as asset:
#         print(asset.read())
