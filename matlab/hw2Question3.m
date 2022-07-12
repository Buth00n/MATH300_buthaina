% Question 3:
A = [1 1
     1 2
     1 3 ];
b = [1
     5
     10];
outcome = [-3.6667;4.5000];
Y = linsolve(A,b);
disp(Y)


disp(A * outcome)