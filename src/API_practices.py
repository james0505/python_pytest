"""Scripts to use requests library to make get, put etc. actions
"""
import requests
def api_get():
    api_url = "https://jsonplaceholder.typicode.com/todos/2" # a free serice provides fake API endpoints that send back
    # responses that request can process
    response = requests.get(api_url)
    if response.status_code == 200:
        #print(f"headers: {response.headers['Content-Type']}\n")
        return {"status": response.status_code, "content": f"{response.json()}"}
    else:
        print(f"request is not successful. Error code: {response.status_code}")
        return {"status": f"{response.status_code:d}", "content": None}

if __name__ == "__main__":
    print(api_get())
