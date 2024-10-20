print('Hi')
print('lol')
print('salama')

from minio import Minio

print('cheburek')

client = Minio("127.0.0.1:9000", access_key="jtxsKOx4PKKwc6InDNpg", secret_key="N7Hq5RfnT8UDGjZStJiSTP1BqqpgLT6Al2BeLibv", secure=False)

client.fput_object('lol', 'test_1.py', 'test.py')