#Made with the help ok KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier
#I have assigned integer values to the respective teams 
A,B,C,D = 0,1,2,3 
labels = [A,C,C,A,D,D,A]
features = [[A,B],[B,C],[C,D],[A,D],[B,D],[C,D],[D,A]]
clf = KNeighborsClassifier()
clf = clf.fit(features,labels)
print("You have to Enter two teams that will have a match\n You can Choose in Between A, B, C, D\n You have to enter input by seprating commas")
print("Example:\n a,b")
x,y = eval(input("Enter two teams:").upper())
prediction = clf.predict([[x,y]])
prediction= int(prediction)
print(prediction)
if prediction == 0:
    print("Team A Won !")
elif prediction == 1:
    print("Team B Won !")
elif prediction == 2:
    print("Team C Won !")
elif prediction == 3:
    print("Team D Won !")
else:
    print("Tie !")
    

