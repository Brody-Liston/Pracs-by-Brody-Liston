
from programming_language import ProgrammingLanguage

def main():

    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(ruby)
    print(python)
    print(visual_basic)

    language_list = [ruby, python, visual_basic]
    print('\n'"The dynamically typed languages are:"'\n')
    for i in language_list:
        i.is_dynamic()
        if i.is_dynamic() is True:
            print(i)


main()