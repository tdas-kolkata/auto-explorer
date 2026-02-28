# Use the official Nanobot image as the base
FROM smanx/nanobot:latest

# Install the free DuckDuckGo search library
RUN pip install --no-cache-dir duckduckgo-search
RUN apt-get -y update && apt-get install -y docker.io
RUN apt-get -y install curl
RUN chmod -R 777 /root/.nanobot