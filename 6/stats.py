import heap_sort,bubble_sort,quick_sort,insert_sort,merge_sort

hs_small, hs_big = heap_sort.stats()
bs_small, bs_big = bubble_sort.stats()
is_small, is_big = insert_sort.stats()
ms_small, ms_big = merge_sort.stats()
qs_small, qs_big = quick_sort.stats()



with open("6/statystyki.txt","w") as file:
    file.write("nazwa algorytmu -- rozmiar tablicy -- sredni czas(sekundy)\n")
    file.write("----------------------------------\n")
    file.write(f"heap sort -- 100 -- {sum(hs_small)/len(hs_small)}\n")
    file.write(f"heap sort -- 10000 -- {sum(hs_big)/len(hs_big)}\n")
    file.write("----------------------------------\n")
    file.write(f"bubble sort -- 100 -- {sum(bs_small)/len(bs_small)}\n")
    file.write(f"bubble sort -- 10000 -- {sum(bs_big)/len(bs_big)}\n")
    file.write("----------------------------------\n")
    file.write(f"insert sort -- 100 -- {sum(is_small)/len(is_small)}\n")
    file.write(f"insert sort -- 10000 -- {sum(is_big)/len(is_big)}\n")
    file.write("----------------------------------\n")
    file.write(f"merge sort -- 100 -- {sum(ms_small)/len(ms_small)}\n")
    file.write(f"merge sort -- 10000 -- {sum(ms_big)/len(ms_big)}\n")
    file.write("----------------------------------\n")
    file.write(f"quick sort -- 100 -- {sum(qs_small)/len(qs_small)}\n")
    file.write(f"quick sort -- 10000 -- {sum(qs_big)/len(qs_big)}\n")
    file.write("----------------------------------\n")