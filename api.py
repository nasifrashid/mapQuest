import urllib.parse
import requests

key = 'y0YbEyGYm7bg8WYWKScze5VtwKH77h3Q'
main_api = "https://www.mapquestapi.com/directions/v2/route?"

while True:
    orig = input("Starting Location: ")

    if orig == "quit" or orig == "q":
        break
    dest = input("End Location: ")
    if orig == "quit" or orig == "q":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    print("URL: " + url)

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A succesful route call.\n")
# print(json_data)

        print("Direction from " + orig + " to " + dest)
        print("Trip Duration: " + (json_data["route"]["formattedTime"]))
        print("Kilometers " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Fuel Used (Ltr.): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("================================================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"] + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)")))
        print("================================================================")

    elif json_status == 402:
        print("\n***************************************************************************")
        print("Status Code: " + str(json_status) + "; Invalid user input for one or both locations.")
        print("\n***************************************************************************")
        print("\n***************************************************************************")
    else:
        print("\n***************************************************************************\n")
        print("Status Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("\n***************************************************************************\n")
