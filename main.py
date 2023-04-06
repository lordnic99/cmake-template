from re import template
import jinja2

project_type    = input("Project type 1, or 2: ")
cmake_version   = input("Please enter cmake minimum version: ")
project_name    = input("Enter porject name: ")
type_one        = "cmake_template_type_one.j2"
type_two        = "cmake_template_type_two.j2"

def open_template(template_path):
    with open(template_path,"r",encoding="UTF-8") as file:
        return file.read()

def save_file(content):
    with open("CMakeLists.txt","w",encoding="UTF-8") as file:
        file.write(content)

if __name__ == "__main__":
    if project_type == 1:
        path = type_one
    else:
        path = type_two
    template_output = jinja2.Template(open_template(path))
    file_content    = template_output.render(CMAKE_VERSION = cmake_version, PROJECT_NAME = project_name)
    save_file(file_content)


