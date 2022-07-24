# from rest_framework import generics

# class GeneralListAPIView(generics.ListAPIView):
#     serializer_class = None

#     def get_queryset(self):
#         model = self.get_serializer().Meta.model
#         return model.objects.filter( IsDeleted= False)

# class AllListAPIView(generics.ListAPIView):
#     serializer_class = None

#     def get_queryset(self):
#         model = self.get_serializer().Meta.model
#         return model.objects.all()