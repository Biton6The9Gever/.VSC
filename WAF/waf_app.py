from flask import Flask, request, Response, redirect
import re
import requests

app = Flask(__name__)

# Target ASP.NET site (update with your actual target URL)
TARGET_URL = 'https://localhost:44330/01LoginPage.aspx'  # Change to protect 01LoginPage.aspx

# Load XSS and SQL injection patterns from files
def load_patterns(file_path):
    with open(file_path, 'r') as file:
        patterns = [line.strip() for line in file if line.strip()]
    return patterns

# Compile patterns into regex
def compile_pattern(patterns):
    return re.compile("|".join(patterns), re.IGNORECASE)

# Load and compile patterns
xss_patterns = compile_pattern(load_patterns(r"D:\Biton\VisualStudio\WAF-Project\WAF\xss_patterns.txt"))
sql_patterns = compile_pattern(load_patterns(r"D:\Biton\VisualStudio\WAF-Project\WAF\sql_patterns.txt"))
command_injection_patterns=compile_pattern(load_patterns(r"D:\Biton\VisualStudio\WAF-Project\WAF\command_injection_patterns.txt"))
# XSS detection function
def check_xss(user_input):
    return xss_patterns.search(user_input) is not None

# SQL injection detection function
def check_sql_injection(user_input):
    return sql_patterns.search(user_input) is not None
# Command injection detection function
def check_command_injection(user_input):
    return command_injection_patterns.search(user_input) is not None


# Get the IP like a pro
def get_ip():
    """Get the IP address of the client making the request."""
    return request.remote_addr

# Function to handle XSS detection for GET and POST data
def handle_xss_detection():
    # Check for XSS in GET request parameters
    if request.method == 'GET':
        user_input = request.args.get('user_input', '')
        if check_xss(user_input):
            print("Potential XSS detected in GET request!")
            return "Potential XSS attack detected!", 400

    # Check for XSS in POST request fields
    elif request.method == 'POST':
        username = request.form.get('txtUsername', '')
        password = request.form.get('txtPassword', '')
        if check_xss(username) or check_xss(password):
            print("Potential XSS detected in POST request!")
            return "Potential XSS attack detected!", 400

    return None  # Return None if no XSS detected

# Function to handle SQL injection detection for GET and POST data
def handle_sql_injection_detection():
    # Check for SQL injection in GET request parameters
    if request.method == 'GET':
        user_input = request.args.get('user_input', '')
        if check_sql_injection(user_input):
            print("Potential SQL Injection detected in GET request!")
            return "Potential SQL Injection detected!", 400

    # Check for SQL injection in POST request fields
    elif request.method == 'POST':
        username = request.form.get('txtUsername', '')
        password = request.form.get('txtPassword', '')
        if check_sql_injection(username) or check_sql_injection(password):
            print("Potential SQL Injection detected in POST request!")
            return "Potential SQL Injection detected!", 400

    return None  # Return None if no SQL injection detected
# Function to handle Command injection detection for GET and POST data
def handle_command_injection_detection():
    # Check for Command injection in GET request parameters
    if request.method == 'GET':
        user_input = request.args.get('user_input', '')
        if check_sql_injection(user_input):
            print("Potential SQL Injection detected in GET request!")
            return "Potential SQL Injection detected!", 400

    # Check for Command injection in POST request fields
    elif request.method == 'POST':
        username = request.form.get('txtUsername', '')
        password = request.form.get('txtPassword', '')
        if check_sql_injection(username) or check_sql_injection(password):
            print("Potential Command Injection detected in POST request!")
            return "Potential Command Injection detected!", 400
    
@app.route('/01LoginPage.aspx', methods=['GET', 'POST'])
def proxy_site():
    print("Incoming request to /01LoginPage.aspx")

    try:
        # Check for XSS and SQL injection vulnerabilities
        xss_response = handle_xss_detection()
        if xss_response:
            return xss_response  # Return error response if XSS is detected

        sql_injection_response = handle_sql_injection_detection()
        if sql_injection_response:
            return sql_injection_response  # Return error response if SQL injection is detected
        
        command_injection_response=handle_command_injection_detection()
        if command_injection_response:
            return command_injection_response

        # Forward the request to the target ASP.NET site if input is safe
        if request.method == 'GET':
            resp = requests.get(TARGET_URL, params=request.args, verify=False)
        else:
            resp = requests.post(TARGET_URL, data=request.form, verify=False)

        # Modify response content if necessary
        if 'text/html' in resp.headers['Content-Type']:
            html_content = resp.content.decode('utf-8')
            html_content = html_content.replace('href="10LoginStyle.css"', 'href="/static/10LoginStyle.css"')
            return Response(html_content, status=resp.status_code, content_type='text/html')

        # Return the target site's response
        return Response(resp.content, status=resp.status_code, content_type=resp.headers['Content-Type'])

    except Exception as e:
        print(f"Error: {str(e)}")
        return f"Internal Server Error: {str(e)}", 500





if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc', port=6969)   # Running on https://localhost:6969
