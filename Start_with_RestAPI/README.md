# Django REST API Overview

## Overview
- This project demonstrates the implementation of RESTful APIs using Django REST Framework (DRF). It 
  showcases both Function-Based Views (FBVs) and Class-Based Views (CBVs), covering a wide range of use cases and approaches for building APIs.

## Features
 - Function-Based Views with api_view decorator.
 - Class-Based Views using:
       - Viewsets
       - Mixins
       - Generics
       - APIView

## Installation

Prerequisites
    Python (3.8 or above)
    Django (4.x or above)
    Django REST Framework (3.x or above)


## API Implementation Details

- Function-Based Views (FBVs)
    - Description:
      Utilizes the api_view decorator to define views for handling HTTP methods like GET, POST, PUT, DELETE.
    - Usage Scenarios:
      Best for simple and straightforward endpoints.

- Class-Based Views (CBVs)
    - Viewsets
        Combines logic for handling CRUD operations in one class.
        Easily integrates with DRF routers for automatic URL generation.

    - Mixins
        Modular and reusable components to handle specific API behaviors (create, retrieve, update, delete).
        Ideal for combining custom and predefined logic.

    - Generics
        Simplifies API creation by combining mixins and base views.
        Common generic views include:
            ListAPIView
            CreateAPIView
            RetrieveUpdateDestroyAPIView

    - APIView
        Base class for class-based views in DRF.
        Provides granular control over request and response handling.