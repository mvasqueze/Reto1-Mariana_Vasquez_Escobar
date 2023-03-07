from concurrent import futures

import json
import grpc
import services_pb2
import services_pb2_grpc

HOST = '[::]:8080'

class Inventory(services_pb2_grpc.InventoryServicer):
    def getProducts(self, request, context):
        productID = request.id
        print("\nRequest received. Hendling product "+productID)
        with open("inventory.json","r") as productList:
            inventory = json.loads(productList.read())

        if productID in inventory.keys():
            print("\nRequest received. Product ID: "+productID+ 
                  ". Product name: "+inventory[productID]["name"]+
                  ". Product quantity: "+inventory[productID]["quantity"]+".")
            return services_pb2.TransactionResponse(status_code=1)
        
        else:
            print("\nRequest received. Product ID: "+productID+" does not exist in this inventory.")
            return services_pb2.TransactionResponse(status_code=0)
            
    def setProducts(self, request, context):
        productID = request.id
        productQuantity=request.quantity
        print("\nRequest received. Hendling product "+productID)
        with open("inventory.json","r") as productList:
            inventory = json.loads(productList.read())

        inventory[productID]["quantity"]+=productQuantity

        if productID in inventory.keys():
            inventory[productID]["quantity"] += productQuantity
            with open("inventory.json", "w") as productListOut:
                json.dump(inventory, productListOut, indent="")
            return services_pb2.TransactionResponse(status_code=1)
        else:
            return services_pb2.TransactionResponse(status_code=0)

    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_InventoryServiceServicer_to_server(
        Inventory(), server)
    server.add_insecure_port(HOST)
    print("Service is running... ")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
