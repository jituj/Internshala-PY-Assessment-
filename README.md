# Internshala-PY-Assessment- FUL.IO




Here i imported re and requests packages

then i created a function to check_wordpress which take the url and try to get the response if its running.If the request fails or returns a non-200 status code, the function returns False.

If the request is successful, the function checks the response text for the presence of the strings "wp-content", "wp-includes", or "wp-admin" using a regular expression. These strings are common in WordPress URLs and suggest that the website is running on WordPress. If any of these strings are found, the function returns True; otherwise, it returns False.

Finally, the script prompts the user to enter a domain name and calls the check_wordpress function to check if the website is running on WordPress. The script then prints a message indicating whether or not the website is running on WordPress.
