package main

// means must have a main() that is the entry point of this package.
// don't need to be named as "main.go", e.g. can be heelo.go
// other file's in the same dir with "package main" cab be invoke here directly
// without import cuz all files in the same dir belong to the same package (main)
// so, "package(logical) + dir(physical)" determines calling structure, start with it!
// finally, in this dir, use "go build" to create exec file named with that "dir"name

import (
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"log"
	"math"
	"math/rand"
	"net"
	"net/http"
	"os"
	"proj_1/utils1"
	"reflect"
	"sort"
	"strconv"
	"strings"
	"sync"
	"sync/atomic"
	"time"

	// 【 go get github.com/google/go-cmp/cmp 】
	// package will be installed in the 【 $GOPATH/pkg 】 folder
	// as dirs like: github.com-->google-->go-cmp-->cmp
	"github.com/google/go-cmp/cmp"
)

func main() {

	// calling concurent merge in merge.go
	done := make(chan int)
	is := []int{7, 9, 1, 4, 0, 6, 13, 2, 5, 3}
	go utils1.Mergesort(is, done)
	<-done

	for _, i := range is {
		fmt.Print(i, " ")
	}
	fmt.Println()

	fmt.Println("hello go!")
	fmt.Println(time.Now())
	// end: merge func

	// short var decl, e.g. a := 4, with ":=" 【only inside func body】
	// regular var decl, e.g. var a int = 4 or var a = 4, with "="
	// can decl multi-var w/o "var", but no explicit type allowed except var (...)
	// e.g. cando "var name, age = "woo", 25", but cannot "var ... age int = ..."
	a, b := 4, 0
	val, err := testDiv(a, b)
	fmt.Println(val, err)

	f := testFunc(3)
	f(4)

	testDefer(10, 2)

	testSlice()

	testMap()

	testStruct()

	//go testCur(1)
	//go testCur(2)
	//time.Sleep(time.Second * 6)

	basics()

	testClosure()

	testPanicRecover()

	// testCP()

	testFile()

	// testNet()

	// testHTTP()

}

