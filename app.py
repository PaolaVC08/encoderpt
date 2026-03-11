from flask import Flask, request, jsonify
import torch
import torch.nn as nn

# -----------------------------
# Modelo
# -----------------------------
class Autoencoder(nn.Module):

    def __init__(self):
        super().__init__()

        self.encoder = nn.Sequential(
            nn.Linear(3,2),
            nn.Sigmoid()
        )

        self.decoder = nn.Sequential(
            nn.Linear(2,3),
            nn.Sigmoid()
        )

    def forward(self, x):
        z = self.encoder(x)
        x_hat = self.decoder(z)
        return x_hat


# -----------------------------
# Cargar modelo
# -----------------------------
model = Autoencoder()
model.load_state_dict(torch.load("autoencoder3.pth"))
model.eval()

# -----------------------------
# API
# -----------------------------
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    x = torch.tensor(data["input"], dtype=torch.float32)

    with torch.no_grad():
        prediction = model(x).tolist()

    return jsonify({
        "prediction": prediction
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)