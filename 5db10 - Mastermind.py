from statistics import mean
import time

timeAv,tryAv=[],[]

def count_minus(guess,ans):
    temp_ans = ans[:]
    pegs = 0
    for i in guess:
        if i in temp_ans:
            temp_ans.remove(i)
            pegs += 1
    return pegs

def count_plus(guess,ans):
    return sum([ans[i] == guess[i] for i in range(0,5)])

def check(guess,ans):
    plus = count_plus(guess,ans)
    minus = count_minus(guess,ans)
    minus -= plus
    arr=[minus,plus]
    return arr
#code checker


def codebreaker(ans):
    start = time.time()

    tr = []
    guesses = [ intToArray(12345) , intToArray(67890) ]
    checks = [ check( guesses[0] , ans) , check( guesses[1] , ans) ]
    temp=0

    while tr != ans:
        for i in range (0,len(guesses)):
            tr = intToArray(temp)
            if check(tr,guesses[i])!=checks[i]:
                temp+=1
                break
            if i==len(guesses)-1:
                guesses.append(tr)
                checks.append(check(tr,ans))
                temp+=1

    end=time.time()

#for statistical data-----------
    timeAv.append(end-start)
    tryAv.append(len(guesses))
#for statistical data-----------

    print (guesses,end-start)
    return


def intToArray(guess):
    guess = [int(x) for x in str(guess)]
    while len(guess)<5:
        guess = [0]+guess
    return guess



def test():
    n=0
    while n<100000:
        answer=intToArray(n)
        codebreaker(answer)
        n+=1
    print("Mean of execution time "+str(mean(timeAv)),"Mean of tries "+ str(mean(tryAv)))



if __name__ == "__main__":
    test()
		
#prints the guesses of codebreaker and runtime in the end of line 