func basics() {
	// testing type of var
	// [reflect] to tell var's type; var's data structure
	fmt.Println("【...testing reflect package's TypeOf & ValueOf Kind】")
	start := time.Now()
	fmt.Println(start)
	fmt.Println(reflect.TypeOf(start))
	fmt.Println(reflect.ValueOf(start).Kind())

	// fmt.Println("【...testing type conv】")
	// var input string
	// fmt.Println("enter your age")
	// fmt.Scanf("%s\n", &input)
	// age, err := strconv.Atoi(input)
	// if err != nil {
	// 	fmt.Println(err)
	// } else {
	// 	fmt.Println("your age is: ", age)
	// }

	// type transfer e.g. str<->int; int<->float
	// str<->int as strconv.Atoi; strconv.Itoa
	// int<->float as int(); float()
	in := "50"
	i, err := strconv.Atoi(in)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println("i is: ", i)
	}
	s := strconv.Itoa(i)
	fmt.Println(s)
	f, err := strconv.ParseFloat("3.14", 64) // err here reused
	fmt.Println("f is: ", f)
	fmt.Println("f to int is: ", int(f))

	// str interpolate: unlike Java, Golang cannot print with str"+"int
	name := "John"
	age := 26
	s = name + " age is: " + strconv.Itoa(age)
	fmt.Println(s)
	// or using Sprintf func to unify
	s = fmt.Sprintf("%s age is %d\n", name, age)
	fmt.Println(s)

	// logic operator: && || !
	// check a num betweern 2 and 9, note "and" here with "||" to achieve
	num := 6
	cond := !(num < 2 || num > 9)
	fmt.Println(cond)

	// 【swith】match var with case in general
	// "fallthrough"; without match var
	score := 79
	grade := ""
	switch { // here without match var "score"
	case score < 60:
		grade = "F"
	case score < 70:
		grade = "C"
	case score < 80:
		grade = "B"
	default:
		grade = "A"
	}
	fmt.Println("grade is：", grade)

	// for-loop: golang only has "for"
	// 【for ... range】: iterate though data structure, get back index and val
	var os [3]string
	os[0] = "ios"
	os[1] = "android"
	os[2] = "windows"
	for i, v := range os {
		fmt.Println(i, v)
	}
	// iterate a string
	for pos, char := range "hello, world!" {
		fmt.Printf("%d %c\n", pos, char)
	}

	// pointer
	x := 5
	y := 6
	swap(&x, &y)
	fmt.Printf("swap val: %d, %d\n", x, y)

	// function
	o, e := countOddEven("123456789")
	fmt.Printf("#odds: %d; #even: %d\n", o, e)

	fmt.Printf("sum of variant # ints: %d\n", addNums(1, 2, 3, 4, 5))

	// anonymous function
	var ff func(x int) int = func(x int) int {
		return x * x
	}
	fmt.Printf("anony call ff: %d\n", ff(7))

	// **** impl closure 【return a func within which an internal val remained】 using anonymous func ****
	// note that the key here is the return type "a function!" as a closure!
	// an interesting merit is of remembering a previous val in func()
	var fib func() func() int
	fib = func() func() int {
		f1 := 0
		f2 := 1
		return func() int {
			f1, f2 = f2, (f1 + f2)
			return f1
		}
	}
	gen := fib()
	for i := 0; i < 10; i++ {
		fmt.Printf("%d ; ", gen())
	}
	fmt.Println()

	// anonymous func impl filter, map, reduce ... 【a func as arg】
	var filter func(arr []int, cond func(int) bool) []int
	filter = func(arr []int, cond func(int) bool) []int {
		result := []int{}
		for _, v := range arr {
			if cond(v) {
				result = append(result, v)
			}
		}
		return result
	}
	a := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 23, 34, 56, 66, 77, 79}
	evens := filter(a, func(val int) bool {
		return val%2 == 0
	})
	fmt.Printf("filter even func call results: %d\n", evens)
	greater5 := filter(a, func(val int) bool {
		return val > 5
	})
	fmt.Printf("filter greater func call results: %d\n", greater5)

	// 【slice】 based on array impl: pointing to a base array with size and
	// capacity.

	// first, see some array examples
	var array = func() {
		// array def: fixed same type elm, with fixed size or [...]
		nums := [5]int{1, 2, 3, 4, 5}
		nums1 := [...]int{1, 2, 3, 4, 5}
		fmt.Printf("array nums: %d\n", nums)
		fmt.Printf("array nums size: %d\n", len(nums))
		fmt.Printf("array nums1: %d\n", nums1)
		fmt.Printf("array nums1 size: %d\n", len(nums1))

		// slice def with make() or []
		// a lice is a view of underlying array, with "ptr, len, cap"
		s := make([]int, 5, 8)
		fmt.Println(s)
		fmt.Println(len(s))
		fmt.Println(cap(s))

		t := []int{1, 2, 3, 4, 5}
		fmt.Println("slice t's len:", len(t))
		fmt.Println("slice t's cap:", cap(t))

		// append to a slice
		// when exceed cap will enlarge 2 times
		t = append(t, 6, 7, 8)
		fmt.Println(len(t))
		fmt.Println(cap(t))
		t = append(t, 9, 10)
		fmt.Println(len(t))
		fmt.Println(cap(t))

		// slice assignment: both point to the same array, but when exceed
		// will create a new slice s.t. no reflection
		u := t
		fmt.Println(u)
		fmt.Println(t)

		u[9] = 100
		t[8] = 200
		fmt.Println("atfer changing u:", u)
		fmt.Println("atfer changing t:", t)

		t = append(t, 21)
		fmt.Println(u)
		fmt.Println(t) // now, t exceeds origin len, so create a new slice (diff from u)

		// slice ranging and insert/delete
		// slice an array or slice results in a new slice based on original array
		// [m:n] is an open range where m is included but n is excluded; cap deducted
		t = t[2:4]
		fmt.Println(t)
		fmt.Println(len(t))
		fmt.Println(cap(t))

		// copy of array by assignment: is a copy! s.t. no reflect changing
		nums2 := [5]int{1, 2, 3, 4, 5}
		nums3 := nums2
		fmt.Println(nums2)
		fmt.Println(nums3)
		nums2[0] = 0
		fmt.Println(nums2)
		fmt.Println(nums3)

		// copy of slice by func copy(dest, src), examine both len and copy min len
		t = []int{1, 2, 3, 4, 5}
		fmt.Println("slice t is: ", t)
		fmt.Println(len(t))
		fmt.Println(cap(t))

		v := make([]int, len(t))
		copy(v, t)
		fmt.Println("t after copy", t)
		fmt.Println("v after copy", v)

		v = make([]int, 2, 5)
		fmt.Println(v)
		copy(v, t)
		fmt.Println(t)
		fmt.Println(v)

		// insert/delete an item into a slice
		var insert func(orig []int, index int, value int) ([]int, error)
		insert = func(orig []int, index int, value int) ([]int, error) {
			if index < 0 {
				return nil, errors.New("index less than 0")
			}
			if index >= len(orig) {
				return append(orig, value), nil
			}
			orig = append(orig[:index+1], orig[index:]...) // note "..." deref variant
			fmt.Println("expanding copy result: ", orig)
			orig[index] = value
			return orig, nil
		}
		t = []int{1, 2, 3, 4, 5}
		t, err := insert(t, 1, 9)
		if err == nil {
			fmt.Println("after insert: ", t)
		} else {
			fmt.Println(err)
		}

	}
	array()

	// struct
	var structure = func() {
		// struct def
		type point struct {
			x float32
			y float32
			z float32
		}
		// struct init
		var pt1 point
		pt1.x = 3.1
		pt1.y = 5.7
		pt1.z = 4.2
		// struct init another way
		pt2 := point{x: 1.2, y: 2.3, z: 3.9}
		pt3 := point{4.5, 5.6, 6.8}

		fmt.Println(pt1)
		fmt.Println(pt2)
		fmt.Println(pt3)

		var newPoint = func(x, y, z float32) *point {
			p := point{x: x, y: y, z: z}
			return &p
		}
		pt4 := newPoint(4.0, 3.2, 9.8)
		pt5 := pt4  // reference to the same point struct
		pt6 := *pt4 // this is a copy, so no reflect changing
		fmt.Println(pt4)
		fmt.Println(*pt4)
		fmt.Println(pt5)
		fmt.Println(pt6)

		// define method instruct
		var length = func(p point) float64 {
			return math.Sqrt((math.Pow(float64(p.x), 2) +
				math.Pow(float64(p.y), 2) +
				math.Pow(float64(p.z), 2)))
		}
		pt4 = newPoint(2.2, 3.3, 4.4)
		fmt.Println("distance is: ", length(*pt4))

		type Point struct { // cuz import "cmp" package, must be Capital name/field
			X    float32
			Y    float32
			Z    float32
			Name []string
		}
		pt10 := Point{X: 1.2, Y: 1.3, Z: 1.4, Name: []string{"pt1"}}
		pt11 := Point{X: 1.2, Y: 1.3, Z: 1.4, Name: []string{"pt1 dfd"}}
		fmt.Println("struct comp pt10~11: ", cmp.Equal(pt10, pt11))
	}
	structure()

	var mymap = func() {
		var heights map[string]int = make(map[string]int)
		heights["peter"] = 170
		heights["joan"] = 168
		heights["jan"] = 175
		fmt.Println(heights["peter"])
		fmt.Println(heights["joan"])
		fmt.Println(heights["jan"])

		// init map with map literal,don't forget ","
		salary := map[string]int{
			"alice": 1000,
			"bob":   2000,
		}
		fmt.Println(salary["alice"])

		// check existence of a key
		if val, ok := heights["jim"]; ok {
			fmt.Println(val)
		} else {
			fmt.Println("key doesn't exists!")
		}

		// delete a key
		if _, ok := heights["peter"]; ok {
			delete(heights, "peter")
			fmt.Println("key \"peter\" is deleted!")
		} else {
			fmt.Println("key doesn't exist")
		}

		// # of items in a map
		fmt.Println(len(heights))

		// iterate over a map
		for k, v := range heights {
			fmt.Println(k, v)
		}

		//get all keys in a map
		var keys []string
		for k := range salary {
			keys = append(keys, k)
		}
		fmt.Println("all keys are: ", keys)

		// set the iteration ordere in a map
		sort.Strings(keys) // cuz keys:[]string are sorted first, then iterate...
		for _, k := range keys {
			fmt.Println(k, salary[k])
		}

		// using structure and map
		// sort kv with v s.t. cannot directly use sort()

		/* type kv struct {
			key   string
			value int
		}
		type kvPairs []kv

		scores := map[string]int{
			"alice": 89,
			"bob":   78,
			"carol": 96,
			"david": 62,
		}

		p := make(kvPairs, len(scores))
		i := 0
		for k, v := range scores {
			p[i] = kv{k, v}
			i++
		}

		func (p kvPairs) Len() int {
			return len(p)
		}

		func (p kvPairs) Less(i, j int) bool {
			return p[i].value < p[j].value
		}

		func (p kvPairs) Swap(i, j int) {
			p[i], p[j] = p[j], p[i]
		}

		sort.Sort(p)

		fmt.Println(p)

		for _, v := range p {
			fmt.Println(v)
		} */

	}
	mymap()

	// decoding Json
	var Myjson = func() {
		type People struct {
			Firstname string
			Lastname  string
			Details   struct {
				Height int
				Weight float32
			}
			Base   string `json:"base currency"`
			Symbol string `json:"destination currency"`
		}
		var persons []People
		jsonString :=
			`[
				{
					"firstname":"ye",
					"lastname":"wu",
					"datails":{
						"height":175,
						"weight":90.1
					},
					"base currency":"EUR",
					"destination currency":"USD",
					"rates":{
						"AUD":1.68,
						"CAD":1.53,
						"USD":1.09
					}
				},
				{
					"firstname":"qian",
					"lastname":"wu",
					"datails":{
						"height":180,
						"weight":80.2
					},
					"base currency":"USD",
					"destination currency":"EUR",
					"rates":{
						"AUD":2.68,
						"CAD":2.53,
						"USD":2.09
					}
				}
			]`
		var results []map[string]interface{}
		json.Unmarshal([]byte(jsonString), &results)
		for _, res := range results {
			fmt.Println(res["firstname"])

			rates := res["rates"]
			fmt.Println(rates)

			curr := rates.(map[string]interface{})
			fmt.Println(curr["USD"])
		}

		err := json.Unmarshal([]byte(jsonString), &persons)
		if err == nil {
			for _, person := range persons {
				fmt.Println(person.Firstname)
				fmt.Println(person.Lastname)
				fmt.Println(person.Details.Height)
				fmt.Println(person.Details.Weight)
				fmt.Println(person.Base)
				fmt.Println(person.Symbol)
			}
		} else {
			fmt.Println(err)
		}

		// encoding json
		/* type Name struct {
			Firstname string
			Lastname  string
		}
		type Address struct {
			Line1 string
			Line2 string
			Line3 string
		}
		type Customer struct {
			Name    Name
			Email   string
			Address Address
			DOB     time.Time
		} */

		// or using interface to encode
		type Customer map[string]interface{}
		type Name map[string]interface{}
		type Address map[string]interface{}

		layoutISO := "2006-01-02"
		dob, _ := time.Parse(layoutISO, "2010-01-08")

		john := Customer{
			"Name": Name{
				"Firstname": "John2",
				"Lastname":  "Smith2",
			},
			"Email": "jognsmith2@example.com",
			"Address": Address{
				"Line1": "the white house 2",
				"Line2": "1400 penn street 2",
				"Line3": "washington DC, 20500 2",
			},
			"DOB": dob,
		}

		/* john := Customer{
			Name: Name{
				Firstname: "John",
				Lastname:  "Smith",
			},
			Email: "jognsmith@example.com",
			Address: Address{
				Line1: "the white house",
				Line2: "1400 penn street",
				Line3: "washington DC, 20500",
			},
			DOB: dob,
		} */
		johnJSON, err := json.MarshalIndent(john, "", "   ")
		if err == nil {
			fmt.Println(string(johnJSON))
		} else {
			fmt.Println(err)
		}

	}
	Myjson()

	// interface

	/* 	var myInterface = func() {
	   		type DigitsCounter interface {
	   			CountOddEven() (int, int)
	   		}
	   		type DigitString string
	   		func (ds DigitString) CountOddEven() (int, int) {
	   			odds, evens := 0, 0
	   			for _, digit := range ds {
	   				if digit % 2 == 0 {
	   					evens ++
	   				} else {
	   					odds++
	   				}
	   			}
	   			return odds, evens
	   		}
	   		s := DigitString("123456789")
	   		fmt.Printf("# of odds:%d, and evens:%d in s\n", odds, evens)

	   	}
	   	myInterface() */

	// go routine

	myGoRutine := func() {
		var balance int64
		var mutex = &sync.Mutex{}

		credit := func(wg *sync.WaitGroup) {
			defer wg.Done()
			for i := 0; i < 10; i++ {
				mutex.Lock()
				atomic.AddInt64(&balance, 100)
				fmt.Println("after credit balance is: ", balance)
				mutex.Unlock()
				time.Sleep(time.Duration(100) * time.Millisecond)
			}
		}

		debit := func(wg *sync.WaitGroup) {
			defer wg.Done()
			for i := 0; i < 5; i++ {
				mutex.Lock()
				atomic.AddInt64(&balance, -100)
				fmt.Println("after debit balance is: ", balance)
				mutex.Unlock()
				time.Sleep(time.Duration(100) * time.Millisecond)
			}
		}

		var wg sync.WaitGroup
		balance = 200
		fmt.Println("init balance is: ", balance)

		wg.Add(1)
		go credit(&wg)

		wg.Add(1)
		go debit(&wg)

		wg.Wait()
		fmt.Println("final balance is: ", balance)

	}
	myGoRutine()

	// unbuffered channel

	unBufChan := func() {

		wg := new(sync.WaitGroup)
		fib := func(n int, c chan int) {
			defer wg.Done()
			a, b := 1, 1
			for i := 0; i < n; i++ {
				c <- a
				a, b = b, a+b
				time.Sleep(20 * time.Millisecond)
			}
			close(c)
		}

		counter := func(n int, c chan int) {
			defer wg.Done()
			for i := 0; i < 10; i++ {
				c <- i
				time.Sleep(10 * time.Millisecond)
			}
			close(c)
		}

		c1 := make(chan int)
		c2 := make(chan int)

		wg.Add(1)
		go fib(10, c1)
		wg.Add(1)
		go counter(10, c2)

		c1Closed := false
		c2Closed := false

		go func() { // this make main tread async s.t. can proceed with other things
			for {
				select {
				case n, ok := <-c1: // retrive val from c1 until close(c1)
					if !ok {
						c1Closed = true
						if c1Closed && c2Closed {
							return
						}
					} else {
						fmt.Println("fib()", n)
					}
				case m, ok := <-c2:
					if !ok {
						c2Closed = true
						if c1Closed && c2Closed {
							return
						}
					} else {
						fmt.Println("counter()", m)
					}
				}
			}
		}()

		wg.Wait()
		fmt.Println(("main tread continue to do sth else ..."))

		// a new example for sum the length of 2 strings
		fmt.Println("sum length of 2 string ...")

		strlen := func(s string, c chan int) {
			c <- len(s)
		}
		var c = make(chan int)
		go strlen("hello", c)
		go strlen("haha", c)
		x, y := <-c, <-c
		fmt.Println("2 string len sum is: ", x, y, x+y)
	}
	unBufChan()

	// bufChan

	bufChan := func() {

		wg := new(sync.WaitGroup)
		sum := func(s []int, c chan int) {
			defer wg.Done()
			sum := 0
			for _, v := range s {
				sum += v
			}
			c <- sum
			fmt.Println("Done! and can continue to do other work")
		}

		s := []int{}
		sliceSize := 10
		for i := 0; i < sliceSize; i++ {
			s = append(s, rand.Intn(100))
		}

		c := make(chan int, 5)
		partSize := 2
		parts := sliceSize / partSize

		i := 0
		for i < parts {
			wg.Add(1)
			go sum(s[i*partSize:(i+1)*partSize], c)
			i += 1
		}
		wg.Wait()
		close(c) // must be closed cuz following will retreve from c (range...)

		i = 0
		total := 0
		for i < 3 {
			partialSum := <-c
			fmt.Println("Partial sum: ", partialSum)
			total += partialSum
			i += 1
		}
		fmt.Println("Total: ", total)

		for val := range c {
			total += val
		}
		fmt.Println("Total: ", total)
		// wg.Wait()  can NOT put here!
	}
	bufChan()

}

