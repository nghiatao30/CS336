from app import app
import get_data

# get_data.get_oxbuild_data()
# get_data.get_paris_data()

app.run('0.0.0.0', 8080)

# docker build -t image-retrieval .
# docker run -p 80:8080 --name image-retrieval image-retrieval
# docker run -p 80:4040 --name image-retrieval image-retrieval
# docker build --no-cache -t image-retrieval .
