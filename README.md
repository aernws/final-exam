###get buyers
##curl -X GET “http://localhost:8080/buyers”
###get products
##curl -X GET “http://localhost:8080/products”
###post new buyer(BUYER_NAME)
##curl -X POST “http://localhost:8080/buyers?name=BUYER_NAME”
###post new product(PRODUCT_NAME)
##curl -X POST “http://localhost:8080/products?name=PRODUCT_NAME”
###buyer(BUYER_NAME) buy new product(PRODUCT_NAME)
##curl -X POST “http://localhost:8080/buyers/{BUYER_NAME}?prod_name={PRODUCT_NAME}”
###get buy list of buyer(BUYER_NAME) 
##curl -X GET “http://localhost:8080/butyers/BUYER_NAME/purchased”
