package main

import "net/http"

func main() {
	panic(http.ListenAndServe(":8086", http.FileServer(http.Dir("/opt/"))))
}