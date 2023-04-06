class MyUser:
    def __init__(self, id, email, username, name, address):
        self.id = id
        self.email = email
        self.username = username
        self.name = name
        self.address = address["city"]
        self.lat = address.get("geo", {}).get("lat")
        self.lng = address.get("geo", {}).get("lng")

    def info(self):
        return (f'ID: {self.id}\n'
                f'Email: {self.email}\n'
                f'Username: {self.username}\n'
                f'Name: {self.name}\n'
                f'City: {self.address}\n'
                f'Geo:\n lat\n "{self.lat}"\n lng\n "{self.lng}"\n')

    def __str__(self):
        return self.info()