func addNums(nums ...int) int { // variant # args
	total := 0
	for _, n := range nums {
		total += n
	}
	return total
}

func countOddEven(s string) (int, int) {
	odds, evens := 0, 0
	for _, c := range s {
		if int(c)%2 == 0 {
			evens++
		} else {
			odds++
		}
	}
	return odds, evens
}

func swap(a, b *int) {
	*a, *b = *b, *a
}

func testDiv(a, b int) (int, error) {
	if b == 0 {
		return 0, errors.New("divided by zero")
	}
	return a / b, nil
}

func testFunc(x int) func(int) {
	return func(y int) {
		fmt.Println(x + y)
	}
}

func testDefer(a, b int) {
	defer fmt.Println("dispose ...")
	fmt.Println(a / b)
}

func testSlice() {
	x := make([]int, 0, 5)
	for i := 0; i < 8; i++ {
		x = append(x, i)
	}
	fmt.Println(x)
}

// testing how to add a member? retrieve? delete member?
func testMap() {
	m := make(map[string]int)
	m["a"] = 5
	x, ok := m["b"]
	fmt.Println(x, ok)
	x, ok = m["a"]
	fmt.Println(x, ok)
	delete(m, "a")
}

func testStruct() {
	type user struct {
		name string
		age  byte
	}
	type manager struct {
		user
		title string
	}
	// although inner embedded, still directly access member
	var m manager
	m.name = "Tom"
	m.age = 20
	m.title = "CEO"

	fmt.Println(m)
}

