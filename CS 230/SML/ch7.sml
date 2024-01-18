(* 2 *)
fun member(e, []) = false
    | member(e, a::bs) =
        if e = a then true
        else member(e, bs);

(* 3 *)
fun less(e, []) = []
    | less(e, a::bs) =
        if e > a then a::less(e, bs)
        else less(e, bs);

(* 4 *)
fun repeats([]) = false
    | repeats([a]) = false
    | repeats(a::b::cs) =
        if a = b then true
        else repeats(b::cs);

(* 5 *)
fun pow(a:real, b:int) =
    if b = 0 then 1.0
    else a * pow(a, b-1);

fun eval(lst, n:real) =
    let
        fun evalHelper([], exp, ans) = ans
            | evalHelper(a::bs, exp, ans) =
                evalHelper(bs, exp + 1, ans + a * (pow(n, exp)))
    in
        evalHelper(lst, 0, 0.0)
    end;

(* 6 *)
fun quicksort([]) = []
  | quicksort(pivot::rest) =
    let
        fun part([], left, right) = (left, right)
          | part(x::xs, left, right) =
            if x < pivot then
                part(xs, x::left, right)
            else
                part(xs, left, x::right)
    in
        let
            val (left, right) = part(rest, [], [])
        in
            (quicksort(left) @ [pivot] @ quicksort(right))
        end
    end;

(* 7 *)
fun icmp (a, b) = a < b;
fun rcmp (a:real, b) = a < b;
fun ircmp (a, b) = a > b;

fun mergesort([], f) = []
  | mergesort([x], f) = [x]
  | mergesort(lst, f) =
    let
        fun halve([], left, right) = (left, right)
          | halve([x], left, right) = (x::left, right)
          | halve(x::y::rest, left, right) = halve(rest, x::left, y::right)

        fun merge([], ys, f) = ys
            | merge(xs, [], f) = xs
            | merge(x::xs, y::ys, f) =
            if f(x, y) then
                x :: merge(xs, y::ys, f)
            else
                y :: merge(x::xs, ys, f)

        val (left, right) = halve(lst, [], [])
    in
        merge(mergesort(left, f), mergesort(right, f), f)
    end;