import socket

#접속할 서버 주소입니다. 여기에서는 localhost 주소를 사용한다.
HOST = '127.0.0.1'
# 클라이언트 접속을 대기하는 포트 번호입니다.
PORT = 9999


#소켓 객체를 생성합니다.
#주소 체계(address family)로 IPv4, 소켓 타입으로 Tcp 사용
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#포트 사용중이라 연결할 수 없다는
#WinError 10048 에러 해결을 위해 필요합니다.
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#bind 함수는 소켓을 특정 네트워크 인터페이스와 포트 번호에 연겨하는데 사용
#Host는 hostname, ip address, 빈 문자열 ""이 될 수 있습니다.
#빈 문자열이면 모든 네트워크 인터페이스로부터의 접속을 허용
#PORT는 1-65535 사이의 숫자를 사용할수 있습니다.
server_socket.bind((HOST,PORT))

#서버가 클라이언트의 접속을 허용하도록 한다(listen)
server_socket.listen()

#accept 함수에서 대기하다가 클라이언트가 접속하면 새로운 소켓을 리턴한다
client_socket, addr = server_socket.accept()

#접속한 클라이언트의 주소
print('Connected by', addr)

#무한루트를 돌면서
while True:

    #클라이언트가 보낸 메세지를 수신하기 위해 대기한다
    data = client_socket.recv(1024)

    #빈 문자열을 수신하면 루프를 중지한다.
    if not data:
        break

    #수신받은 문자열을 출력
    print('Received from',addr,data.decode()) 

    #받은 문자열을 다시 클라이언트로 전송해줍니다.(에코)
    client_socket.sendall(data)

#소켓을 닫는다.
client_socket.close()
server_socket.close()       
