import os
import re

def replace_css_variables(file_path, variable_map):
    """Replace CSS variable values if their name matches an entry in the variable_map."""
    updated_lines = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            matches = re.finditer(r'(--[a-zA-Z0-9_-]+):\s*([^;]+);', line)
            for match in matches:
                var_name = match.group(1)
                if var_name in variable_map:
                    old_value = match.group(2)
                    new_value = variable_map[var_name]
                    line = line.replace(f'{var_name}: {old_value};', f'{var_name}: {new_value};')
            updated_lines.append(line)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(updated_lines)

def replace_html_variables(file_path, variable_dict):
    """Replace content inside {{}} in an HTML file if its key matches an entry in variable_dict."""
    updated_lines = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            matches = re.finditer(r'{{(.*?)}}', line)
            for match in matches:
                var_name = match.group(1).strip()
                if var_name in variable_dict:
                    line = line.replace(f'{{{{ {var_name} }}}}', variable_dict[var_name])
            updated_lines.append(line)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(updated_lines)

def traverse_and_replace(directory, css_variable_map, html_variable_dict):
    """Traverse directory and replace variables in CSS and HTML files."""
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith('.css'):
                replace_css_variables(file_path, css_variable_map)
            elif file.endswith('.html'):
                replace_html_variables(file_path, html_variable_dict)

def main():
    directory = input("Enter the directory path to scan: ").strip()
    if not os.path.exists(directory):
        print("The specified directory does not exist.")
        return

    css_variable_map = {
        '--main-color': 'blue',
        '--secondary-color': 'green',
    }

    html_variable_dict = {
        'username': 'JohnDoe',
        'email': 'johndoe@example.com',
    }

    traverse_and_replace(directory, css_variable_map, html_variable_dict)
    print("Replacement complete!")

if __name__ == "__main__":
    main()

