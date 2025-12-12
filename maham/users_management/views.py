from .models import User_Role, Administrator
from .serializers import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from customers.models import Customer
from flight_companies.models import Country

# Create your views here.


def initialize_backend():
    try:
        # Check if admin exists
        admin_exists = Customer.objects.filter(email="admin@admin.com").exists()
        if not admin_exists:
            # Add admin user
            Customer.objects.create_user(
                password="admin",
                email="admin@admin.com",
                first_name="Admin",
                last_name="Admin",
                username="admin",
                is_staff=True,
                is_superuser=True,
            )
            print("[INITIALIZATION][SUCCESS]: Admin user added")
        else:
            print("[INITIALIZATION][EXISTS]: Admin user already exists")

        if Country.objects.count() == 0:
            # Add default countries
            default_countries = [
                "Afghanistan",
                "Albania",
                "Algeria",
                "Andorra",
                "Angola",
                "Anguilla",
                "Antigua and Barbuda",
                "Argentina",
                "Armenia",
                "Aruba",
                "Australia",
                "Austria",
                "Azerbaijan",
                "Bahamas",
                "Bahrain",
                "Bangladesh",
                "Barbados",
                "Belarus",
                "Belgium",
                "Belize",
                "Benin",
                "Bermuda",
                "Bhutan",
                "Bolivia",
                "Bosnia and Herzegovina",
                "Botswana",
                "Brazil",
                "British Virgin Islands",
                "Brunei",
                "Bulgaria",
                "Burkina Faso",
                "Burundi",
                "Cambodia",
                "Cameroon",
                "Cape Verde",
                "Cayman Islands",
                "Chad",
                "Chile",
                "China",
                "Colombia",
                "Congo",
                "Cook Islands",
                "Costa Rica",
                "Cote D Ivoire",
                "Croatia",
                "Cruise Ship",
                "Cuba",
                "Cyprus",
                "Czech Republic",
                "Denmark",
                "Djibouti",
                "Dominica",
                "Dominican Republic",
                "Ecuador",
                "Egypt",
                "El Salvador",
                "Equatorial Guinea",
                "Estonia",
                "Ethiopia",
                "Falkland Islands",
                "Faroe Islands",
                "Fiji",
                "Finland",
                "France",
                "French Polynesia",
                "French West Indies",
                "Gabon",
                "Gambia",
                "Georgia",
                "Germany",
                "Ghana",
                "Gibraltar",
                "Greece",
                "Greenland",
                "Grenada",
                "Guam",
                "Guatemala",
                "Guernsey",
                "Guinea",
                "Guinea Bissau",
                "Guyana",
                "Haiti",
                "Honduras",
                "Hong Kong",
                "Hungary",
                "Iceland",
                "India",
                "Indonesia",
                "Iran",
                "Iraq",
                "Ireland",
                "Isle of Man",
                "Israel",
                "Italy",
                "Jamaica",
                "Japan",
                "Jersey",
                "Jordan",
                "Kazakhstan",
                "Kenya",
                "Kuwait",
                "Kyrgyz Republic",
                "Laos",
                "Latvia",
                "Lebanon",
                "Lesotho",
                "Liberia",
                "Libya",
                "Liechtenstein",
                "Lithuania",
                "Luxembourg",
                "Macau",
                "Macedonia",
                "Madagascar",
                "Malawi",
                "Malaysia",
                "Maldives",
                "Mali",
                "Malta",
                "Mauritania",
                "Mauritius",
                "Mexico",
                "Moldova",
                "Monaco",
                "Mongolia",
                "Montenegro",
                "Montserrat",
                "Morocco",
                "Mozambique",
                "Namibia",
                "Nepal",
                "Netherlands",
                "Netherlands Antilles",
                "New Caledonia",
                "New Zealand",
                "Nicaragua",
                "Niger",
                "Nigeria",
                "Norway",
                "Oman",
                "Pakistan",
                "Palestine",
                "Panama",
                "Papua New Guinea",
                "Paraguay",
                "Peru",
                "Philippines",
                "Poland",
                "Portugal",
                "Puerto Rico",
                "Qatar",
                "Reunion",
                "Romania",
                "Russia",
                "Rwanda",
                "Saint Pierre and Miquelon",
                "Samoa",
                "San Marino",
                "Satellite",
                "Saudi Arabia",
                "Senegal",
                "Serbia",
                "Seychelles",
                "Sierra Leone",
                "Singapore",
                "Slovakia",
                "Slovenia",
                "South Africa",
                "South Korea",
                "Spain",
                "Sri Lanka",
                "St Kitts and Nevis",
                "St Lucia",
                "St Vincent",
                "St. Lucia",
                "Sudan",
                "Suriname",
                "Swaziland",
                "Sweden",
                "Switzerland",
                "Syria",
                "Taiwan",
                "Tajikistan",
                "Tanzania",
                "Thailand",
                "Timor L'Este",
                "Togo",
                "Tonga",
                "Trinidad and Tobago",
                "Tunisia",
                "Turkey",
                "Turkmenistan",
                "Turks and Caicos",
                "Uganda",
                "Ukraine",
                "United Arab Emirates",
                "United Kingdom",
                "Uruguay",
                "Uzbekistan",
                "Venezuela",
                "Vietnam",
                "Virgin Islands (US)",
                "Yemen",
                "Zambia",
                "Zimbabwe",
            ]
            for country_name in default_countries:
                Country.objects.create(name=country_name)
            print("[INITIALIZATION][SUCCESS]: Default countries added")

    except Exception as e:
        print("[INITIALIZATION][ERROR]:", str(e))


