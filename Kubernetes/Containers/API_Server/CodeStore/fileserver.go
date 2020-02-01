package main

import "net/http"

func main() {
	panic(http.ListenAndServe(":8096", http.FileServer(http.Dir("/opt/"))))
}