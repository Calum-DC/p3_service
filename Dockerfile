FROM python

ENV SQS_P3_URL=""
ENV AWS_REGION=""
ENV AWS_ACCESS_KEY_ID=""
ENV AWS_SECRET_ACCESS_KEY=""
ENV SES_EMAIL=""
ENV RECIPIENT_EMAIL=""

WORKDIR /p3_service
COPY . /p3_service
RUN pip install -r requirements.txt
EXPOSE 8003
CMD ["gunicorn", "--bind","0.0.0.0:8003", "main:app"]

