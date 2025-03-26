import requests
import json
def get_ticket(): 
    base_url = "http://10.215.26.60/api/v1/ticket/"
    header = {"content-type": "application/json"}
    body = json.dumps({
        "username": "admin",
        "password": "vnpro@123"
    })
    responses = requests.post(base_url, headers = header, data= body, verify= False) #thực hiện gửi yêu cầu tạo ticket và trả về kết quả
    data = responses.json()
    print(json.dumps(data, indent=4))
    ticket = data['response']['serviceTicket'] #Truy cập vào dữ liệu bên trong để lấy ticket.
    print(ticket) 
    return ticket
get_ticket()
def network_device():
    url = "https://10.215.26.60/api/v1/api-docs/inventory-manager/network-devive"
    header = {
        "x-auth-token": get_ticket()
    }
    response_device = requests.get(url, headers=header, verify=False)
    print (response_device)
    list_networkdevice = response_device.json()
    #print(json.dumps(data, indent = 4))

    return list_networkdevice   
network_device()

