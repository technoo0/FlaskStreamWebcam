from main import app
from engineio.payload import Payload

Payload.max_decode_packets = 500
if __name__ == "__main__":
  app.run()