func testCur(id int) {
	for i := 0; i < 5; i++ {
		fmt.Printf("this is %d: %d\n", id, i)
		time.Sleep(time.Second)
	}
}

func testCP() {
	consumer := func(data chan int, done chan bool) {
		for x := range data {
			fmt.Println("recieve: ", x)
		}
		done <- true
	}
	producer := func(data chan int) {
		for i := 0; i < 4; i++ {
			data <- i
		}
		close(data)
	}
	done := make(chan bool)
	data := make(chan int)

	go consumer(data, done)
	go producer(data)
	<-done // should have, otherwise this proc will be interupted by others

	// simple read-write example
	var c chan string
	reader := func() {
		msg := <-c
		fmt.Println("I'm reader, ", msg)
	}
	c = make(chan string)
	go reader()
	fmt.Println("begin sleep ...")
	time.Sleep(time.Second * 1)
	c <- "hello, write to chan"
	time.Sleep(time.Second * 1)

	// 3 go-routine with 2 chan to transfer data
	c1 := make(chan int)
	c2 := make(chan int)
	go func() {
		for i := 0; i < 3; i++ {
			c1 <- i
			time.Sleep(time.Second * 1)
		}
		close(c1)
	}()
	go func() {
		for {
			num, ok := <-c1
			if !ok {
				break
			}
			c2 <- num * num
		}
		close(c2)
	}()
	for {
		num, ok := <-c2
		if !ok {
			break
		}
		fmt.Printf("finally, c2's square val: %d\n", num)
	}

	// Another with chan as param: 3 go-routine with 2 chan to transfer data
	c11 := make(chan int)
	c22 := make(chan int)
	go func(out chan<- int) {
		for i := 0; i < 3; i++ {
			out <- i
			time.Sleep(time.Second * 1)
		}
		close(out)
	}(c11)
	go func(in <-chan int, out chan<- int) {
		for {
			num, ok := <-in
			if !ok {
				break
			}
			out <- num * num * num
		}
		close(c22)
	}(c11, c22)
	for {
		num, ok := <-c22
		if !ok {
			break
		}
		fmt.Printf("finally, c22's cube val: %d\n", num)
	}

	// timer and ticker
	ticker := time.NewTicker(time.Second)
	num := 3
	for {
		data := <-ticker.C
		fmt.Printf("ticker's output: %d\n", data)
		num--
		if num == 0 {
			break
		}
	}
	ticker.Stop()

	// rocket launch by ticker
	ticker2 := time.NewTicker(time.Second)
	num2 := 3
	launch := func() {
		fmt.Println("rocket launch!")
	}
	for {
		<-ticker2.C
		fmt.Println(num2)
		num2--
		if num2 == 0 {
			break
		}
	}
	ticker2.Stop()
	launch()

	// multi-chan monitor
	ticker3 := time.NewTicker(time.Second)
	fmt.Println("begin launching! cancel if press return")
	num3 := 5
	chan_stdin := make(chan string)
	go func(out chan<- string) {
		data := make([]byte, 10)
		os.Stdin.Read(data)
		out <- "cancel..."
	}(chan_stdin)
	for {
		select {
		case <-ticker3.C:
			fmt.Println(num3)
			num3--
		case <-chan_stdin:
			fmt.Println("cancel launch now!")
			return
		}
		if num3 == 0 {
			ticker3.Stop()
			break
		}
	}
	launch()

}

