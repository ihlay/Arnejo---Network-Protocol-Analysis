Good day po, Sir! I used po yong tip ninyo nakaraang activity which is this: TIP Compress your video using ffmpeg by issuing this command to your terminal (requires ffmpeg in your path) 
ffmpeg -i INPUTVIDEO.mp4 -c:v libx264 -crf 37 -preset ultrafast -c:a aac -b:a 128k -movflags +faststart -vf scale=-2:720 OUTPUT_VIDEO.mp4 

The quality po is not that clear, it's because of that compressor po.

If you can't watch the video po. 
Here's a googledrive video link that I uploaded in my drive: 

https://drive.google.com/drive/folders/1V4qaA3z3h7NUrztylpf3aa4kBMoDCCnm?usp=sharing

Which is much clearer po compared sa inupload ko pong video dito sa repository.
Thank you po!

Overview
This repository has my solution for the IT6 Take Home Drill. It involves making a Python script to guess a 3-digit PIN for a web application using socket programming.

Problem Statement
The challenge was to create a script to test all possible 3-digit PIN combinations (000-999) for a local web application, using Python's socket library.

My Approach
Initial Investigation
1.	Running the Executable: First, I ran the program and checked the web app through my browser.
2.	Understanding the Login: The app needed a 3-digit number to log in.
3.	Using Wireshark: I used Wireshark to capture network data during manual login tries.

Network Analysis Findings
•	Server Location: The server is on 127.0.0.1 (localhost) at port 8888.
•	Login Process: Logins use HTTP POST requests to "/verify".
•	PIN Submission: The PIN is sent as form data labeled "magicNumber".
•	Success Response: The server says "Access Granted" when the correct PIN is entered.

Implementation Strategy
•	Python Script: I made a script with Python's socket library to create HTTP requests.
•	Testing PINs: I used a brute-force method to test all PINs (000-999).
•	Handling Delays: I added a 1.2-second delay between attempts to manage server limits.
•	Detecting Success: Logic was added to know when the right PIN was found.

Challenges Faced
•	Rate Limiting: The server slowed down repeated tries.
•	Header Formatting: Correctly setting HTTP headers, like Content-Length, was crucial.
•	Response Parsing: I carefully read the server's HTTP responses to know if the attempt was successful.

Running the Solution
1.	Server Ready: Ensure the web server is running.
2.	Script Execution: Run "pin_script.py".
3.	Outcome: The script will test each PIN in order and say when it finds the correct one.

Code Explanation
•	Connecting: A socket link is made for each try.
•	HTTP Request: I made the correct HTTP POST with the current PIN guess.
•	Success Check: The reply is read to see if the login worked.
•	Delay Handling: Time delays between tries help respect server rules.
