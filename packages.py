
from flask import request
import packages,json

#request-handling functions


with open("packages.json","r") as file:
    packages = json.load(file) #deserilization loading the file to python


def view_packages():
    return packages #works

def get_package(id): #works
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
        with open("packages.json", "w") as file:
            json.dump(packages,file)
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
                
                with open("packages.json", "w") as file:
                    json.dump(packages,file)                
                return {
                "message" : "updated packaged",
                "package" : p} 


        else:
            return {"error" : "enter valid id"}
        
def delete_package(id):
    for p in packages:
        if p["id"] == id:
            packages.remove(p)
            with open("packages.json", "w") as file:
                json.dump(packages,file)
            return {
            "message": "package removed",
            "removed package": p
            }
    else:
        return {"error" : "enter valid id"}
