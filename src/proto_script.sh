python3 -m grpc_tools.protoc --proto_path=./proto --python_out=pb2_module/country --grpc_python_out=pb2_module/country proto/country.proto
python3 -m grpc_tools.protoc --proto_path=./proto --python_out=pb2_module/key --grpc_python_out=pb2_module/key proto/key.proto
python3 -m grpc_tools.protoc --proto_path=./proto --python_out=pb2_module/proxy --grpc_python_out=pb2_module/proxy proto/proxy.proto
python3 -m grpc_tools.protoc --proto_path=./proto --python_out=pb2_module/subscription --grpc_python_out=pb2_module/subscription proto/subscription.proto
python3 -m grpc_tools.protoc --proto_path=./proto --python_out=pb2_module/user --grpc_python_out=pb2_module/user proto/user.proto