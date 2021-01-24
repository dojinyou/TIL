# https://www.acmicpc.net/problem/2011

def test(c):
    # c = input()
    n = len(c)
    isPrinted = False

    if c[0] == "0" :
        print("0")
        isPrinted = True
    elif n == 1:
        print("1")
        isPrinted = True
    else :
        for i in range(1,n):
            if c[i] == "0" and c[i-1] != "2" and c[i-1] != "1":
                print("0")
                isPrinted = True
    if not isPrinted :
        mod = 1000000
        dp = [1]*n
        for i in range(1,n):
            if c[i]=="0" :
                dp[i] = dp[i-2]
            elif c[i-1] + c[i] <= "26" and c[i-1] != "0":
                dp[i] = dp[i-1] + dp[i-2]
            else :
                dp[i] = dp[i-1]
        print(dp[n-1] % mod)
test(input())
# assert(test("0"))==0
# assert(test("1")) == 1
# assert(test("000")) == 0
# assert(test("01")) == 0
# assert(test("007")) == 0
# assert(test("9")) == 1
# assert(test("10")) == 1
# assert(test("11")) == 2
# assert(test("17")) == 2
# assert(test("0020")) == 0
# assert(test("20")) == 1
# assert(test("26")) == 2
# assert(test("27")) == 1
# assert(test("30")) == 0
# assert(test("99")) == 1
# assert(test("100")) == 0
# assert(test("101")) == 1
# assert(test("103")) == 1
# assert(test("110")) == 1
# assert(test("123")) == 3
# assert(test("1010")) == 1
# assert(test("2220")) == 2
# assert(test("2626")) == 4
# assert(test("8100")) == 0
# assert(test("208227")) == 2
# assert(test("28713831")) == 2
# assert(test("6398101327")) == 2
# assert(test("123456789")) == 3
# assert(test("9876543210")) == 1
# assert(test("321131321321331")) == 90
# assert(test("132232332132132312321")) == 1296
# assert(test("1233123123113232123113232131232323123231233123213131")) == 687040