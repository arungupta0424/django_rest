import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
    data = {}
    id = input('Enter Id: ')
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    try:
        r = requests.get(url=URL, data=json_data)
        data = r.json()
        print(data)
    except:
        print('Record not found...')


    

# print('Enter Id:')
# get_data(input())

def post_data():
    nm = input('Enter Name: ')
    ro = int(input('Enter Roll: '))
    ci = input('Enter City: ')
    data = {
        'name':nm,
        'roll':ro,
        'city':ci,
    }

    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)

# post_data()

#######Update Data
def update_data():
    id = input('Enter Id: ')
    nm = input('Enter Name: ')
    ci = input('Enter City: ')
    data = {
        'id':id,
        'name':nm,
        'city':ci,
    }
    
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)

# update_data()

def delete_data():
    id = input('Enter Id for Delete: ')
    data = {
        'id':id,
    }

    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)


print('(Enter choice bracket value Below:) \nCreate(c)--retrive(r)--update(u)--delete(d):\n')
user_input=input('Enter your Choice: ')
if user_input == 'c':
    post_data()
elif user_input == 'r':
    get_data()
elif user_input == 'u':
    update_data()
elif user_input == 'd':
    delete_data()
