package main

import (
	"fmt"
	"os"
)

func main(){
    // 깃헙 액션 변수명은 고정이 되어 있음 대문자로 꼭 써줘야함
    leader := os.Getenv("INPUT_LEADER")
	member := os.Getenv("INPUT_MEMBER")

	fmt.Println("Hello " + leader)
	fmt.Println("Hello " + member)
}