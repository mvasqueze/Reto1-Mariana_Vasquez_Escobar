from concurrent import futures

import json
import grpc
import services_pb2
import services_pb2_grpc

HOST = '[::]:8080'

class ShoppingCart(services_pb2_grpc.ShoppingCartServicer):
    def AddProduct(self, request, context):
        productID = request.id
        print("\nRequest received. Hendling product "+productID)
        with open("orders.json","r") as orderList:
            orders = json.loads(orderList.read())

        if productID in orders.keys():
            print("\nRequest received. Product ID: "+productID+ 
                  ". Product name: "+orders[productID]["name"]+
                  ". Product quantity: "+orders[productID]["quantity"]+".")
            return services_pb2.TransactionResponse(status_code=1)
        
        else:
            print("\nRequest received. Product ID: "+productID+" does not exist in this orders.")
            return services_pb2.TransactionResponse(status_code=0)
            
    def ConfirmOrder(self, request, context):
        productID = request.id
        print("\nRequest received. Handling product "+productID)
        with open("orders.json","r") as orderList:
            orders = json.loads(orderList.read())

        units = int(orders[productID]["quantity"])
        price = int(orders[productID]["price_for_unit"])
        finalPrice = units*price

        if productID in orders.keys():
            print("\nThe total price of your order is "+finalPrice)

        return super().setProducts(request, context)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_ShoppingCartServicer_to_server(
        ShoppingCart(), server)
    server.add_insecure_port(HOST)
    print("Service is running... ")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
