% Question 4:
a = rand(100,1);
Limit = 20;
Acu = 0;
N = 1;
while Acu < Limit
    Acu = Acu + a(N, 1);
    N = N +1;
end

ave_count = sum(a)/n;
disp(ave_count)