# Call the function to initialize the backend
initialize_backend()


@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def roles(request, pk=-1):
    try:
        if int(pk) > -1:  # get single product
            roleObj = User_Role.objects.get(id=pk)
            serializer = RolesSerializer(roleObj, many=False)
        else:
            roles = User_Role.objects.all()
            serializer = RolesSerializer(
                roles, many=True
            )  ################can the 'many' be removed?
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    except:
        roles = User_Role.objects.all()
        serializer = RolesSerializer(
            roles, many=True
        )  ################can the 'many' be removed?
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.data)


@api_view(["POST"])
def createRole(request):
    serializer = RolesSerializer(data=request.data)
    try:
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
    except Exception as ex:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": ex})


@api_view(["PUT"])
def updateRole(request, pk=-1):  # check if exist?
    try:
        role = User_Role.objects.get(id=pk)
        serializer = RolesSerializer(instance=role, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
    except Exception as ex:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": ex})


@api_view(["DELETE"])
def deleteRole(request, pk=-1):  # check if exist?
    try:
        role = User_Role.objects.get(id=pk)
        role.delete()
        return Response(status=status.HTTP_200_OK, data="role was deleted")
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data="id does not exist")


@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def administrators(request, pk=-1):
    try:
        if int(pk) > -1:  # get single product
            administratorObj = Administrator.objects.get(id=pk)
            serializer = AdminSerializer(administratorObj, many=False)
        else:
            administrators = Administrator.objects.all()
            serializer = AdminSerializer(
                administrators, many=True
            )  ################can the 'many' be removed?
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    except:
        administrators = Administrator.objects.all()
        serializer = AdminSerializer(administrators, many=True)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.data)


@api_view(["POST"])
def createAdministrator(request):
    serializer = AdminSerializer(data=request.data)
    try:
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
    except Exception as ex:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": ex})


@api_view(["PUT"])
def updateAdministrator(request, pk=-1):  # check if exist?
    try:
        administrator = Administrator.objects.get(id=pk)
        serializer = AdminSerializer(instance=administrator, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
    except Exception as ex:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": ex})


@api_view(["DELETE"])
def deleteAdministrator(request, pk=-1):  # check if exist?
    try:
        administrator = Administrator.objects.get(id=pk)
        administrator.delete()
        return Response(status=status.HTTP_200_OK, data="administrator was deleted")
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data="id does not exist")
