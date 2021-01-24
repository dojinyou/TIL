# https://www.acmicpc.net/problem/10825

import sys

class Student :
    def __init__(self,array):
        self.name = array[0]
        self.kor = int(array[1])
        self.eng = int(array[2])
        self.math = int(array[3])
    def __lt__(self, other):
        if not self.kor == other.kor :
            return self.kor > other.kor
        if not self.eng == other.eng :
            return self.eng < other.eng
        if not self.math == other.math :
            return self.math > other.math
        if not self.name == other.name :
            return self.name < other.name
    def __str__(self):
        return self.name
        
n = int(sys.stdin.readline())
studentScoreList = []
for _ in range(n):
    student = Student(sys.stdin.readline().split())
    studentScoreList.append(student)
for student in sorted(studentScoreList):
    print(student)
