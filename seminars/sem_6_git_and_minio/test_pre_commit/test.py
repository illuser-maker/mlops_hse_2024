print('Hi')
print('lol')

from minio import Minio

client = Minio("127.0.0.1:9000", access_key="RhYIg01QKPJm5JyfQObb", secret_key="pKOd1WcZgj2giqzhPSAK8Pbqzzon3KtWECHWgtzq", secure=False)

client.fget_object('gachi', 'test_1.py', './test_1.py')