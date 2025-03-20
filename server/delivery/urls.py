from django.urls import path
from .package import createPackage, deletePackage, bulkCreatePackages, getAllPackages
from .truck import createTruck, getAllTrucks, deleteTruck
urlpatterns = [
    path('packages/', getAllPackages.as_view(), name='get-all-packages'),
    path('packages/create/', createPackage.as_view(), name='create-package'),
    path('packages/<int:id>/', deletePackage.as_view(), name='delete-package'),
    path('packages/bulk-create/', bulkCreatePackages.as_view(), name='bulk-create-packages'),

    
    path('trucks/', getAllTrucks.as_view(), name='get-all-trucks'),
    path('trucks/create/', createTruck.as_view(), name='create-truck'),
    path('trucks/<int:id>/', deleteTruck.as_view(), name='delete-truck'),
]