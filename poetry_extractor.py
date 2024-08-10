from vo.poetry import Poetry
import os


def extract():
    file_path = 'poetries.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    poetries = content.split('==========')

    poetry_list = []
    for index in range(len(poetries)):
        poetry_list.append(__extract_poetry(poetries[index], index))

    return poetry_list


def __extract_poetry(poetry_content, progress):
    poetry_lines = poetry_content.split('\n')
    line_count = len(poetry_lines)

    if poetry_lines[0] == '':
        poetry_lines.pop(0)
        line_count -= 1
    if poetry_lines[line_count - 1] == '':
        poetry_lines.pop()
        line_count -= 1

    art_picture_path = os.path.join('resource', 'pic{}.png'.format((progress % 3) + 1))
    title, subtitle = __extract_title_subtitle(poetry_lines[0])
    author = __extract_author(poetry_lines[1])
    publish_time = __extract_publish_time(poetry_lines[-2])
    address = __extract_address(poetry_lines[-1])
    introduce_index, introduce = __extract_introduce_and_index(poetry_lines, line_count)

    main_text = ''
    main_text_start_index = 2 if introduce_index == -1 else introduce_index + 2
    for index in range(main_text_start_index, line_count - 3):
        main_text = ''.join([main_text, poetry_lines[index], '\n'])
    main_text = ''.join([main_text, poetry_lines[line_count - 3]])

    return Poetry(title, author, main_text, publish_time, address, subtitle, introduce, recite_progress=progress,
                  art_picture_path=art_picture_path)


def __extract_title_subtitle(poetry_line):
    segments = poetry_line.split('•')
    title = segments[0]
    subtitle = segments[1] if len(segments) > 1 else None
    return title, subtitle


def __extract_author(poetry_line):
    return poetry_line.strip()


def __extract_publish_time(poetry_line):
    return poetry_line.strip()


def __extract_address(poetry_line):
    return poetry_line.strip()


def __extract_introduce_and_index(poetry_lines, line_count):
    change_line_index = -1
    for index in range(2, line_count - 2):
        if poetry_lines[index] != '':
            continue

        change_line_index = index
        break

    introduce_index = -1 if change_line_index == -1 else change_line_index - 1
    introduce = None if introduce_index == -1 else poetry_lines[introduce_index]
    return introduce_index, introduce
