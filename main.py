# 1
POST /login HTTP/1.1
Host: www.example.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 27

username=admin&password=secret


# 2
POST /api/users HTTP/1.1
Host: www.example.com
Content-Type: application/json
Content-Length: 39

{
  "name": "John Doe",
  "email": "john.doe@example.com"
}


# 3
GET /search?query=blue+shoes HTTP/1.1
Host: www.example.com

# 4
POST /api/chunked HTTP/1.1
Host: www.example.com
Transfer-Encoding: chunked

7
Hello, 
6
world!
0
