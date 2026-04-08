import heapq

def min_rooms(meetings):
    meeting_queue = []
    num_rooms = 0
    sorted_meetings = sorted(meetings)

    for start, end in sorted_meetings:
        heapq.heappush(meeting_queue, (end, start))
        cur_end = meeting_queue[0][0]
        if start < cur_end:
            num_rooms += 1
    
    return num_rooms

def check(test_name, got, expected):
    status = "✅ PASS" if got == expected else f"❌ FAIL  →  expected {expected}, got {got}"
    print(f"  {status}  |  {test_name}")


# --- Edge cases ---
print("\nEdge cases:")
check("empty list",                     min_rooms([]),                  0)
check("single meeting",                 min_rooms([(0, 10)]),           1)
check("two non-overlapping",            min_rooms([(0, 10), (10, 20)]), 1)
check("two overlapping",                min_rooms([(0, 10), (5, 15)]),  2)

# --- All meetings overlap ---
print("\nAll meetings overlap:")
check("3 fully overlapping",            min_rooms([(0, 30), (0, 30), (0, 30)]),          3)
check("5 all starting at same time",    min_rooms([(0, 10), (0, 20), (0, 30), (0, 40), (0, 50)]), 5)

# --- No meetings overlap ---
print("\nNo overlap (sequential):")
check("4 sequential meetings",          min_rooms([(0,10),(10,20),(20,30),(30,40)]),      1)
check("5 sequential with gaps",         min_rooms([(0,5),(10,15),(20,25),(30,35),(40,45)]), 1)

# --- Mixed overlaps ---
print("\nMixed overlaps:")
check("classic 3-meeting example",      min_rooms([(0,30),(5,10),(15,20)]),              2)
check("cascade overlap",                min_rooms([(0,10),(5,15),(10,20),(15,25)]),      2)
check("peak then taper",
    min_rooms([(0,20),(0,20),(0,20),(20,40),(20,40)]),                                   3)

# --- Large bursts ---
print("\nLarge bursts:")
check("10 simultaneous meetings",
    min_rooms([(i, i+30) for i in range(10)]),                                          10)

check("20 meetings, 2 rooms sufficient",
    min_rooms([(i*10, i*10+10) for i in range(20)]),                                    1)

check("alternating overlap pattern",
    min_rooms([(i, i+3) for i in range(0, 20, 2)]),                                     2)
    # each meeting spans 3 units, new one starts every 2 → always 2 active at once

# --- Unsorted input ---
print("\nUnsorted input:")
check("reverse order input",
    min_rooms([(30,40),(20,30),(10,20),(0,10)]),                                         1)
check("random order, 3 rooms needed",
    min_rooms([(10,20),(0,15),(5,25),(15,30),(20,35)]),                                  3)

# --- Long meetings with short ones interleaved ---
print("\nLong + short meetings interleaved:")
check("1 long + many short non-overlapping",
    min_rooms([(0,100),(10,20),(20,30),(30,40),(40,50)]),                                2)
check("2 long + many short overlapping",
    min_rooms([(0,100),(0,100),(10,20),(20,30),(30,40)]),  3)


    
