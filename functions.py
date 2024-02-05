import requests

api_key = "a726b2004caaeb746f855ddd970ba633"
def get_data(place,days= None):
    url =f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"

    content = requests.get(url)
    data = content.json()
    filtered_data = data['list']
    nr_values = 8 * days
    filtered_data = filtered_data[:nr_values ]



    return filtered_data

if __name__=="__main__":
    print(get_data(place="Tokyo", days= 3))