// test closure
func testClosure() {
	getSequence := func() func() int {
		i := 0
		return func() int {
			i += 1
			return i
		}
	}

	// getSequence() return a function with type ()-->int, thus nextNum() results in an int // i
	nextNum := getSequence()
	fmt.Println(nextNum())
	fmt.Println(nextNum())
	fmt.Println(nextNum())

	nextNum1 := getSequence()
	fmt.Println(nextNum1())
	fmt.Println(nextNum1())
}

// test panic-recover
// usually panic is a big issue to raise progran exit, but can be handled by panic for not exit;
// however recover must be exec before panic, thus arrange it in "defer"
func testPanicRecover() {
	pr := func() {
		defer func() {
			fmt.Println("defer recover panic") // will print out
			recover()
		}()
		panic("game over")         // raise error
		fmt.Println("pr run over") // this won't print out
	}
	pr()
	fmt.Println("hi, game not over!")
}

// about file operations
func testFile() {
	fd, err := os.OpenFile("test.txt", os.O_WRONLY|os.O_CREATE, 0666)
	if err != nil {
		fmt.Println("failed to open/create file", err)
		return
	}
	defer fd.Close()
	fd.WriteString("hello golang!")
	fmt.Println("write a string success")

	// now read dir
	fd, err = os.Open("./") // fd is defined before, so using "="
	if err != nil {
		fmt.Println("failed to open file", err)
		return
	}
	infos, err := fd.Readdir(-1)
	if err != nil {
		fmt.Println("failed to read dir", err)
		return
	}
	for _, v := range infos {
		fmt.Printf("name=%s, isdir=%t, size=%d\n", v.Name(), v.IsDir(), v.Size())
	}
}

