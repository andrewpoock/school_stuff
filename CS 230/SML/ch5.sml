fun cube n = n * n * n;


fun cuber n:real = n * n * n;


fun fourth lst = hd(tl(tl(tl(lst))));


fun min3(a, b, c) =
    if a <= b andalso a <= c then a
    else if b <= a andalso b <= c then b
    else c;


fun red3((a, b, c)) = (a, c);


fun thirds str = hd(tl(tl(explode str)));


fun cycle1 lst = tl(lst) @ [hd(lst)];


fun sort3(a:real, b:real, c:real) =
    if a <= b andalso a <= c then
        if b <= c then [a, b, c]
        else [a, c, b]
    else if b <= a andalso b <= c then
        if a <= c then [b, a, c]
        else [b, c, a]
    else
        if a <= b then [c, a, b]
        else [c, b, a];


fun del3 lst = [hd(lst)] @ [hd(tl(lst))] @ tl(tl(tl(lst)));


fun sqsum n =
    if n = 0 then 0
    else n * n + sqsum(n-1);


fun cycle(lst, n) =
    if n = 0 then lst
    else cycle(cycle1(lst), n-1);


fun pow(a:real, b:int) =
    if b = 0 then 1.0
    else a * pow(a, b-1);


fun maxhelper(lst, max) =
    if null lst then max
    else if hd(lst) > max then maxhelper(tl(lst), hd(lst))
    else maxhelper(tl(lst), max);

fun max x = maxhelper(tl x, hd x);


fun checkDivisors(n, num) =
    if num * num > n then true
    else if n mod num = 0 then false
    else checkDivisors(n, num + 6);

fun isPrime n =
    if n <= 1 then false
    else if n <= 3 then true
    else if n mod 2 = 0 orelse n mod 3 = 0 then false
    else checkDivisors(n, 5);


fun select(lst, func) =
    if null lst then []
    else if func(hd(lst)) = true then [hd(lst)] @ select(tl(lst), func)
    else select(tl(lst), func);