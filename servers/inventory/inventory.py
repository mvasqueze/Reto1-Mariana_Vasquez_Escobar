from concurrent import futures

import json
import grpc
import inventory_pb2
import inventory_pb2_grpc

HOST = '[::]:8080'

class Inventory(inventory_pb2_grpc.InventoryServicer):
    def getProducts(self, request, context):
        productID = str(request.id)
        print("\nRequest received. Handling product "+productID)
        with open("inventory.json","r") as productList:
            inventory = json.loads(productList.read())

        if productID in inventory.keys():
            print("\nRequest received. Product ID: "+productID
            + ". Product name: "+inventory[productID]["name"]+
            ". Product quantity: "+str(inventory[productID]["quantity"])+".")
            return inventory_pb2.TransactionResponse(status_code=1)
        
        else:
            print("\nRequest received. Product ID: "+productID+" does not exist in this inventory.")
            return inventory_pb2.TransactionResponse(status_code=0)
            
    def setProducts(self, request, context):
        productID = request.id
        productQuantity=request.quantity
        print("\nRequest received. Handling product "+productID)
        with open("inventory.json","r") as productList:
            inventory = json.loads(productList.read())


        if productID in inventory.keys():
            inventory[productID]["quantity"] += productQuantity
            with open("inventory.json", "w") as productListOut:
                json.dump(inventory, productListOut, indent="")
            return inventory_pb2.TransactionResponse(status_code=1)
        else:
            return inventory_pb2.TransactionResponse(status_code=0)

    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inventory_pb2_grpc.add_InventoryServicer_to_server(
        Inventory(), server)
    server.add_insecure_port(HOST)
    print("Service is running... ")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
