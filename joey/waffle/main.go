package main

import (
"bufio"
"os"
"strings"
"strconv"
"fmt"
"math"
)

func main(){
    scanner := bufio.NewScanner(os.Stdin)
    for scanner.Scan() {
    
        text := scanner.Text()
        if text == "" {
           break 
        }

        line := strings.Split(text, " ")
        isUp := true
        rate, _ := strconv.ParseFloat(line[0], 64)
        time, _ := strconv.ParseFloat(line[1], 64)
        
        if int(math.Floor(time/rate)) % 2 > 0 {
           isUp = false 
        }

        if int(time) % int(rate) > int(rate)/2 {
            isUp = !isUp
            fmt.Println("passed the halfway point and is now facing: ", isUp)
        }

        if isUp == true {
            
            fmt.Println("up")

        }
        if isUp == false {

            fmt.Println("down")

        }
    }
}
