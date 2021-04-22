import random


#referenzmatrix
A = [
        ["[0][0]", "[0][1]", "[0][2]", "[0][3]", "[0][4]"],
        ["[1][0]", "[1][1]", "[1][2]", "[1][3]", "[1][4]"],
        ["[2][0]", "[2][1]", "[2][2]", "[3][3]", "[4][4]"],
        ["[3][0]", "[3][1]", "[3][2]", "[3][3]", "[3][4]"],
        ["[4][0]", "[4][1]", "[4][2]", "[4][3]", "[4][4]"],
    ]

def print_grid(grid):
    print("\n")
    for row in grid:
        print(row)
    print("\n")


def give_subgrid(x,y):  # determines which subgrid x,y is in

    if 0 <= x <= 2 and 0 <= y <= 2:
        return 0
        # return dict_subgrid_list["1"]
    if 0 <= x <= 2 and 3 <= y <= 5:
        return 3
        # return dict_subgrid_list["4"]
    if 0 <= x <= 2 and 6 <= y <= 8:
        return 6
        # return dict_subgrid_list["7"]
    if 3 <= x <= 5 and 0 <= y <= 2:
        return 1
        # return dict_subgrid_list["2"]
    if 3 <= x <= 5 and 3 <= y <= 5:
        return 4
        # return dict_subgrid_list["3"]
    if 3 <= x <= 5 and 6 <= y <= 8:
        return 7
        # return dict_subgrid_list["8"]
    if 6 <= x <= 8 and 0 <= y <= 2:
        return 2
        # return dict_subgrid_list["3"]
    if 6 <= x <= 8 and 3 <= y <= 5:
        return 5
        # return dict_subgrid_list["6"]
    if 6 <= x <= 8 and 6 <= y <= 8:
        return 8
        # return dict_subgrid_list["9"]



def generator(grd):

    print("\n ----NEW ATTEMPT----")

    grid = grd
    max_k = 0
    Error = False

    subgrid_list = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
    ]
    x_list = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
    ]

    y_list = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
    ]

    for k in range(9):  # iterates rows = y-dim
        for l in range(9):  # iterates cols = x-dim

            if k == l:  # hold diag element
                # print("\ndiagpos = " + str(k))      ###DEBUG###
                # print_grid(grid)                
            
                for i in range(9):  # cols = x-dim

                    # create r_val
                    if grid[k][i] == 0:

                        cur_subgrid = give_subgrid(i, k)

                        first_intersect = [x for x in y_list[k] if x in x_list[i]]
                        sec_intersect = [x for x in first_intersect if x in subgrid_list[cur_subgrid]]
                        intersect = sec_intersect

                        if len(intersect) > 0:
                            r_val = random.choice(intersect)
                            grid[k][i] = r_val

                            # remove r_val 
                            x_list[i].remove(r_val)
                            y_list[k].remove(r_val)
                            subgrid_list[cur_subgrid].remove(r_val)

                            # print("y_list: "+ str(k) + " Iteration: "+ str(i) )   ###DEBUG###
                            # print(y_list[k])        


                if len(y_list[k]) == 0:
                    Error = False
                if len(y_list[k]) != 0:
                    Error = True

                    print("\ndiagpos = " + str(k))      
                    print_grid(grid)
                    max_k = k
                    print("#LIST_NOT_EMPTY_ERROR at y_list["+ str(k) +"]: " + str(Error))    
                    grid = [[0 for x in range(9)] for x in range(9)]
                    return [False, max_k]


                # print("\ndiagpos = " + str(k))    ###DEBUG###
                # print_grid(grid)        


                for j in range(9):  # rows = y-dim

                    # create r_val
                    if grid[j][k] == 0:

                        cur_subgrid = give_subgrid(k, j)

                        first_intersect = [x for x in x_list[k] if x in y_list[j]]
                        sec_intersect = [x for x in first_intersect if x in subgrid_list[cur_subgrid]]
                        intersect = sec_intersect

                        if len(intersect) > 0:
                            r_val = random.choice(intersect)
                            grid[j][k] = r_val

                            # remove r_val 
                            x_list[k].remove(r_val)
                            y_list[j].remove(r_val)
                            subgrid_list[cur_subgrid].remove(r_val)

                            # print("x-list: " + str(k)+ " Iteration: "+ str(j) )   ###DEBUG###
                            # print(x_list[k])


                if len(x_list[k]) == 0:
                    Error = False
                if len(x_list[k]) != 0:
                    Error = True

                    print("\ndiagpos = " + str(k))      
                    print_grid(grid)

                    print("#LIST_NOT_EMPTY_ERROR at x_list["+ str(k) +"]: " + str(Error))    
                    grid = [[0 for x in range(9)] for x in range(9)]
                    return [False, max_k]
                
    return [True, max_k]



# grid1 = [[0 for x in range(9)] for x in range(9)]
# grid1[0][0] = 1
# grid1[0][1] = 2
# grid1[0][2] = 3
# grid1[1][0] = 4
# grid1[1][1] = 5
# grid1[1][2] = 6
# grid1[2][0] = 7
# grid1[2][1] = 8
# grid1[2][2] = 9
# grid2 = [[0 for x in range(9)] for x in range(9)]
# grid3 = [[0 for x in range(9)] for x in range(9)]
# grid4 = [[0 for x in range(9)] for x in range(9)]
grid5 = [[0 for x in range(9)] for x in range(9)]


# generator_row(grid2)
# generator_subgrid(grid3)
# generator_col(grid4)
# print("row:")
# print_grid(grid2)
# print("subgrid:")
# print_grid(grid3)
# print("col:")
# print_grid(grid4)

def main(grd, rep):

    c = 0
    max_k = 0

    while not generator(grd)[0]:
        if c < 10**rep: 

            grd = [[0 for x in range(9)] for x in range(9)]
            k = generator(grd)[1]

            if k > max_k:
                max_k = k
            c += 1

        else:
            break

    if c < 10**rep:
        print("----------SUCCESS---------- \n grid generated:\n")
        print_grid(grd)
        print("\n---------------------------\n")
    else:
        print("\n\n-------FAIL------- \n AFTER ATTEMPT: " + str(10**rep) +  "\n highest diag: " + str(max_k) + "\n------------------\n")
    

main(grid5, 6)

# print("\n\n\nsubgrid_test:")
# print("0,4 (3): " + str(give_subgrid(0, 4)))
# print("1,5 (3): " + str(give_subgrid(1, 5)))
# print("6,3 (5): " + str(give_subgrid(6, 3)))


