from concurrent import futures

import json
import grpc
import shipment_pb2
import shipment_pb2_grpc

HOST = '[::]:8082'

class Shipment(shipment_pb2_grpc.ShipmentServicer):
    def ShipmentRegister(self, request, context):
        packageID= str(request.id)
        packageAdd = request.address
        packageQuant= request.productQuantity
        print("\nRequest received. Handling package with id "+packageID)
        with open("shippings.json","r") as packageList:
            packages = json.loads(packageList.read())

        if packageID in packages.keys():
            print("\nRequest received. Package id: "+packageID+", Product quantity: "+ str(packageQuant)+ ". New package address: "+packageAdd+".")
            packages[packageID]["address"]=packageAdd

            with open("shippings.json", "w") as packageAddressOut:
                json.dump(packages, packageAddressOut, indent="")
            return shipment_pb2.TransactionResponse(status_code=1)
        
        else:
            print("\nRequest received. Package ID: "+packageID+" does not exist in this packages.")
            return shipment_pb2.TransactionResponse(status_code=0)
            
    
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    shipment_pb2_grpc.add_ShipmentServicer_to_server(
        Shipment(), server)
    server.add_insecure_port(HOST)
    print("Service is running... ")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
