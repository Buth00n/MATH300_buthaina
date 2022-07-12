% Question 4:
a = rand(200,1);
Limit = 20;
b = 0;
N = 1;
while b < Limit
    b = b + a(N, 1);
    N = N +1;
end

disp(N - 1);