// network programming
func testNet() {
	listener, err := net.Listen("tcp", "localhost:8888")
	if err != nil {
		log.Panic("failed to listen", err)
	}
	defer listener.Close()
	for {
		conn, err := listener.Accept()
		if err != nil {
			fmt.Println("failed to accept", err)
			continue
		}
		fmt.Println("new conn ->", conn.RemoteAddr().String())
		go func(conn net.Conn) {
			defer conn.Close()
			buf := make([]byte, 256)
			for {
				n, err := conn.Read(buf)
				if err != nil {
					if err != io.EOF {
						fmt.Println("client @", conn.RemoteAddr().String(), "is closed")
						break
					}
					fmt.Println("failed to read data ", err)
					break
				}
				n, err = conn.Write(buf[:n])
				if err != nil {
					fmt.Println("failed to write to client ", conn.RemoteAddr().String(), err)
					break
				}
			}
		}(conn)
	}
}

func testHTTP() {
	helloSrv := func(w http.ResponseWriter, req *http.Request) {
		path := req.URL.Path
		fmt.Println(path)
		users := strings.Split(path, "/")
		fmt.Println(len(users), users)
		if len(users) == 3 {
			io.WriteString(w, users[1]+", "+users[2])
		}
	}

	byeSrv := func(w http.ResponseWriter, req *http.Request) {
		path := req.URL.Path
		fmt.Println(path)
		users := strings.Split(path, "/")
		fmt.Println(len(users), users)
		if len(users) == 3 {
			io.WriteString(w, users[1]+", "+users[2])
		}
	}

	http.HandleFunc("/hello/", helloSrv)
	http.HandleFunc("/bye/", byeSrv)
	err := http.ListenAndServe(":12345", nil)
	if err != nil {
		log.Panic("ListenAndServe: ", err)
	}

}
