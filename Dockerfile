FROM python:3.8-slim-buster

WORKDIR /app

# Create the hsq user.
RUN groupadd -f -g 1000 hsq
RUN useradd -o --shell /bin/bash -u 1000 -g 1000 -m hsq
RUN echo "hsq ALL=(ALL)NOPASSWD: ALL" >> /etc/sudoers
USER hsq

# Move application
COPY --chown=hsq:hsq requirements.txt requirements.txt
COPY --chown=hsq:hsq hsq/ hsq/
COPY --chown=hsq:hsq templates/ templates/
COPY --chown=hsq:hsq app.py .

# Install application dependancies
RUN pip3 install -r requirements.txt

# Run the API
EXPOSE 443
CMD ["python", "/app/app.py"]
