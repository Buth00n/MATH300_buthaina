%% File name : Math 300 Homework 2
% Name: Buthaina Al habsi
% Date : July 5th, 2022.

% Question 1:
A_1 = [2 -1 4
     9  6 2 
     1  3 8];
B = [1 1 1
     1 1 1 
     1 1 1 ];
x = [3
     6
     8];
y = [5 10 15];

disp(A_1 * B)
disp(A_1 * x)
disp(x' * B)
%disp(B * y) % this one says error "incorrect dimension for matrix multiplication"
%disp(x * A_1) % this one says error "incorrect dimension for matrix multiplication"
disp(x * y)
disp(y * x)
%disp(x * y') % this one too!! for incorrect dimension.
%disp(x. * y) -not sure why this and the next have errors.
%disp(A_1. * B.)



% Question 2:
A_2 = [1 1 1
     1 2 3 
     1 3 6];
b = [1
    -5
    2];
 X = linsolve(A_2,b);
 disp(X)

% Question 3:
A_3 = [1 1
     1 2
     1 3 ];
b = [1
     5
     10];
outcome = [-3.6667;4.5000];
Y = linsolve(A_3,b);
disp(Y)
disp(A_3 * outcome)

% Question 4:
sum1=0;
k=1;
while sum1<20
    sum1=sum1+k;
    k=randi(20);
end
disp(sum1);
disp(k);

% Question 5:
t= linspace (pi,-pi, 1000);
xt = 1+ cos(2*t);
yt = -1 + 3 * sin(4*t);
plot(xt)
hold on
plot(yt)
hold off

