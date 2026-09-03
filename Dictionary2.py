info = {"car": {"brand":"Toyota", "model":"Camry", "year":2022}}
info["car"]["color"] = "black"
info["car"]["year"] = 2023
info["car"].pop("model", None)

print(info)