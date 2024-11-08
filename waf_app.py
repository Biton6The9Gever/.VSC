from flask import Flask, request, Response ,redirect
import re
import requests

app = Flask(__name__)

# Target ASP.NET site (update with your actual target URL)
TARGET_URL = 'https://localhost:44330/XSSme.aspx'

# XSS detection pattern (matches <script> tags and alert() calls)
xss_pattern = re.compile(r'<script.*?>.*?</script>|alert\((.*?)\)', re.IGNORECASE)

# get the ip like a pro
def get_ip():
    """Get the IP address of the client making the request."""
    return request.remote_addr

# Function to check if input contains XSS
def is_xss_safe(user_input):
    if xss_pattern.search(user_input):
        return False
    return True


@app.route('/XSSme.aspx', methods=['GET', 'POST'])
def proxy_site():
    print("Incoming request to /XSSme.aspx")
    
    try:
        # Check GET request for XSS (in query params)
        user_input = request.args.get('user_input', '')
        print(f"GET user_input: {user_input}")
        if user_input and not is_xss_safe(user_input):
            print("Potential XSS detected in GET request!")
            return "Potential XSS attack detected!", 400

        # Check POST request for XSS (in form data)
        if request.method == 'POST':
            user_input = request.form.get('txtInput', '')
            print(f"POST user_input: {user_input}")
            if not is_xss_safe(user_input):
                print(f"Potential XSS detected in POST request! {get_ip()}")
                return f"Potential XSS attack detected! {get_ip()}", 400

        # If input is safe, forward the request to the target ASP.NET site
        if request.method == 'GET':
            resp = requests.get(TARGET_URL, params=request.args, verify=False)
        else:
            resp = requests.post(TARGET_URL, data=request.form, verify=False)

        # Forward the response from the target site
        return Response(resp.content, status=resp.status_code, content_type=resp.headers['Content-Type'])

    except Exception as e:
        print(f"Error: {str(e)}")
        return f"Internal Server Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc', port=5000)   # Running on https://localhost:5000
