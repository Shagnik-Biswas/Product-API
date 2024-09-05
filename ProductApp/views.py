from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from bson import ObjectId
from .serializer import ProductSerializer
from .mongo import Product_collection

class ProductView(APIView):

    def get(self, request, product_id=None):
        """Retrieve a product by ID or search products by name, description, or category."""
        product_id = product_id or request.query_params.get('id')

        if product_id:
            try:
                # Check if the provided ID is valid
                if not ObjectId.is_valid(product_id):
                    return Response({"error": "Invalid product ID format"}, status=status.HTTP_400_BAD_REQUEST)

                # Retrieve a product by its ID
                product = Product_collection.find_one({"_id": ObjectId(product_id)})
                if product:
                    product['_id'] = str(product['_id'])  # Convert ObjectId to string
                    serializer = ProductSerializer(product)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            # Search products by query params (name, description, category)
            name = request.query_params.get('name')
            description = request.query_params.get('description')
            category = request.query_params.get('category')

            query = {}
            if name:
                query['name'] = {"$regex": name, "$options": "i"}
            if description:
                query['description'] = {"$regex": description, "$options": "i"}
            if category:
                query['category'] = {"$regex": category, "$options": "i"}

            products = Product_collection.find(query)
            product_list = []
            for product in products:
                product['_id'] = str(product['_id'])  # Convert ObjectId to string
                product_list.append(ProductSerializer(product).data)

            return Response(product_list, status=status.HTTP_200_OK)


    def post(self, request):
        """Create a new product."""
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product_data = serializer.validated_data
            try:
                # Ensure 'sales' field is initialized to 0 if not provided
                if 'sales' not in product_data:
                    product_data['sales'] = 0

                result = Product_collection.insert_one(product_data)
                return Response({"message": "Product created", "id": str(result.inserted_id)}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, product_id):
        """Update an existing product."""
        serializer = ProductSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            try:
                print("product id, ", product_id)
                product = Product_collection.find_one({"_id": ObjectId(product_id)})
                if product:
                    updated_product = serializer.validated_data
                    Product_collection.update_one({"_id": ObjectId(product_id)}, {"$set": updated_product})
                    return Response({"message": "Product updated"}, status=status.HTTP_200_OK)
                return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_id):
        """Delete a product."""
        try:
            result = Product_collection.delete_one({"_id": ObjectId(product_id)})
            if result.deleted_count > 0:
                return Response({"message": "Product deleted"}, status=status.HTTP_200_OK)
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ProductPopularityView(APIView):
    def get(self, request, product_id):
        """Calculate product popularity based on total sales quantity."""
        try:
            # Retrieve the product to check if it exists
            product = Product_collection.find_one({"_id": ObjectId(product_id)})
            if not product:
                return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

            # Popularity score based on sales
            popularity_score = product.get('sales', 0)

            return Response({"product_id": product_id, "popularity_score": popularity_score}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
