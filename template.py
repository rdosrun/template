import os
import re
"""
CSS Variables:
--dark-color
--primary-color
--primary-company-color
--secondary-color
--var
--store-button
--light-color
--store-button-hover

HTML Variables ({{ }} content):
company_description
faq
company_name
company_email
answer
services
"""


def extract_css_variables(file_path):
    """Extract all CSS variable names (e.g., --var-name) from a CSS file."""
    variables = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            matches = re.findall(r'--[a-zA-Z0-9_-]+', line)
            variables.extend(matches)
    return variables

def extract_html_variables(file_path):
    """Extract all content inside {{ }} in an HTML file."""
    variables = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            matches = re.findall(r'{{(.*?)}}', line)
            variables.extend(matches)
    return variables

def traverse_directory(directory):
    """Traverse a directory and extract CSS and HTML variables."""
    css_variables = []
    html_variables = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith('.css'):
                css_variables.extend(extract_css_variables(file_path))
            elif file.endswith('.html'):
                html_variables.extend(extract_html_variables(file_path))

    return css_variables, html_variables

def main():
    directory = input("Enter the directory path to scan: ").strip()
    if not os.path.exists(directory):
        print("The specified directory does not exist.")
        return

    css_variables, html_variables = traverse_directory(directory)

    print("\nCSS Variables:")
    for var in set(css_variables):
        print(var)

    print("\nHTML Variables ({{ }} content):")
    for var in set(html_variables):
        print(var)

if __name__ == "__main__":
    main()

