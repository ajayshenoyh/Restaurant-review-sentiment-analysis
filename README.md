# Restaurant-review-sentiment-analysis

____1) Install WAMP

____2) Install Python

3) open ...wamp\bin\apache\apacheXXXX\conf\httpd.conf, then search & replace 
Options Indexes FollowSymLinks 
with 
Options Indexes FollowSymLinks ExecCGI (or Options Indexes FollowSymLinks Includes ExecCGI)
p.s. also, Find & ensure that LoadModule cgi_module is NOT commented.

4) search & replace 
#AddHandler cgi-script .cgi 
with (...removing # ) 
AddHandler cgi-script .cgi 
AddHandler cgi-script .py

5) Find the line: DirectoryIndex index.php index.php3 index.html index.htm 
and add in the end of them:  index.cgi index.py 
Now, Restart Apache.
