package main
import (
  "fmt"
  "time"
)
func main() {
  nowUTC := time.Now().UTC()
  custom := nowUTC.Format("2006-01-02")
  fmt.Println(custom)
}