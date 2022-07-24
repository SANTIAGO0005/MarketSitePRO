
from apps.Product.api.serializers import ProductSerializer, CategoryProductSerializer
# Create your views here.
from rest_framework import viewsets





class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductSerializer.Meta.model.objects.filter(IsDeleted=False)

    # def get_queryset(self, pk=None):
    #     if pk is None:
    #         return self.get_serializer().Meta.model.objects.filter(IsDeleted=False)
    #     return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    # def list(self, request):
    #     ProductSerializer = self.get_serializer(self.get_queryset(), many=True)
    #     data = {
    #         "total": self.get_queryset().count(),
    #         "totalNotFiltered": self.get_queryset().count(),
    #         "rows": ProductSerializer.data
    #     }
    #     return Response(data, status=status.HTTP_200_OK)

    # def create(self, request):
    #     # send information to serializer 
    #     data = validate_files(request.data,'image')
    #     serializer = self.serializer_class(data=data)     
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'message': 'Producto creado correctamente!'}, status=status.HTTP_201_CREATED)
    #     return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    # def retrieve(self, request, pk=None):
    #     product = self.get_queryset(pk)
    #     if product:
    #         ProductSerializer = ProductRetrieveSerializer(product)
    #         return Response(product_serializer.data, status=status.HTTP_200_OK)
    #     return Response({'error':'No existe un Producto con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)

    # def update(self, request, pk=None):
    #     if self.get_queryset(pk):
    #         # send information to serializer referencing the instance
    #         data = validate_files(request.data, 'image', True)
    #         ProductSerializer = self.serializer_class(self.get_queryset(pk), data=data)            
    #         if ProductSerializer.is_valid():
    #             ProductSerializer.save()
    #             return Response({'message':'Producto actualizado correctamente!'}, status=status.HTTP_200_OK)
    #         return Response({'message':'', 'error':product_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    # def destroy(self, request, pk=None):
    #     product = self.get_queryset().filter(id=pk).first() # get instance        
    #     if product:
    #         product.IsDeleted = True
    #         product.save()
    #         return Response({'message':'Producto eliminado correctamente!'}, status=status.HTTP_200_OK)
    #     return Response({'error':'No existe un Producto con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)

class CategoryProductViewSet(viewsets.ModelViewSet):

    serializer_class = CategoryProductSerializer
    queryset = CategoryProductSerializer.Meta.model.objects.all()













