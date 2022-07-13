% Question 4:
a = rand(100,1);
Limit = 20;
b = 0;
N = 1;
while b <= Limit
    b = b + a(N, 1);
    N = N +1;
    disp(b);  
end

fprintf('The amount of number is took to exceed 20 is %d\n', N)




