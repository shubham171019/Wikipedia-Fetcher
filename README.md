# Wikipedia-Fetcher
web scrapping mini project\
\
There are two ways to extract data from website\
1.Use the API of the website(if it exist)\
  For eg: Facebook has Facebook Graph API which allows retrival of data posted on Facebook.\
2.Access the HTML of the webpage and extract useful information/data from it.\
  (This technique is called web scrapping)\
\
STEPS are as follow:\
-> Send the HTTP request to the URL of the webpage that you want to access. The server respond to the request by returning the HTML content of the webpage.\
  Here we are using REQUEST module, to make the request to a webpage.\
\
-> Once we accessed the HTML content, we are left with task of parsing the data. Since the HTML data is nested, we take the help of parser libraries which is "html5lib".\
\
-> Now, all we are need to do is navigate and search.
