import dotenv from 'dotenv';
import grpc from '@grpc/grpc-js';
import protoLoader from '@grpc/proto-loader';

dotenv.config()

const PROTO_PATH = process.env.PROTO_PATH;
const REMOTE_HOST = process.env.REMOTE_HOST;

const packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
    });

console.info("Consumer service is started...");

const inventoryService = grpc.loadPackageDefinition(packageDefinition).Inventory;
const shoppingCartService = grpc.loadPackageDefinition(packageDefinition).ShoppingCart;
const shipmentService = grpc.loadPackageDefinition(packageDefinition).Shipment;

function main(){

  const productId = "1";
  const client = new inventoryService(REMOTE_HOST,grpc.credentials.createInsecure());

  // get product
  client.getProducts({id: productId} , (err, data) => {

    if(err){
      console.log(err);
    } else {
      console.log('Product received from inventory:', data); // API response

      // add product to cart
      const client2 = new shoppingCartService(REMOTE_HOST,grpc.credentials.createInsecure());
      client2.AddProduct({id: productId} , (err2, data2) => {
        if(err2){
          console.log(err2);
        } else {
          console.log('Response received from shopping cart:', data2); // API response

          // confirm order
          const client3 = new shoppingCartService(REMOTE_HOST,grpc.credentials.createInsecure());
          client3.ConfirmOrder({id: "1"} , (err3, data3) => {
            if(err3){
              console.log(err3);
            } else {
              console.log('Order confirmed:', data3); // API response

              // register shipment
              const client4 = new shipmentService(REMOTE_HOST,grpc.credentials.createInsecure());
              client4.ShipmentRegister({id: "1", address: "Avenida 123"} , (err4, data4) => {
                if(err4){
                  console.log(err4);
                } else {
                  console.log('Shipment registered:', data4); // API response
                }
              });
            }
          });
        }
      });
    }
   });

};

main();
