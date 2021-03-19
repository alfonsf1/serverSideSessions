Server-side Session  
===============================
In this server-side session project we make HTTP requests from a python progeam and use this ability to store server-side session data in a seperate storage service.   

Contributors of the group project:  
---------------------------------- 
1) Alfonso Figueroa - Figueroa.a@csu.fullerton.edu  
2) Ryan Luong - Ryan12@csu.fullerton.edu  
  
Technologies      
===============================
1) Python  
2) Bottle Framework  
3) DBM Database   
4) Foreman  
5) HTTPie  

Install Technologies (Ubuntu)  
===============================
1) Foreman, httpie  
   ``` $ sudo apt install --yes python3-pip ruby-foreman httpie  ```
2) Bottle and SQLite plugin for bottle  
   ``` $ python3 -m pip install bottle  ```  

How to run project:
--------------------  
1) git clone ``` https://github.com/alfonsf1/serverSideSessions.git ```      
3) To start the program  
   - In the terminal type:  
      ``` $ formman start ```  
4) Make an executable out of dump.py  
   - In the terminal type:
      ``` $ chmod 755 dump.py```  
   - To execute dump.py use the following method.  
      ``` $ ./dump.py http://localhost:5100```  
  
    
>localhost:5000 is connected to app.py    
  
>localhost:5100 is connected kv.py    
  
  
How to use the project    
--------------  
- Increment  
   - Increments count 2 by 1  
- Launch server and refresh  
   - increments count 1 by 1    
- Reset  
   - resets the counter and gives a new session id and removes the previous session.   
