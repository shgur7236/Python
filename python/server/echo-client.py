import socket

#서버 주소
HOST = '127.0.0.1'
#서버 포트 번호
PORT = 9999


#소켓 객체 생성
#주소 체계 IPv4, 소켓 타입은 TCP사용
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#지정한 HOST와 PORT를 사용하여 서버 접속
client_socket.connect((HOST,PORT))

#메세지 전송
client_socket.sendall('안녕'.encode()) 
#encode는 문자열 바이트 코드를 utf-8과 같은 형식의 바이트코드로 변환

#메세지 수신
data = client_socket.recv(1024)
print('Received',repr(data.decode())) 
#decode는 byte코드를 문자열로 변환

#소켓을 닫습니다.
client_socket.close()