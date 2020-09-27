# Use the official lightweight Python image
FROM python:3.8-slim
# Install our dependency to create a virtual environment in Python
RUN pip install virtualenv
# Setting our virtual environment variable
ENV VIRTUAL_ENV=/venv
# Creating a virtual environment
RUN virtualenv venv -p python3
# Setting the path for our virtual environment
ENV PATH="VIRTUAL_ENV/bin:$PATH"
# Setting our working directory to .app
WORKDIR /app
ADD . /app
# Installing our dependencies
RUN pip install -r requirements.txt
# Copying all files over
COPY . /app
# Expose port 
ENV PORT 8501
# cmd to launch app when container is run
CMD streamlit run app.py

# streamlit-specific commands for config
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
    [general]\n\
    email = \"\"\n\
    " > /root/.streamlit/credentials.toml'

RUN bash -c 'echo -e "\
    [server]\n\
    enableCORS = false\n\
    " > /root/.streamlit/config.toml'