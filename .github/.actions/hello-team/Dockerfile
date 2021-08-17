FROM golang:1.15

WORKDIR /go/src/hello

COPY . .

RUN go get -d -v ./_

RUN go install -v ./_

CMD ["hello"]