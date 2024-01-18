fun sum_loop(lst, sofar) =
    if null lst then
        sofar
    else
        sum_loop(tl lst, sofar + (hd lst))

fun sumList2(lst) =
    sum_loop(lst, 0)