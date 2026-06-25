
from flask import request

packages = [
    {"id": 1,
    "sender": "A",
    "recipient": "B",
    },
    { 
    "id": 3,
    "sender": "C",
    "recipient": "D",
    },
    {
    "id": 2,
    "sender": "E",
    "recipient": "F",
    }
]




def view_packages():
    return packages

def get_package(id):
    for p in packages:
        if p["id"] == id:
            return p
    
    return {"error" : "that package does not seem to exist"}
    
def create_package():
    sender = request.args.get("sender")
    recipient = request.args.get("recipient")
    if not sender or not recipient:
        return {"error": "sender and recipient required"}
    else:
        new_id = max(item["id"] for item in packages)
        package = {
            "id" : new_id+1,
            "sender" : sender ,
            "recipient" : recipient
        }
        packages.append(package)
        return {
            "message": "package created",
            "package": package
        }       

def update_package(id):
    sender = request.args.get("sender")
    recipient = request.args.get("recipient")
    if not sender and not recipient:
        return {"error": "sender or recipient required"}
    else:
        for p in packages:
            print("checking", p["id"])
            if p["id"] == id:
                
                if sender: #You're treating each field independently instead of creating separate cases for every combination.
                    p["sender"] = sender
                if recipient:
                    p["recipient"] =  recipient
                
                return {
                "message" : "updated packaged",
                "package" : p} 


        else:
            return {"error" : "enter valid id"}
        
def delete_package(id):
    for p in packages:
        if p["id"] == id:
            packages.remove(p)
            return {
            "message": "package removed",
            "removed package": p
            }
    else:
        return {"error" : "enter valid id"}
